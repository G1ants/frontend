import time
import streamlit as st


def display_message(message: str, isError: bool) -> None:
    POPUP_TEMPLATE = f"""<div style="
        position: fixed;
        top: 15%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: {"red" if isError else "green"};
        color: white;
        padding: 10px;
        border-radius: 5px;
        z-index: 9999;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        width: auto;
        max-width: 80%;  /* Ensures it doesn't get too wide on large screens */
    ">
        <strong>{message}</strong>
    </div>
    """
    popup = st.empty()
    popup.markdown(POPUP_TEMPLATE, unsafe_allow_html=True)
    time.sleep(2)
    popup.empty()
