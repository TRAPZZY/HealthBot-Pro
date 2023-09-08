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