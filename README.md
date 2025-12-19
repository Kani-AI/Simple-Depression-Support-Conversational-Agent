# Simple-Depression-Support-Conversational-Agent
A Streamlit-based mental health support chatbot that provides empathetic, non-judgmental conversations using AI. Designed to offer coping strategies, emotional validation, and crisis-aware support in real time.
MindCare Chatbot is a Streamlit-based depression support chatbot designed to provide empathetic, non-judgmental conversations for users experiencing emotional distress.
It leverages large language models to offer supportive dialogue, basic coping strategies, and crisis guidance when necessary.

⚠️ This chatbot is not a replacement for professional mental health care.

🎯 Objectives

Provide a safe space for users to express emotions

Offer empathetic and supportive responses

Encourage healthy coping mechanisms

Detect crisis-related language and provide emergency resources

Maintain respectful and ethical AI interaction

🧠 Key Features

🗣️ Conversational mental-health support

🧍 Optional user context (name, age, concerns)

⚠️ Crisis keyword detection

🚨 Emergency support protocol activation

💬 Persistent chat history using Streamlit session state

🛠️ Tech Stack

Programming Language: Python

Framework: Streamlit

AI Model API: OpenRouter (LLM-based chat completion)

Libraries:

streamlit

openai (OpenRouter compatible client)

🏗️ System Architecture

User provides optional personal context

Chat interface accepts user input

Messages are stored in session state

Input is checked for crisis indicators

AI model generates empathetic response

Emergency resources are shown if risk is detected

🚀 How to Run
1️⃣ Clone the Repository
git clone https://github.com/your-username/mindcare-chatbot.git
cd mindcare-chatbot

2️⃣ Install Dependencies
pip install streamlit openai

3️⃣ Set API Key

Replace the API key placeholder in the code or use environment variables:

export OPENROUTER_API_KEY="your_api_key_here"

4️⃣ Run the App
streamlit run app.py

⚠️ Crisis Handling

The chatbot monitors user input for high-risk phrases such as:

“want to die”

“kill myself”

“end it all”

If detected, it:

Displays emergency contact information

Encourages immediate professional help

Avoids giving medical or harmful advice

🚫 Limitations

Not a licensed therapist

Relies on keyword-based crisis detection

Responses depend on the underlying language model

Requires internet connectivity

🔮 Future Enhancements

NLP-based emotion classification

Multi-language support

Secure user authentication

Chat analytics (without storing personal data)

Mobile-friendly deployment

⚖️ Ethical Disclaimer

This project is intended only for educational and supportive purposes.
It does not diagnose, treat, or replace professional mental health services.

If you or someone else is in danger, contact local emergency services immediately.
