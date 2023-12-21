from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class ReellyMainPage(Page):

    def open_main(self):
        self.open_url('https://soft.reelly.io')
        self.wait.until(EC.url_changes('https://soft.reelly.io/sign-in'))
