import pytest
from playwright.sync_api import  Page
from pages.lang_page import SelectLanguage



@pytest.fixture
def english_app(page: Page):
    lang = SelectLanguage(page)
    lang.open()
    lang.select_english()
    return page