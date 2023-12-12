from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SignInPage(Page):
    SIGN_IN_TXT = (By.XPATH, "//span[text()='Sign into your Target account']")
    USER_FIELD = (By.CSS_SELECTOR, '#username')
    PW_FIELD = (By.CSS_SELECTOR, '#password')
    LOGIN_BTN = (By.CSS_SELECTOR, '#login')
    NO_ACCOUNT_TXT = (By.CSS_SELECTOR, "[data-test='authAlertDisplay']")
    TERMS_AND_CONDITIONS_LNK = (By.CSS_SELECTOR, "[aria-label='terms & conditions - opens in a new window']")

    def open_sign_in(self):
        self.open_url('https://www.target.com/account')

    def verify_sign_in(self):
        self.verify_text('Sign into your Target account', *self.SIGN_IN_TXT)

    def input_credentials(self):
        self.input('mcw5@coredp.com', *self.USER_FIELD)
        self.input('hdUeq83%&@L', *self.PW_FIELD)
        self.click(*self.LOGIN_BTN)

    def verify_login(self):
        self.wait_to_disappear(self.SIGN_IN_TXT)

    def click_terms_and_conditions(self):
        self.click(*self.TERMS_AND_CONDITIONS_LNK)

    def verify_failed_login(self):
        self.wait_for_visible(self.NO_ACCOUNT_TXT)
