from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SearchResultsPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[id*="addToCartButtonOrTextId"]')
    CLOSE_SIDE_WNDW_BTN = (By.CSS_SELECTOR, "[class*='styles__CellContent'] [aria-label='close']")
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

    def add_product_to_cart(self):
        self.wait_for_clickable(self.ADD_TO_CART_BTN)
        close_btn = self.wait_for_visible(self.CLOSE_SIDE_WNDW_BTN)
        close_btn.click()
        self.click(*self.CLOSE_SIDE_WNDW_BTN)
        self.click(*self.CART_BTN)
