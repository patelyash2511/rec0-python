from rec0 import Memory

# Initialize client
mem = Memory(
    api_key='r0_live_sk_...',
    user_id='user_123'
)

# Store a memory
result = mem.store("User prefers dark mode and Italian food")
print(f"Stored: {result}")

# Recall memories
context = mem.recall(query="food preferences")
print(f"Recalled: {context}")
