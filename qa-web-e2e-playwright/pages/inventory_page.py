"""
Page Object Model for the SauceDemo inventory/products page.
"""
from playwright.sync_api import Page, expect


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
        """Check if the inventory page is loaded."""
        return self.cart_icon.is_visible()
    
    def get_cart_count(self) -> int:
        """Get the current cart item count from the badge."""
        if self.cart_badge.is_visible():
            return int(self.cart_badge.text_content() or "0")
        return 0
    
    def add_item_to_cart(self, item_name: str = None, index: int = 0) -> None:
        """
        Add an item to the cart.
        
        Args:
            item_name: Name of the item to add (if None, uses index)
            index: Index of the item to add (0-based, default: first item)
        """
        if item_name:
            # Find item by name
            item = self.product_items.filter(has_text=item_name)
            add_button = item.locator("button").filter(has_text="Add to cart")
        else:
            # Use index
            item = self.product_items.nth(index)
            add_button = item.locator("button").filter(has_text="Add to cart")
        
        add_button.click()
    
    def click_cart_icon(self) -> None:
        """Click the shopping cart icon."""
        self.cart_icon.click()
    
    def logout(self) -> None:
        """Perform logout action."""
        self.menu_button.click()
        # Wait for menu to be visible
        self.page.wait_for_selector("#logout_sidebar_link", state="visible")
        self.logout_link.click()

