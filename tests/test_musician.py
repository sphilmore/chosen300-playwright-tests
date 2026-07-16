from playwright.sync_api import expect
from pages.new_login import NewVolunteer
from pages.musician_page import MusicianUser
from config import FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, NEW_PHONE_NUMBER
from test_data.musician_data import DRUMS
def test_musician_sign_up(english_app):
    instrument= MusicianUser(english_app)
    instrument.select_musician()
    music= NewVolunteer(english_app)
    music.fill_registration_form(FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, NEW_PHONE_NUMBER)

    instrument.select_instrument(DRUMS)
    instrument.click_check_box()
    expect(instrument.complete_registration_button()).to_be_visible()
