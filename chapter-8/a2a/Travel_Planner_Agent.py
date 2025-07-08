from python_a2a import AgentNetwork, A2AClient, AIAgentRouter


from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM
import asyncio



async def main():
    # Create an agent network
    network = AgentNetwork(name="Travel Assistant Network")

    # Add agents to the network
    network.add("weather", "http://localhost:8001")
    network.add("search", "http://localhost:8002")

    # List all available agents
    print("\nAvailable Agents:")
    for agent_info in network.list_agents():
        print(f"- {agent_info['name']}: {agent_info['description']}")

    # Create a llm client
    llm_client=A2AClient("http://localhost:5001")

    params = {
        "destination": "Paris",
        "travel_dates": "June 21-25"
    }
    
    weather_agent = network.get_agent("weather")
    forecast = weather_agent.ask(f"What's the weather in {params["destination"]}?")
    print ("Weather forecast: "+ forecast)

    search_agent = network.get_agent("search")

    if "sunny" in forecast.lower() or "clear" in forecast.lower():
        activities = search_agent.ask(f"Recommend outdoor activities in {params["destination"]}")
    else:
        activities = search_agent.ask(f"Recommend indoor activities in {params["destination"]}")
    
    # Make summary of the plan
    prompt = f"You are a travel assistant. Based on the weather forecast result {forecast} and the recommendations [{activities}], suggest me a few must-see attractions on date {params["travel_dates"]}."
    print(f"Prompt: {prompt}")

    llm_result = llm_client.ask(prompt)

    print(f"LLM response: {llm_result}")

    
if __name__ == "__main__":
    asyncio.run(main())