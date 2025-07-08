# LLM client
# uv run ./examples/ollama/llm_client.py

from python_a2a import A2AClient

print("Running LLM client ...")

# Test the servers
llm_client = A2AClient("http://localhost:5001")
travel_client = A2AClient("http://localhost:5002")

llm_result = llm_client.ask("What is the capital of Bangladesh?")
travel_result = travel_client.ask('{"query": "What are some must-see attractions in Bangladesh?"}')

print(llm_result)
print(travel_result)
