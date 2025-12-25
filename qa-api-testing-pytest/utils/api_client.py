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
    Validate user object schema for JSONPlaceholder API.
    
    This function checks that the user object contains required fields
    with correct data types. Note: This is specific to JSONPlaceholder
    API structure (name, username, email fields).
    
    Args:
        data: User data dictionary to validate
        require_id: Whether ID field is required (default: True)
        
    Raises:
        AssertionError: If schema validation fails (missing fields or wrong types)
    """
    if require_id:
        assert "id" in data, "User data should contain 'id' field"
        assert isinstance(data["id"], int), "User 'id' should be an integer"
    
    assert "email" in data, "User data should contain 'email' field"
    assert isinstance(data["email"], str), "User 'email' should be a string"
    
    assert "name" in data, "User data should contain 'name' field"
    assert isinstance(data["name"], str), "User 'name' should be a string"
    
    assert "username" in data, "User data should contain 'username' field"
    assert isinstance(data["username"], str), "User 'username' should be a string"


def validate_list_response(response_data: Dict[str, Any], data_key: str = "data") -> None:
    """
    Validate list response schema for paginated APIs.
    
    This function validates that the response contains a list of items
    and optional pagination metadata. Note: JSONPlaceholder returns
    arrays directly, but this function supports wrapped responses too.
    
    Args:
        response_data: Response JSON data dictionary
        data_key: Key containing the list data (default: "data")
                  For JSONPlaceholder, pass the array directly
        
    Raises:
        AssertionError: If schema validation fails
    """
    assert data_key in response_data, f"Response should contain '{data_key}' key"
    assert isinstance(response_data[data_key], list), f"'{data_key}' should be a list"
    
    # Optional pagination fields (not used by JSONPlaceholder but included for flexibility)
    if "page" in response_data:
        assert isinstance(response_data["page"], int), "'page' should be an integer"
    
    if "per_page" in response_data:
        assert isinstance(response_data["per_page"], int), "'per_page' should be an integer"
    
    if "total" in response_data:
        assert isinstance(response_data["total"], int), "'total' should be an integer"

