from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_main(context):
    context.app.target_main_page.open_main()


@given('Open Target Circle page')
def open_target_circle(context):
    context.app.target_main_page.open_circle()


@when('Search for {product}')
def input_search_field(context, product):
    context.app.target_main_page.search(product)


@when('Click on cart icon')
def click_cart(context):
    context.app.target_main_page.click_cart()
#    context.app.target_main_page.wait_for_url_change('https//www.target.com/cart)


@when('Click on Sign In')
def click_sign_in(context):
    context.app.target_main_page.click_sign_in()


@when('Click on Menu Sign In')
def click_menu_sign_in(context):
    context.app.target_main_page.click_side_menu_sign_in()
