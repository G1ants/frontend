import streamlit as st


def apply_custom_style():
    st.markdown(
        """
        <style>
        .stButton > button {
            border-radius: 15px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
