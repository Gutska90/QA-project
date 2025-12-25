"""
Page Object Model for the SauceDemo inventory/products page.

This module contains the InventoryPage class which handles interactions
with the product listing page, including adding items to cart and navigation.
"""
from playwright.sync_api import Page


class InventoryPage:
    """Page Object for the inventory/products page."""
    
    def __init__(self, page: Page):
        self.page = page
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")
        self.product_items = page.locator(".inventory_item")
    
    def is_loaded(self) -> bool:
        """
        Check if the inventory page is fully loaded.
        
        Returns:
            True if cart icon is visible (indicates page loaded), False otherwise
        """
        return self.cart_icon.is_visible()
    
    def get_cart_count(self) -> int:
        """
        Get the current number of items in the cart from the badge.
        
        Returns:
            Number of items in cart (0 if badge is not visible)
        """
        if self.cart_badge.is_visible():
            return int(self.cart_badge.text_content() or "0")
        return 0
    
    def add_item_to_cart(self, item_name: str = None, index: int = 0) -> None:
        """
        Add an item to the shopping cart.
        
        Args:
            item_name: Name of the item to add (if provided, searches by name)
            index: Index of the item to add (0-based, default: first item)
                  Only used if item_name is None
        """
        if item_name:
            # Find item by name using text filter
            item = self.product_items.filter(has_text=item_name)
            add_button = item.locator("button").filter(has_text="Add to cart")
        else:
            # Use index to select item by position
            item = self.product_items.nth(index)
            add_button = item.locator("button").filter(has_text="Add to cart")
        
        add_button.click()
    
    def click_cart_icon(self) -> None:
        """Click the shopping cart icon to navigate to the cart page."""
        self.cart_icon.click()
    
    def logout(self) -> None:
        """
        Perform logout action by opening menu and clicking logout link.
        
        Note: Waits for the logout link to be visible before clicking.
        """
        self.menu_button.click()
        # Wait for sidebar menu to be visible before accessing logout link
        self.page.wait_for_selector("#logout_sidebar_link", state="visible")
        self.logout_link.click()

