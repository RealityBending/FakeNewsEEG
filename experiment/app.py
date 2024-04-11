from flask import Flask, render_template, request
import tobii_research as tr 
import pandas as pd
import csv

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

def check_eye_tracker_connection():
    # Code to check if Tobii eye tracker is connected
    eye_trackers = tr.find_all_eyetrackers()
    if eye_trackers:
        print(eye_trackers[0])
        return True  # Assuming only one eye tracker is connected
    else:
        return False
    # Return True if connected, False otherwise

# To start eye tracking
def get_eye_tracking_data():
    found_eye_trackers = tr.find_all_eyetrackers()
    eye_tracker = found_eye_trackers[0]
    global eye_trackers
    eye_trackers = eye_tracker
    eye_trackers.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
    print("Eye tracking data streaming started.")
    return True

# To pause eye tracking
def pause_eye_tracking_data():
    # found_eye_trackers = tr.find_all_eyetrackers()
    # eye_trackers = found_eye_trackers[0]
    eye_trackers.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
    print("Eye tracking data streaming paused.")
    # df_eyetr_dict = pd.DataFrame({'name':global_gaze_data.keys(), 'value':global_gaze_data.values})
    print("Last received gaze package:")
    print("Gaze data so far:")
    # print(df_eyetr_dict)
    # print(df_final_eyetr_dict)
    csvfile.close()
    print("CSV file closed.")
    print(csvfile)

# Callback function to handle gaze data
def gaze_data_callback(gaze_data):
    global csvfile
    with open('gaze_data.csv', 'a', newline='') as file:
        print("writing data")
        csvfile = file
        writer = csv.writer(csvfile)
        timestamp = gaze_data['system_time_stamp']
        left_eye_gaze = gaze_data['left_gaze_point_on_display_area']
        right_eye_gaze = gaze_data['right_gaze_point_on_display_area']
        writer.writerow([timestamp, left_eye_gaze[0], left_eye_gaze[1], right_eye_gaze[0], right_eye_gaze[1]])

@app.route('/check_eye_tracker_connection')
def route_check_eye_tracker_connection():
    return str(check_eye_tracker_connection())

# Route to get eye tracking data
@app.route('/get_eye_tracking_data')
def route_get_eye_tracking_data():
    return str(get_eye_tracking_data())

@app.route('/pause_eye_tracking_data')
def route_pause_eye_tracking_data():
    return str(pause_eye_tracking_data())

if __name__ == "__main__":
    app.run(debug=True)