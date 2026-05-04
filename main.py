import asyncio
from dotenv import load_dotenv
import os

from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client

from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

stdio_server_params = StdioServerParameters(
    command="python",
    args=["C:/mcp/shellserver/mcp-crash-course/servers/math_server.py"],
)
async def main():
    print("Hello from mcp-crash-course!")
    

if __name__ == "__main__":
    asyncio.run(main())
