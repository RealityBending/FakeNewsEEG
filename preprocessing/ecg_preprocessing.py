import glob
import os
import ast
import matplotlib.pyplot as plt
import neurokit2 as nk
import pandas as pd

# Set current directory/folder containing raw files to analyse
current_dir = "C:/Users/wilson.lim/Desktop/PROOF/PhysioData/Study"
os.chdir(current_dir)

### EXTRACTING EXCERPT NUM AND COND LISTS ### 

# Set path for processed questionnaire file
preprocessed_q_dir = "C:/Users/wilson.lim/Desktop/PROOF_EEG_questionnairedata.csv"

preprocessed_data = pd.read_csv(preprocessed_q_dir)

### RESTING STATE ECG PREPROCESSING ###

# Setting empty lists to insert individual subject dataframes into
resting_data_df = pd.DataFrame()
trials_ecg_data_df = pd.DataFrame()
trials_rsp_data_df = pd.DataFrame()
trials_rsa_data_df = pd.DataFrame()

# Analyse data for each subject
for idx, file in enumerate(glob.glob("*.txt")):
    print(idx)
    print(file)
    # Retrieve name of all .txt files
    name = file[:-4]
    print(name)

    # Set figure parameters
    # plt.rcParams['legend.fontsize']=9
    # plt.rcParams['figure.figsize']= (18,10)

    # Set working directory to where the file is, put data under the same folder
    # Read data from .txt file
    data, sampling_rate = nk.read_bitalino(file)
    # Specify sampling rate data type
    sampling_rate = sampling_rate['sampling_rate']

    # Reset index of data to samples
    # data["index"] = np.arange(0, len(data))

    # Extract condition and label lists
    
    if "_1" in name:
        event_conditions_full = ast.literal_eval(preprocessed_data["Excerpt_Condition_List"][idx/2])
        event_labels_full = ast.literal_eval(preprocessed_data["Excerpt_Num_List"][idx/2])
        event_conditions = event_conditions_full[0:22]
        event_labels = event_labels_full[0:22]
        print('labeled 1')
    if "_2" in name:
        event_conditions = event_conditions_full[22:42]
        event_labels = event_labels_full[22:42]
        print('labeled 2')

    ## RESTING ##

    # Resting state data in file 1 (before mid-expt calibration)
    if "_1" in name:
        print('processing resting')

        # Define event conditions Resting based on LUX signals
        resting = nk.events_find(data["LUX"], threshold=0, duration_min=445000, duration_max=500000,
                                threshold_keep='below', event_conditions=["Resting"])
        
        ## Plots
        # Standardized Signal PLots
        # nk.signal_plot(data[["ECGB", "RESP", "HR", "LUX"]], sampling_rate=sampling_rate, standardize=True)  # sampling_rate provided, will plot in seconds
        # Plot unstandardized original signals with event marking
        # plot = nk.events_plot(events, data[["ECGB", "RESP", "HR", "LUX"]])

        # Read ECG signals and epoch
        rsp_signals, rsp_info = nk.rsp_process(data["RESP"], sampling_rate=sampling_rate)
        ecg_signals, ecg_info = nk.ecg_process(data["ECGB"], sampling_rate=sampling_rate)

        rsp_epochs = nk.epochs_create(rsp_signals, resting, epochs_start=0, epochs_end=480, sampling_rate=sampling_rate)
        ecg_epochs = nk.epochs_create(ecg_signals, resting, epochs_start=0, epochs_end=480, sampling_rate=sampling_rate)
        # for i, epoch in enumerate(ecg_epochs):
        #     epoch = ecg_epochs[epoch]  # iterate epochs",
        #     epoch = epoch[['ECG_Clean', 'ECG_Rate']]  # Select relevant columns",
        #     title = "Resting"
            # nk.standardize(epoch).plot(title=title, legend=True)  # Plot scaled signals"

        # Plot R-R peaks, heart rate and individual heartbeats(to check method identifies peaks well)
        # nk.ecg_plot(ecg_signals, info=ecg_info)
        # plt.subplots_adjust(wspace=0.3, hspace=0.6)

        # Plotting to check data
        # nk.rsp_plot(rsp_signals, info=rsp_info) # To show raw and cleaned signal, breathing rate and amplitude, respiratory volume per time, and circle symmetry for the whole duration of the recording
        # plt.subplots_adjust(wspace=0.3, hspace=0.6)
        # nk.epochs_plot(rsp_epochs) # To show RSP_Raw, RSP_Clean, RSP_Amplitude, RSP_Rate, RSP_RVT, RSP_Phase, RSP_Phase_Completion, RSP_Symmetry_PeakTrough, RSP_Symmetry_RiseDecay, RSP_Peaks, and RSP_Troughs
        # plt.show()

        # pd.Series(ecg_signals["ECG_Clean"]).plot()
        # np.max(ecg_signals["ECG_Rate"])

        # Labelling data epochs (Resting State)
        resting_ecg_data = ecg_epochs["1"]
        resting_rsp_data = rsp_epochs["1"]

        # print(resting_ecg_data)
        # print(resting_rsp_data)
        print("here")
        # print(ecg_info["ECG_R_Peaks"])

        # Plot and print HRV indices for resting state ECG
        peaks, info = nk.ecg_peaks(resting_ecg_data["ECG_Clean"], sampling_rate=sampling_rate)
        resting_quality = nk.ecg_quality(resting_ecg_data["ECG_Clean"], rpeaks=info["ECG_R_Peaks"], sampling_rate=sampling_rate, method="zhao2018")
        plt.close()
        # print("Subject ECG Quality:")
        # print(resting_quality)
        hrv_time_indices = nk.hrv_time(peaks, sampling_rate=sampling_rate, show=True)
        # plt.subplots_adjust(wspace=0.3, hspace=0.4)
        time = hrv_time_indices[["HRV_RMSSD", "HRV_SDNN", "HRV_MeanNN", "HRV_CVNN"]]
        hrv_freq_indices = nk.hrv_frequency(peaks, sampling_rate=sampling_rate, show=True, normalize=True)
        freq = hrv_freq_indices[["HRV_LF", "HRV_HF", "HRV_LFHF", "HRV_LFn", "HRV_HFn"]]
        # print(freq)
        time = time.rename(index={0: name})
        freq = freq.rename(index={0: name})
        resting_timefreq_data = pd.concat([time, freq], axis=1)

        # Add resting heart rate into dataframe "resting_timefreq_data"
        HR_mean = [resting_ecg_data["ECG_Rate"].mean()]
        # print(HR_mean)
        resting_timefreq_data["Heart Rate"] = HR_mean

        # Plot and print RSP indices for resting state
        peaks, info = nk.rsp_peaks(resting_rsp_data["RSP_Clean"], sampling_rate=sampling_rate)
        # print(peaks)
        # print(info)
        resting_rsp = nk.rsp_intervalrelated(resting_rsp_data, sampling_rate=sampling_rate)
        resting_rsp = resting_rsp.rename(index={0: name})
        # print(resting_rsp)

        # Print RSA indices for resting state
        resting_rsa_dict = nk.hrv_rsa(resting_ecg_data, resting_rsp_data, ecg_info, sampling_rate=sampling_rate, continuous=False)
        # print(resting_rsa_dict)
        resting_rsa = pd.DataFrame([resting_rsa_dict])
        # print(resting_rsa)
        resting_rsa = resting_rsa.rename(index={0: name})

        # Combine RSA and RSP indices into single dataframe
        resting_rsarsp_data = pd.concat([resting_rsa, resting_rsp], axis=1)
        # print(resting_rsarsp_data)

        # Combine HRV and RSP indices into single dataframe
        resting_physio_data = pd.concat([resting_timefreq_data, resting_rsarsp_data], axis=1)

        # Add ECG quality check into dataframe "timefreq_data"
        resting_physio_data["ECG Quality"] = resting_quality

        # Insert subject code as first column
        resting_physio_data.insert(0, "Subject_Num", name)

        resting_data_df = resting_data_df._append(resting_physio_data, ignore_index = True)
        # print(resting_data_df)


    ## TRIALS ##

    trials = nk.events_find(data["LUX"], threshold=0, duration_min=10000, duration_max=210000, threshold_keep='below', 
                        event_labels=event_labels, 
                        event_conditions=event_conditions)
    
    # print(trials)

    rsp_trial_epochs = nk.epochs_create(rsp_signals, trials, epochs_start=0, epochs_end="from_events", 
                                        sampling_rate=sampling_rate,
                                        event_labels=event_labels, 
                                        event_conditions=event_conditions)
    ecg_trial_epochs = nk.epochs_create(ecg_signals, trials, epochs_start=0, epochs_end="from_events", 
                                        sampling_rate=sampling_rate,
                                        event_labels=event_labels, 
                                        event_conditions=event_conditions)
    for i, epoch in enumerate(ecg_trial_epochs):
        ecg_epoch = ecg_trial_epochs[epoch]  # iterate epochs",
        ecg_epoch = ecg_epoch[['Label', 'ECG_Clean', 'ECG_Rate']]  # Select relevant columns",
        title = "Trial"

        peaks, info = nk.ecg_peaks(ecg_epoch["ECG_Clean"], sampling_rate=sampling_rate)
        trial_quality = nk.ecg_quality(ecg_epoch["ECG_Clean"], rpeaks=info["ECG_R_Peaks"], sampling_rate=sampling_rate, method="zhao2018")
        trial_hrv_time_indices = nk.hrv_time(peaks, sampling_rate=sampling_rate, show=True)
        # plt.subplots_adjust(wspace=0.3, hspace=0.4)
        trial_time = trial_hrv_time_indices[["HRV_RMSSD", "HRV_SDNN", "HRV_MeanNN", "HRV_CVNN"]]
        trial_hrv_freq_indices = nk.hrv_frequency(peaks, sampling_rate=sampling_rate, show=True, normalize=True)
        trial_freq = trial_hrv_freq_indices[["HRV_LF", "HRV_HF", "HRV_LFHF", "HRV_LFn", "HRV_HFn"]]

        trial_time = trial_time.rename(index={0: name})
        trial_freq = trial_freq.rename(index={0: name})

        # Add resting heart rate into dataframe "trials_data_df"
        trial_HR_mean = [ecg_epoch["ECG_Rate"].mean()]
        # print(trial_HR_mean)

        # trials_data_df.insert(12, "Heart_Rate", trial_HR_mean)
        trial_timefreq_data = pd.concat([trial_time, trial_freq], axis=1)
        # print(trial_timefreq_data)
        trial_timefreq_data.insert(0, "Subject_Num", name)
        trial_timefreq_data.insert(1, "Excerpt_Num", event_labels[i])
        trial_timefreq_data.insert(2, "Condition", event_conditions[i])
        trial_timefreq_data.insert(3, "Heart Rate", trial_HR_mean)
        # print(i)
        trials_ecg_data_df = trials_ecg_data_df._append(trial_timefreq_data, ignore_index=True)
        # print(trials_ecg_data_df)

        

        # Plot and print RSP indices for trials
        # rsp_epoch = rsp_trial_epochs[epoch]
        # print(rsp_epoch)

        # peaks, info = nk.rsp_peaks(rsp_epoch["RSP_Clean"], sampling_rate=sampling_rate)
        # trials_rsp = nk.rsp_intervalrelated(rsp_epoch, sampling_rate=sampling_rate)
        # trials_rsp = trials_rsp.rename(index={0: name})
        # print(trials_rsp)
        # trials_rsp_data_df = trials_rsp_data_df._append(trials_rsp, ignore_index=True)
        # print(trials_rsp_data_df)

        # Print RSA indices for trials
        # trials_rsa_dict = nk.hrv_rsa(ecg_epoch, rsp_epoch, ecg_info, sampling_rate=sampling_rate, continuous=False)
        # print(trials_rsa_dict)
        # trials_rsa = pd.DataFrame([trials_rsa_dict])
        # print(trials_rsa)
        # trials_rsa = trials_rsa.rename(index={0: name})
        # trials_rsa_data_df = trials_rsa_data_df._append(trials_rsa, ignore_index=True)

        # Combine RSA and RSP indices into single dataframe
        # trials_rsarsp_data = pd.concat([trials_rsa_data_df, trials_rsp_data_df], axis=1)
        # print(trials_rsarsp_data)

        # Combine HRV and RSP indices into single dataframe
        trials_physio_data = pd.concat([trials_ecg_data_df], axis=1)
        print(trials_physio_data)
        print("next trial")
        plt.close()


    # print(ecg_trial_epochs)


# Save data
resting_data_df.to_csv("PROOF-physio-resting_Data.csv")
trials_physio_data.to_csv("PROOF-physio-trials_Data.csv")

# plt.show()



