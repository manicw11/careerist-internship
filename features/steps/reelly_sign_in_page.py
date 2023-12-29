from behave import given, when, then
from time import sleep


@given('Verify Sign In page opens')
def verify_reelly_sign_in(context):
    context.app.reelly_sign_in_page.verify_sign_in_opens()


@when('Input Reelly Username and Password')
def input_reelly_username_and_password(context):
    sleep(2)
    context.app.reelly_sign_in_page.input_credentials()
