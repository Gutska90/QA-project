"""
Page Object Model for the SauceDemo login page.

This module contains the LoginPage class which encapsulates all interactions
with the login page, including form filling, submission, and error handling.
"""
from playwright.sync_api import Page


class LoginPage:
    """Page Object for the login page."""
    
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("h3[data-test='error']")
    
    def navigate(self, base_url: str) -> None:
        """
        Navigate to the login page.
        
        Args:
            base_url: Base URL of the application
        """
        self.page.goto(f"{base_url}/")
    
    def fill_username(self, username: str) -> None:
        """
        Fill the username input field.
        
        Args:
            username: Username to enter
        """
        self.username_input.fill(username)
    
    def fill_password(self, password: str) -> None:
        """
        Fill the password input field.
        
        Args:
            password: Password to enter
        """
        self.password_input.fill(password)
    
    def click_login(self) -> None:
        """Click the login button to submit the form."""
        self.login_button.click()
    
    def login(self, username: str, password: str) -> None:
        """
        Perform complete login action (fill credentials and submit).
        
        Args:
            username: Username to login with
            password: Password to login with
        """
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()
    
    def get_error_message(self) -> str:
        """
        Get the error message text if present.
        
        Returns:
            Error message text or empty string if not visible
        """
        return self.error_message.text_content() or ""
    
    def is_error_visible(self) -> bool:
        """
        Check if error message is currently visible on the page.
        
        Returns:
            True if error message is visible, False otherwise
        """
        return self.error_message.is_visible()
    
    def is_login_button_visible(self) -> bool:
        """
        Check if login button is currently visible on the page.
        
        Returns:
            True if login button is visible, False otherwise
        """
        return self.login_button.is_visible()

