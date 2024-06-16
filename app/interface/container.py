from typing import Optional
import streamlit as st

from api.message import send_message
from interface.messages import display_messages
from utils import display_message
from models.message import Message, MessageRequest, MessageResponse, Role

if 'input' not in st.session_state:
    st.session_state.input = ""
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [] 

def display_interface():
    display_messages()
    st.session_state.input = st.text_input(label="chat_input", label_visibility="collapsed", placeholder="Type here...")
    
    _, sendBtnCol = st.columns((7, 1))
    with sendBtnCol:
        send_btn = st.button(
            label="Send", 
            key="send_button", 
            disabled=not st.session_state.get("input"),
        )
        if send_btn:
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
                chat_history: list[Message] = st.session_state.get("chat_history")
                curr_shot: list[Message] = [
                    Message(
                        role=Role.USER,
                        content=st.session_state.get("input")
                    ),
                    Message(
                        role=Role.ASSISTANT,
                        content=message_response.message
                    )
                ] 
                chat_history.extend(curr_shot)
                st.session_state.chat_history = chat_history
                print(st.session_state.chat_history)