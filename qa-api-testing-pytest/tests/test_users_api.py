"""
API test cases for JSONPlaceholder users endpoints.
"""
import pytest
from utils.api_client import APIClient


@pytest.mark.smoke
@pytest.mark.get
def test_get_list_users_returns_200_and_schema(api_client, base_url, timeout):
    """Test GET list users returns 200 and validates schema expectations."""
    client = APIClient(base_url, api_client)
    response = client.get("users", timeout=timeout)
    
    # Verify status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Verify response is JSON array
    response_data = response.json()
    assert isinstance(response_data, list), "Response should be a list"
    assert len(response_data) > 0, "Response should contain at least one user"
    
    # Validate first user schema
    first_user = response_data[0]
    assert "id" in first_user, "User should contain 'id' field"
    assert isinstance(first_user["id"], int), "User 'id' should be an integer"
    assert "name" in first_user, "User should contain 'name' field"
    assert isinstance(first_user["name"], str), "User 'name' should be a string"
    assert "email" in first_user, "User should contain 'email' field"
    assert isinstance(first_user["email"], str), "User 'email' should be a string"
    assert "username" in first_user, "User should contain 'username' field"


@pytest.mark.smoke
@pytest.mark.get
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_single_user_returns_expected_id_and_fields(api_client, base_url, timeout, user_id):
    """Test GET single user returns expected id and fields."""
    client = APIClient(base_url, api_client)
    response = client.get(f"users/{user_id}", timeout=timeout)
    
    # Verify status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Verify response structure
    user_data = response.json()
    
    # Verify user ID matches
    assert user_data["id"] == user_id, f"Expected user id {user_id}, got {user_data['id']}"
    
    # Validate required fields
    assert "name" in user_data, "User data should contain 'name' field"
    assert isinstance(user_data["name"], str), "Name should be a string"
    assert "email" in user_data, "User data should contain 'email' field"
    assert isinstance(user_data["email"], str), "Email should be a string"
    assert "username" in user_data, "User data should contain 'username' field"
    assert isinstance(user_data["username"], str), "Username should be a string"


@pytest.mark.smoke
@pytest.mark.post
def test_post_create_user_returns_201_and_created_object(api_client, base_url, timeout):
    """Test POST create user returns 201 and validates created object fields."""
    client = APIClient(base_url, api_client)
    
    # Test data
    new_user = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "john.doe@example.com"
    }
    
    response = client.post("users", json=new_user, timeout=timeout)
    
    # Verify status code
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    
    # Verify response structure
    response_data = response.json()
    
    # Verify created object contains expected fields
    assert "id" in response_data, "Created user should contain 'id' field"
    assert isinstance(response_data["id"], int), "ID should be an integer"
    
    assert "name" in response_data, "Created user should contain 'name' field"
    assert response_data["name"] == new_user["name"], \
        f"Name should match input: {new_user['name']}"
    
    assert "email" in response_data, "Created user should contain 'email' field"
    assert response_data["email"] == new_user["email"], \
        f"Email should match input: {new_user['email']}"


@pytest.mark.put
def test_put_update_user_returns_200_and_updated_fields(api_client, base_url, timeout):
    """Test PUT update user returns 200 and validates updated fields."""
    client = APIClient(base_url, api_client)
    
    # Test data for update
    user_id = 1
    updated_user = {
        "name": "Jane Smith",
        "username": "janesmith",
        "email": "jane.smith@example.com"
    }
    
    response = client.put(f"users/{user_id}", json=updated_user, timeout=timeout)
    
    # Verify status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Verify response structure
    response_data = response.json()
    
    # Verify updated fields
    assert "name" in response_data, "Updated user should contain 'name' field"
    assert response_data["name"] == updated_user["name"], \
        f"Name should match update: {updated_user['name']}"
    
    assert "email" in response_data, "Updated user should contain 'email' field"
    assert response_data["email"] == updated_user["email"], \
        f"Email should match update: {updated_user['email']}"


@pytest.mark.negative
def test_get_non_existing_user_returns_404(api_client, base_url, timeout):
    """Test GET non-existing user returns 404."""
    client = APIClient(base_url, api_client)
    
    # Use a non-existing user ID
    non_existing_id = 999
    response = client.get(f"users/{non_existing_id}", timeout=timeout)
    
    # Verify status code (JSONPlaceholder returns 404 for non-existing resources)
    assert response.status_code == 404, \
        f"Expected 404 for non-existing user, got {response.status_code}"
