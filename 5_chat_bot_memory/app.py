import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from google import genai


load_dotenv(Path(__file__).with_name(".env"))

st.set_page_config(page_title="Memory Chat", page_icon="💬", layout="centered")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,600;9..144,700&display=swap');

    .stApp {
        background: radial-gradient(ellipse at 8% 0%, #e7f0e8 0, transparent 34%),
                    linear-gradient(145deg, #fbfcf8 0%, #f3f6f0 100%);
        color: #26352d;
        font-family: 'DM Sans', sans-serif;
    }
    h1, h2, h3 { font-family: 'Fraunces', Georgia, serif !important; color: #244331; }
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: #ffffff;
        border-color: #dce6dc;
        border-radius: 8px;
    }
    [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"],
    [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] * {
        color: #000000 !important;
        -webkit-text-fill-color: #000000;
    }
    [data-testid="stChatInput"] {
        border-color: #c8d7c9;
    }
    [data-testid="stChatInput"] textarea {
        color: #ffffff !important;
        caret-color: #ffffff;
        -webkit-text-fill-color: #ffffff;
    }
    [data-testid="stChatInput"] textarea::placeholder {
        color: #c9cbd3 !important;
        -webkit-text-fill-color: #c9cbd3;
        opacity: 1;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Memory Chat")
st.write("A conversation that keeps the context as you go.")

if "conversation" not in st.session_state:
    st.session_state.conversation = []

with st.sidebar:
    st.subheader("Conversation")
    st.caption(f"{len(st.session_state.conversation) // 2} exchanges")
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.conversation = []
        st.rerun()

chat_history = st.container(border=True)
with chat_history:
    for message in st.session_state.conversation:
        with st.chat_message(message["role"]):
            st.markdown(message["text"])

user_message = st.chat_input("Send a message")
if user_message:
    st.session_state.conversation.append({"role": "user", "text": user_message})
    with chat_history:
        with st.chat_message("user"):
            st.markdown(user_message)

    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("Gemini API key not found. Add GEMINI_API_KEY to 5_chat_bot_memory/.env and try again.")
    else:
        contents = [
            {
                "role": "model" if message["role"] == "assistant" else "user",
                "parts": [{"text": message["text"]}],
            }
            for message in st.session_state.conversation
        ]
        try:
            client = genai.Client(api_key=api_key)
            with chat_history:
                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        response = client.models.generate_content(
                            model="gemini-3.5-flash-lite",
                            contents=contents,
                        )
                    reply = response.text or "I couldn't produce a text response. Please try again."
                    st.markdown(reply)
            st.session_state.conversation.append({"role": "assistant", "text": reply})
        except Exception as error:
            st.error(f"Gemini couldn't reply right now. Please try again. Details: {error}")