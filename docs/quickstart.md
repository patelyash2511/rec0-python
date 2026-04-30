# Quick Start Guide

## Installation

```bash
pip install memorylayer-py
```

## Initialize Client

```python
from rec0 import Memory

mem = Memory(
    api_key='r0_live_sk_...',
    user_id='user_123'
)
```

## Store Memory

```python
mem.store("User is a Python developer")
```

## Recall Memory

```python
context = mem.recall(query="programming preferences")
print(context)
```

## Next Steps

- Read the [API Reference](api_reference.md)
- Explore [Examples](examples.md)
- Visit full docs at https://rec0.vercel.app/docs
