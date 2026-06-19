import streamlit as st
import random

# Page config
st.set_page_config(page_title="Virtual Listening Ear", page_icon="🛋️")

import re

def contains_keywords(text, keywords):
    for word in keywords:
        if re.search(r'\b' + re.escape(word) + r'\b', text):
            return True
    return False

def get_response(user_input):
    user_input = user_input.lower()
    
    # Simple rule-based keyword matching using whole words
    if contains_keywords(user_input, ["hello", "hi", "hey"]):
        return random.choice(["Hello there. How are you feeling today?", "Hi. What's on your mind?"])
        
    elif contains_keywords(user_input, ["sad", "depressed", "unhappy", "down", "terrible", "cry", "hurt", "hurted", "fight"]):
        return random.choice([
            "I'm really sorry you're feeling this way. Do you want to talk more about what's making you feel sad?", 
            "It sounds like you're going through a tough time. I'm here to listen."
        ])
        
    elif contains_keywords(user_input, ["anxious", "nervous", "stress", "stressed", "panic", "overwhelmed"]):
        return random.choice([
            "Take a deep breath. Stress can be really overwhelming. What's causing you to feel this way?", 
            "Anxiety is tough to deal with. Try to focus on the present moment. Want to talk about what's stressing you?"
        ])
        
    elif contains_keywords(user_input, ["lonely", "alone", "isolated"]):
        return "Feeling lonely is really hard. Please know that I'm here chatting with you right now. Do you have anyone you can reach out to?"
        
    elif contains_keywords(user_input, ["angry", "mad", "frustrated", "annoyed"]):
        return "It's normal to feel frustrated when things don't go right. Do you want to vent about it?"
        
    elif contains_keywords(user_input, ["happy", "good", "great", "better", "fine", "love", "luv"]):
        return "That sounds like a really strong emotion! It's important to process these feelings."
        
    elif contains_keywords(user_input, ["thank", "thanks"]):
        return "You're welcome. I'm always here to listen."
        
    elif contains_keywords(user_input, ["bye", "goodbye"]):
        return "Take care of yourself. Goodbye for now."
        
    else:
        # Fallback responses if no keywords match
        return random.choice([
            "Tell me more about that.",
            "How does that make you feel?",
            "I'm listening.",
            "That sounds difficult. Can you elaborate?",
            "I see. Go on."
        ])

st.title("Virtual Listening Ear 🛋️")
st.write("A safe space to share your thoughts. I'm just a simple bot, but I'm here to listen.")

# Set up the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Start with a greeting
    st.session_state.messages.append({"role": "assistant", "content": "Hi there. How are you feeling today?"})

# Draw the past messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get new input from user
prompt = st.chat_input("Type how you feel here...")

if prompt:
    # Show user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get and show bot response
    response = get_response(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
        
    st.session_state.messages.append({"role": "assistant", "content": response})
