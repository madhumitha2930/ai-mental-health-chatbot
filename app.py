import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Mental Health Companion", page_icon="🧠")

st.title("🧠 AI Mental Health Companion")

# Load AI model (emotion understanding)
@st.cache_resource
def load_model():
    return pipeline("text-classification",
                    model="j-hartmann/emotion-english-distilroberta-base")

emotion_model = load_model()

# Store conversation (like ChatGPT memory)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello 👋 I'm here to listen. How are you feeling today?"}
    ]

# Show old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type your thoughts...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # AI thinking
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            emotion = emotion_model(user_input)[0]["label"]

            if emotion in ["sadness", "fear"]:
                reply = "I'm really sorry you're feeling this way 💙 Want to tell me more?"
            elif emotion == "anger":
                reply = "That sounds frustrating. Let's slow down and breathe together."
            elif emotion == "joy":
                reply = "I'm glad to hear that 😊 What made your day good?"
            else:
                reply = "I understand. I'm here with you. Tell me more."

            st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    
