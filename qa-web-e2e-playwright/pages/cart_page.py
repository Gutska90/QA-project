"""
Page Object Model for the SauceDemo cart page.

This module contains the CartPage class which handles interactions
with the shopping cart page, including item management and checkout navigation.
"""
from playwright.sync_api import Page


class CartPage:
    """Page Object for the cart page."""
    
    def __init__(self, page: Page):
        """
        Initialize CartPage with page locators.
        
        Args:
            page: Playwright Page instance
        """
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping_button = page.locator("#continue-shopping")
    
    def is_loaded(self) -> bool:
        """
        Check if the cart page is fully loaded.
        
        Returns:
            True if checkout button is visible (indicates page loaded), False otherwise
        """
        return self.checkout_button.is_visible()
    
    def get_cart_item_count(self) -> int:
        """
        Get the number of items currently in the cart.
        
        Returns:
            Number of cart items
        """
        return self.cart_items.count()
    
    def click_checkout(self) -> None:
        """Click the checkout button to proceed to checkout information page."""
        self.checkout_button.click()
    
    def click_continue_shopping(self) -> None:
        """Click the continue shopping button to return to inventory page."""
        self.continue_shopping_button.click()

