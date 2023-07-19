import streamlit as st
import openai
import os

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]


# Sidebar
st.sidebar.title("Configuration")

def model_callback():
    st.session_state["model"] = st.session_state["model_selection"]

# initialize model
if "model" not in st.session_state:
    st.session_state.model = "gpt-3.5-turbo"

st.session_state.model = st.sidebar.radio(
    "Model Selection",
    ("gpt-3.5-turbo", "gpt-3.5-turbo-16k"),
    index=0 if st.session_state["model"] else 1,
    on_change=model_callback,
    key="model_selection",
)

st.sidebar.markdown(
    f"""
    ### ℹ️ <span style="white-space: pre-line; font-family: Arial; font-size: 14px;">Current model: {st.session_state.model}.</span>
    """,
    unsafe_allow_html=True,
)

# Bot roles and their respective initial messages
bot_roles = {
    "English": {
        "role": "system",
        "content": "You are a friendly assistant",
        "description": "This is a standard ChatGPT model.",
    },
    "Polish bot": {
        "role": "system",
        "content": "You are a friendly bot that speaks only Polish",
        "description": "This is a friendly bot speaking in Polish.",
    },
    "German bot": {
        "role": "system",
        "content": "You are a friendly bot that speaks only German",
        "description": "This is a friendly bot speaking in German.",
    },
    "English Pirate bot": {
        "role": "system",
        "content": "You are a friendly bot that speaks only English Pirate",
        "description": "This is a friendly bot speaking in English Pirate.",
    },
}

def bot_role_callback():
    st.session_state["bot_role"] = st.session_state["bot_role_selected"]
    st.session_state["messages"] = [bot_roles[st.session_state["bot_role"]]]

if "bot_role" not in st.session_state:
    st.session_state["bot_role"] = "English"

st.session_state.bot_role = st.sidebar.radio(
    "Select bot role",
    tuple(bot_roles.keys()),
    index=list(bot_roles.keys()).index(st.session_state["bot_role"]),
    on_change=bot_role_callback,
    key="bot_role_selected"
)

description = bot_roles[st.session_state["bot_role"]]["description"]

st.sidebar.markdown(
    f"""
    ### ℹ️ Description
    <span style="white-space: pre-line; font-family: Arial; font-size: 14px;">{description}</span>
    """,
    unsafe_allow_html=True,
)


# Main App
st.title("My Own ChatGPT!🤖")

def reset_messages():
    return [bot_roles[st.session_state["bot_role"]]]

# Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = reset_messages()


for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# user input
if user_prompt := st.chat_input("Your prompt"):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # generate responses
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        for response in openai.ChatCompletion.create(
            model=st.session_state.model,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
