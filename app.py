import streamlit as st
from textblob import TextBlob
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="AI Mental Health Companion")

st.title("🧠 AI Mental Health Companion")
st.write("I am here to listen to you. You can talk freely 💙")

# memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# function
def mood_score(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity
def save_mood(score):
    date = datetime.now().strftime("%Y-%m-%d")

    data = {"date": [date], "mood": [score]}

    file = "mood_log.csv"

    if os.path.exists(file):
        df = pd.read_csv(file)
        df = pd.concat([df, pd.DataFrame(data)], ignore_index=True)
    else:
        df = pd.DataFrame(data)

    df.to_csv(file, index=False)

# show old chats
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# input
user_input = st.chat_input("How are you feeling today?")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    score = mood_score(user_input)
    save_mood(score)

    if score < -0.5:
        reply = "I'm really sorry you're feeling this way 💙 I'm here with you. Want to tell me what happened?"
    elif score < 0:
        reply = "I understand. It sounds a bit difficult. I'm listening."
    else:
        reply = "That’s nice to hear 😊 What made your day better?"

    st.chat_message("assistant").write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
st.divider()
st.subheader("📈 Your Mood Progress")

if os.path.exists("mood_log.csv"):
    df = pd.read_csv("mood_log.csv")
    st.line_chart(df.set_index("date"))
else:
    st.write("No mood history yet")
