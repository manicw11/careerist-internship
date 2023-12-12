from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class CartPage(Page):
    EMPTY_CART_TXT = (By.XPATH, "//h1[text()='Your cart is empty']")
    CART_ITEM = (By.CSS_SELECTOR, "[data-test='cartItem']")

    def verify_empty_cart(self):
        self.verify_text('Your cart is empty', *self.EMPTY_CART_TXT)

    def verify_product_in_cart(self, product):
        self.verify_partial_text(product, *self.CART_ITEM)
