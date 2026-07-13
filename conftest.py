import pytest
from playwright.sync_api import sync_playwright
from pages.lang_page import SelectLanguage


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page=browser.new_page()
        yield page
        browser.close()
@pytest.fixture
def english_app(page):
    lang = SelectLanguage(page)
    lang.open()
    lang.select_english()
    return lang