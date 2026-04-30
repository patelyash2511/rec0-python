# API Reference

## `Memory(api_key, user_id, app_id=None, base_url=None)`

Initialize the memory client.

### Parameters

- `api_key` (str): Your rec0 API key
- `user_id` (str): Unique identifier for the user
- `app_id` (str, optional): Application identifier
- `base_url` (str, optional): Custom API endpoint

## `store(content, metadata=None)`

Store a memory.

### Parameters

- `content` (str): The content to remember
- `metadata` (dict, optional): Additional metadata

### Returns

- `dict` containing `memory_id`

## `recall(query, limit=10, threshold=0.0)`

Retrieve relevant memories.

### Parameters

- `query` (str): Search query
- `limit` (int): Maximum number of results
- `threshold` (float): Minimum relevance threshold

### Returns

- `list` of memory objects

## `delete(memory_id=None, user_id=None)`

Delete memories.

### Parameters

- `memory_id` (str, optional): Specific memory to delete
- `user_id` (str, optional): Delete all memories for user

### Returns

- `dict` containing deletion status
