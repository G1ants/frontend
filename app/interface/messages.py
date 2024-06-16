import streamlit as st
from models.message import Role

def display_messages():
    for message in st.session_state.get("chat_history", []):
        if message.role == Role.USER:
            st.markdown(f"""
                <div style='background-color: black; padding: 10px; border-radius: 10px; margin-bottom: 10px; max-width: 70%; float: left;'>
                    {message.content}
                </div>
            """, unsafe_allow_html=True)
        elif message.role == Role.ASSISTANT:
            st.markdown(f"""
                <div style='background-color: grey; padding: 10px; border-radius: 10px; margin-bottom: 10px; max-width: 70%; float: right;'>
                    {message.content}
                </div>
            """, unsafe_allow_html=True)