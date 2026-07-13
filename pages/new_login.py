from pages.base_page import BasePage


class NewVolunteer(BasePage):
    def click_new_volunteer(self):
        self.page.get_by_role("button", name="Register as New Volunteer").click()

    def volunteer_text(self):
        return self.page.get_by_text("Volunteer Registration")

    def fill_first_name(self, first_name):
        self.page.locator("#firstName").fill(first_name)

    def fill_last_name(self, last_name):
        self.page.locator("#lastName").fill(last_name)

    def fill_email(self, email):
        self.page.locator("#email").fill(email)

    def fill_new_phone_number(self, phone_number):
        self.page.locator("#phone").fill(phone_number)

    def fill_registration_form(self, first_name, last_name, email, phone_number):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_email(email)
        self.fill_new_phone_number(phone_number)
    def click_continue(self):
        self.page.get_by_role("button", name="Continue to Site Selection").click()
    def select_site(self):
        self.page.get_by_role("radio", name="West Philadelphia").check()
    def click_to_wavier(self):
        self.page.get_by_role("button", name="Continue to Waiver").click()
    def wavier_text(self):
        return self.page.get_by_role("heading", name="Volunteer Waiver and Release of Liability")
    def alert_text(self):
        return self.page.get_by_role("alert")
    
