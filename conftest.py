import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


@pytest.fixture
def driver():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = browser.new_page()
        yield page
        page.close()
        context.close()
        browser.close()
