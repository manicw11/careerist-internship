from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class ReellyMainMenuPage(Page):
    CNNCT_COMP_BTN = (By.XPATH, "//div[text()='Connect the company']")
    SIGN_IN_URL = "https://soft.reelly.io/sign-in"

    def verify_successful_login(self):
        self.wait_for_url_change(self.SIGN_IN_URL)

    def click_connect_comp(self):
        self.wait_for_visible(self.CNNCT_COMP_BTN).click()



