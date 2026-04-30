import os

import pytest

from rec0 import Memory


@pytest.mark.integration
def test_store_and_recall_integration():
    api_key = os.getenv("REC0_API_KEY")
    user_id = os.getenv("REC0_TEST_USER_ID", "test_user_123")

    if not api_key:
        pytest.skip("REC0_API_KEY not set")

    mem = Memory(api_key=api_key, user_id=user_id)

    mem.store("Integration test memory")
    results = mem.recall(query="integration test", limit=5)

    assert isinstance(results, list)
