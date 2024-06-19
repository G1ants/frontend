import streamlit as st
import logging
from models.agent import Agent


log = logging.getLogger(__name__)

if 'agent' not in st.session_state:
    st.session_state.agent = None
    
# Function to handle button clicks and set the agent
def set_agent(agent: Agent):
    st.session_state.agent = agent
    log.info(f"Agent set to {agent}")

# Function to display the menu with buttons
def display_menu():
    if st.button("Paul Graham"):
        set_agent(agent=Agent.PAUL_GRAHAM)
    if st.button("Naval Ravikant"):
        set_agent(agent=Agent.NAVAL_RAVIKANT)
    if st.button("Steve Jobs"):
        set_agent(agent=Agent.STEVE_JOBS)
    if st.button("Napoleon"):
        set_agent(agent=Agent.NAPOLEON)
    if st.button("Oppenheimer"):
        set_agent(agent=Agent.OPPENHEIMER)
    
    
    if st.session_state.get("agent"):
        st.write(f"Leader selected: {st.session_state.get('agent').value}")
