from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_openai import OpenAI

from bot import get_agent

def main():
    agent = get_agent()

    # Get input from the user
    user_input = input("User: ")

    # Run the agent with the user's input
    response = agent.run(user_input)
    print("Bot: ", response)

if __name__ == "__main__":
    main()