from pages.base_page import BasePage


class CommunityService(BasePage):

    def click_community_service_button(self):
        self.page.get_by_role("button", name="Community Service").click()

    def select_reg_type(self, community_service):
        self.page.get_by_role("radio", name=community_service).check()

    def select_reason_for_service(self, reason):
        self.page.locator("#serviceReason").click()
        self.page.get_by_role("option", name=reason).click()

    def assigning_institution(self, assigning_institution):
        self.page.locator("#serviceInstitution").fill(assigning_institution)
