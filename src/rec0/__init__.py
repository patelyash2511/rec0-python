"""
rec0 Python SDK
Official client library for rec0 Memory API
"""

from .client import Memory
from .exceptions import Rec0Error, AuthenticationError, APIError
from .version import __version__

__all__ = [
    'Memory',
    'Rec0Error',
    'AuthenticationError',
    'APIError',
    '__version__',
]
