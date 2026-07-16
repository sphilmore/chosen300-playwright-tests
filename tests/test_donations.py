from playwright.sync_api import expect
from pages.donations import Donations
from pages.new_login import NewVolunteer
from config import FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, NEW_PHONE_NUMBER, ORG
from test_data.community_data import WEST_PHILADELPHIA


def test_donation_services(english_app):
    donation = Donations(english_app)
    donation_user = NewVolunteer(english_app)
    donation.select_donation_button()
    donation.enter_org(ORG)
    donation_user.fill_registration_form(FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, NEW_PHONE_NUMBER)
    donation.click_to_continue_donation()
    donation.check_boxes()
    donation.fill_quantity("1")
    donation.click_to_continue_donation()
    donation.drop_off_location(WEST_PHILADELPHIA)
    donation.click_to_continue_donation()
    expect(donation.tax_deduction_notice()).to_be_visible()
