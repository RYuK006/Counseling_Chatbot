import streamlit as st
import random

# Page config
st.set_page_config(page_title="Virtual Listening Ear", page_icon="🛋️")

def get_response(user_input):
    user_input = user_input.lower()
    
    # Simple rule-based keyword matching
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return random.choice(["Hello there. How are you feeling today?", "Hi. What's on your mind?"])
        
    elif any(word in user_input for word in ["sad", "depressed", "unhappy", "down", "terrible"]):
        return random.choice([
            "I'm really sorry you're feeling this way. Do you want to talk more about what's making you feel sad?", 
            "It's completely okay to feel down sometimes. I'm here to listen."
        ])
        
    elif any(word in user_input for word in ["anxious", "nervous", "stress", "stressed", "panic"]):
        return random.choice([
            "Take a deep breath. Stress can be really overwhelming. What's causing you to feel this way?", 
            "Anxiety is tough to deal with. Try to focus on the present moment. Want to talk about what's stressing you?"
        ])
        
    elif any(word in user_input for word in ["lonely", "alone", "isolated"]):
        return "Feeling lonely is really hard. Please know that I'm here chatting with you right now. Do you have anyone you can reach out to?"
        
    elif any(word in user_input for word in ["angry", "mad", "frustrated", "annoyed"]):
        return "It's normal to feel frustrated when things don't go right. Do you want to vent about it?"
        
    elif any(word in user_input for word in ["happy", "good", "great", "better", "fine"]):
        return "I'm so glad to hear that! It's important to appreciate the good days."
        
    elif "thank" in user_input:
        return "You're welcome. I'm always here to listen."
        
    elif "bye" in user_input:
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
