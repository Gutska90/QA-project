"""
Pytest configuration and fixtures for API tests.
"""
import pytest
import requests
from typing import Generator


@pytest.fixture(scope="session")
def base_url() -> str:
    """Base URL for the API under test."""
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="function")
def api_client(base_url: str) -> Generator:
    """
    API client fixture that provides a requests session.
    
    Yields:
        requests.Session: Configured session object
    """
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    
    yield session
    
    session.close()


@pytest.fixture
def timeout() -> int:
    """Default timeout for API requests in seconds."""
    return 10

