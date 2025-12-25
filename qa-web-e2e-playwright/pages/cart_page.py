"""
Page Object Model for the SauceDemo cart page.
"""
from playwright.sync_api import Page


class CartPage:
    """Page Object for the cart page."""
    
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping_button = page.locator("#continue-shopping")
    
    def is_loaded(self) -> bool:
        """Check if the cart page is loaded."""
        return self.checkout_button.is_visible()
    
    def get_cart_item_count(self) -> int:
        """Get the number of items in the cart."""
        return self.cart_items.count()
    
    def click_checkout(self) -> None:
        """Click the checkout button."""
        self.checkout_button.click()
    
    def click_continue_shopping(self) -> None:
        """Click the continue shopping button."""
        self.continue_shopping_button.click()

