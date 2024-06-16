from typing import Optional
import streamlit as st

from api.message import send_message
from utils import display_message
from models.message import Message, MessageRequest, MessageResponse, Role
    
def display_interface():
    for message in st.session_state.chat_history:
        with st.chat_message(message.role):
            st.markdown(message.content)

    if prompt := st.chat_input("Enter text here..."):
        st.session_state.chat_history.append(
            Message(
                role=Role.USER,
                content=prompt
            )
        )
        
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_response: Optional[MessageResponse] = send_message(
                input=MessageRequest(
                    message=st.session_state.input,
                    chat_history=st.session_state.get("chat_history")
                )
            )
            if not message_response:
                display_message(
                    message="Error occurred while sending message",
                    isError=True
                )
            else:
                st.session_state.chat_history.append(
                    Message(
                        role=Role.ASSISTANT,
                        content=message_response.message
                    )
                )