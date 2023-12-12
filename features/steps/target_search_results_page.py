from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Add product to cart')
def add_product_to_cart(context):
    #    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.app.target_search_results_page.add_product_to_cart()
