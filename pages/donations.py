from pages.base_page import BasePage

check_boxes=["Clothing", "Food", "Furniture","School & Office Supplies","Cleaning & Household Essentials","Bric-a-Brac", "Toys",
"Electronics", "Hygiene & Personal Care","Pet Supplies"]
class Donations(BasePage):
    def select_donation_button(self):
        self.page.get_by_role("button", name="Donations").click()
    def entering_org(self,org):
        self.page.locator("#org").fill(org)
    def check_boxes(self):
        for items in check_boxes:
            self.page.get_by_role("checkbox", name=items).click()
    def fill_quantity(self, quantity="1"):
        self.page.locator("#quantity").fill(quantity)
    def click_to_continue_donation(self):
        self.page.get_by_role("button", name="Continue").click()
    def drop_off_location(self):
        self.page.locator("#dropoff-site").click()
        self.page.get_by_role("option", name="West Philadelphia").click()
    def tax_deduction_notice(self):
        return self.page.get_by_role("heading", name="Tax Deduction Notice")

