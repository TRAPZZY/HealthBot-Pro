def draw_bold_chatbot_name():
    bold_name = [
        "████████╗██╗  ██╗ ██████╗ ██████╗ ██╗     ██╗ ██████╗ ███╗   ██╗",
        "╚══██╔══╝██║  ██║██╔═══██╗██╔══██╗██║     ██║██╔═══██╗████╗  ██║",
        "   ██║   ███████║██║   ██║██████╔╝██║     ██║██║   ██║██╔██╗ ██║",
        "   ██║   ██╔══██║██║   ██║██╔══██╗██║     ██║██║   ██║██║╚██╗██║",
        "   ██║   ██║  ██║╚██████╔╝██████╔╝███████╗██║╚██████╔╝██║ ╚████║",
        "   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝",
    ]

    for line in bold_name:
        print(line)

# Draw the bold chatbot name
draw_bold_chatbot_name()

print('   ')
print('CREATED BY TRAPZZY')

import random
import nltk
from nltk.tokenize import word_tokenize

# Download NLTK data (if not already downloaded)
nltk.download('punkt')

# Dictionary to store user queries and responses
conversation_history = {}

# Medical symptom database
symptoms_database = {
    "fever": "Fever can be a symptom of various illnesses. It's essential to consult a healthcare professional for a proper diagnosis.",
    "cough": "A persistent cough may be a symptom of an underlying condition. I recommend seeing a doctor for evaluation.",
    "headache": "Headaches can have various causes, including stress, dehydration, or underlying health issues. It's important to identify the cause.",
    "Common Cold": ["Runny or stuffy nose", "Sneezing", "Cough", "Sore throat", "Mild headache"],
    "Influenza (Flu)": ["Fever", "Chills", "Muscle aches", "Fatigue", "Cough"],
    "COVID-19": ["Fever", "Dry cough", "Shortness of breath", "Fatigue", "Loss of taste or smell"],
    "Allergies": ["Sneezing", "Runny or itchy nose", "Watery eyes", "Coughing", "Skin rash"],
    "Asthma": ["Shortness of breath", "Wheezing", "Chest tightness", "Coughing"],
    "Migraine": ["Severe headache", "Nausea", "Vomiting", "Sensitivity to light and sound"],
    "Heart Attack": ["Chest pain or discomfort", "Shortness of breath", "Nausea", "Cold sweat"],
    "Stroke": ["Sudden numbness or weakness in the face, arm, or leg", "Confusion", "Trouble speaking"],
    "Diabetes": ["Frequent urination", "Increased thirst", "Unexplained weight loss", "Fatigue"],
    "High Blood Pressure": ["Headaches", "Dizziness", "Chest pain", "Shortness of breath"],
    "Pneumonia": ["High fever", "Cough with phlegm", "Chest pain", "Shortness of breath"],
    "Gastroenteritis": ["Nausea", "Vomiting", "Diarrhea", "Abdominal pain", "Fever"],
    "Arthritis": ["Joint pain", "Swelling", "Stiffness", "Reduced range of motion"],
    "Osteoporosis": ["Bone pain", "Fractures", "Loss of height", "Back pain"],
    "Alzheimer's Disease": ["Memory loss", "Confusion", "Difficulty with familiar tasks", "Personality changes"],
    "Parkinson's Disease": ["Tremors", "Slowed movement", "Muscle stiffness", "Balance problems"],
    "Cancer": ["Unexplained weight loss", "Fatigue", "Lumps or masses", "Change in skin or moles"],
    "HIV/AIDS": ["Fatigue", "Fever", "Swollen lymph nodes", "Night sweats", "Rapid weight loss"],
    "Anxiety Disorders": ["Excessive worry", "Restlessness", "Irritability", "Panic attacks"],
    "Depression": ["Persistent sadness", "Loss of interest in activities", "Changes in sleep and appetite"],
    "Bipolar Disorder": ["Manic episodes (elevated mood)", "Depressive episodes", "Impulsivity"],
    "Schizophrenia": ["Hallucinations", "Delusions", "Disorganized thinking", "Social withdrawal"],
    "Epilepsy": ["Seizures", "Loss of consciousness", "Convulsions", "Confusion"],
    "Malaria": ["Fever", "Chills", "Sweating", "Headaches", "Muscle pain"],
    "Tuberculosis (TB)": ["Cough that lasts 3 weeks or more", "Chest pain", "Weight loss", "Fever"],
    "Lupus": ["Fatigue", "Joint pain", "Skin rashes", "Fever", "Swelling"],
    "Rheumatoid Arthritis": ["Joint pain", "Morning stiffness", "Swelling", "Fatigue", "Fever"],
    "Chronic Obstructive Pulmonary Disease (COPD)": ["Shortness of breath", "Chronic cough", "Wheezing", "Chest tightness"],
    "Eating Disorders": ["Excessive preoccupation with food and body weight", "Restrictive eating", "Binge eating"],
    "Fibromyalgia": ["Chronic pain", "Fatigue", "Sleep disturbances", "Tender points"],
    "Obsessive-Compulsive Disorder (OCD)": ["Obsessions (repetitive, unwanted thoughts)", "Compulsions (repetitive behaviors)"],
    "Post-Traumatic Stress Disorder (PTSD)": ["Flashbacks", "Nightmares", "Severe anxiety", "Avoidance of reminders"],
    "Bipolar II Disorder": ["Hypomanic episodes (less severe than mania)", "Depressive episodes", "Impulsivity"],
    "Binge-Eating Disorder": ["Frequent episodes of excessive eating", "Lack of control during binge eating", "Feelings of guilt"],
    "Generalized Anxiety Disorder (GAD)": ["Excessive worry and anxiety", "Restlessness", "Muscle tension"],
    "Panic Disorder": ["Panic attacks", "Sudden and intense fear", "Heart palpitations", "Sweating"],
    "Borderline Personality Disorder (BPD)": ["Impulsive behaviors", "Intense mood swings", "Fear of abandonment"],
    "Schizoaffective Disorder": ["Symptoms of both schizophrenia and mood disorders"],
    "Bulimia Nervosa": ["Binge eating followed by purging behaviors (vomiting, laxatives)"],
    "Narcolepsy": ["Excessive daytime sleepiness", "Sudden sleep attacks", "Sleep paralysis"],
    "Hypochondria (Illness Anxiety Disorder)": ["Excessive worry about having a serious illness", "Frequent medical tests"],
    "Body Dysmorphic Disorder": ["Preoccupation with perceived flaws in physical appearance"],
    "Social Anxiety Disorder (Social Phobia)": ["Intense fear of social situations", "Avoidance of social interactions"],
    "Panic Disorder": ["Recurrent panic attacks", "Fear of future attacks"],
    "Seasonal Affective Disorder (SAD)": ["Depression that occurs seasonally, typically in the winter months"],
    "Restless Leg Syndrome (RLS)": ["Uncomfortable sensations in the legs", "Urge to move legs"],
    "Ehlers-Danlos Syndrome": ["Joint hypermobility", "Skin hyperextensibility", "Easy bruising"],
    "Sickle Cell Disease": ["Pain crises", "Anemia", "Fatigue", "Jaundice"],
    "Hemophilia": ["Excessive bleeding", "Joint pain", "Bruising"],
    "Celiac Disease": ["Digestive problems", "Abdominal pain", "Bloating", "Diarrhea"],
    "Crohn's Disease": ["Abdominal pain", "Diarrhea", "Weight loss", "Fatigue"],
    "Ulcerative Colitis": ["Bloody diarrhea", "Abdominal pain", "Weight loss", "Fatigue"],
    "Polycystic Ovary Syndrome (PCOS)": ["Irregular periods", "Excess hair growth", "Acne", "Weight gain"],
    "Endometriosis": ["Pelvic pain", "Painful periods", "Pain during intercourse"],
    "Interstitial Cystitis": ["Pelvic pain", "Frequent urination", "Urgency to urinate"],
    "Chronic Fatigue Syndrome (CFS)": ["Severe fatigue", "Muscle pain", "Sleep disturbances"],
    "Fibrous Dysplasia": ["Bone pain", "Bone deformities", "Fractures"],
    "Lyme Disease": ["Fever", "Fatigue", "Joint pain", "Rash"],
    "Huntington's Disease": ["Motor symptoms (involuntary movements)", "Cognitive decline", "Emotional changes"],
    "Myasthenia Gravis": ["Muscle weakness", "Fatigue", "Double vision"],
    "Nephrotic Syndrome": ["Swelling (edema)", "Proteinuria", "Fatigue"],
    "Sarcoidosis": ["Lung symptoms (cough, shortness of breath)", "Skin rashes", "Fatigue"],
    "Turner Syndrome": ["Short stature", "Lack of menstrual periods", "Webbed neck"],
    "Klinefelter Syndrome": ["Low testosterone levels", "Tall stature", "Small testes"],
    "Down Syndrome": ["Intellectual disability", "Distinct facial features", "Heart defects"],
    "Tourette Syndrome": ["Tics (involuntary movements or sounds)", "Obsessions and compulsions"],
    "Muscular Dystrophy": ["Progressive muscle weakness", "Difficulty with motor skills"],
    "Bacterial Pneumonia": ["High fever", "Cough with green or yellow mucus", "Chest pain"],
    "Hepatitis": ["Jaundice", "Fatigue", "Abdominal pain", "Nausea"],
    "Lupus": ["Fatigue", "Joint pain", "Skin rashes", "Fever", "Swelling"],
    "Rheumatoid Arthritis": ["Joint pain", "Morning stiffness", "Swelling", "Fatigue", "Fever"],
    "Chronic Obstructive Pulmonary Disease (COPD)": ["Shortness of breath", "Chronic cough", "Wheezing", "Chest tightness"],
    "Eating Disorders": ["Excessive preoccupation with food and body weight", "Restrictive eating", "Binge eating"],
    "Fibromyalgia": ["Chronic pain", "Fatigue", "Sleep disturbances", "Tender points"],
    "Obsessive-Compulsive Disorder (OCD)": ["Obsessions (repetitive, unwanted thoughts)", "Compulsions (repetitive behaviors)"],
    "Post-Traumatic Stress Disorder (PTSD)": ["Flashbacks", "Nightmares", "Severe anxiety", "Avoidance of reminders"],
    "Bipolar II Disorder": ["Hypomanic episodes (less severe than mania)", "Depressive episodes", "Impulsivity"],
    "Binge-Eating Disorder": ["Frequent episodes of excessive eating", "Lack of control during binge eating", "Feelings of guilt"],
    "Generalized Anxiety Disorder (GAD)": ["Excessive worry and anxiety", "Restlessness", "Muscle tension"],
    "Multiple Sclerosis": ["Fatigue", "Difficulty walking", "Numbness or tingling", "Muscle weakness"],

    # Add more symptoms and information here
}

# Responses for different user inputs
responses = {
    "hello": [
        "Hello! How can I assist you today?", 
        "Hi there! How can I help you?", 
        "Greetings! What can I do for you today?", 
        "Good day! What brings you here?",
    ],
    "symptoms": [
        "Please tell me more about your symptoms.", 
        "I'm here to help with your symptoms. What are you experiencing?", 
        "Let's talk about your symptoms.",
        "I'm listening. What symptoms are you dealing with?",
    ],
    "thank you": [
        "You're welcome! If you have more questions, feel free to ask.", 
        "You're welcome. If you need further assistance, don't hesitate to ask.",
        "No problem at all! If you require more information, just let me know.",
    ],
    "default_responses": [
        "I'm sorry, I may not have the information you need. It's best to consult a healthcare professional for personalized advice.",
        "I'm here to provide information, but it's important to consult a doctor for a proper evaluation.",
        "I'm not a doctor, but I can offer some general guidance. Please consult a healthcare professional for medical advice.",
        "I appreciate your question, but remember that I can't replace a medical professional's expertise.",
    ],
     "additional_responses": [
        "How can I assist you today?",
        "Your health is important to us. What's on your mind?",
        "Feel free to ask me anything related to health.",
        "Hi there! How can I help you?",
        "What health-related questions do you have?",
        "Greetings! What can I do for you today?",
        "Good day! What brings you here?",
        "I'm listening. How can I be of service?",
        "Hello! How can I assist with your health concerns?",
        "Welcome! What health-related inquiries do you have?",
        "I'm here to provide health information. What's on your mind?",
        "No problem at all! If you require more information, just let me know.",
        "Your health matters. How can I assist you today?",
        "I'm your health information source. What do you need?",
        "What's on your health agenda today?",
        "Please share your health-related queries with me.",
        "I'm here to help with your health-related questions.",
        "Let's discuss your health concerns.",
        "Hi! What health topics are you interested in?",
        "I'm your source for health insights. What's your query?",
        "I'm your health assistant. How can I help you?",
        "Greetings! Your health is important. How can I assist you today?",
        "Your well-being is our priority. How can I assist?",
        "Hello! I'm here to assist with your health-related questions.",
        "Welcome! Let's talk about your health and wellness.",
        "Good to see you! How can I assist you in your health journey?",
        "I'm here to provide information and guidance. What's your question?",
        "Hello! Feel free to ask anything related to health and wellness.",
        "I'm here to assist you on your path to better health. What's your query?",
        "Your health and wellness are our top priorities. How can I assist you today?",
        "Hi there! Your health journey begins here. What do you need?",
        "Your health is in good hands. What can I do for you today?",
        "Greetings! Let's explore the world of health together.",
        "Good day! I'm here to empower you with health knowledge.",
        "I'm all ears! How can I assist with your health concerns?",
        "Hello! I'm here to guide you on your health and wellness journey.",
        "Welcome! Your health goals are important. How can I help you achieve them?",
        "Your health is unique. Let's tailor our discussion to your needs.",
        "I'm here to provide health wisdom. What questions do you have?",
        "Your well-being matters to us. How can I support you today?",
        "Hi! Let's chat about your health and well-being.",
        "Your health is a priority. How can I contribute to your well-being?",
        "Greetings! Your health is valuable. How can I assist you today?",
        "Good day! I'm here to provide insights for your health journey.",
        "I'm ready to assist. What health topics interest you today?",
        "Hello! Your health is our concern",
     ]
    
}

# Function to tokenize user input
def tokenize_input(user_input):
    return word_tokenize(user_input.lower())

# Function to generate a response
def get_response(user_input):
    tokens = tokenize_input(user_input)

    # Check if the user's input contains medical symptoms
    for token in tokens:
        if token in symptoms_database:
            return symptoms_database[token]
    
    # Check if the user's input is in the conversation history
    if user_input in conversation_history:
        response = conversation_history[user_input]
    else:
        response = random.choice(responses["default_responses"])  # Random default response

    return response

# Main chat loop
print("Healthcare Chatbot: Hi there! I'm here to provide health information. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Healthcare Chatbot: Goodbye! Take care.")
        break
    response = get_response(user_input)
    print("Healthcare Chatbot:", response)

    # Learn from user input and store feedback
    new_response = input("Healthcare Chatbot: If my response was not helpful, please provide a better response. Otherwise, type 'no': ")
    if new_response.lower() != "no":
        conversation_history[user_input] = new_response

# Print conversation history
print("Conversation History:")
for user_input, response in conversation_history.items():
    print(f"You: {user_input}")
    print(f"Chatbot: {response}")