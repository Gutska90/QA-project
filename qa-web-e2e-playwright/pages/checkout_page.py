"""
Page Object Model for the SauceDemo checkout pages.
"""
from playwright.sync_api import Page


class CheckoutPage:
    """Page Object for the checkout flow (information, overview)."""
    
    def __init__(self, page: Page):
        self.page = page
        # Checkout Information page elements
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.cancel_button = page.locator("#cancel")
        
        # Checkout Overview page elements
        self.summary_info = page.locator(".summary_info")
        self.summary_total_label = page.locator(".summary_total_label")
        self.finish_button = page.locator("#finish")
        self.cancel_button_overview = page.locator("#cancel")
    
    def is_information_page_loaded(self) -> bool:
        """Check if checkout information page is loaded."""
        return self.first_name_input.is_visible()
    
    def is_overview_page_loaded(self) -> bool:
        """Check if checkout overview page is loaded."""
        return self.summary_info.is_visible()
    
    def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Fill the checkout information form."""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
    
    def click_continue(self) -> None:
        """Click the continue button on information page."""
        self.continue_button.click()
    
    def get_summary_total(self) -> str:
        """Get the total amount from the summary."""
        if self.summary_total_label.is_visible():
            return self.summary_total_label.text_content() or ""
        return ""
    
    def is_summary_visible(self) -> bool:
        """Check if the summary section is visible."""
        return self.summary_info.is_visible()

