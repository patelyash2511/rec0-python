from rec0 import Memory
from openai import OpenAI


def chat_with_memory(user_message: str, user_id: str = "user_123"):
    # Initialize clients
    mem = Memory(api_key='r0_live_sk_...', user_id=user_id)
    ai = OpenAI()

    # Get relevant context
    context = mem.recall(query=user_message)

    # Send to LLM with context
    response = ai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"Context: {context}"},
            {"role": "user", "content": user_message}
        ]
    )

    assistant_message = response.choices[0].message.content

    # Store conversation
    mem.store(f"User: {user_message}\nAssistant: {assistant_message}")

    return assistant_message


if __name__ == "__main__":
    reply = chat_with_memory("What's my favorite food?")
    print(reply)
