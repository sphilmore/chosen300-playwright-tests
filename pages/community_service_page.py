from pages.base_page import BasePage
class CommunityService(BasePage):

    def click_community_service_button(self):
        self.page.get_by_role("button", name="Community Service").click()
    def select_reg_type(self):
        self.page.get_by_role("radio", name="Community Service").check()
    def select_reason_for_service(self):
        self.page.locator("#serviceReason").click()
        self.page.get_by_role("option", name="School").click()
    def assiging_insitiution(self, assigning_insitution):
        self.page.locator("#serviceInstitution").fill(assigning_insitution)
        


