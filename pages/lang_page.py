
from pages.base_page import BasePage
from playwright.sync_api import expect
class SelectLanguage(BasePage):
    
    def select_english(self):
        self.page.get_by_role("button", name="English").click()
    def already_registered(self):
        return self.page.get_by_text("Already Registered")
    def select_spanish(self):
        self.page.get_by_role("button", name="Spanish").click()
    def spanish_already_registered(self):
        return self.page.get_by_text("Ya estoy registrado")
        
    
