from pages.base_page import BasePage

class MusicianUser(BasePage):
    def select_musician(self):
        self.page.get_by_role("button", name="Register as Musician").click()
    def select_instrument(self):
     self.page.get_by_role("combobox").filter(has_text="Select your primary instrument").click()
     self.page.get_by_role("option", name="Drums").click()

    def click_check_box(self):
        self.page.get_by_role("checkbox", name="I have").click()

    def complete_registration_button(self):
        return self.page.get_by_role("button", name="Complete Registration")