from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify {number} Benefit Boxes are present')
def verify_benefit_boxes(context, number):
    number = int(number)
    links = context.driver.find_elements(By.CSS_SELECTOR, ".h-text-center [class*='styles__Benefit'] li")
    assert len(links) == number, f'Expected {number} links, but got {len(links)}'
