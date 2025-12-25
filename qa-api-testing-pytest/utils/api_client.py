"""
API client helper utilities.
"""
import requests
from typing import Dict, Any, Optional


class APIClient:
    """Helper class for API operations."""
    
    def __init__(self, base_url: str, session: Optional[requests.Session] = None):
        """
        Initialize API client.
        
        Args:
            base_url: Base URL for the API
            session: Optional requests session (creates new if not provided)
        """
        self.base_url = base_url.rstrip("/")
        self.session = session or requests.Session()
    
    def get(self, endpoint: str, params: Optional[Dict] = None, timeout: int = 10) -> requests.Response:
        """
        Perform GET request.
        
        Args:
            endpoint: API endpoint (relative to base_url)
            params: Optional query parameters
            timeout: Request timeout in seconds
            
        Returns:
            Response object
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self.session.get(url, params=params, timeout=timeout)
    
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None, 
             json: Optional[Dict[str, Any]] = None, timeout: int = 10) -> requests.Response:
        """
        Perform POST request.
        
        Args:
            endpoint: API endpoint (relative to base_url)
            data: Optional form data
            json: Optional JSON data
            timeout: Request timeout in seconds
            
        Returns:
            Response object
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self.session.post(url, data=data, json=json, timeout=timeout)
    
    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None,
            json: Optional[Dict[str, Any]] = None, timeout: int = 10) -> requests.Response:
        """
        Perform PUT request.
        
        Args:
            endpoint: API endpoint (relative to base_url)
            data: Optional form data
            json: Optional JSON data
            timeout: Request timeout in seconds
            
        Returns:
            Response object
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self.session.put(url, data=data, json=json, timeout=timeout)
    
    def delete(self, endpoint: str, timeout: int = 10) -> requests.Response:
        """
        Perform DELETE request.
        
        Args:
            endpoint: API endpoint (relative to base_url)
            timeout: Request timeout in seconds
            
        Returns:
            Response object
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self.session.delete(url, timeout=timeout)


def validate_user_schema(data: Dict[str, Any], require_id: bool = True) -> None:
    """
    Validate user object schema.
    
    Args:
        data: User data dictionary
        require_id: Whether ID is required (default: True)
        
    Raises:
        AssertionError: If schema validation fails
    """
    if require_id:
        assert "id" in data, "User data should contain 'id' field"
        assert isinstance(data["id"], int), "User 'id' should be an integer"
    
    assert "email" in data, "User data should contain 'email' field"
    assert isinstance(data["email"], str), "User 'email' should be a string"
    
    assert "first_name" in data or "firstName" in data, \
        "User data should contain 'first_name' or 'firstName' field"
    
    assert "last_name" in data or "lastName" in data, \
        "User data should contain 'last_name' or 'lastName' field"


def validate_list_response(response_data: Dict[str, Any], data_key: str = "data") -> None:
    """
    Validate list response schema.
    
    Args:
        response_data: Response JSON data
        data_key: Key containing the list data (default: "data")
        
    Raises:
        AssertionError: If schema validation fails
    """
    assert data_key in response_data, f"Response should contain '{data_key}' key"
    assert isinstance(response_data[data_key], list), f"'{data_key}' should be a list"
    
    if "page" in response_data:
        assert isinstance(response_data["page"], int), "'page' should be an integer"
    
    if "per_page" in response_data:
        assert isinstance(response_data["per_page"], int), "'per_page' should be an integer"
    
    if "total" in response_data:
        assert isinstance(response_data["total"], int), "'total' should be an integer"

