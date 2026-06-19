# AI Virtual Counselor 🛋️

This is an intelligent, generative AI-powered counseling chatbot built with Python, Streamlit, and the Google Gemini API. It provides a safe space for users to express their feelings, offering deeply empathetic and context-aware counseling advice.

## My Approach
Initially, I built a simple rule-based chatbot, but I quickly realized it lacked the nuance required for real emotional support. I upgraded the system to use **an API for a generative AI model** (Google Gemini 1.5 Flash). 

I gave the model a specific "system instruction" to act as a compassionate, professional virtual counselor. By plugging into the Gemini API, the chatbot now truly understands complex relationship dynamics, validates feelings, and offers dynamic advice rather than just repeating canned scripts.

## Setup Instructions

1. Clone this repository to your local computer.
2. Make sure you have Python installed.
3. Open a terminal in the project folder and install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the chatbot by running:
   ```bash
   streamlit run app.py
   ```
5. Your web browser will open the interface. 
6. You will need to enter a free Google Gemini API key in the sidebar to chat. You can get one from [Google AI Studio](https://aistudio.google.com/app/apikey).

## Challenges Faced
The main challenge was switching from a simple string-matching logic to managing an active AI chat history. I had to learn how to initialize the `genai.GenerativeModel` and use Streamlit's `session_state` to store the Gemini `chat_session` object so the AI remembers the context of the conversation across messages. Passing the "system instruction" was critical to make sure the AI acted like a counselor instead of just a generic AI assistant.
