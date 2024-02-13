import pytest

from .locators import *
from .input_data import *
from .expected_values import *

from playwright.sync_api import Playwright, sync_playwright, expect, Page


@pytest.fixture(scope = "class", params = [URI.MAIN_HOST])
def auth_fixture(request):
    """Фикстура для создания браузера и его настроек"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        chrome_context = browser.new_context()
        auth_page = chrome_context.new_page()
        auth_page.goto(request.param)
        yield auth_page
        auth_page.close()
        browser.close()
        