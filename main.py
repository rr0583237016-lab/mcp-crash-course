import asyncio
from dotenv import load_dotenv
import os
load_dotenv()
async def main():
    print("Hello from mcp-crash-course!")
    print(os.getenv("GOOGLE_API_KEY"))

if __name__ == "__main__":
    asyncio.run(main())
