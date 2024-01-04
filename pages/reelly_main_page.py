from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class ReellyMainPage(Page):
    PROFILE_BTN = (By.CSS_SELECTOR, "[wized='userProfileImage'][class='menu-img-agent-listing']")

    def open_main(self):
        self.open_url('https://soft.reelly.io')
        self.wait.until(EC.url_changes('https://soft.reelly.io/sign-in'))

    def click_profile_image_btn(self):
        self.wait_for_visible(self.PROFILE_BTN).click()
