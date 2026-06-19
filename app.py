import streamlit as st
import google.generativeai as genai

# Page config
st.set_page_config(page_title="AI Virtual Counselor", page_icon="🛋️")

st.title("AI Virtual Counselor 🛋️")
st.write("A safe, intelligent space to share your thoughts. Powered by Google Gemini.")

# Sidebar for API Key
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter your Google Gemini API Key:", type="password")
st.sidebar.markdown("[Get a free Gemini API key here](https://aistudio.google.com/app/apikey)")

if not api_key:
    st.warning("Please enter your Gemini API Key in the sidebar to start chatting.")
    st.stop()

# Configure the generative AI model
genai.configure(api_key=api_key)

# Initialize the chat session in session state
if "chat_session" not in st.session_state:
    # Use gemini-1.5-flash which is fast and great for general text
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-latest",
        system_instruction="You are a compassionate, empathetic, and professional virtual counselor. Listen to the user's problems, validate their feelings, and offer thoughtful, gentle advice without being overly clinical. Keep your responses conversational, concise, and focused on helping the user process their emotions."
    )
    st.session_state.chat_session = model.start_chat(history=[])
    st.session_state.messages = []
    
    # Add a welcoming message
    greeting = "Hi there. I'm here to listen and help. How are you feeling today?"
    st.session_state.messages.append({"role": "assistant", "content": greeting})

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

    # Get bot response
    try:
        with st.spinner("Thinking..."):
            response = st.session_state.chat_session.send_message(prompt)
            assistant_response = response.text
            
            with st.chat_message("assistant"):
                st.markdown(assistant_response)
                
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    except Exception as e:
        st.error(f"An error occurred: {e}")
