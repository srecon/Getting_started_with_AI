#pip install langchain
from langchain_community.llms import Ollama
llm = Ollama(
    base_url='http://192.168.1.124:11434',
    model="llama3.1:latest", temperature=0
)
llm.invoke("tell me a joke")
print ("what happened! ")