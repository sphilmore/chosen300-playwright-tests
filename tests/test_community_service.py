from config import FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, NEW_PHONE_NUMBER, ASSIGNING_INSTITUTION
from pages.new_login import NewVolunteer
from pages.community_service_page import CommunityService
from test_data.community_data import COMMUNITY_SERVICE, SCHOOL, WEST_PHILADELPHIA
from playwright.sync_api import expect
from test_data.volunteer_data import WEST_PHILADELPHIA


def test_community_page(english_app):
    service = CommunityService(english_app)
    service.click_community_service_button()
    service.select_reg_type(COMMUNITY_SERVICE)

    reg = NewVolunteer(english_app)
    reg.fill_registration_form(FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, NEW_PHONE_NUMBER)
    service.select_reason_for_service(SCHOOL)
    service.assigning_institution(ASSIGNING_INSTITUTION)
    reg.click_continue()
    reg.select_site(WEST_PHILADELPHIA)
    reg.click_to_waiver()
    expect(reg.waiver_text()).to_be_visible()
