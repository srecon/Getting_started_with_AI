# client.py
# Run after agent_server.py is running.
import asyncio
from acp_sdk.client import Client
from acp_sdk.models import Message, MessagePart

BASE = "http://127.0.0.1:8000"

async def main() -> None:
    async with Client(base_url=BASE) as client:
        run = await client.run_sync(
            agent="calculator",
            input=[Message(parts=[MessagePart(content="2+2*3")])],
        )
        print("Answer:", run.output[0].parts[0].content)   # -> 8

if __name__ == "__main__":
    asyncio.run(main())
