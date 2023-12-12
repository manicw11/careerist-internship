from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainPage(Page):
    SEARCH_FIELD = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    SIDE_MENU_SIGN_IN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

    def open_main(self):
        self.open_url('https://www.target.com')

    def open_circle(self):
        self.open_url('https://www.target.com/circle')

    def search(self, product):
        self.input(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(5)

    def click_cart(self):
        self.click(*self.CART_BTN)
        sleep(5)

    def click_sign_in(self):
        self.click(*self.SIGN_IN_BTN)

    def click_side_menu_sign_in(self):
        self.click(*self.SIDE_MENU_SIGN_IN)
