from pages.base_page import Page
from pages.reelly_connect_company_page import ReellyConnectCompanyPage
from pages.reelly_main_page import ReellyMainPage
from pages.reelly_main_menu_page import ReellyMainMenuPage
from pages.reelly_sign_in_page import ReellySignInPage


class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.reelly_connect_company_page = ReellyConnectCompanyPage(driver)
        self.reelly_main_page = ReellyMainPage(driver)
        self.reelly_main_menu_page = ReellyMainMenuPage(driver)
        self.reelly_sign_in_page = ReellySignInPage(driver)
