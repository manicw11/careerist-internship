from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')
driver.find_element(By.CSS_SELECTOR, '#nav-link-accountList').click()
driver.find_element(By.CSS_SELECTOR, '#createAccountSubmit').click()

# Amazon logo
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')
# Create account
driver.find_element(By.CSS_SELECTOR, '.a-box-inner .a-spacing-small')
# Your name field
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
# Email field
driver.find_element(By.CSS_SELECTOR, '#ap_email')
# Password field
driver.find_element(By.CSS_SELECTOR, '#ap_password')
# Password must be 6 characters text
driver.find_element(By.XPATH, "//div[contains(text(), 'Passwords must be')]")
# Reenter password field
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
# Continue button
driver.find_element(By.CSS_SELECTOR, '#continue')
# Conditions of Use
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
# Privacy Notice
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
# Sign in link
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')

