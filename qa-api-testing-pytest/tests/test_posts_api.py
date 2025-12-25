"""
API test cases for JSONPlaceholder posts endpoints.
"""
import pytest
from utils.api_client import APIClient


@pytest.mark.get
def test_get_list_posts_returns_200_and_schema(api_client, base_url, timeout):
    """Test GET list posts returns 200 and validates schema."""
    client = APIClient(base_url, api_client)
    response = client.get("posts", timeout=timeout)
    
    # Verify status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Verify response is JSON array
    response_data = response.json()
    assert isinstance(response_data, list), "Response should be a list"
    assert len(response_data) > 0, "Response should contain at least one post"
    
    # Validate first post has expected structure
    first_post = response_data[0]
    assert "id" in first_post, "Post should contain 'id' field"
    assert isinstance(first_post["id"], int), "Post 'id' should be an integer"
    assert "title" in first_post, "Post should contain 'title' field"
    assert isinstance(first_post["title"], str), "Post 'title' should be a string"
    assert "body" in first_post, "Post should contain 'body' field"
    assert isinstance(first_post["body"], str), "Post 'body' should be a string"
    assert "userId" in first_post, "Post should contain 'userId' field"
    assert isinstance(first_post["userId"], int), "Post 'userId' should be an integer"


@pytest.mark.get
@pytest.mark.parametrize("post_id", [1, 2])
def test_get_single_post_returns_expected_id_and_fields(api_client, base_url, timeout, post_id):
    """Test GET single post returns expected id and fields."""
    client = APIClient(base_url, api_client)
    response = client.get(f"posts/{post_id}", timeout=timeout)
    
    # Verify status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Verify response structure
    post_data = response.json()
    
    # Verify ID matches
    assert post_data["id"] == post_id, \
        f"Expected post id {post_id}, got {post_data['id']}"
    
    # Verify required fields
    assert "title" in post_data, "Post data should contain 'title' field"
    assert isinstance(post_data["title"], str), "Title should be a string"
    
    assert "body" in post_data, "Post data should contain 'body' field"
    assert isinstance(post_data["body"], str), "Body should be a string"
    
    assert "userId" in post_data, "Post data should contain 'userId' field"
    assert isinstance(post_data["userId"], int), "UserId should be an integer"


@pytest.mark.negative
def test_get_non_existing_post_returns_404(api_client, base_url, timeout):
    """Test GET non-existing post returns 404."""
    client = APIClient(base_url, api_client)
    
    # Use a non-existing post ID
    non_existing_id = 999
    response = client.get(f"posts/{non_existing_id}", timeout=timeout)
    
    # Verify status code
    assert response.status_code == 404, \
        f"Expected 404 for non-existing post, got {response.status_code}"
