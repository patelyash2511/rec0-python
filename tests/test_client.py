from unittest.mock import Mock, patch

import pytest

from rec0 import Memory
from rec0.exceptions import APIError, AuthenticationError


def test_memory_initialization():
    client = Memory(api_key="r0_test", user_id="user_123")
    assert client.api_key == "r0_test"
    assert client.user_id == "user_123"
    assert client.app_id == "default"


@patch("requests.Session.request")
def test_store_memory(mock_request):
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"memory_id": "mem_1"}
    mock_request.return_value = mock_response

    client = Memory(api_key="r0_test", user_id="user_123")
    result = client.store("User likes Python")

    assert result["memory_id"] == "mem_1"


@patch("requests.Session.request")
def test_recall_memory(mock_request):
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "memories": [{"id": "mem_1", "content": "User likes Python"}]
    }
    mock_request.return_value = mock_response

    client = Memory(api_key="r0_test", user_id="user_123")
    result = client.recall(query="Python")

    assert len(result) == 1
    assert result[0]["content"] == "User likes Python"


@patch("requests.Session.request")
def test_auth_error(mock_request):
    from requests.exceptions import HTTPError

    mock_response = Mock()
    mock_response.status_code = 401

    error = HTTPError("401")
    error.response = mock_response

    mock_request.return_value.raise_for_status.side_effect = error

    client = Memory(api_key="invalid", user_id="user_123")

    with pytest.raises(AuthenticationError):
        client.store("test")


@patch("requests.Session.request")
def test_request_error(mock_request):
    from requests.exceptions import RequestException

    mock_request.side_effect = RequestException("Connection failed")

    client = Memory(api_key="r0_test", user_id="user_123")

    with pytest.raises(APIError):
        client.recall("test")
