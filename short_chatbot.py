import streamlit as st
import openai
import os

from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

st.title("My Own ChatGPT!🤖")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if "model" not in st.session_state:
    st.session_state.model = "gpt-3.5-turbo"

if user_prompt := st.chat_input("Your prompt"):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # generate responses
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = openai.ChatCompletion.create(
            model=st.session_state.model,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
        )
        message_placeholder.markdown(response.choices[0].message.content)

    st.session_state.messages.append({"role": "assistant", "content": response})
