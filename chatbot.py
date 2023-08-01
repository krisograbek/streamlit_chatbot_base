import streamlit as st
import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()

openai.api_key = st.secrets["OPEN_AI_API"]

st.title("Experience Our AI-powered Customer Services! 🤖")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.prompt_tokens = 0
    st.session_state.completion_tokens = 0
    st.session_state.total_tokens = 0

    st.session_state.cost_of_response = st.session_state.total_tokens * 0.000002


for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# initialize model
if "model" not in st.session_state:
    st.session_state.model = "gpt-3.5-turbo"

# user input
if user_prompt := st.chat_input("Your prompt"):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # generate responses
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        json_response = openai.ChatCompletion.create(
            model=st.session_state.model,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=False,
        )

        string_response = json_response["choices"][0]["message"]["content"]
        st.session_state.prompt_tokens += json_response["usage"]["prompt_tokens"]
        st.session_state.completion_tokens += json_response["usage"]["completion_tokens"]
        st.session_state.total_tokens += json_response["usage"]["total_tokens"]
        for s in string_response:
            full_response += s
            message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response +  json.dumps(string_response))

    st.session_state.messages.append({"role": "assistant", "content": full_response})

