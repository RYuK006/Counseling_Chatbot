# Virtual Listening Ear 🛋️

This is a simple counseling chatbot built with Python and Streamlit. It provides a safe space for users to express their feelings and offers empathetic, pre-scripted responses.

## My Approach
I decided to go with a **rule-based approach** instead of connecting to a generative AI API (like OpenAI). I wanted to build something from scratch that doesn't rely on external services or cost money. This was a great way to practice simple Python logic, text parsing, and UI building.

It works by checking the user's input for specific emotion keywords (like "sad", "stressed", "lonely") and pulling a random empathetic response tailored to that feeling. 

## Setup Instructions

1. Clone this repository to your local computer.
2. Make sure you have Python installed.
3. Open a terminal in the project folder and install the required library:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the chatbot by running:
   ```bash
   streamlit run app.py
   ```
5. Your web browser should automatically open the chatbot interface!

## Challenges Faced
The biggest challenge was figuring out how to make the conversation feel natural without using a complex AI model. I had to think of a lot of synonyms for feelings and use `random.choice` so the bot wouldn't repeat the exact same sentence every time. Setting up the `session_state` in Streamlit to keep the chat history visible on the screen also took some trial and error, but reading through the Streamlit documentation really helped clear it up!
