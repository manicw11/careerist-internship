from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class ReellyMainMenuPage(Page):
    CNNCT_COMP_BTN = (By.XPATH, "//div[text()='Connect the company']")
    USERNAME = (By.XPATH, "//div[text()='test+mani+careerist']")

    def click_connect(self):
        self.wait_for_visible(self.CNNCT_COMP_BTN).click()

    def verify_successful_login(self):
        self.wait_for_visible(self.USERNAME)

