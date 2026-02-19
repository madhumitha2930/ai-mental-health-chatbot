import streamlit as st
from groq import Groq

st.set_page_config(page_title="AI Mental Health Companion")

st.title("🧠 AI Mental Health Companion")
st.write("Hello 👋 I'm here to listen. How are you feeling today?")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your thoughts...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are a supportive mental health companion. Be kind and empathetic."},
                    {"role": "user", "content": user_input}
                ],
            )

            reply = completion.choices[0].message.content
            st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
   
    
