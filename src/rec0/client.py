"""
Main client for rec0 Memory API
"""

import requests
from typing import Optional, Dict, List, Any
from .exceptions import AuthenticationError, APIError


class Memory:
    """
    rec0 Memory client for storing and retrieving AI memories.

    Example:
        >>> from rec0 import Memory
        >>> mem = Memory(api_key='r0_...', user_id='user_123')
        >>> mem.store("User loves Italian food")
        >>> mem.recall(query="food preferences")
    """

    def __init__(
        self,
        api_key: str,
        user_id: str,
        app_id: Optional[str] = None,
        base_url: str = "https://memorylayer-production.up.railway.app"
    ):
        """
        Initialize Memory client.

        Args:
            api_key: Your rec0 API key
            user_id: Unique identifier for the user
            app_id: Optional application identifier
            base_url: API endpoint (default: production)
        """
        self.api_key = api_key
        self.user_id = user_id
        self.app_id = app_id or "default"
        self.base_url = base_url.rstrip('/')

        self.session = requests.Session()
        self.session.headers.update({
            'X-API-Key': self.api_key,
            'Content-Type': 'application/json'
        })

    def store(self, content: str, metadata: Optional[Dict[str, Any]] = None) -> Dict:
        """
        Store a memory.

        Args:
            content: The content to remember
            metadata: Optional metadata dictionary

        Returns:
            dict: Response with memory_id

        Raises:
            AuthenticationError: Invalid API key
            APIError: API request failed
        """
        payload = {
            'user_id': self.user_id,
            'app_id': self.app_id,
            'content': content,
        }

        if metadata:
            payload['metadata'] = metadata

        return self._request('POST', '/v1/memory/store', json=payload)

    def recall(
        self,
        query: str,
        limit: int = 10,
        threshold: float = 0.0
    ) -> List[Dict]:
        """
        Retrieve relevant memories.

        Args:
            query: Search query
            limit: Maximum number of results (default: 10)
            threshold: Minimum relevance threshold (default: 0.0)

        Returns:
            list: List of memory objects
        """
        payload = {
            'user_id': self.user_id,
            'app_id': self.app_id,
            'query': query,
            'limit': limit,
            'threshold': threshold,
        }

        response = self._request('POST', '/v1/memory/recall', json=payload)
        return response.get('memories', [])

    def delete(
        self,
        memory_id: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> Dict:
        """
        Delete specific memory or all memories for a user.

        Args:
            memory_id: Specific memory to delete
            user_id: Delete all memories for this user (GDPR right-to-erasure)

        Returns:
            dict: Response with deletion status
        """
        payload = {}

        if memory_id:
            payload['memory_id'] = memory_id
        if user_id:
            payload['user_id'] = user_id

        return self._request('POST', '/v1/memory/delete', json=payload)

    def _request(self, method: str, endpoint: str, **kwargs) -> Dict:
        """Make HTTP request to API."""
        url = f"{self.base_url}{endpoint}"

        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise AuthenticationError("Invalid API key")
            raise APIError(f"API request failed: {e}")

        except requests.exceptions.RequestException as e:
            raise APIError(f"Request failed: {e}")
