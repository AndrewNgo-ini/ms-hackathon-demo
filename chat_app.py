import streamlit as st
import datetime
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_openai import OpenAI
from dotenv import load_dotenv
from bot import get_agent

load_dotenv()  # take environment variables from .env.

def get_current_time():
    return datetime.datetime.now().strftime("%H:%M")

def main():
    st.set_page_config(page_title="Streamlit Chat App with Langchain", page_icon=":speech_balloon:")

    st.title("Streamlit Chat App with Langchain")

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "agent" not in st.session_state:
        st.session_state.agent = get_agent()

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(f"{message['name']} - {message['time']}")
            st.write(message["content"])

    # User input
    user_name = st.text_input("Your Name", value="User")
    user_input = st.chat_input("Type your message here...")

    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "name": user_name,
            "time": get_current_time()
        })

        # Display user message
        with st.chat_message("user"):
            st.write(f"{user_name} - {get_current_time()}")
            st.write(user_input)

        # Get response from the agent
        with st.spinner("Thinking..."):
            response = st.session_state.agent.run(user_input)
        
        # Add response to chat history
        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "name": "Assistant",
            "time": get_current_time()
        })

        # Display assistant response
        with st.chat_message("assistant"):
            st.write(f"Assistant - {get_current_time()}")
            st.write(response)

if __name__ == "__main__":
    main()