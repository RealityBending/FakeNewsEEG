let data = [];
let gamepadIndex = null;
let animationFrameId = null;

window.addEventListener("gamepadconnected", function(e) {
    console.log("Gamepad connected at index %d: %s. %d buttons, %d axes.",
    e.gamepad.index, e.gamepad.id,
    e.gamepad.buttons.length, e.gamepad.axes.length);
    gamepadIndex = e.gamepad.index;
});

window.addEventListener("gamepaddisconnected", function(e) {
    console.log("Gamepad disconnected from index %d: %s",
    e.gamepad.index, e.gamepad.id);
    gamepadIndex = null;
});

function startRecording(num) {
    if (gamepadIndex !== null) {
        // data.push("new")
        animationFrameId = requestAnimationFrame(readGamepad);
        console.log("start recording " + num)
        data.push([num, num])
    }
}

function readGamepad() {
    let gamepad = navigator.getGamepads()[gamepadIndex];
    if (gamepad) {
        let axesData = gamepad.axes.map(axis => axis.toFixed(6));
        console.log(axesData[0],axesData[1])
        data.push([axesData[0],axesData[1]]);
        checkButtonPress()
        test = checkButtonPress()
        console.log(test)
        // console.log(gamepad.axes[0])
    }
    animationFrameId = requestAnimationFrame(readGamepad);
}

function checkButtonPress() {
    let gamepad = navigator.getGamepads()[gamepadIndex];
    if (gamepad.buttons[0].pressed) {
        console.log("pressed")
        return true
    }
    else {
        return false
    }
}

function stopRecording() {
    cancelAnimationFrame(animationFrameId)
    console.log("stop recording")
}

function exportToCSV() {
    let csvContent = ["x-axis","y-axis"] + "\r\n";
    data.forEach(function(rowArray) {
        let row = rowArray.join(",");
        csvContent += row + "\r\n";
    });
    let blob = new Blob([csvContent], { type: "text/csv" });
    saveAs(blob, "gamepad_data.csv");
    console.log("saved")
}