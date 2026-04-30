from rec0 import Memory


def build_rag_context(query: str, user_id: str = "user_123"):
    mem = Memory(api_key='r0_live_sk_...', user_id=user_id)

    # Retrieve relevant memories
    memories = mem.recall(query=query, limit=5)

    # Format for RAG context
    context = "\n".join([
        f"- {m.get('content', '')}" for m in memories
    ])

    return f"Relevant user context:\n{context}"


if __name__ == "__main__":
    context = build_rag_context("What technologies does user prefer?")
    print(context)
