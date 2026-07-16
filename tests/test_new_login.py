from config import FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, NEW_PHONE_NUMBER
from pages.new_login import NewVolunteer
from playwright.sync_api import expect
from test_data.volunteer_data import WEST_PHILADELPHIA


def test_new_login(english_app):
    new_user = NewVolunteer(english_app)
    new_user.click_new_volunteer()
    expect(new_user.volunteer_text()).to_be_visible()


def test_fill_form(english_app):
    form = NewVolunteer(english_app)
    form.click_new_volunteer()
    form.fill_registration_form(FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, NEW_PHONE_NUMBER)
    form.click_continue()
    form.select_site(WEST_PHILADELPHIA)
    form.click_to_waiver()
    expect(form.waiver_text()).to_be_visible()

def test_not_clicking_waiver(english_app):
    waiver=NewVolunteer(english_app)
    waiver.click_new_volunteer()
    waiver.click_continue()
    expect(waiver.alert_text()).to_be_visible()
    
    
