function startEyeTracker(num) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_eye_tracking_data', true);
    xhr.onload = function() {
      if (xhr.status === 200) {
        var isEyeTrackerConnected = xhr.responseText === 'True';
        if (isEyeTrackerConnected) {
          console.log('Tobii eye tracker is connected.');
          // Perform actions if Tobii eye tracker is connected
        } else {
          console.log('Tobii eye tracker is not connected.');
          // Perform actions if Tobii eye tracker is not connected
        }
      } else {
        console.error('Failed to check Tobii eye tracker connection.');
      }
    };
    var data = JSON.stringify(num);
    xhr.send(data);
}

function pauseEyeTracker() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/pause_eye_tracking_data', true);
    xhr.onload = function() {
      if (xhr.status === 200) {
        var isEyeTrackerConnected = xhr.responseText === 'True';
        if (isEyeTrackerConnected) {
          console.log('Tobii eye tracker is connected and data collection paused.');
          // Perform actions if Tobii eye tracker is connected
        } else {
          console.log('Tobii eye tracker is not connected.');
          // Perform actions if Tobii eye tracker is not connected
        }
      } else {
        console.error('Failed to check Tobii eye tracker connection.');
      }
    };
    xhr.send();
}