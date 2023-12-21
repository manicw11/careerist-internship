from behave import given, when, then
from time import sleep


@given('Open Reelly main page')
def open_reelly_main(context):
    context.app.reelly_main_page.open_main()
