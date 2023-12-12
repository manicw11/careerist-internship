from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open sign in page')
def open_sign_in(context):
    context.app.target_sign_in_page.open_sign_in()


@when('Store original windows')
def store_windows(context):
    context.windows = context.app.page.get_all_windows()
    context.current_window = context.app.page.get_current_window()


@when('Click on Target terms and conditions link')
def click_terms_and_conditions(context):
    context.app.target_sign_in_page.click_terms_and_conditions()


@then('Verify Sign In page opens')
def verify_sign_in(context):
    context.app.target_sign_in_page.verify_sign_in()


@when('Input Username and Password')
def input_credentials(context):
    context.app.target_sign_in_page.input_credentials()


@then('Verify User is logged in')
def verify_login(context):
    context.app.target_sign_in_page.verify_login()


@when('Switch to the newly opened window')
def switch_window(context):
    context.app.page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_terms_conditions_opened(context):
    context.app.target_terms_and_conditions_page.verify_terms_and_conditions_opened()


@then('User can close new window and switch back to original')
def close_window_return_to_original(context):
    context.app.page.close_page()
    context.app.page.switch_to_window(context.current_window)


@then('Verify User cannot log in')
def verify_failed_login(context):
    context.app.target_sign_in_page.verify_failed_login()
