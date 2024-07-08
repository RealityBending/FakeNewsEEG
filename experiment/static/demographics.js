// Retrieve and save browser info ========================================================
var demographics_browser_info = {
    type: jsPsychBrowserCheck,
    data: {
        screen: "browser_info",
        date: new Date().toLocaleDateString("fr-FR"),
        time: new Date().toLocaleTimeString("fr-FR"),
    },
    on_finish: function (data) {
        dat = jsPsych.data.get().filter({ screen: "browser_info" }).values()[0]

        // Rename
        data["screen_height"] = dat["height"]
        data["screen_width"] = dat["width"]

        // Add URL variables - ?sona_id=x&exp=1
        let urlvars = jsPsych.data.urlVariables()
        data["sona_id"] = urlvars["sona_id"]
        data["researcher"] = urlvars["exp"]
    },
}
// For stopping collection when quota hits
var demographics_quotahit = function (
    link = "https://dominiquemakowski.github.io/PHQ4R/study2/experiment/experimenter1.html"
) {
    return {
        type: jsPsychHtmlButtonResponse,
        css_classes: ["narrow-text"],
        stimulus:
            "<img src='https://seeklogo.com/images/N/nanyang-technological-university-logo-99C7E42213-seeklogo.com.png' width='150px' align='right'/><br><br><br><br><br>" +
            "<br><p>Thank you for your interest in our study!</p>" +
            "<p>We have currently reached our participant quota, however, we may open more slots in the coming weeks.</p>" +
            "<p>If you are interested in taking part if more quota is made available please email gameplaystudy@gmail.com to indicate your interest.</p>",
        choices: ["End"],
        data: { screen: "endscreen" },
    }
}


// Participant ID ========================================================================
var demographics_participant_id = {
    type: jsPsychSurveyText,
    questions: [
        {
            prompt: "Enter participant ID:",
            placeholder: "001",
            name: "Participant_ID",
        },
    ],
    data: {
        screen: "participant_id",
    },
    on_finish: function () {
        // Store `participant_id` so that it can be reused later
        jsPsych.data.addProperties({
            participant_id: jsPsych.data.get().last().values()[0]["response"]["Participant_ID"],
        })
    },
}

// Consent form ========================================================================
var demographics_consent = {
    type: jsPsychHtmlButtonResponse,
    css_classes: ["narrow-text"],
    stimulus:
        // Logo and title
        "<img src='https://seeklogo.com/images/N/nanyang-technological-university-logo-99C7E42213-seeklogo.com.png' width='150px' align='right'/><br><br><br><br><br>" +
        "<h1>Informed Consent</h1>" +
        // Overview
        "<p align='left'><b>Invitation to Take Part</b><br>" +
        "You are being invited to take part in a research study to further our understanding of human psychology. Thank you for carefully reading this information sheet. This study is being conducted by Prof Annabel Chen from the School of Social Sciences, Nanyang Technological University, who is happy to be contacted if you have any questions.</p>" +
        // Description
        "<p align='left'><b>Why have I been invited and what will I do?</b><br>" +
        "We are surveying adults to understand how people judge real and fake news articles. The whole experiment will take you <b>about 45 min</b> to complete. Please make sure that you are in a quiet environment, and that you have time to complete it in one go. You will be reimbursed <b>$15</b> for your participation in this study.</p>" +
        // Results and personal information
        "<p align='left'><b>What will happen to the results and my personal information?</b><br>" +
        "The results of this research may be written into a scientific publication. Your anonymity will be ensured in the way described in the consent information below. Please read this information carefully and then, if you wish to take part, please acknowledge that you have fully understood this sheet, and that you consent to take part in the study as it is described here.</p>" +
        "<p align='left'><b>Consent</b><br></p>" +
        // Bullet points
        "<li align='left'>I understand that by signing below I am agreeing to take part in the Nanyang Technological University research described here, and that I have read and understood this information sheet.</li>" +
        "<li align='left'>I understand that my participation is entirely voluntary, that I can choose not to participate in part or all of the study, and that I can withdraw at any stage without having to give a reason and without being penalised in any way (e.g., if I am a student, my decision whether or not to take part will not affect my grades).</li>" +
        "<li align='left'>I understand that since the study is anonymous, it will be impossible to withdraw my data once I have completed and submitted the test/questionnaire.</li>" +
        "<li align='left'>I understand that my personal data will be used for the purposes of this research study and will be handled in accordance with Data Protection legislation. I understand that the University's Privacy Notice provides further information on how the University uses personal data in its research.</li>" +
        "<li align='left'>I understand that my collected data will be stored in a de-identified way. De-identified data may be made publically available through secured scientific online data repositories.</li>" +
        // Incentive
        "<li align='left'>I acknowledge, agree and consent that Nanyang Technological University ('NTU') is permitted to collect, use, disclose and/or process my personal data for facilitating, processing, administering and/or managing payments arising from my participation in this study (the 'Purpose'). I further acknowledge, agree and consent that NTU is permitted to collect, use or process my personal data and to disclose my personal data to third parties (whether located within or outside Singapore), in each respect, for the above Purpose and for the third parties to subsequently collect, use, disclose and/or process your personal data for the above Purpose.</li>" +
        "<li align='left'><b>Please note that various checks will be performed to ensure the validity of the data. We reserve the right to withhold credit awards or reimbursement should we detect non-valid responses (e.g., random patterns of answers, instructions not read, ...).</b></li>" +
        "<li align='left'><b>This study is also currently only open to invited participants who have received an email invite from the study team. We reserve the right to withhold credit awards or reimbursement to participants who did not receive the invitation email from the study team.</b></li>" +
        "<li align='left'>By participating, you agree to follow the instructions and provide honest answers. If you do not wish to participate, simply close your browser.</li>" +
        "</p>" +
        "<p align='left'><br><sub><sup>For further information about this research, or if you have any concerns, please contact Prof Annabel Chen (annabelchen@ntu.edu.sg). This research has been approved (IRB-2022-785) by the ethics board of the University.</sup></sub></p>",

    choices: ["I read, understood, and I consent"],
    data: { screen: "consent" },
}

// Thank you ========================================================================
var demographics_waitdatasaving = {
    type: jsPsychHtmlButtonResponse,
    stimulus:
        "<p>Done!  Now click on 'Continue' and <b>wait until your responses have been successfully saved</b> before closing the tab.</p> ",
    choices: ["Continue"],
    data: { screen: "waitdatasaving" },
}

var demographics_endscreen = function (
    link = "https://dominiquemakowski.github.io/PHQ4R/study2/experiment/experimenter1.html"
) {
    return {
        type: jsPsychHtmlButtonResponse,
        css_classes: ["narrow-text"],
        stimulus:
            "<h1>Thank you for participating</h1>" +
            "<a/></b></p><br>" +
            "<h2>Information</h2>" +
            "<p align='left'>The purpose of this study was for us to understand how people can discriminate between real and fake news. Your participation in this study will be kept completely confidential.</p>" +
            "<p align='left'>If you have any questions about the project, please contact D.Makowski@sussex.ac.uk.</p>" +
            "<p><b>You can safely close the tab now.</b></p>",
        choices: ["End"],
        data: { screen: "endscreen" },
        on_finish: function() {
            exportToCSV()
            saveEyeTrackingData()
        }
    }
}

// Demographic debrief

function removeBackgroundGrey() {
    // Add the CSS class to the body element
    document.body.classList.remove('grey-background');
}

var demographics_debrief = {
    type: jsPsychSurveyMultiChoice,
    preamble: "<b>It's done!</b> Just before we end, please answer the following questions:",
    questions: [
        // {
        //     prompt: "Have you previously taken part in a study involving the creation of fake and real news?",
        //     options: ["Yes", "No"],
        //     name: "generation_participation",
        //     required: true,
        // },
        {
            prompt: "In general, would you consider yourself to be good at knowing whether a news is real or fake?",
            options: [
                "Very good",
                "Somewhat good",
                "Neither good nor bad",
                "Somewhat bad",
                "Very bad",
            ],
            name: "discrimination_ability",
            required: true,
        },
    ],
    on_load: function () {
        removeBackgroundGrey()
    },
    data: { screen: "demographics_debrief" },
}

// Demographic PayNow
var jsPsych = initJsPsych()
var random_id = jsPsych.randomization.randomID(8)
var demographics_paynow = {
    type: jsPsychHtmlButtonResponse,
    stimulus: 
        "<p>To process your reimbursement for taking part in this study, please copy the code below and send it as the subject title via email to <u>gameplaystudy@gmail.com</u>, and include your <b>full name</b> and your <b>PayNow registered phone number</b> in the email text. <b>DO NOT EXIT ON THIS PAGE, PLEASE NAVIGATE TO THE END OF THE STUDY FOR YOUR SUBMISSION TO BE DEEMED COMPLETE.</b><br><br></p>" + "<b><p style='background-color: #f2f2f2'>" + random_id + "</p></b><br><br>",       
    choices: ["Continue"],
    data: { screen: "demographics_paynow" },
}

// Demographic info ========================================================================
var demographics_multichoice = {
    type: jsPsychSurveyMultiChoice,
    css_classes: "narrow-text",
    preamble: "<b>Please answer the following questions:</b>",
    questions: [
        {
            prompt: "What is your gender?",
            options: ["Male", "Female", "Other"],
            name: "gender",
            required: true
        },
        {
            prompt: "Are you currently a student?",
            options: ["Yes", "No"],
            name: "student",
            required: true
        },
        {
            prompt: "What is your highest completed education level?",
            options: [
                "University (doctorate)",
                "University (master) <sub><sup>or equivalent</sup></sub>",
                "University (bachelor) <sub><sup>or equivalent</sup></sub>",
                "High school or equivalent (A-levels, Diploma, etc.)",
                "Secondary school up to 16 years",
                "Primary school",
                "Other",
            ],
            name: "education",
            required: true
        },
        {
            prompt: "What is your current English level?",
            options: [
                "Native",
                "Fluent (academic)",
                "Fluent (conversational)",
                "Intermediate",
                "Beginner",
            ],
            name: "english",
            required: true
        },
        {
            prompt: "What would your rate your experience/expertise with AI-generation programs like ChatGPT?",
            options: [
                "Highly experienced (I use it a lot)",
                "Experienced (I use it often)",
                "Relatively experienced (I used it a few times)",
                "Little experience (I tried it)",
                "No experience (but I heard about it)",
                "No experience (I don't know what it is)",
            ],
            name: "ai_expertise",
            required: true
        },
    ],
    data: {
        screen: "demographics_1",
    },
}

var demographics_freetext = {
    type: jsPsychSurveyText,
    questions: [
        {
            prompt: "What is your area of study?",
            placeholder: "e.g., 'Business', 'Computer Science', 'Arts and Humanities'",
            name: "discipline",
            required: true
        },
        {
            prompt: "Please enter your age (in years)",
            placeholder: "e.g., '31'",
            name: "age",
            required: true
        },
        {
            prompt: "Please enter your nationality",
            name: "nationality",
            required: true
        },
        {
            prompt: "Please enter your ethnicity",
            placeholder: "e.g., Caucasian",
            name: "ethnicity",
            required: true
        },
        {
            prompt: "How many years have you lived in Singapore?",
            name: "years_singapore",
            required: true
        },
    ],
    data: {
        screen: "demographics_2",
    },
}

var demographics_info = {
    timeline: [demographics_multichoice, demographics_freetext],
}
