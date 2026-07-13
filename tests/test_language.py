
from pages.lang_page import SelectLanguage
from playwright.sync_api import expect


def test_select_english_shows_already_registered(page):
    lang= SelectLanguage(page)
    lang.open()
    lang.select_english()
    expect(lang.already_registered()).to_be_visible()
def test_select_spanish_shows_already_registered(page):
    lang=SelectLanguage(page)
    lang.open()
    lang.select_spanish()
    expect(lang.spanish_already_registered()).to_be_visible()
    