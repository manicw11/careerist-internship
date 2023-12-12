from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


LIST_OF_COLOURS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
COLOUR_NAME = (By.CSS_SELECTOR, "[class*='styles__CellVariationHeaderWrapper']")


@given('Open Target A-53709185 page')
def open_target_product_page(context):
    context.driver.get('https://www.target.com/p/A-53709185')
    sleep(5)


@then('Loop through colours of A-53709185')
def loop_thru_colours(context):
    colour_options = []
    expected_colours = ['Wasabi Green', 'Charcoal', 'Teal', 'Purple']

    colours = context.driver.find_elements(*LIST_OF_COLOURS)
    for colour in colours:
        colour.click()
        selected_colour = context.driver.find_element(*COLOUR_NAME).text.split('\n')[1]
        colour_options.append(selected_colour)

    print(colour_options)
    assert colour_options == expected_colours, f'Actual colours, {colour_options}, are not the same as expected colours'
