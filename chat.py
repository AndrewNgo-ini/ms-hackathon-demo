from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_openai import OpenAI
from dotenv import load_dotenv

def main():
    load_dotenv()

    llm = OpenAI(temperature=0)

    # Load tools, in this case, the SerpAPI tool
    tools = load_tools(["serpapi"], llm=llm)
    
    # Initialize the agent
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    # Get input from the user
    user_input = input("User: ")

    # Run the agent with the user's input
    response = agent.run(user_input)
    print("Bot: ", response)

if __name__ == "__main__":
    main()