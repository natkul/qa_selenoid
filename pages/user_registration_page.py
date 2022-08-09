import logging

from driver.web_driver import WebDriver
import configs.config as config


class UserRegistration:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def visit_user_page(self):
        url = config.URL + '/index.php?route=account/register'
        self._driver.driver.get(url)
        logging.info('Open user registration page.')

    def get_account_title(self):
        return self._driver.find_element_by_tag("h1").text

    def first_name_field(self):
        self._driver.find_element_by_css_selector("input[id='input-firstname']")

    def telephone_field(self):
        self._driver.find_element_by_css_selector("input[id='input-telephone']")

    def password_field(self):
        self._driver.find_element_by_css_selector("input[id='input-password']")

    def continue_button(self):
        self._driver.find_element_by_css_selector("input[value='Continue']")
        logging.info('The user is registered')
