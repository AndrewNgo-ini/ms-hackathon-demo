from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_openai import OpenAI
from dotenv import load_dotenv
from bot import get_agent

agent = get_agent()
agent.run("quán ăn ngon quận 1 nguyễn du")
