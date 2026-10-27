
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"),
    timeout=180.0
)

print("Sending request to Ollama...")

messages = []

messages.append(
    {
        "role" :"system",
        "content" :"Act like a very humble agent and respond always under 20 words"
    }
)

while True:

    user_input = input("\nSatendra: ")

    if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )

    assistant_response = response.choices[0].message.content

    print("\nLLM Response:")
    print("Assistant:", assistant_response)

    messages.append({
        "role": "assistant",
        "content": assistant_response
    })
