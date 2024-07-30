#export GROQ_API_KEY=<your-api-key-here>
import os
from groq import Groq
groq_key=""
client = Groq(
    api_key=os.environ.get(groq_key),
)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Who is the author of the Apache Ignite book?",
        }
    ],
    model="llama-3.1-70b-versatile",
)
#llama-3.1-70b-versatile
print(chat_completion.choices[0].message.content)