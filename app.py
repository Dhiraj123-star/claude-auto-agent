import os
import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Claude Auto Agent", page_icon="🤖", layout="centered")

st.title("🤖 Claude Auto-Agent Chat UI")

# Backend URL
API_URL = os.getenv("API_URL")

# Chat History Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation
for role, msg in st.session_state.messages:
    if role == "user":
        st.chat_message("user").markdown(msg)
    else:
        st.chat_message("assistant").markdown(msg)

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Display user message
    st.session_state.messages.append(("user", user_input))
    st.chat_message("user").markdown(user_input)

    # Call backend
    try:
        response = requests.post(API_URL, params={"message": user_input})
        reply = response.json().get("response", "")
    except Exception:
        reply = "⚠️ Error connecting to backend."

    # Display assistant response
    st.session_state.messages.append(("assistant", reply))
    st.chat_message("assistant").markdown(reply)
