import asyncio
import os

from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_openai import OpenAIAugmentedLLM
from mcp_agent.workflows.llm.augmented_llm import RequestParams

app = MCPApp(name="Inventory Agent")

async def example_usage():
    async with app.run() as mcp_agent_app:
        logger = mcp_agent_app.logger
        context = mcp_agent_app.context

        model="qwen2.5:14b"
        # This agent will use the invemtory api to communicate with the FastAPI REST application
        inventory_agent = Agent(
            name="inventory",
            instruction="""You can use API to working with orders from the warehouse.
                Return the requested information when asked.""",
            server_names=["fastapi-mcp"], # MCP servers this Agent can use
        )

        async with inventory_agent:
            # Automatically initializes the MCP servers and adds their tools for LLM use
            tools = await inventory_agent.list_tools()
            logger.info(f"Tools available:", data=tools)

            # Attach an OpenAI LLM to the agent (defaults to GPT-4o)
            llm = await inventory_agent.attach_llm(OpenAIAugmentedLLM)

            # invoke fast-api MCP Server
            result = await llm.generate_str(
                message="Let me know all the orders from the warehouse",
                request_params=RequestParams(model=model),
            )
            logger.info(f"Available orders: {result}")

            # Multi-turn interactions by default
            result = await llm.generate_str(
                "Summarize the result in human language",
                request_params=RequestParams(model=model),
                )
            logger.info(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(example_usage())
