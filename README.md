# AI-CHATBOT-WITH-NLP-
COMPANY: CODTECH IT SOLUTIONS

NAME: VITHYAA A

INTERN ID: CTO4DZ52

DOMAIN: python development

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH
🧠 AI Chatbot with NLP – Project Description

The AI Chatbot with NLP is an intelligent conversational system designed to simulate human-like interactions using Natural Language Processing (NLP) techniques. It is a rule-based chatbot that understands basic user inputs such as greetings, time queries, weather-related questions, and exit commands. The chatbot uses Python as the core programming language and leverages the spaCy NLP library to process and understand user input. This project demonstrates how AI and NLP can be used to build interactive, user-friendly digital assistants.

🔍 Project Objective

The primary goal of the project is to create a text-based AI chatbot that can:

Understand natural language typed by users.

Identify the user’s intent (greeting, asking time, weather, etc.).

Respond with relevant, predefined answers using a rule-based approach.


While it does not connect to external APIs like weather services, it showcases how conversational logic and basic intent recognition work in a chatbot system using NLP techniques.


---

⚙ Tools and Technologies Used

1. Python

Python is the core programming language used to develop the chatbot. Its simplicity, readability, and wide library support make it the ideal choice for NLP and AI-based projects.

2. spaCy (Natural Language Processing)

spaCy is an open-source NLP library that allows the chatbot to process and understand the structure of user inputs. It is used for:

Tokenization (breaking text into words/tokens)

Part-of-speech tagging

Text normalization


In this project, spaCy helps detect certain keywords (like "time", "weather", "hello") to identify the user’s intent.

Command to install:

pip install spacy
python -m spacy download en_core_web_sm

3. datetime Module

The built-in datetime module is used to fetch the current system time, allowing the chatbot to answer time-related questions dynamically.

4. random Module

The Python random module is used to vary the bot’s responses for the same intent, making the interaction feel more natural and less robotic.

5. Visual Studio Code (VS Code)

VS Code is the integrated development environment (IDE) used to write, test, and run the chatbot script. It provides useful features like syntax highlighting, terminal integration, and debugging support.


---

🧩 How It Works

1. User Input: The chatbot reads the user's message via the console.


2. Intent Detection: The chatbot uses a simple rule-based logic to check if the message contains known keywords like “hi”, “time”, “weather”, etc.


3. Response Generation: Based on the identified intent, the chatbot selects a random predefined response or dynamically generates one (e.g., current time).


4. Exit Handling: If the user types “exit”, the chatbot responds with a farewell message and ends the conversation.




---

✅ Features

Basic NLP-based intent recognition

Multiple responses per intent (adds variation)

Time-based dynamic responses

User-friendly interaction through a command-line interface



---

📌 Future Improvements

Integrating real-time weather data using APIs (like OpenWeatherMap)

Adding machine learning for intent classification

Enhancing dialogue flow and memory for multi-turn conversations

Creating a GUI-based chatbot or deploying it on a web app



---

Let me know if you want this in PDF format or need a project report template too!
