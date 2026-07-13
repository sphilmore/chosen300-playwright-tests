from config import PHONE_NUMBER, INVALID_PHONE_NUMBER
from pages.login_page import LoginPage
from playwright.sync_api import expect


def test_login(english_app, page):
    login = LoginPage(page)
    login.open_sign_in()
    login.enter_phone_number(PHONE_NUMBER)
    login.submit()
    expect(login.dashboard_text()).to_be_visible()


def test_login_with_invalid_phone_shows_error(english_app, page):
    login = LoginPage(page)
    login.open_sign_in()
    login.enter_invalid_phone_number(INVALID_PHONE_NUMBER)
    login.submit()
    expect(login.alert_text()).to_be_visible()
    expect(login.dashboard_text()).not_to_be_visible()
