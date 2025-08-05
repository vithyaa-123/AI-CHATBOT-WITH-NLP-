import spacy
from datetime import datetime
import random

# Load spaCy language model
nlp = spacy.load("en_core_web_sm")

# Define sample responses
responses = {
    "greeting": [
        "Hello! How can I assist you today?",
        "Hi there! What can I do for you?",
        "Hey! Need any help?"
    ],
    "time": [
        lambda: f"The current time is {datetime.now().strftime('%I:%M %p')}. What's next on your schedule?"
    ],
    "weather": [
        "The weather's always nice in the digital world! What's the weather like where you are?"
    ],
    "goodbye": [
        "Catch you later! Have a great day!",
        "Goodbye! Stay safe.",
        "Bye! Come back anytime."
    ],
    "unknown": [
        "I'm not sure I understand. Can you please rephrase?",
        "Hmm... I didn't get that. Could you try again?"
    ]
}

# Simple intent matching function
def get_intent(text):
    text = text.lower()
    if "hi" in text or "hello" in text:
        return "greeting"
    elif "time" in text:
        return "time"
    elif "weather" in text:
        return "weather"
    elif "bye" in text or "exit" in text:
        return "goodbye"
    else:
        return "unknown"

# Chatbot main loop
def chatbot():
    print("Welcome to the xAI Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print(random.choice(responses["goodbye"]))
            break

        intent = get_intent(user_input)
        reply = random.choice(responses[intent])
        # If response is a function (e.g., lambda for time), call it
        if callable(reply):
            reply = reply()
        print(f"Bot: {reply}")

# Run the chatbot
if _name_ == "_main_":
    chatbot()
