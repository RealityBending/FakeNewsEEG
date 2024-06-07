var trial_number = 1

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1))
        ;[array[i], array[j]] = [array[j], array[i]]
    }
    return array
}

// Option 1: mixed-design, ppts assigned either human or AI generated stimuli
// Option 2: ppts view all 80 stimuli
// Option 3: ppts view 2 categories from fake/human, fake/AI, real/human, real/AI

// Option 1
// Randomly assign human/AI excerpts
human_AI = []
for (let nat of [...new Set(stimuli.map((a) => a.type))]) {
    human_AI.push(nat)
}
shuffleArray(human_AI)

stimuli_list = [] // Initialize
var nat_stimuli = stimuli.filter((a) => a.type == human_AI[1]) // Select human/AI generated excerpts
stimuli_list = shuffleArray(nat_stimuli) // Shuffle
console.log(stimuli_list)

// Option 2
// stimuli_list = shuffleArray(stimuli) // Initialize
// console.log(stimuli_list)

// Option 3


// for (let cat of [...new Set(stimuli.filter((a) => a.type == human_AI[1]))]) {
//     // Get all stimuli of this category
//     console.log(cat)
//     var cat_stimuli = stimuli.filter((a) => a.code == cat)
//     var nat_stimuli = stimuli.filter((a) => a.type == human_AI[1])
//     // nat_stimuli = shuffleArray(nat_stimuli) // Shuffle
//     console.log(nat_stimuli)

//     // // AI vs. Human
//     // for (let nat of [...new Set(stimuli.map((a) => a.type))]) {
//     //     // console.log(nat)
//     //     var nat_stimuli = stimuli.filter((a) => a.type == nat)
//         // nat_stimuli = shuffleArray(nat_stimuli) // Shuffle
//         // console.log(nat_stimuli)
//     //     // Add 2 first stimuli to stimuli_list
//     //     nat_stimuli.slice(0, 2).forEach((a) => stimuli_list.push(a))
//     // }
// }
// stimuli_list = shuffleArray(stimuli_list) // Shuffle


// Randomize ticks order
var ticks_real = shuffleArray(["Real", "Fake"])
if (ticks_real[1] == "Real") {
    var ticks_real_type = "Positive_Real"
} else {
    var ticks_real_type = "Positive_Fake"
}
var ticks_ai = shuffleArray(["Human", "AI"])
if (ticks_ai[1] == "Human") {
    var ticks_ai_type = "Positive_Human"
} else {
    var ticks_ai_type = "Positive_AI"
}

// Instructions - start of study before first block
function addBackgroundGrey() {
    // Add the CSS class to the body element
    // document.body.classList.add('grey-background');
    document.body.style.backgroundColor = "#808080"
}

// Marker
var marker_position = [0, 0, 200, 200] // [0, 0, 100, 100]
function create_black_marker(marker_position, color = "black") {
    const html = `<div id="black_marker" style="position: absolute; background-color: ${color};\
    left:${marker_position[0]}; top:${marker_position[1]}; \
    width:${marker_position[2]}px; height:${marker_position[3]}px";></div>`
    document.querySelector("body").insertAdjacentHTML("beforeend", html)
}

function create_white_marker(marker_position, color = "white") {
    const html = `<div id="white_marker" style="position: absolute; background-color: ${color};\
    left:${marker_position[0]}; top:${marker_position[1]}; \
    width:${marker_position[2]}px; height:${marker_position[3]}px";></div>`
    document.querySelector("body").insertAdjacentHTML("beforeend", html)
}

var fakenews_instructions_start1 = {
    type: jsPsychHtmlButtonResponse,
    css_classes: ["trial-text"],
    stimulus:
        "<h1>Instructions</h1>" +
        "<p style='text-align: left'>In this experiment, we are interested in how you judge and perceive different short <b>news excerpts</b>.</p>" +
        "<p style='text-align: left'>Importantly, some of these texts correspond to <b>real news</b> (true), but others are <b>fake</b> (not true). Some were written <b>by Humans</b> and some were created by an <b>Artificial Intelligence (AI) algorithm</b> (like ChatGPT).</p>" +
        "<p style='text-align: left'>You will have to read each news excerpt, and then answer a few questions about it and evaluate each news on the following scales:</p>" +
        "<ul style='text-align: left'>" +
        "<li><b>Real vs. Fake</b>: Do you think that the content of the news is <b>real</b> (true) or <b>fake</b> (false).</li>" +
        "<li><b>Human vs. AI-generated</b>: Do you think the text was written by a <b>Human or an AI</b> (regardless of whether the content is true or false).</li>" +
        "<li><b>Engaging</b>: To what extent did you find the news engaging (e.g., interesting or fun). Strongly engaging content would typically lead us to spend more time searching more information, or commenting on and sharing it.</li>" +
        '<li><b>Emotionality</b>: To what extent was the news "emotional". Did the news trigger any feelings in you while reading it?</li>' +
        "<li><b>Importance</b>: Assuming the news is true, to what extent is it important in general for the world (e.g., a matter of national concern)?</li>" +
        "<li><b>Relevance</b>: To what extent was the news about something relevant to you, either because it's something you care about, or something that might impact you directly.</li></ul>" +
        "<p style='text-align: left'> Please read the <b>entire</b> news excerpt, and read each excerpt as you would do with a regular news article. Knowing the answer can sometimes be <b>very hard</b>, so go with your gut feelings! You can also give more or less extreme responses depending on how <b>confident</b> you are. You will be tasked to read 32 excerpts in total.</p>",
    choices: ["Ready"],
    on_load: function () {
        create_white_marker(marker_position)
        addBackgroundGrey()
    },
    // on_finish: function () {
    //     document.querySelector('#white_marker').remove()
    // },
    data: { screen: "fakenews_instructions_start1" },
}

var fakenews_instructions_start2 = {
    type: jsPsychHtmlButtonResponse,
    css_classes: ["trial-text"],
    stimulus:
        "<h1>Instructions</h1>" +
        "<p style='text-align: left'>We will first do a practice trial before starting the actual study.</p>",
    choices: ["Ready"],
    data: { screen: "fakenews_instructions_start2" },
}

var fakenews_instructions1 = {
    type: jsPsychHtmlButtonResponse,
    css_classes: ["trial-text"],
    stimulus:
        "<p style='text-align: left'>You have completed the practice trial. If you have any questions, please ask the experimenter(s) before proceeding.</p>"+
        "<p style='text-align: left'>If there are no questions, please click ready to start the study when prompted by the experimenter.</p>",
    choices: ["Ready"],
    data: { screen: "fakenews_instructions1" },
}

// Instructions - end of first block, before start of second block
var fakenews_instructions2 = {
    type: jsPsychHtmlButtonResponse,
    css_classes: ["trial-text"],
    stimulus:
        "<p> You have completed the first half of the study. We will perform another re-calibration of the eye-tracker.</p><br />When instructed by the experimenter, please click 'Ready' to continue with the second half of the study.",
    choices: ["Ready"],
    data: { screen: "fakenews_instructions2" },
}

// Trials ==========================================================

// Fixation cross
var fixation = {
    type: jsPsychHtmlKeyboardResponse,
    stimulus: '<div style="font-size:60px;">+</div>',
    choices: "NO_KEYS",
    trial_duration: 1500,
    // trial_duration: 0,  // for testing
    // on_start: function () {
    //     ; (document.body.style.cursor = "none"),
    //         (document.querySelector(
    //             "#jspsych-progressbar-container"
    //         ).style.display = "none")
    // },
    on_load: function () {
        addBackgroundGrey()
    },
    save_trial_parameters: {
        trial_duration: true,
    },
    data: { screen: "fixation" },
}

var fakenews_practice_text_1 = {
    type: jsPsychHtmlButtonResponse,
    css_classes: ["trial-text"],
    stimulus: function () {
        // var title = "<h2>News " + trial_number + " / " + stimuli_list.length + "</h2>"
        var stim =
            "<p style='background-color: #808080'>" + " In a recent development, Singapore has observed a notable rise in urban gardening and community farming initiatives. With the rapid urbanization of the city-state, the push towards sustainable living has been gaining momentum. Community members are banding together to cultivate plots of land, often converting rooftops and unused urban spaces into productive gardens. The government, recognizing the potential benefits, has extended support by offering grants and resources for these urban farming projects. The goal is to not only promote sustainable living but also address minor concerns related to food security and self-sufficiency. Additionally, these initiatives have the added advantage of promoting social cohesion as residents come together for a common purpose. Experts in urban planning have lauded these efforts, seeing them as an innovative solution to maximize land use in the densely populated city. As the nation continues to grow, these community-driven projects may serve as a model for other cities around the world." + "</p>" + "<p style='font-size:0%'>" + 'practice' + "</p>"
        return stim
    },
    choices: ["I Read"],
    data: { screen: "fakenews_text" },
    on_load: function() {
        create_black_marker(marker_position)
        startRecording(jsPsych.timelineVariable("excerpt_num"))
        startEyeTracker(jsPsych.timelineVariable("excerpt_num"))
    },
    on_finish: function () {
        stopRecording()
        trial_number++
        document.querySelector("#black_marker").remove()
        pauseEyeTracker()
    },
}

var fakenews_practice_text_2 = {
    type: jsPsychHtmlButtonResponse,
    css_classes: ["trial-text"],
    stimulus: function () {
        // var title = "<h2>News " + trial_number + " / " + stimuli_list.length + "</h2>"
        var stim =
            "<p style='background-color: #808080'>" + "Danish bank Nykredit Bank has been embroiled in a money laundering scandal, sending shockwaves throughout the country well-known for its stringent and well-regulated financial system. Danish police arrested 5 individuals on Sunday, including 3 foreigners from Romania, Russia, and North Macedonia. This scandal has raised questions about Nykredit Bank's adherence to anti-money laundering rules. As of Tuesday, Nykredit Bank's stock price has fallen by 12%, its sharpest drop since the 2007-08 global financial crisis. Other Danish banks also saw their stock prices drop. Denmark's largest bank, Danske Bank, saw its stock price fall by 6%, and Jyske Bank's stock price fell by 8%. Danish authorities are currently investigating the money laundering case at Nykredit. Nykredit Bank declined to comment on the case, citing ongoing investigations by authorities. This money laundering scandal follows the rumoured allegations of Nykredit Bank being involved in Russian banking transactions, which has been outlawed by the EU since Russia's illegal invasion of Ukraine in early 2022." + "</p>" + "<p style='font-size:0%'>" + 'practice' + "</p>"
        return stim
    },
    choices: ["I Read"],
    data: { screen: "fakenews_text" },
    on_load: function() {
        create_black_marker(marker_position)
        startRecording(jsPsych.timelineVariable("excerpt_num"))
        startEyeTracker(jsPsych.timelineVariable("excerpt_num"))
    },
    on_finish: function () {
        stopRecording()
        trial_number++
        document.querySelector("#black_marker").remove()
        pauseEyeTracker()
    },
}

var fakenews_text = {
    type: jsPsychHtmlButtonResponse,
    css_classes: ["trial-text"],
    stimulus: function () {
        // var title = "<h2>News " + trial_number + " / " + stimuli_list.length + "</h2>"
        var stim =
            "<p style='background-color: #808080'>" + jsPsych.timelineVariable("stimulus") + "</p>" + "<p style='font-size:0%'>" + jsPsych.timelineVariable("excerpt_num") + "</p>"
        return stim
    },
    choices: ["I Read"],
    data: { screen: "fakenews_text" },
    on_load: function() {
        create_black_marker(marker_position)
        startRecording(jsPsych.timelineVariable("excerpt_num"))
        startEyeTracker(jsPsych.timelineVariable("excerpt_num"))
    },
    on_finish: function () {
        stopRecording()
        trial_number++
        document.querySelector("#black_marker").remove()
        pauseEyeTracker()
    },
}
// Attention check qn
// var fakenews_questions = {
//     type: jsPsychSurveyMultiChoice,
//     questions: [
//         {
//             prompt: "What is the topic of the news excerpt you just read?",
//             options: ["Economy", "Politics", "Science and Technology", "Social Issues", "Others"],
//             name: "Topic",
//             // required: true,
//             required: true,
//         },
//         {
//             prompt: "Was the news excerpt related to Singapore?",
//             options: ["Yes", "No"],
//             name: "SingaporeRelated",
//             // required: true,
//             required: true,
//         },
//     ],
//     data: {
//         screen: "fakenews_questions",
//     },
// }

var fakenews_ratings_reality = {
    type: jsPsychMultipleSlider, // this is a custom plugin in utils
    questions: shuffleArray([
        // The order of the questions is randomized per participant
        {
            prompt:
                "<b>Do you think the news' content is <i>" +
                ticks_real[0] +
                "</i> or <i>" +
                ticks_real[1] +
                "</i>?</b><br>",
            name: "Reality",
            ticks: ticks_real,
            // required: true,
            required: true,
            min: 0,
            max: 1,
            step: 0.01,
            slider_start: 0.5,
        },
        {
            prompt: function () {
                if (ticks_ai_type == "Positive_AI") {
                    return "<b>Do you think the news was written by a <i>Human</i> or an <i>AI</i>?</b><br>"
                } else {
                    return "<b>Do you think the news was written by an <i>AI</i> or a <i>Human</i>?</b><br>"
                }
            },
            name: "Artificiality",
            ticks: ticks_ai,
            // required: true,
            required: true,
            min: 0,
            max: 1,
            step: 0.01,
            slider_start: 0.5,
        },
    ]),
    require_movement: true,
    data: {
        screen: "fakenews_ratings_reality",
        ticks_real: ticks_real_type,
        ticks_ai: ticks_ai_type,
    },
}

var fakenews_ratings_appraisal = {
    type: jsPsychMultipleSlider, // this is a custom plugin in utils
    questions: shuffleArray([
        {
            prompt: "<b>Was the news engaging (e.g., interesting or fun)?</b><br>",
            name: "Engaging",
            ticks: ["Not at all", "Very"],
            required: true,
            min: 0,
            max: 1,
            step: 0.01,
            slider_start: 0.5,
        },
        {
            prompt: "<b>Did you feel any emotions while reading the news?</b><br>",
            name: "Emotionality",
            ticks: ["Not at all", "Very"],
            required: true,
            min: 0,
            max: 1,
            step: 0.01,
            slider_start: 0.5,
        },
        {
            prompt: "<b>Assuming the news was true, to what extent would it be important for the world?</b><br>",
            name: "Importance",
            ticks: ["Not at all", "Very"],
            required: true,
            min: 0,
            max: 1,
            step: 0.01,
            slider_start: 0.5,
        },
        {
            prompt: "<b>To what extent was the news' content relevant to you?</b><br>",
            name: "Relevance",
            ticks: ["Not at all", "Very"],
            required: true,
            min: 0,
            max: 1,
            step: 0.01,
            slider_start: 0.5,
        },
    ]),
    require_movement: true,
    data: {
        screen: "fakenews_ratings_appraisal",
    },
}

// Randomize ratings order between the 2 blocks (scales first, nature after or vice versa)
// TODO: do 2 blocks with questionnaires in between
var fakenews_practice = {
    timeline: [
        fixation,
        fakenews_practice_text_1,
        fixation,
        fakenews_ratings_reality,
        fakenews_ratings_appraisal,
        fixation,
        fakenews_practice_text_2,
        fixation,
        fakenews_ratings_reality,
        fakenews_ratings_appraisal,
    ]
}

var fakenews_block1 = {
    timeline: [
        fixation,
        fakenews_text,
        fixation,
        // fakenews_questions,
        fakenews_ratings_reality,
        fakenews_ratings_appraisal,
    ],
    timeline_variables: stimuli_list.slice(0, 16),
    randomize_order: true,
}

var fakenews_block2 = {
    timeline: [
        fixation,
        fakenews_text,
        fixation,
        // fakenews_questions,
        fakenews_ratings_reality,
        fakenews_ratings_appraisal,
    ],
    timeline_variables: stimuli_list.slice(16, 32),
    randomize_order: true,
}
