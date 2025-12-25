"""
Page Object Model for the SauceDemo login page.
"""
from playwright.sync_api import Page, expect


class LoginPage:
    """Page Object for the login page."""
    
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("h3[data-test='error']")
    
    def navigate(self, base_url: str) -> None:
        """Navigate to the login page."""
        self.page.goto(f"{base_url}/")
    
    def fill_username(self, username: str) -> None:
        """Fill the username field."""
        self.username_input.fill(username)
    
    def fill_password(self, password: str) -> None:
        """Fill the password field."""
        self.password_input.fill(password)
    
    def click_login(self) -> None:
        """Click the login button."""
        self.login_button.click()
    
    def login(self, username: str, password: str) -> None:
        """Perform complete login action."""
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()
    
    def get_error_message(self) -> str:
        """Get the error message text if present."""
        return self.error_message.text_content() or ""
    
    def is_error_visible(self) -> bool:
        """Check if error message is visible."""
        return self.error_message.is_visible()
    
    def is_login_button_visible(self) -> bool:
        """Check if login button is visible."""
        return self.login_button.is_visible()

