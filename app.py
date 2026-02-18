import streamlit as st
from transformers import pipeline

sentiment = pipeline("sentiment-analysis")

st.title("🧠 AI Mental Health Companion")
st.write("Hello 👋 I am here to listen to you.")

def mood_score(text):
    result = sentiment(text)[0]
    if result['label'] == 'NEGATIVE':
        return -result['score']
    else:
        return result['score']

user_input = st.text_input("How are you feeling today?")

if user_input:
    score = mood_score(user_input)

    if score < -0.5:
        st.error("You seem very sad today 💙 I'm here for you.")
    elif score < 0:
        st.warning("I understand. Tell me more 🤍")
    else:
        st.success("Nice! That sounds positive 😊")

   


    
