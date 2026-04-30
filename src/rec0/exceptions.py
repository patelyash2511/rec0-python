"""
Custom exceptions for rec0 SDK
"""


class Rec0Error(Exception):
    """Base exception for rec0 SDK"""
    pass


class AuthenticationError(Rec0Error):
    """Invalid API key or authentication failed"""
    pass


class APIError(Rec0Error):
    """API request failed"""
    pass
