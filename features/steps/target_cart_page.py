from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify {product} in cart')
def verify_product_in_cart(context, product):
    context.app.target_cart_page.verify_product_in_cart(product)


@then('Verify cart is empty message shown')
def verify_empty_cart_msg(context):
    context.app.target_cart_page.verify_empty_cart()
