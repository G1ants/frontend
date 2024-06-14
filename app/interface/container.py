import streamlit as st

from api.message import send_message

if 'input' not in st.session_state:
    st.session_state.input = ""
    
def display_interface():
    st.text_area(label="chat_box", label_visibility="collapsed", height=500, disabled=True)
    st.session_state.input = st.text_input(label="chat_input", label_visibility="collapsed", placeholder="Type here...")
    
    _, sendBtnCol = st.columns((7, 1))
    with sendBtnCol:
        send_btn = st.button(
            label="Send", 
            key="send_button", 
            disabled=not st.session_state.get("input"),
        )
        if send_btn:
            send_message()