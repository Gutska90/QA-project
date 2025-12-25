"""
End-to-end test cases for SauceDemo application.
"""
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.smoke
@pytest.mark.login
def test_successful_login(page, base_url):
    """Test successful login with valid credentials."""
    login_page = LoginPage(page)
    login_page.navigate(base_url)
    login_page.login("standard_user", "secret_sauce")
    
    # Verify redirect to inventory page
    inventory_page = InventoryPage(page)
    assert inventory_page.is_loaded(), "Inventory page should be loaded after successful login"


@pytest.mark.login
def test_invalid_login_shows_error(page, base_url):
    """Test that invalid login credentials show an error message."""
    login_page = LoginPage(page)
    login_page.navigate(base_url)
    login_page.login("invalid_user", "wrong_password")
    
    # Verify error message is displayed
    assert login_page.is_error_visible(), "Error message should be visible for invalid login"
    error_text = login_page.get_error_message()
    assert "Epic sadface" in error_text or "Username and password do not match" in error_text, \
        f"Error message should contain expected text, got: {error_text}"


@pytest.mark.smoke
@pytest.mark.cart
def test_add_item_to_cart_and_verify_count(page, base_url):
    """Test adding an item to cart and verifying the cart count badge."""
    # Login first
    login_page = LoginPage(page)
    login_page.navigate(base_url)
    login_page.login("standard_user", "secret_sauce")
    
    # Add item to cart
    inventory_page = InventoryPage(page)
    assert inventory_page.is_loaded(), "Inventory page should be loaded"
    
    initial_count = inventory_page.get_cart_count()
    inventory_page.add_item_to_cart(index=0)
    
    # Verify cart count increased
    new_count = inventory_page.get_cart_count()
    assert new_count == initial_count + 1, \
        f"Cart count should increase from {initial_count} to {initial_count + 1}, got {new_count}"


@pytest.mark.smoke
@pytest.mark.checkout
def test_checkout_flow_up_to_overview(page, base_url):
    """Test checkout flow from cart to overview page and verify summary is visible."""
    # Login and add item to cart
    login_page = LoginPage(page)
    login_page.navigate(base_url)
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart(index=0)
    
    # Go to cart
    inventory_page.click_cart_icon()
    cart_page = CartPage(page)
    assert cart_page.is_loaded(), "Cart page should be loaded"
    
    # Start checkout
    cart_page.click_checkout()
    
    # Fill checkout information
    checkout_page = CheckoutPage(page)
    assert checkout_page.is_information_page_loaded(), "Checkout information page should be loaded"
    checkout_page.fill_checkout_information("John", "Doe", "12345")
    checkout_page.click_continue()
    
    # Verify overview page is loaded and summary is visible
    assert checkout_page.is_overview_page_loaded(), "Checkout overview page should be loaded"
    assert checkout_page.is_summary_visible(), "Summary section should be visible on overview page"
    
    # Verify summary total is displayed
    total = checkout_page.get_summary_total()
    assert "Total" in total, f"Summary total should be displayed, got: {total}"


@pytest.mark.smoke
def test_logout_works(page, base_url):
    """Test that logout functionality works correctly."""
    # Login first
    login_page = LoginPage(page)
    login_page.navigate(base_url)
    login_page.login("standard_user", "secret_sauce")
    
    # Verify we're on inventory page
    inventory_page = InventoryPage(page)
    assert inventory_page.is_loaded(), "Inventory page should be loaded after login"
    
    # Logout
    inventory_page.logout()
    
    # Verify we're back on login page
    assert login_page.is_login_button_visible(), "Login button should be visible after logout"

