from config import FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, NEW_PHONE_NUMBER
from pages.new_login import NewVolunteer
from playwright.sync_api import expect


def test_new_login(english_app, page):
    new_user = NewVolunteer(page)
    new_user.click_new_volunteer()
    expect(new_user.volunteer_text()).to_be_visible()


def test_fill_form(english_app, page):
    form = NewVolunteer(page)
    form.click_new_volunteer()
    form.fill_registration_form(FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, NEW_PHONE_NUMBER)
    form.click_continue()
    form.select_site()
    form.click_to_wavier()
    expect(form.wavier_text()).to_be_visible()

def test_not_clicking_waiver(english_app, page):
    waiver=NewVolunteer(page)
    waiver.click_new_volunteer()
    waiver.click_continue()
    expect(waiver.alert_text()).to_be_visible()
    
    
