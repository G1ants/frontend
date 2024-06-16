import streamlit as st

from interface.container import display_interface
from style import apply_custom_style
from menu.container import display_menu

apply_custom_style()
menu, interface = st.columns((2, 8))
if 'input' not in st.session_state:
    st.session_state.input = ""
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
with menu:
    display_menu()
    
with interface:
    display_interface()
