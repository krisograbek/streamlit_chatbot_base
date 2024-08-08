import streamlit as st
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

st.title("My Own ChatGPT!🤖")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if "model" not in st.session_state:
    st.session_state.model = "gpt-4o-mini"

if user_prompt := st.chat_input("Your prompt"):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # generate responses
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = client.chat.completions.create(
            model=st.session_state.model,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
        )
        message_placeholder.markdown(response.choices[0].message.content)

    st.session_state.messages.append({"role": "assistant", "content": response})
