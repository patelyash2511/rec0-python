# rec0 Python SDK

Official Python client library for [rec0](https://rec0.vercel.app) - Persistent memory infrastructure for AI applications.

[![PyPI version](https://badge.fury.io/py/memorylayer-py.svg)](https://pypi.org/project/memorylayer-py/)
[![Tests](https://github.com/patelyash2511/rec0-python/workflows/tests/badge.svg)](https://github.com/patelyash2511/rec0-python/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Quick Start

```python
from rec0 import Memory

# Initialize with your API key
mem = Memory(
    api_key='r0_live_sk_...',
    user_id='user_123'
)

# Store a memory
mem.store("User prefers dark mode and Italian food")

# Recall relevant memories
context = mem.recall(query="user preferences")
print(context)
# Returns: "User prefers dark mode and Italian food"
```

## Install

```bash
pip install memorylayer-py
```

**Note:** The package name is `memorylayer-py` but you import it as `rec0`:

```python
from rec0 import Memory  # Import name is 'rec0', not 'memorylayer'
```

## Get Your API Key

1. Sign up at [rec0.vercel.app](https://rec0.vercel.app)
2. Get your API key from the dashboard
3. Start building!

## Documentation

- [Quick Start Guide](docs/quickstart.md)
- [API Reference](docs/api_reference.md)
- [Examples](docs/examples.md)
- [Full Documentation](https://rec0.vercel.app/docs)

## Features

- **Auto-Capture**: Automatically extracts entities, facts, and preferences
- **Smart Retrieval**: Hybrid BM25 + cosine similarity search
- **Memory Decay**: Intelligent aging and conflict resolution
- **Privacy-first**: Per-user encryption, data isolation, and GDPR-compliant deletion. Your users' data is encrypted and never shared with third parties.
- **LLM-Agnostic**: Works with any LLM (OpenAI, Anthropic, Google, local models)

## rec0 vs Mem0

| rec0 | Mem0 |
|------|------|
| Privacy: Per-user encryption & isolation | Standard cloud storage |

## Enterprise Deployment

The Python SDK is fully open source (MIT license). The backend API is
closed source but available for enterprise on-premise deployment.

For self-hosted deployments, contact: enterprise@rec0.vercel.app

## Examples

### Basic Usage

```python
from rec0 import Memory

mem = Memory(api_key='r0_...', user_id='user_123')

# Store
mem.store("User is a Python developer")

# Recall
context = mem.recall(query="programming")
```

### AI Chatbot with Memory

```python
from rec0 import Memory
from openai import OpenAI

mem = Memory(api_key='r0_...', user_id='user_456')
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

# Store the conversation
mem.store(f"User: {user_message}\nAssistant: {response}")
```

See [examples/](examples/) for more.

## API Reference

### `Memory(api_key, user_id, app_id=None, base_url=None)`

Initialize the memory client.

**Parameters:**
- `api_key` (str): Your rec0 API key
- `user_id` (str): Unique identifier for the user
- `app_id` (str, optional): Application identifier
- `base_url` (str, optional): Custom API endpoint

### `store(content, metadata=None)`

Store a memory.

**Parameters:**
- `content` (str): The content to remember
- `metadata` (dict, optional): Additional metadata

**Returns:** `dict` with `memory_id`

### `recall(query, limit=10)`

Retrieve relevant memories.

**Parameters:**
- `query` (str): Search query
- `limit` (int): Maximum number of results

**Returns:** `list` of memory objects

### `delete(memory_id=None, user_id=None)`

Delete memories.

**Parameters:**
- `memory_id` (str, optional): Specific memory to delete
- `user_id` (str, optional): Delete all memories for user

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Links

- [rec0.vercel.app](https://rec0.vercel.app)
- [GitHub](https://github.com/patelyash2511/rec0-python)
- [Docs](https://rec0.vercel.app/docs)

## Support

- GitHub Issues: [Report bugs](https://github.com/patelyash2511/rec0-python/issues)
- Email: support@rec0.vercel.app

---

Made with ❤️ by [rec0](https://rec0.vercel.app)
