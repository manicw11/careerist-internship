from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from support.logger import logger

from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    ### OTHER BROWSERS ###
    # service = Service(executable_path='C:/Users/manic/OneDrive/Desktop/internship-project/careerist-internship/geckodriver.exe')
    # context.driver = webdriver.Firefox(service=service)
    # context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'mcwood_H6dQRr'
    # bs_key = 'QxqRwAmqukyDxdmuij8d'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '11',
    #     'browserName': 'Chrome',
    #     'sessionName': scenario_name
    # }
    # bstack_options = {
    #     "os": "OS X",
    #     "osVersion": "Sonoma",
    #     "browserName": "Safari",
    #     "browserVersion": "17.0",
    #     "sessionName": scenario_name
    # }

    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    # context.driver.wait = WebDriverWait(context.driver, 15)
    # context.driver.maximize_window()
    # context.driver.set_window_size(1280, 720)
    # context.driver.implicitly_wait(4)
    # context.app = Application(context.driver)

    ### MOBILE EMULATION ###
    mobile_emulation = {"deviceName": "Samsung Galaxy S20 Ultra"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.set_window_size(412, 915)
    context.driver.wait = WebDriverWait(context.driver, 25)
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)
    # context.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
    #                           desired_capabilities=chrome_options.to_capabilities())


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'\nStarted step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.warning(f'\nStarted step: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
