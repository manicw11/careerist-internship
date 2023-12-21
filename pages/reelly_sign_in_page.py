from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class ReellySignInPage(Page):
    LOGIN_BTN = (By.CSS_SELECTOR, "[class*='login-button']")
    PW_FIELD = (By.CSS_SELECTOR, "[data-name='Password']")
    SIGN_IN_TXT = (By.XPATH, "//h1[text()='Sign in or create new account']")
    USERNAME_FIELD = (By.CSS_SELECTOR, "[data-name='Email 2']")

    def verify_sign_in_opens(self):
        self.wait_for_visible(self.SIGN_IN_TXT)

    def input_credentials(self):
        self.input('manicw11@gmail.com', *self.USERNAME_FIELD)
        self.input('pks8N47wC3bEsmY', *self.PW_FIELD)
        self.click(*self.LOGIN_BTN)