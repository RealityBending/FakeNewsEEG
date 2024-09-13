import json

import os
import pandas as pd

## CHANGE DIRECTORY PATH BASED ON WHERE THE CSV FILES ARE STORED
files = os.listdir("C:/Users/wilson.lim/Desktop/New folder")
print(files)

# Loop through files ======================================================
alldata_sub = pd.DataFrame()  # Initialize empty dataframe
alldata_fakenews = pd.DataFrame()  # Initialize empty dataframe
## SET YOUR DIRECTORY PATH BASED ON WHERE THE CSV FILES ARE STORED
os.chdir("C:/Users/wilson.lim/Desktop/New folder")

# Loading stimuli_master.csv to retrieve condition data
## SET PATH BASED ON WHERE THE FAKENEWSEEG LOCAL REPOSITORY IS LOCATED
stimuli = pd.read_csv("C:/Users/wilson.lim/Desktop\PROOF/FakeNewsEEG/stimuli/stimuli_master.csv")

# Dataframe for PROOF_EEG_questionnairedata.csv
df = pd.DataFrame(columns=["Participant",
                            "Experiment_Duration",
                            "Date",
                            "Time",
                            "Browser",
                            "Mobile",
                            "Platform",
                            "Screen_Width",
                            "Screen_Height",
                            "Nationality",
                            "Gender",
                            "Ethnicity",
                            "Education",
                            "Discipline",
                            "Age",
                            "Student",
                            "English_Level",
                            "Years_Singapore",
                            "AI_Expertise",
                            "Discrimination_Ability",
                            "MediaFreq_Internet",
                            "MediaFreq_PhoneApps",
                            "MediaFreq_SocialMedia",
                            "MediaFreq_TV",
                            "MediaFreq_Newspapers",
                            "MediaFreq_Radio",
                            "News_Interest",
                            "News_Engagement",
                            "News_Sharing",
                            "News_Types",
                            "IPIP_Extraversion",
                            "IPIP_Agreeableness",
                            "IPIP_Conscientiousness",
                            "IPIP_Neuroticism",
                            "IPIP_Openness",
                            "IPIP_HonestyHumility",
                            "IPIP6_Extraversion_Q1",
                            "IPIP6_Extraversion_Q7_R",
                            "IPIP6_Extraversion_Q19_R",
                            "IPIP6_Extraversion_Q23",
                            "IPIP6_Agreeableness_Q2",
                            "IPIP6_Agreeableness_Q8_R",
                            "IPIP6_Agreeableness_Q14",
                            "IPIP6_Agreeableness_Q20_R",
                            "IPIP6_Conscientiousness_Q3",
                            "IPIP6_Conscientiousness_Q10",
                            "IPIP6_Conscientiousness_Q11_R",
                            "IPIP6_Conscientiousness_Q22_R",
                            "IPIP6_Neuroticism_Q4",
                            "IPIP6_Neuroticism_Q15_R",
                            "IPIP6_Neuroticism_Q16",
                            "IPIP6_Neuroticism_Q17_R",
                            "IPIP6_Openness_Q5",
                            "IPIP6_Openness_Q9_R",
                            "IPIP6_Openness_Q13_R",
                            "IPIP6_Openness_Q21_R",
                            "IPIP6_HonestyHumility_Q6_R",
                            "IPIP6_HonestyHumility_Q12_R",
                            "IPIP6_HonestyHumility_Q18_R",
                            "IPIP6_HonestyHumility_Q24_R",
                            "PID5_Total",
                            "PID5_Avg",
                            "PID5_Disinhibition_Total",
                            "PID5_Disinhibition_Avg",
                            "PID5_Detachment_Total",
                            "PID5_Detachment_Avg",
                            "PID5_Psychotism_Total",
                            "PID5_Psychotism_Avg",
                            "PID5_NegAffect_Total",
                            "PID5_NegAffect_Avg",
                            "PID5_Antagonism_Total",
                            "PID5_Antagonism_Avg",
                            "PID5_Disinhibition_1",
                            "PID5_Disinhibition_2",
                            "PID5_Disinhibition_3",
                            "PID5_Detachment_4",
                            "PID5_Disinhibition_5",
                            "PID5_Disinhibition_6",
                            "PID5_Psychoticism_7",
                            "PID5_NegativeAffect_8",
                            "PID5_NegativeAffect_9",
                            "PID5_NegativeAffect_10",
                            "PID5_NegativeAffect_11",
                            "PID5_Psychoticism_12",
                            "PID5_Detachment_13",
                            "PID5_Detachment_14",
                            "PID5_NegativeAffect_15",
                            "PID5_Detachment_16", 
                            "PID5_Antagonism_17",
                            "PID5_Detachment_18",
                            "PID5_Antagonism_19",
                            "PID5_Antagonism_20", 
                            "PID5_Psychoticism_21", 
                            "PID5_Antagonism_22",
                            "PID5_Psychoticism_23",
                            "PID5_Psychoticism_24",
                            "PID5_Antagonism_25",
                            "GAAIS_Positive_Total",
                            "GAAIS_Positive_Avg",
                            "GAAIS_Negative_Total",
                            "GAAIS_Negative_Avg",
                            "GAAIS_Positive_7",
                            "GAAIS_Positive_12",
                            "GAAIS_Positive_17",
                            "GAAIS_Negative_9",
                            "GAAIS_Negative_10",
                            "GAAIS_Negative_15",
                            "BAIT_Text_Avg",
                            "BAIT_Visual_Avg",
                            "BAIT_Visual_1",
                            "BAIT_Visual_2",
                            "BAIT_Visual_5",
                            "BAIT_Visual_6",
                            "BAIT_Text_7",
                            "BAIT_Text_8",
                            "GCB_GovernmentMalfeasance_Avg",
                            "GCB_MalevolentGlobalConspiracy_Avg",
                            "GCB_ETCoverUp_Avg",
                            "GCB_PersonalWellbeing_Avg",
                            "GCB_ControlofInformation_Avg",
                            "GCB_Avg",
                            "GCB_GovernmentMalfeasance_1",
                            "GCB_GovernmentMalfeasance_6",
                            "GCB_GovernmentMalfeasance_11",
                            "GCB_MalevolentGlobalConspiracy_2",
                            "GCB_MalevolentGlobalConspiracy_7",
                            "GCB_MalevolentGlobalConspiracy_12",
                            "GCB_ETCoverUp_3",
                            "GCB_ETCoverUp_8",
                            "GCB_ETCoverUp_13",
                            "GCB_PersonalWellbeing_4",
                            "GCB_PersonalWellbeing_9",
                            "GCB_PersonalWellbeing_14",
                            "GCB_ControlofInformation_5",
                            "GCB_ControlofInformation_10",
                            "GCB_ControlofInformation_15",
                            "IAS_Total",
                            "PHQ4_Total",
                            "PHQ4_Anxiety_Total",
                            "PHQ4_Depression_Total",
                            "PHQ4_Anxiety_1",
                            "PHQ4_Anxiety_2",
                            "PHQ4_Depression_3",
                            "PHQ4_Depression_4",
                            "Rest_DoM_1",
                            "Rest_DoM_2",
                            "Rest_DoM_3",
                            "Rest_ToM_1",
                            "Rest_ToM_2",
                            "Rest_ToM_3",
                            "Rest_Self_1",
                            "Rest_Self_2",
                            "Rest_Self_3",
                            "Rest_Plan_1",
                            "Rest_Plan_2",
                            "Rest_Plan_3",
                            "Rest_Sleep_1",
                            "Rest_Sleep_2",
                            "Rest_Sleep_3",
                            "Rest_Comfort_1",
                            "Rest_Comfort_2",
                            "Rest_Comfort_3",
                            "Rest_SomA_1",
                            "Rest_SomA_2",
                            "Rest_SomA_3",
                            "Excerpt_Num_List",
                            "Excerpt_Condition_List",])

for i, file in enumerate(files):
    print(f"File N°{i+1}/{len(files)}")

    data = pd.read_csv(file)
    print("File: " + file)

    # Participant ========================================================
    # data["screen"].unique()

    # Browser info -------------------------------------------------------
    browser = data[data["screen"] == "browser_info"].iloc[0]

    # Demographics -------------------------------------------------------
    demo1 = data[data["screen"] == "demographics_1"].iloc[0]
    demo1 = json.loads(demo1["response"])
    demo2 = data[data["screen"] == "demographics_2"].iloc[0]
    demo2 = json.loads(demo2["response"])
    debrief = data[data["screen"] == "demographics_debrief"].iloc[0]
    debrief = json.loads(debrief["response"])

    participant = file[:-4]
    experiment_duration = data["time_elapsed"].max() / 1000 / 60
    nationality = demo2["nationality"]
    gender = demo1["gender"]
    ethnicity = demo2["ethnicity"]
    education = demo1["education"]
    discipline = demo2["discipline"] 
    age = demo2["age"]
    student = demo1["student"]
    english_level = demo1["english"]
    years_singapore = demo2["years_singapore"]
    AI_expertise = demo1["ai_expertise"]
    discrimination_ability = debrief["discrimination_ability"]

    ## Questionnaires =============================================================

    # Media frequency and news types ----------------------------------------------
    media_freq = data[data["screen"] == "questionnaire_media_frequency"].iloc[0]
    media_freq = json.loads(media_freq["response"])

    mediaFreq_Internet = media_freq["newsfrequency_internet"]
    mediaFreq_PhoneApps = media_freq["newsfrequency_phoneapps"]
    mediaFreq_SocialMedia = media_freq["newsfrequency_socialmedia"]
    mediaFreq_TV = media_freq["newsfrequency_tv"]
    mediaFreq_Newspapers = media_freq["newsfrequency_newspapers"]
    mediaFreq_Radio = media_freq["newsfrequency_radio"]
    news_Interest = media_freq["news_interest"]
    news_Engagement = media_freq["news_engagement"]
    news_Sharing = media_freq["news_sharing"]

    news_read = data[data["screen"] == "questionnaire_news_types"].iloc[0]
    news_read = json.loads(news_read["response"])

    news_Types = news_read["type"]

    #IPIP6 ------------------------------------------------------------------------
    ipip6 = data[data["screen"] == "questionnaire_ipip6"].iloc[0]
    ipip6 = json.loads(ipip6["response"])

    IPIP_Extraversion = ((ipip6["Extraversion_1"] + 
                               (1 - ipip6["Extraversion_7_R"]) +
                               (1 - ipip6["Extraversion_19_R"]) +
                               ipip6["Extraversion_23"]) / 4)
    IPIP_Agreeableness = ((ipip6["Agreeableness_2"] + 
                               (1 - ipip6["Agreeableness_8_R"]) +
                               (1 - ipip6["Agreeableness_20_R"]) +
                               ipip6["Agreeableness_14"]) / 4)
    IPIP_Conscientiousness = ((ipip6["Conscientiousness_3"] + 
                               (1 - ipip6["Conscientiousness_11_R"]) +
                               (1 - ipip6["Conscientiousness_22_R"]) +
                               ipip6["Conscientiousness_10"]) / 4)
    IPIP_Neuroticism = ((ipip6["Neuroticism_4"] + 
                               (1 - ipip6["Neuroticism_15_R"]) +
                               (1 - ipip6["Neuroticism_17_R"]) +
                               ipip6["Neuroticism_16"]) / 4)
    IPIP_Openness = ((ipip6["Openness_5"] + 
                               (1 - ipip6["Openness_9_R"]) +
                               (1 - ipip6["Openness_13_R"]) +
                               (1 - ipip6["Openness_21_R"])) / 4)
    IPIP_HonestyHumility = (((1 - ipip6["HonestyHumility_6_R"]) + 
                               (1 - ipip6["HonestyHumility_12_R"]) +
                               (1 - ipip6["HonestyHumility_18_R"]) +
                               (1 - ipip6["HonestyHumility_24_R"])) / 4)

    IPIP6_Extraversion_Q1 = ipip6["Extraversion_1"]
    IPIP6_Extraversion_Q7_R = 1 - ipip6["Extraversion_7_R"]
    IPIP6_Extraversion_Q19_R = 1 - ipip6["Extraversion_19_R"]
    IPIP6_Extraversion_Q23 = ipip6["Extraversion_23"]
    IPIP6_Agreeableness_Q2 = ipip6["Agreeableness_2"]
    IPIP6_Agreeableness_Q8_R = 1 - ipip6["Agreeableness_8_R"]
    IPIP6_Agreeableness_Q14 = ipip6["Agreeableness_14"]
    IPIP6_Agreeableness_Q20_R = 1 - ipip6["Agreeableness_20_R"]
    IPIP6_Conscientiousness_Q3 = ipip6["Conscientiousness_3"]
    IPIP6_Conscientiousness_Q10 = ipip6["Conscientiousness_10"]
    IPIP6_Conscientiousness_Q11_R = 1- ipip6["Conscientiousness_11_R"]
    IPIP6_Conscientiousness_Q22_R = 1- ipip6["Conscientiousness_22_R"]
    IPIP6_Neuroticism_Q4 = ipip6["Neuroticism_4"]
    IPIP6_Neuroticism_Q15_R = 1 - ipip6["Neuroticism_15_R"]
    IPIP6_Neuroticism_Q16 = ipip6["Neuroticism_16"]
    IPIP6_Neuroticism_Q17_R = 1 - ipip6["Neuroticism_17_R"]
    IPIP6_Openness_Q5 = ipip6["Openness_5"]
    IPIP6_Openness_Q9_R = 1 - ipip6["Openness_9_R"]
    IPIP6_Openness_Q13_R = 1 - ipip6["Openness_13_R"]
    IPIP6_Openness_Q21_R = 1 - ipip6["Openness_21_R"]
    IPIP6_HonestyHumility_Q6_R = 1 - ipip6["HonestyHumility_6_R"]
    IPIP6_HonestyHumility_Q12_R = 1 - ipip6["HonestyHumility_12_R"]
    IPIP6_HonestyHumility_Q18_R = 1 - ipip6["HonestyHumility_18_R"]
    IPIP6_HonestyHumility_Q24_R = 1 - ipip6["HonestyHumility_24_R"]

    # PID5 -----------------------------------------------------------------------
    pid5 = data[data["screen"] == "questionnaire_pid5"].iloc[0]
    pid5 = json.loads(pid5["response"])

    PID5_Total = (pid5["Disinhibition_1"] +
                    pid5["Disinhibition_2"] +
                    pid5["Disinhibition_3"] +
                    pid5["Detachment_4"] +
                    pid5["Disinhibition_5"] +
                    pid5["Disinhibition_6"] +
                    pid5["Psychoticism_7"] +
                    pid5["NegativeAffect_8"] +
                    pid5["NegativeAffect_9"] +
                    pid5["NegativeAffect_10"] +
                    pid5["NegativeAffect_11"] +
                    pid5["Psychoticism_12"] +
                    pid5["Detachment_13"] +
                    pid5["Detachment_14"] +
                    pid5["NegativeAffect_15"] +
                    pid5["Detachment_16"] +
                    pid5["Antagonism_17"] +
                    pid5["Detachment_18"] +
                    pid5["Antagonism_19"] +
                    pid5["Antagonism_20"] +
                    pid5["Psychoticism_21"] +
                    pid5["Antagonism_22"] +
                    pid5["Psychoticism_23"] +
                    pid5["Psychoticism_24"] +
                    pid5["Antagonism_25"])
    PID5_Avg = (pid5["Disinhibition_1"] +
                    pid5["Disinhibition_2"] +
                    pid5["Disinhibition_3"] +
                    pid5["Detachment_4"] +
                    pid5["Disinhibition_5"] +
                    pid5["Disinhibition_6"] +
                    pid5["Psychoticism_7"] +
                    pid5["NegativeAffect_8"] +
                    pid5["NegativeAffect_9"] +
                    pid5["NegativeAffect_10"] +
                    pid5["NegativeAffect_11"] +
                    pid5["Psychoticism_12"] +
                    pid5["Detachment_13"] +
                    pid5["Detachment_14"] +
                    pid5["NegativeAffect_15"] +
                    pid5["Detachment_16"] +
                    pid5["Antagonism_17"] +
                    pid5["Detachment_18"] +
                    pid5["Antagonism_19"] +
                    pid5["Antagonism_20"] +
                    pid5["Psychoticism_21"] +
                    pid5["Antagonism_22"] +
                    pid5["Psychoticism_23"] +
                    pid5["Psychoticism_24"] +
                    pid5["Antagonism_25"]) / 25
    PID5_Disinhibition_Total = (pid5["Disinhibition_1"] +
                    pid5["Disinhibition_2"] +
                    pid5["Disinhibition_3"] +
                    pid5["Disinhibition_5"] +
                    pid5["Disinhibition_6"])
    PID5_Disinhibition_Avg = (pid5["Disinhibition_1"] +
                    pid5["Disinhibition_2"] +
                    pid5["Disinhibition_3"] +
                    pid5["Disinhibition_5"] +
                    pid5["Disinhibition_6"]) / 5
    PID5_Detachment_Total = (pid5["Detachment_4"] +
                    pid5["Detachment_13"] +
                    pid5["Detachment_14"] +
                    pid5["Detachment_16"] +
                    pid5["Detachment_18"])
    PID5_Detachment_Avg = (pid5["Detachment_4"] +
                    pid5["Detachment_13"] +
                    pid5["Detachment_14"] +
                    pid5["Detachment_16"] +
                    pid5["Detachment_18"]) / 5
    PID5_Psychotism_Total = (pid5["Psychoticism_7"] +
                    pid5["Psychoticism_12"] +
                    pid5["Psychoticism_21"] +
                    pid5["Psychoticism_23"] +
                    pid5["Psychoticism_24"])
    PID5_Psychotism_Avg = (pid5["Psychoticism_7"] +
                    pid5["Psychoticism_12"] +
                    pid5["Psychoticism_21"] +
                    pid5["Psychoticism_23"] +
                    pid5["Psychoticism_24"]) / 5
    PID5_NegAffect_Total = (pid5["NegativeAffect_8"] +
                    pid5["NegativeAffect_9"] +
                    pid5["NegativeAffect_10"] +
                    pid5["NegativeAffect_11"] +
                    pid5["NegativeAffect_15"])
    PID5_NegAffect_Avg = (pid5["NegativeAffect_8"] +
                    pid5["NegativeAffect_9"] +
                    pid5["NegativeAffect_10"] +
                    pid5["NegativeAffect_11"] +
                    pid5["NegativeAffect_15"]) / 5
    PID5_Antagonism_Total = (pid5["Antagonism_17"] +
                    pid5["Antagonism_19"] +
                    pid5["Antagonism_20"] +
                    pid5["Antagonism_22"] +
                    pid5["Antagonism_25"])
    PID5_Antagonism_Avg = (pid5["Antagonism_17"] +
                    pid5["Antagonism_19"] +
                    pid5["Antagonism_20"] +
                    pid5["Antagonism_22"] +
                    pid5["Antagonism_25"]) / 5  
    
    PID5_Disinhibition_1 = pid5["Disinhibition_1"]
    PID5_Disinhibition_2 = pid5["Disinhibition_2"]
    PID5_Disinhibition_3 = pid5["Disinhibition_3"] 
    PID5_Detachment_4 = pid5["Detachment_4"] 
    PID5_Disinhibition_5 = pid5["Disinhibition_5"] 
    PID5_Disinhibition_6 = pid5["Disinhibition_6"] 
    PID5_Psychoticism_7 = pid5["Psychoticism_7"] 
    PID5_NegativeAffect_8 = pid5["NegativeAffect_8"] 
    PID5_NegativeAffect_9 = pid5["NegativeAffect_9"] 
    PID5_NegativeAffect_10 = pid5["NegativeAffect_10"] 
    PID5_NegativeAffect_11 = pid5["NegativeAffect_11"] 
    PID5_Psychoticism_12 = pid5["Psychoticism_12"] 
    PID5_Detachment_13 = pid5["Detachment_13"] 
    PID5_Detachment_14 = pid5["Detachment_14"] 
    PID5_NegativeAffect_15 = pid5["NegativeAffect_15"] 
    PID5_Detachment_16 = pid5["Detachment_16"] 
    PID5_Antagonism_17 = pid5["Antagonism_17"] 
    PID5_Detachment_18 = pid5["Detachment_18"] 
    PID5_Antagonism_19 = pid5["Antagonism_19"] 
    PID5_Antagonism_20 = pid5["Antagonism_20"] 
    PID5_Psychoticism_21 = pid5["Psychoticism_21"] 
    PID5_Antagonism_22 = pid5["Antagonism_22"] 
    PID5_Psychoticism_23 = pid5["Psychoticism_23"] 
    PID5_Psychoticism_24 = pid5["Psychoticism_24"] 
    PID5_Antagonism_25 = pid5["Antagonism_25"]
    
    # BAIT + GAAIS --------------------------------------------------------------
    bait = data[data["screen"] == "questionnaire_bait"].iloc[0]
    bait = json.loads(bait["response"]) 

    GAAIS_Positive_Total = (bait["GAAIS_Positive_7"] +
                                bait["GAAIS_Positive_12"] +
                                bait["GAAIS_Positive_17"])
    GAAIS_Positive_Avg = (bait["GAAIS_Positive_7"] +
                            bait["GAAIS_Positive_12"] +
                            bait["GAAIS_Positive_17"]) / 3
    GAAIS_Negative_Total = (bait["GAAIS_Negative_9"] +
                                bait["GAAIS_Negative_10"] +
                                bait["GAAIS_Negative_15"])
    GAAIS_Negative_Avg = (bait["GAAIS_Negative_9"] +
                                bait["GAAIS_Negative_10"] +
                                bait["GAAIS_Negative_15"]) / 3
    BAIT_Text_Avg = (bait["BAIT_7_TextRealistic"] +
                     bait["BAIT_8_TextIssues"]) / 2
    BAIT_Visual_Avg = (bait["BAIT_1_ImagesRealistic"] +
                       bait["BAIT_2_ImagesIssues"] +
                       bait["BAIT_5_ImitatingReality"] +
                       bait["BAIT_6_EnvironmentReal"]) / 4
    
    GAAIS_Positive_7 = bait["GAAIS_Positive_7"]
    GAAIS_Positive_12 = bait["GAAIS_Positive_12"]
    GAAIS_Positive_17 = bait["GAAIS_Positive_17"]
    GAAIS_Negative_9 = bait["GAAIS_Negative_9"]
    GAAIS_Negative_10 = bait["GAAIS_Negative_10"]
    GAAIS_Negative_15 = bait["GAAIS_Negative_15"]

    BAIT_Visual_1 = bait["BAIT_1_ImagesRealistic"]
    BAIT_Visual_2 = bait["BAIT_2_ImagesIssues"]
    BAIT_Visual_5 = bait["BAIT_5_ImitatingReality"]
    BAIT_Visual_6 = bait["BAIT_6_EnvironmentReal"]
    BAIT_Text_7 = bait["BAIT_7_TextRealistic"]
    BAIT_Text_8 = bait["BAIT_8_TextIssues"]

    # GCB -----------------------------------------------------------------------
    gcb = data[data["screen"] == "questionnaire_gcb"].iloc[0]
    gcb = json.loads(gcb["response"]) 

    GCB_GovernmentMalfeasance_Avg = (gcb["GovernmentMalfeasance_1"] +
                                     gcb["GovernmentMalfeasance_6"] +
                                     gcb["GovernmentMalfeasance_11"]) / 3
    GCB_MalevolentGlobalConspiracy_Avg = (gcb["MalevolentGlobalConspiracy_2"] +
                                          gcb["MalevolentGlobalConspiracy_7"] +
                                          gcb["MalevolentGlobalConspiracy_12"]) / 3
    GCB_ETCoverUp_Avg = (gcb["ETCoverUp_3"] +
                         gcb["ETCoverUp_8"] +
                         gcb["ETCoverUp_13"]) / 3
    GCB_PersonalWellbeing_Avg = (gcb["PersonalWellbeing_4"] +
                                 gcb["PersonalWellbeing_9"] +
                                 gcb["PersonalWellbeing_14"]) / 3
    GCB_ControlofInformation_Avg = (gcb["ControlofInformation_5"] +
                                    gcb["ControlofInformation_10"] +
                                    gcb["ControlofInformation_15"]) / 3
    GCB_Avg = (GCB_GovernmentMalfeasance_Avg +
               GCB_MalevolentGlobalConspiracy_Avg +
               GCB_ETCoverUp_Avg +
               GCB_PersonalWellbeing_Avg +
               GCB_ControlofInformation_Avg) / 5

    GCB_GovernmentMalfeasance_1 = gcb["GovernmentMalfeasance_1"]
    GCB_GovernmentMalfeasance_6 = gcb["GovernmentMalfeasance_6"]
    GCB_GovernmentMalfeasance_11 = gcb["GovernmentMalfeasance_11"]
    GCB_MalevolentGlobalConspiracy_2 = gcb["MalevolentGlobalConspiracy_2"]
    GCB_MalevolentGlobalConspiracy_7 = gcb["MalevolentGlobalConspiracy_7"]
    GCB_MalevolentGlobalConspiracy_12 = gcb["MalevolentGlobalConspiracy_12"]
    GCB_ETCoverUp_3 = gcb["ETCoverUp_3"]
    GCB_ETCoverUp_8 = gcb["ETCoverUp_8"]
    GCB_ETCoverUp_13 = gcb["ETCoverUp_13"]
    GCB_PersonalWellbeing_4 = gcb["PersonalWellbeing_4"]
    GCB_PersonalWellbeing_9 = gcb["PersonalWellbeing_9"]
    GCB_PersonalWellbeing_14 = gcb["PersonalWellbeing_14"]
    GCB_ControlofInformation_5 = gcb["ControlofInformation_5"]
    GCB_ControlofInformation_10 = gcb["ControlofInformation_10"]
    GCB_ControlofInformation_15 = gcb["ControlofInformation_15"]

    # IAS ----------------------------------------------------------------------------
    ias = data[data["screen"] == "questionnaire_ias"].iloc[0]
    ias = json.loads(ias["response"]) 

    IAS_Total = (ias["Heart_1"] +
                 ias["Hungry_2"] +
                 ias["Breathing_3"] +
                 ias["Thirsty_4"] +
                 ias["Urinate_5"] +
                 ias["Defecate_6"] +
                 ias["Taste_7"] +
                 ias["Vomit_8"] +
                 ias["Sneeze_9"] +
                 ias["Cough_10"] +
                 ias["Temperature_11"] +
                 ias["Sexual-Arousal_12"] +
                 ias["Wind_13"] +
                 ias["Burp_14"] +
                 ias["Muscles_15"] +
                 ias["Bruise_16"] +
                 ias["Pain_17"] +
                 ias["Blood-Sugar_18"] +
                 ias["Affective-Touch_19"] +
                 ias["Tickle_20"] +
                 ias["Itch_21"])
    
    # PHQ4 ----------------------------------------------------------------------------
    phq4 = data[data["screen"] == "questionnaire_phq4"].iloc[0]
    phq4 = json.loads(phq4["response"]) 

    PHQ4_Total = (phq4["Anxiety_1"] +
                  phq4["Anxiety_2"] +
                  phq4["Depression_3"] +
                  phq4["Depression_4"])
    PHQ4_Anxiety_Total = (phq4["Anxiety_1"] +
                          phq4["Anxiety_2"])
    PHQ4_Depression_Total = (phq4["Depression_3"] + 
                             phq4["Depression_4"])
    PHQ4_Anxiety_1 = phq4["Anxiety_1"]
    PHQ4_Anxiety_2 = phq4["Anxiety_2"]
    PHQ4_Depression_3 = phq4["Depression_3"]
    PHQ4_Depression_4 = phq4["Depression_4"]

    # Resting state questionnaire -----------------------------------------------------
    rest = data[data["screen"] == "questionnaire_restingstate"].iloc[0]
    rest = json.loads(rest["response"]) 
    
    Rest_DoM_1 = rest["DoM_1"]
    Rest_DoM_2 = rest["DoM_2"]
    Rest_DoM_3 = rest["DoM_3"]
    Rest_ToM_1 = rest["ToM_1"]
    Rest_ToM_2 = rest["ToM_2"]
    Rest_ToM_3 = rest["ToM_3"]
    Rest_Self_1 = rest["Self_1"]
    Rest_Self_2 = rest["Self_2"]
    Rest_Self_3 = rest["Self_3"]
    Rest_Plan_1 = rest["Plan_1"]
    Rest_Plan_2 = rest["Plan_2"]
    Rest_Plan_3 = rest["Plan_3"]
    Rest_Sleep_1 = rest["Sleep_1"]
    Rest_Sleep_2 = rest["Sleep_2"]
    Rest_Sleep_3 = rest["Sleep_3"]
    Rest_Comfort_1 = rest["Comfort_1"]
    Rest_Comfort_2 = rest["Comfort_2"]
    Rest_Comfort_3 = rest["Comfort_3"]
    Rest_SomA_1 = rest["SomA_1"]
    Rest_SomA_2 = rest["SomA_2"]
    Rest_SomA_3 = rest["SomA_3"]
   
    ## Fake/Real News ====================================================================

    fakenews_text = data[data["screen"] == "fakenews_text"]
    fakenews_ratings_reality = data[data["screen"] == "fakenews_ratings_reality"].iloc[0:40]
    fakenews_ratings_appraisal = data[data["screen"] == "fakenews_ratings_appraisal"].iloc[0:40]

    excerpt_num_list = []
    excerpt_condition_list = []
    excerpt_viewingtime_list = []
    excerpt_reality_realfake_list = []
    excerpt_reality_humanai_list = []
    excerpt_appraisal_importance_list = []
    excerpt_appraisal_emotionality_list = []
    excerpt_appraisal_engaging_list = []
    excerpt_appraisal_relevance_list = []

    # To extract excerpt numbers for all excerpts per participant
    for excerpt in fakenews_text["stimulus"]:
        excerpt_num = excerpt.rsplit(">",2)
        excerpt_num = excerpt_num[1].rsplit("<")
        excerpt_num = excerpt_num[0]
        excerpt_num_list.append(excerpt_num)
        try:
            idx = stimuli[stimuli["excerpt_num"] == int(excerpt_num)].index.values
            excerpt_condition_list.append(stimuli.at[idx[0], "condition"])
        except ValueError:
            excerpt_condition_list.append("practice")
    excerpt_num_list_final = excerpt_num_list[2:]
    excerpt_condition_list_final = excerpt_condition_list[2:]

    # To extract total time taken to read each excerpt    
    for excerpt in fakenews_text["rt"]:
        excerpt_viewingtime_list.append(excerpt/1000)
    excerpt_viewingtime_list_final = excerpt_viewingtime_list[2:]

    # To extract answers for reality belief questions (Fake - Real: -1 to 1, AI - Human: 0 - 1)
    for i in range(len(fakenews_ratings_reality["response"])):
        reality = json.loads(fakenews_ratings_reality["response"].iloc[i])
        if fakenews_ratings_reality["ticks_real"].iloc[0] == "Positive_Fake":
            excerpt_reality_realfake_list.append(reality["Reality"]*-1)
        else:
            excerpt_reality_realfake_list.append(reality["Reality"])
        if fakenews_ratings_reality["ticks_ai"].iloc[0] == "Positive_AI":
            excerpt_reality_humanai_list.append(round(1 - reality["Artificiality"],2))
        else:
            excerpt_reality_humanai_list.append(reality["Artificiality"])

    # To extract answers for appraisal questions
    for i in range(len(fakenews_ratings_appraisal["response"])):
        appraisal = json.loads(fakenews_ratings_appraisal["response"].iloc[i])
        excerpt_appraisal_importance_list.append(appraisal["Importance"])
        excerpt_appraisal_emotionality_list.append(appraisal["Emotionality"])
        excerpt_appraisal_engaging_list.append(appraisal["Engaging"])
        excerpt_appraisal_relevance_list.append(appraisal["Relevance"]) 

    # Dataframe for data_fakenews.csv
    fn = pd.DataFrame(columns=["Participant",
                               "Experiment_Duration",
                               "Date",
                               "Time",
                               "Browser",
                               "Mobile",
                               "Platform",
                               "Screen_Width",
                               "Screen_Height",
                               "Excerpt_Num",
                               "Excerpt_Condition",
                               "Excerpt_RT",
                               "Excerpt_Reality_FakeReal",
                               "Excerpt_Reality_HumanAI",
                               "Excerpt_Importance",
                               "Excerpt_Emotionality",
                               "Excerpt_Engaging",
                               "Excerpt_Relevance"])

    for i in range(len(excerpt_num_list_final)):
        new_row = {
            "Participant": participant,
            "Experiment_Duration": data["time_elapsed"].max() / 1000 / 60,
            "Date": browser["date"],
            "Time": browser["time"],
            "Browser": browser["browser"],
            "Mobile": browser["mobile"],
            "Platform": browser["os"],
            "Screen_Width": browser["screen_width"],
            "Screen_Height": browser["screen_height"],
            "Excerpt_Num": excerpt_num_list_final[i],
            "Excerpt_Condition": excerpt_condition_list_final[i],
            "Excerpt_RT": excerpt_viewingtime_list_final[i],
            "Excerpt_Reality_FakeReal": excerpt_reality_realfake_list[i],
            "Excerpt_Reality_HumanAI": excerpt_reality_humanai_list[i],
            "Excerpt_Importance": excerpt_appraisal_importance_list[i],
            "Excerpt_Emotionality": excerpt_appraisal_emotionality_list[i],
            "Excerpt_Engaging": excerpt_appraisal_engaging_list[i],
            "Excerpt_Relevance": excerpt_appraisal_relevance_list[i]
        }
        fn = fn._append(new_row, ignore_index=True)    

    # Merge ----------------------------------------------------------------
    
    alldata_fakenews = pd.concat([alldata_fakenews, fn], axis=0, ignore_index=True)

    ## Finalising questionnaire file
    
    # Append row for each participant into dataframe
    new_row_df = {
            "Participant": participant,
            "Experiment_Duration": data["time_elapsed"].max() / 1000 / 60,
            "Date": browser["date"],
            "Time": browser["time"],
            "Browser": browser["browser"],
            "Mobile": browser["mobile"],
            "Platform": browser["os"],
            "Screen_Width": browser["screen_width"],
            "Screen_Height": browser["screen_height"],
            "Nationality": nationality,
            "Gender": gender,
            "Ethnicity": ethnicity,
            "Education": education,
            "Discipline": discipline,
            "Age": age,
            "Student": student,
            "English_Level": english_level,
            "Years_Singapore": years_singapore,
            "AI_Expertise": AI_expertise,
            "Discrimination_Ability": discrimination_ability,
            "MediaFreq_Internet": mediaFreq_Internet,
            "MediaFreq_PhoneApps": mediaFreq_PhoneApps,
            "MediaFreq_SocialMedia": mediaFreq_SocialMedia,
            "MediaFreq_TV": mediaFreq_TV,
            "MediaFreq_Newspapers": mediaFreq_Newspapers,
            "MediaFreq_Radio": mediaFreq_Radio,
            "News_Interest": news_Interest,
            "News_Engagement": news_Engagement,
            "News_Sharing": news_Sharing,
            "News_Types": news_Types,
            "IPIP_Extraversion": IPIP_Extraversion,
            "IPIP_Agreeableness": IPIP_Agreeableness,
            "IPIP_Conscientiousness": IPIP_Conscientiousness,
            "IPIP_Neuroticism": IPIP_Neuroticism,
            "IPIP_Openness": IPIP_Openness,
            "IPIP_HonestyHumility": IPIP_HonestyHumility,
            "IPIP6_Extraversion_Q1": IPIP6_Extraversion_Q1,
            "IPIP6_Extraversion_Q7_R": IPIP6_Extraversion_Q7_R,
            "IPIP6_Extraversion_Q19_R": IPIP6_Extraversion_Q19_R,
            "IPIP6_Extraversion_Q23": IPIP6_Extraversion_Q23,
            "IPIP6_Agreeableness_Q2": IPIP6_Agreeableness_Q2,
            "IPIP6_Agreeableness_Q8_R": IPIP6_Agreeableness_Q8_R,
            "IPIP6_Agreeableness_Q14": IPIP6_Agreeableness_Q14,
            "IPIP6_Agreeableness_Q20_R": IPIP6_Agreeableness_Q20_R,
            "IPIP6_Conscientiousness_Q3": IPIP6_Conscientiousness_Q3,
            "IPIP6_Conscientiousness_Q10": IPIP6_Conscientiousness_Q10,
            "IPIP6_Conscientiousness_Q11_R": IPIP6_Conscientiousness_Q11_R,
            "IPIP6_Conscientiousness_Q22_R": IPIP6_Conscientiousness_Q22_R,
            "IPIP6_Neuroticism_Q4": IPIP6_Neuroticism_Q4,
            "IPIP6_Neuroticism_Q15_R": IPIP6_Neuroticism_Q15_R,
            "IPIP6_Neuroticism_Q16": IPIP6_Neuroticism_Q16,
            "IPIP6_Neuroticism_Q17_R": IPIP6_Neuroticism_Q17_R,
            "IPIP6_Openness_Q5": IPIP6_Openness_Q5,
            "IPIP6_Openness_Q9_R": IPIP6_Openness_Q9_R,
            "IPIP6_Openness_Q13_R": IPIP6_Openness_Q13_R,
            "IPIP6_Openness_Q21_R": IPIP6_Openness_Q21_R,
            "IPIP6_HonestyHumility_Q6_R": IPIP6_HonestyHumility_Q6_R,
            "IPIP6_HonestyHumility_Q12_R": IPIP6_HonestyHumility_Q12_R,
            "IPIP6_HonestyHumility_Q18_R": IPIP6_HonestyHumility_Q18_R,
            "IPIP6_HonestyHumility_Q24_R": IPIP6_HonestyHumility_Q24_R,
            "PID5_Total": PID5_Total,
            "PID5_Avg": PID5_Avg,
            "PID5_Disinhibition_Total": PID5_Disinhibition_Total,
            "PID5_Disinhibition_Avg": PID5_Disinhibition_Avg,
            "PID5_Detachment_Total": PID5_Detachment_Total,
            "PID5_Detachment_Avg": PID5_Detachment_Avg,
            "PID5_Psychotism_Total": PID5_Psychotism_Total,
            "PID5_Psychotism_Avg": PID5_Psychotism_Avg,
            "PID5_NegAffect_Total": PID5_NegAffect_Total,
            "PID5_NegAffect_Avg": PID5_NegAffect_Avg,
            "PID5_Antagonism_Total": PID5_Antagonism_Total,
            "PID5_Antagonism_Avg": PID5_Antagonism_Avg,
            "PID5_Disinhibition_1": PID5_Disinhibition_1,
            "PID5_Disinhibition_2": PID5_Disinhibition_2,
            "PID5_Disinhibition_3": PID5_Disinhibition_3,
            "PID5_Detachment_4": PID5_Detachment_4,
            "PID5_Disinhibition_5": PID5_Disinhibition_5,
            "PID5_Disinhibition_6": PID5_Disinhibition_6,
            "PID5_Psychoticism_7": PID5_Psychoticism_7,
            "PID5_NegativeAffect_8": PID5_NegativeAffect_8,
            "PID5_NegativeAffect_9": PID5_NegativeAffect_9,
            "PID5_NegativeAffect_10": PID5_NegativeAffect_10,
            "PID5_NegativeAffect_11": PID5_NegativeAffect_11,
            "PID5_Psychoticism_12": PID5_Psychoticism_12,
            "PID5_Detachment_13": PID5_Detachment_13,
            "PID5_Detachment_14": PID5_Detachment_14,
            "PID5_NegativeAffect_15": PID5_NegativeAffect_15,
            "PID5_Detachment_16": PID5_Detachment_16,
            "PID5_Antagonism_17": PID5_Antagonism_17,
            "PID5_Detachment_18": PID5_Detachment_18,
            "PID5_Antagonism_19": PID5_Antagonism_19,
            "PID5_Antagonism_20": PID5_Antagonism_20,
            "PID5_Psychoticism_21": PID5_Psychoticism_21,
            "PID5_Antagonism_22": PID5_Antagonism_22,
            "PID5_Psychoticism_23": PID5_Psychoticism_23,
            "PID5_Psychoticism_24": PID5_Psychoticism_24,
            "PID5_Antagonism_25": PID5_Antagonism_25,
            "GAAIS_Positive_Total": GAAIS_Positive_Total,
            "GAAIS_Positive_Avg": GAAIS_Positive_Avg,
            "GAAIS_Negative_Total": GAAIS_Negative_Total,
            "GAAIS_Negative_Avg": GAAIS_Negative_Avg,
            "GAAIS_Positive_7": GAAIS_Positive_7,
            "GAAIS_Positive_12": GAAIS_Positive_12,
            "GAAIS_Positive_17": GAAIS_Positive_17,
            "GAAIS_Negative_9": GAAIS_Negative_9,
            "GAAIS_Negative_10":GAAIS_Negative_10,
            "GAAIS_Negative_15": GAAIS_Negative_15,
            "BAIT_Text_Avg": BAIT_Text_Avg,
            "BAIT_Visual_Avg": BAIT_Visual_Avg,
            "BAIT_Visual_1": BAIT_Visual_1,
            "BAIT_Visual_2": BAIT_Visual_2,
            "BAIT_Visual_5": BAIT_Visual_5,
            "BAIT_Visual_6": BAIT_Visual_6,
            "BAIT_Text_7": BAIT_Text_7,
            "BAIT_Text_8": BAIT_Text_8,
            "GCB_GovernmentMalfeasance_Avg": GCB_GovernmentMalfeasance_Avg,
            "GCB_MalevolentGlobalConspiracy_Avg": GCB_MalevolentGlobalConspiracy_Avg,
            "GCB_ETCoverUp_Avg": GCB_ETCoverUp_Avg,
            "GCB_PersonalWellbeing_Avg": GCB_PersonalWellbeing_Avg,
            "GCB_ControlofInformation_Avg": GCB_ControlofInformation_Avg,
            "GCB_Avg": GCB_Avg,
            "GCB_GovernmentMalfeasance_1": GCB_GovernmentMalfeasance_1,
            "GCB_GovernmentMalfeasance_6": GCB_GovernmentMalfeasance_6,
            "GCB_GovernmentMalfeasance_11": GCB_GovernmentMalfeasance_11,
            "GCB_MalevolentGlobalConspiracy_2": GCB_MalevolentGlobalConspiracy_2,
            "GCB_MalevolentGlobalConspiracy_7": GCB_MalevolentGlobalConspiracy_7,
            "GCB_MalevolentGlobalConspiracy_12": GCB_MalevolentGlobalConspiracy_12,
            "GCB_ETCoverUp_3": GCB_ETCoverUp_3,
            "GCB_ETCoverUp_8": GCB_ETCoverUp_8,
            "GCB_ETCoverUp_13": GCB_ETCoverUp_13,
            "GCB_PersonalWellbeing_4": GCB_PersonalWellbeing_4,
            "GCB_PersonalWellbeing_9": GCB_PersonalWellbeing_9,
            "GCB_PersonalWellbeing_14": GCB_PersonalWellbeing_14,
            "GCB_ControlofInformation_5": GCB_ControlofInformation_5,
            "GCB_ControlofInformation_10": GCB_ControlofInformation_10,
            "GCB_ControlofInformation_15": GCB_ControlofInformation_15,
            "IAS_Total": IAS_Total,
            "PHQ4_Total": PHQ4_Total,
            "PHQ4_Anxiety_Total": PHQ4_Anxiety_Total,
            "PHQ4_Depression_Total": PHQ4_Depression_Total,
            "PHQ4_Anxiety_1": PHQ4_Anxiety_1,
            "PHQ4_Anxiety_2":PHQ4_Anxiety_2,
            "PHQ4_Depression_3": PHQ4_Depression_3,
            "PHQ4_Depression_4": PHQ4_Depression_4,
            "Rest_DoM_1": Rest_DoM_1,
            "Rest_DoM_2": Rest_DoM_2,
            "Rest_DoM_3": Rest_DoM_3,
            "Rest_ToM_1": Rest_ToM_1,
            "Rest_ToM_2": Rest_ToM_2,
            "Rest_ToM_3": Rest_ToM_3,
            "Rest_Self_1": Rest_Self_1,
            "Rest_Self_2": Rest_Self_2,
            "Rest_Self_3": Rest_Self_3,
            "Rest_Plan_1": Rest_Plan_1,
            "Rest_Plan_2": Rest_Plan_2,
            "Rest_Plan_3": Rest_Plan_3,
            "Rest_Sleep_1": Rest_Sleep_1,
            "Rest_Sleep_2": Rest_Sleep_2,
            "Rest_Sleep_3": Rest_Sleep_3,
            "Rest_Comfort_1": Rest_Comfort_1,
            "Rest_Comfort_2": Rest_Comfort_2,
            "Rest_Comfort_3": Rest_Comfort_3,
            "Rest_SomA_1": Rest_SomA_1,
            "Rest_SomA_2": Rest_SomA_2,
            "Rest_SomA_3": Rest_SomA_3,
            "Excerpt_Num_List": excerpt_num_list,
            "Excerpt_Condition_List": excerpt_condition_list,
    }
    # print(new_row_df)
    df = df._append(new_row_df, ignore_index=True) 
    print(df)

alldata_sub = pd.concat([alldata_sub, df], axis=0, ignore_index=True)

## Save =====================================================================
## SET PATHS TO WHERE YOU WANT TO SAVE THE OUTPUT FILES
alldata_sub.to_csv("C:/Users/wilson.lim/Desktop/PROOF_EEG_questionnairedata.csv", index=False)
alldata_fakenews.to_csv("C:/Users/wilson.lim/Desktop/PROOF_EEG_behaviouraldata.csv", index=False)
print("Done!")
print(excerpt_num_list)
print(excerpt_condition_list)
