from pages.base_page import BasePage
from test_data.donations_data import DONATION_CATEGORIES


class Donations(BasePage):
    def select_donation_button(self):
        self.page.get_by_role("button", name="Donations").click()

    def enter_org(self, org):
        self.page.locator("#org").fill(org)

    def check_boxes(self):
        for item in DONATION_CATEGORIES:
            self.page.get_by_role("checkbox", name=item).click()

    def fill_quantity(self, quantity="1"):
        self.page.locator("#quantity").fill(quantity)

    def click_to_continue_donation(self):
        self.page.get_by_role("button", name="Continue").click()

    def drop_off_location(self, location):
        self.page.locator("#dropoff-site").click()
        self.page.get_by_role("option", name=location).click()

    def tax_deduction_notice(self):
        return self.page.get_by_role("heading", name="Tax Deduction Notice")
