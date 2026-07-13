
from pages.base_page import BasePage

class LoginPage(BasePage):
    def open_sign_in(self):
         self.page.get_by_role("button", name="Already Registered").click()

    def enter_phone_number(self, phone_number):
        self.page.locator("#loginInput").fill(phone_number)
    def submit(self):
        self.page.get_by_role("button", name="Sign In").click()
    def dashboard_text(self):
        return self.page.get_by_text("Volunteer Dashboard")
    def enter_invalid_phone_number(self, invalid_phone_number):
        self.page.locator("#loginInput").fill(invalid_phone_number)
    def alert_text(self):
        return self.page.get_by_role("alert")



