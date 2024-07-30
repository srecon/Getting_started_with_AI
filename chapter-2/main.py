import os
from groq import Groq
groq_key="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"
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