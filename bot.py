import os 

from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_openai import OpenAI, AzureChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


def get_agent():
    #llm = OpenAI(temperature=0)
    llm = AzureChatOpenAI(
        openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
        azure_deployment=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"],
    )

    tools = load_tools(["serpapi"], llm=llm)
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    return agent 
