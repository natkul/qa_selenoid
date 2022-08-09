import logging

from driver.web_driver import WebDriver
import configs.config as config
import random


class RegisterPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self.password = None

    def visit_register_page(self):
        url = config.URL + '/index.php?route=account/register'
        self._driver.driver.get(url)
        logging.info('Open register page.')

    def input_first_name(self):
        self._driver.find_element_by_css_selector('input[id="input-firstname"]').send_keys(
            'test_first_name' + str(random.randint(0, 10000)))
        logging.info('the user entered first name')

    def input_last_name(self):
        self._driver.find_element_by_css_selector('input[id="input-lastname"]').send_keys(
            'test_last_name' + str(random.randint(0, 10000)))
        logging.info('the user entered last name')

    def input_email(self):
        self._driver.find_element_by_css_selector('input[id = "input-email"]').send_keys(
            str(random.randint(0, 10000)) + 'test_email@ya.ru')
        logging.info('the user entered email')

    def input_telephone(self):
        self._driver.find_element_by_css_selector('input[id = "input-telephone"]').send_keys(
            '+7' + str(random.randint(0, 10000000)))
        logging.info('the user entered telephone')

    def input_password(self):
        self._driver.find_element_by_css_selector('input[id = "input-password"]').send_keys(
            'test_password' + str(random.randint(0, 10000)))
        self.password = self._driver.find_element_by_css_selector('input[id = "input-password"]').get_property('value')
        logging.info('the user entered password')

    def input_confirm_password(self):
        self._driver.find_element_by_css_selector('input[id = "input-confirm"]').send_keys(self.password)

    def click_checkbox_privacy_policy(self):
        self._driver.find_element_by_css_selector('input[name="agree"]').click()

    def click_button_continue(self):
        self._driver.find_element_by_css_selector('input[value="Continue"]').click()
        current_url = self._driver.get_url()
        return "success" in current_url
