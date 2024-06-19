from typing import Optional
import streamlit as st

from api.message import send_message
from utils import display_message
from models.message import Message, MessageRequest, MessageResponse, Role


def display_interface():
    for message in st.session_state.chat_history:
        with st.chat_message(message.role):
            st.markdown(message.content)

    with st.form(key="chat_input_form"):
        prompt: str = st.text_input("Enter text here...")
        submit_button = st.form_submit_button(
            label="Send", disabled=st.session_state.get("agent") is None
        )

    if submit_button:
        message_response: Optional[MessageResponse] = send_message(
            input=MessageRequest(
                message=prompt,
                chat_history=st.session_state.get("chat_history"),
                agent=st.session_state.get("agent"),
            )
        )

        if message_response:
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                if not message_response:
                    display_message(
                        message="Error occurred while sending message", isError=True
                    )
                else:

                    st.session_state.chat_history.append(
                        Message(role=Role.USER, content=prompt)
                    )
                    st.session_state.chat_history.append(
                        Message(role=Role.ASSISTANT, content=message_response.content)
                    )
