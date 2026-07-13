from config import FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, NEW_PHONE_NUMBER, PHONE_NUMBER, ASSINGING_INSTITUTION
from pages.new_login import NewVolunteer
from pages.community_service_page import CommunityService
from playwright.sync_api import expect

def test_community_page(english_app, page):
    service= CommunityService(page)
    service.click_community_service_button()
    service.select_reg_type()
    
    reg = NewVolunteer(page)
    reg.fill_registration_form(FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, NEW_PHONE_NUMBER)
    service.select_reason_for_service()
    service.assiging_insitiution(ASSINGING_INSTITUTION)
    reg.click_continue()
    reg.select_site()
    reg.click_to_wavier()
    expect(reg.wavier_text()).to_be_visible()