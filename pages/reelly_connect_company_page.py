from pages.base_page import Page
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


class ReellyConnectCompanyPage(Page):

    def verify_connect_company_open(self):
        self.verify_partial_url('book-presentation')
