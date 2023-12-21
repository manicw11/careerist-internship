from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Connect The Company')
def click_on_connect_the_company(context):
    context.app.reelly_main_menu_page.click_connect()


@when('Verify Login is Successful')
def verify_successful_login(context):
    context.app.reelly_main_menu_page.verify_successful_login()
