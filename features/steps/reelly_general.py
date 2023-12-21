from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Store original windows')
def store_windows(context):
    context.windows = context.app.page.get_all_windows()
    context.current_window = context.app.page.get_current_window()


@when('Switch to the newly opened window')
def switch_window(context):
    context.app.page.switch_to_new_window()


@then('Verify Connect The Company tab opens')
def verify_connect_company_tab_open(context):
    context.app.reelly_connect_company_page.verify_connect_company_open()
