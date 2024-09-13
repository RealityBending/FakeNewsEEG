var questionnaire_media_frequency = {
    type: jsPsychSurveyMultiChoice,
    css_classes: "questionnaire-text",
    preamble:
        "<br><p><b>We would like to understand more about how your news reading habits.</b></p>" +
        "<p><b>How often do you watch/read <i>news</i> using each of the following?</b></p>",
    // TODO: Media ? Or News only?
    questions: [
        {
            prompt: "<b>Internet (news websites)</b>",
            name: "newsfrequency_internet",
            options: [
                "Several times a day",
                "Once a day",
                "4-6 days a week",
                "2-3 days a week",
                "Once a week",
                "Less often than once a week",
            ],
            required: true,
        },
        {
            prompt: "<b>Phone apps</b>",
            name: "newsfrequency_phoneapps",
            options: [
                "Several times a day",
                "Once a day",
                "4-6 days a week",
                "2-3 days a week",
                "Once a week",
                "Less often than once a week",
            ],
            required: true,
        },
        {
            prompt: "<b>Social media (Twitter, Reddit, Facebook, ...)</b>",
            name: "newsfrequency_socialmedia",
            options: [
                "Several times a day",
                "Once a day",
                "4-6 days a week",
                "2-3 days a week",
                "Once a week",
                "Less often than once a week",
            ],
            required: true,
        },
        {
            prompt: "<b>Television</b>",
            name: "newsfrequency_tv",
            options: [
                "Several times a day",
                "Once a day",
                "4-6 days a week",
                "2-3 days a week",
                "Once a week",
                "Less often than once a week",
            ],
            required: true,
        },
        {
            prompt: "<b>Newspapers</b>",
            name: "newsfrequency_newspapers",
            options: [
                "Several times a day",
                "Once a day",
                "4-6 days a week",
                "2-3 days a week",
                "Once a week",
                "Less often than once a week",
            ],
            required: true,
        },
        // {
        //     prompt: "<b>Books</b>",
        //     name: "newsfrequency_books",
        //     options: [
        //         "Several times a day",
        //         "Once a day",
        //         "4-6 days a week",
        //         "2-3 days a week",
        //         "Once a week",
        //         "Less often than once a week",
        //     ],
        //     required: false,
        // },
        {
            prompt: "<b>Radio</b>",
            name: "newsfrequency_radio",
            options: [
                "Several times a day",
                "Once a day",
                "4-6 days a week",
                "2-3 days a week",
                "Once a week",
                "Less often than once a week",
            ],
            required: true,
        },
        {
            prompt: "<b>In general, how interested are you in keeping up with news?</b>",
            name: "news_interest",
            options: [
                "Extremely interested",
                "Very interested",
                "Somewhat interested",
                "Not very interested",
                "Not at all interested",
            ],
            // required: true,
            required: true,
        },
        {
            prompt: "<b>In general, how often do you engage with the news (commenting them, discussing them on social media, bringing them up in conversations, etc.)</b>",
            name: "news_engagement",
            options: [
                "Everyday",
                "A few times a week",
                "Once a week",
                "A few times a month",
                "Rarely",
                "Never",
            ],
            // required: true,
            required: true,
        },
        {
            prompt: "<b>In general, how often do you share news and news links (i.e., do you often do you forward or send news articles to other people)</b>",
            name: "news_sharing",
            options: [
                "Everyday",
                "A few times a week",
                "Once a week",
                "A few times a month",
                "Rarely",
                "Never",
            ],
            // required: true,
            required: true,
        },
    ],
    require_movement: true,
    data: {
        screen: "questionnaire_media_frequency",
    },
}

var questionnaire_news_types = {
    type: jsPsychSurveyMultiSelect,
    css_classes: "questionnaire-text",
    questions: [
        {
            prompt: "<b>Which of the following types of news are you most interested in?</b>",
            options: [
                "Local news",
                "International news",
                "Business and financial news",
                "World politics",
                "Local politics",
                "News about the economy",
                "Fun/weird news",
                "Health and education news",
                "Lifestyle news",
                "Arts and culture news",
                "Sports news",
                "Science and technology news",
                "Crime/sensational news",
                "Celebrity-related news",
            ],
            name: "type",
            required: true,
        },
    ],
    require_movement: true,
    data: {
        screen: "questionnaire_news_types",
    },
}

// PHQ4 ========================================================================

var PHQ4_instructions = 
    "<h2>About you...</h2>"+
    "<p>Over the last two weeks, how often have you been bothered by the following problems? </p>"

var PHQ4_items = [
    "Feeling nervous, anxious or on edge",
    "Not being able to stop or control worrying",
    "Little interest or pleasure in doing things",
    "Feeling down, depressed, or hopeless"
]

var PHQ4_dimensions = [
    "Anxiety_1",
    "Anxiety_2",
    "Depression_3",
    "Depression_4"
]

function PHQ4(
    required = true,
    ticks = [
        "Not at all",
        "Several days",
        "More than half the days",
        "Nearly every day",
    ],
    items = PHQ4_items,
    dimensions = PHQ4_dimensions
) {
    var questions = []
    for (const [index, element] of items.entries()) {
        questions.push({
            prompt: "<b>" + element + "</b>",
            name: dimensions[index],
            labels: ticks,
            required: required,
        })
    }
    return questions
}

var questionnaire_phq4 = {
    type: jsPsychSurveyLikert,
    css_classes: "questionnaire-text",
    questions: PHQ4((required = true)),
    randomize_question_order: false,
    preamble: PHQ4_instructions,
    required: true,
    slider_width: 700,
    data: {
        screen: "questionnaire_phq4",
    },
}

// Interoceptive Awareness Scale (IAS) =========================================

var ias_instructions = 
    "<h2>About you...</h2>"+
    "<p>Below are several statements regarding how accurately you can perceive specific bodily sensations. Please rate on the scale how well you believe you can perceive each specific signal. For example, if you often feel you need to urinate and then realise you do not need to when you go to the toilet you would rate your accuracy perceiving this bodily signal as low.</p>"+
    "<p>Please only rate how well you can perceive these signals without using external cues, for example, if you can only perceive how fast your heart is beating when you measure it by taking your pulse this would not count as accurate internal perception.</p>"

var ias_items = [
    "I can always accurately perceive when my heart is beating fast",
    "I can always accurately perceive when I am hungry",
    "I can always accurately perceive when I am breathing fast",
    "I can always accurately perceive when I am thirsty",
    "I can always accurately perceive when I need to urinate",
    "I can always accurately perceive when I need to defecate",
    "I can always accurately perceive when I encounter different tastes",
    "I can always accurately perceive when I am going to vomit",
    "I can always accurately perceive when I am going to sneeze",
    "I can always accurately perceive when I am going to cough",
    "I can always accurately perceive when I am hot/cold",
    "I can always accurately perceive when I am sexually aroused",
    "I can always accurately perceive when I am going to pass wind",
    "I can always accurately perceive when I am going to burp",
    "I can always accurately perceive when my muscles are tired/sore",
    "I can always accurately perceive when I am going to get a bruise",
    "I can always accurately perceive when I am in pain",
    "I can always accurately perceive when my blood sugar is low",
    "I can always accurately perceive when someone is touching me affectionately rather than nonaffectionately",
    "I can always accurately perceive when something is going to be ticklish",
    "I can always accurately perceive when something is going to be itchy"
]

var ias_dimensions = [
    "Heart_1",
    "Hungry_2",
    "Breathing_3",
    "Thirsty_4",
    "Urinate_5",
    "Defecate_6",
    "Taste_7",
    "Vomit_8",
    "Sneeze_9",
    "Cough_10",
    "Temperature_11",
    "Sexual-Arousal_12",
    "Wind_13",
    "Burp_14",
    "Muscles_15",
    "Bruise_16",
    "Pain_17",
    "Blood-Sugar_18",
    "Affective-Touch_19",
    "Tickle_20",
    "Itch_21"
]

function IAS(
    required = true,
    ticks = [
        "Strongly Disagree",
        "Disagree",
        "Neither Agree or Disagree",
        "Agree",
        "Strongly Agree"
    ],
    items = ias_items,
    dimensions = ias_dimensions
) {
    var questions = []
    for (const [index, element] of items.entries()) {
        questions.push({
            prompt: "<b>" + element + "</b>",
            name: dimensions[index],
            labels: ticks,
            required: required,
        })
    }
    return questions
}

var questionnaire_ias = {
    type: jsPsychSurveyLikert,
    css_classes: "questionnaire-text",
    questions: IAS((required = true)),
    randomize_question_order: true,
    preamble: ias_instructions,
    required: true,
    slider_width: 600,
    data: {
        screen: "questionnaire_ias",
    },
}

// Generic Conspiracist Beliefs Scale (GCSB) ===================================

var GCB_instructions =
    "<h2>About your Attitudes...</h2>" +
    "<p>We are interested in your general attitude.</p>" +
    "<p>Please read the statements below carefully and indicate the extent to which you agree with each statement.</p>"

var GCB_items = [
    "<b>The government is involved in the murder of innocent citizens and/or well-known public figures, and keeps this a secret.</b><br>",
    "<b>The power held by heads of state is second to that of small unknown groups who really control world politics.</b><br>",
    "<b>Secret organizations communicate with extraterrestrials, but keep this fact from the public.</b><br>",
    "<b>The spread of certain viruses and/or diseases is the result of the deliberate, concealed efforts of some organization.</b><br>",
    "<b>Groups of scientists manipulate, fabricate, or suppress evidence in order to deceive the public.</b><br>",
    "<b>The government permits or perpetrates acts of terrorism on its own soil, disguising its involvement.</b><br>",
    "<b>A small, secret group of people is responsible for making all major world decisions, such as going to war.</b><br>",
    "<b>Evidence of alien contact is being concealed from the public.</b><br>",
    "<b>Technology with mind-control capacities is used on people without their knowledge.</b><br>",
    "<b>New and advanced technology which would harm current industry is being suppressed.</b><br>",
    "<b>The government uses people as patsies to hide its involvement in criminal activity.</b><br>",
    "<b>Certain significant events have been the result of the activity of a small group who secretly manipulate world events.</b><br>",
    "<b>Some UFO sightings and rumors are planned or staged in order to distract the public from real alien contact.</b><br>",
    "<b>Experiments involving new drugs or technologies are routinely carried out on the public without their knowledge or consent.</b><br>",
    "<b>A lot of important information is deliberately concealed from the public out of self-interest.</b><br>",
];
  
var GCB_dimensions = [
    "GovernmentMalfeasance_1",
    "MalevolentGlobalConspiracy_2",
    "ETCoverUp_3",
    "PersonalWellbeing_4",
    "ControlofInformation_5",
    "GovernmentMalfeasance_6",
    "MalevolentGlobalConspiracy_7",
    "ETCoverUp_8",
    "PersonalWellbeing_9",
    "ControlofInformation_10",
    "GovernmentMalfeasance_11",
    "MalevolentGlobalConspiracy_12",
    "ETCoverUp_13",
    "PersonalWellbeing_14",
    "ControlofInformation_15",
];

function GCB(
    required = true,
    ticks = [
        "Strongly Disagree",
        "Disagree",
        "Neither Agree or Disagree",
        "Agree",
        "Strongly Agree"
    ],
    items = GCB_items,
    dimensions = GCB_dimensions
) {
    var questions = []
    for (const [index, element] of items.entries()) {
        questions.push({
            prompt: "<b>" + element + "</b>",
            name: dimensions[index],
            labels: ticks,
            required: required,
        })
    }
    return questions
}

var questionnaire_gcb = {
    type: jsPsychSurveyLikert,
    css_classes: "questionnaire-text",
    questions: GCB((required = true)),
    randomize_question_order: true,
    preamble: GCB_instructions,
    required: true,
    slider_width: 700,
    data: {
        screen: "questionnaire_gcb",
    },
}

// BAIT ========================================================================

var bait_dimensions = [
    "GAAIS_Negative_9",
    "GAAIS_Negative_10",
    "GAAIS_Negative_15",
    "GAAIS_Positive_7",
    "GAAIS_Positive_12",
    "GAAIS_Positive_17",
    "BAIT_1_ImagesRealistic",
    "BAIT_2_ImagesIssues",
    "BAIT_3_VideosRealistic",
    "BAIT_4_VideosIssues",
    "BAIT_5_ImitatingReality",
    "BAIT_6_EnvironmentReal",
    "BAIT_7_TextRealistic",
    "BAIT_8_TextIssues",
]

function format_questions_analog(
    items,
    dimensions,
    ticks = ["Inaccurate", "Accurate"]
) {
    var questions = []
    for (const [index, element] of items.entries()) {
        questions.push({
            prompt: "<b>" + element + "</b>",
            name: dimensions[index],
            ticks: ticks,
            required: true,
            min: 0,
            max: 1,
            step: 0.01,
            slider_start: 0.5,
        })
    }
    return questions
}

var bait_instructions =
    "<h2>About AI...</h2>" +
    "<p>We are interested in your thoughts about Artificial Intelligence (AI).<br>" +
    "Please read the statements below carefully and indicate the extent to which you agree with each statement.</p>"

// General Attitudes towards Artificial Intelligence Scale (GAAIS; Schepman et al., 2020, 2022)
// We used the most loaded items from Schepman et al. (2023) - loadings from the 2 CFAs are in parentheses
// We adedd items specifically about CGI and artificial media (BAIT)
var bait_items = [
    // Neg3 (0.406, 0.405) - Low loadings
    // "Organisations use Artificial Intelligence unethically",
    // Neg9 (0.726, 0.717) - Not used in FakeFace
    "Artificial Intelligence might take control of people",
    // Neg10 (0.850, 0.848) - Modified: removed "I think"
    "Artificial Intelligence is dangerous",
    // Neg15 (1.014, 0.884) - Not used in FakeFace. Modified: replaced "I shiver with discomfort when I think about" by "I am worried about"
    "I am worried about future uses of Artificial Intelligence",
    // Pos7 (0.820, 0.878)
    "I am interested in using artificially intelligent systems in my daily life",
    // Pos12 (0.734, 0.554)
    "Artificial Intelligence is exciting",
    // Pos14 (0.516, 0.346) - Low loadings
    // "There are many beneficial applications of Artificial Intelligence",
    // Pos17 (0.836, 0.656) - Not used in FakeFace
    "Much of society will benefit from a future full of Artificial Intelligence",

    // New items (Beliefs about Artificial Images Technology - BAIT) ---------------------------
    // Revised from Makowski et al. (Fake Face study)
    // Changes from FakeFace: remove "I think"
    "Current Artificial Intelligence algorithms can generate very realistic images",
    "Images of faces or people generated by Artificial Intelligence always contain errors and artifacts",
    "Videos generated by Artificial Intelligence have obvious problems that make them easy to spot as fake",
    "Current Artificial Intelligence algorithms can generate very realistic videos",
    "Computer-Generated Images (CGI) are capable of perfectly imitating reality",
    "Technology allows the creation of environments that seem just as real as reality", // New
    "Artificial Intelligence assistants can write texts that are indistinguishable from those written by humans", // New
    "Documents and paragraphs written by Artificial Intelligence usually read differently compared to Human productions", // New
]

var bait_ticks = ["Disagree", "Agree"] // In Schepman et al. (2022) they removed 'Strongly'

// BAIT 2.0
var questionnaire_bait = {
    type: jsPsychMultipleSlider,
    css_classes: "questionnaire-text",
    questions: format_questions_analog(
        bait_items,
        bait_dimensions,
        // In Schepman et al. (2022) they removed 'Strongly'
        (ticks = bait_ticks)
    ),
    randomize_question_order: true,
    preamble: bait_instructions,
    require_movement: true,
    slider_width: 600,
    data: {
        screen: "questionnaire_bait",
    },
}

// Other
// Most of the variables are loaded from online by the script
var questionnaire_ipip6 = {
    type: jsPsychMultipleSlider,
    css_classes: "questionnaire-text",
    questions: ipip6((required = true)),
    randomize_question_order: false,
    preamble: ipip6_instructions,
    require_movement: true,
    slider_width: 600,
    data: {
        screen: "questionnaire_ipip6",
    },
}

// Create questionnaire variable
var questionnaire_pid5 = {
    type: jsPsychSurveyLikert,
    css_classes: "questionnaire-text",
    questions: pid5((required = true)),
    randomize_question_order: true,
    preamble: pid5_instructions,
    required: true,
    slider_width: 700,
    data: {
        screen: "questionnaire_pid5",
    },
}

// End of questionnaires
var questionnaire_end = {
    type: jsPsychHtmlButtonResponse,
    stimulus:
        "<p><b>Instructions</b></p>" +
        "<p><b>DO NOT PROCEED UNTIL INSTRUCTED BY THE EXPERIMENTER!</b></p>" +
        "<p>Thank you for completing the questionnaires. You may relax while the EEG gel application is being done.</p>",
    choices: ["Continue"],
}