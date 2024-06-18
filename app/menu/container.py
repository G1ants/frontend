import streamlit as st

if 'agent' not in st.session_state:
    st.session_state.agent = None
    
def display_menu():
    st.button(label="Paul Graham")
    st.button(label="Naval Ravikant")
    st.button(label="Steve Jobs")
    st.button(label="Napoleon")
    st.button(label="Oppenheimer")
