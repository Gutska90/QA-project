"""
Pytest configuration and fixtures for Playwright E2E tests.
"""
import pytest
from playwright.sync_api import Page, Browser, BrowserContext, sync_playwright


@pytest.fixture(scope="session")
def playwright():
    """Playwright instance for the test session."""
    with sync_playwright() as playwright_instance:
        yield playwright_instance


@pytest.fixture(scope="session")
def browser(playwright) -> Browser:
    """Browser instance for the test session."""
    browser = playwright.chromium.launch(
        headless=True,  # Set to False for visible browser
        slow_mo=0  # Add delay between actions (ms)
    )
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser) -> BrowserContext:
    """Browser context for each test."""
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        ignore_https_errors=True
    )
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context) -> Page:
    """Page instance for each test."""
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="session")
def base_url() -> str:
    """Base URL for the application under test."""
    return "https://www.saucedemo.com"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshots on test failure."""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        # Get the page fixture if available
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            try:
                import os
                screenshot_dir = "reports/screenshots"
                os.makedirs(screenshot_dir, exist_ok=True)
                screenshot_path = f"{screenshot_dir}/{item.name}_{rep.when}.png"
                page.screenshot(path=screenshot_path, full_page=True)
                print(f"\nScreenshot saved: {screenshot_path}")
            except Exception as e:
                print(f"Failed to capture screenshot: {e}")

