#export GROQ_API_KEY=<your-api-key-here>
import os
from groq import Groq
#groq_key=""
client = Groq(
    api_key=os.environ.get("$GROQ_API_KEY"),
)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Write a python web app for tranfer file and messages",
        }
    ],
    model="llama-3.1-70b-versatile",
)
#llama-3.1-70b-versatile
print(chat_completion.choices[0].message.content)