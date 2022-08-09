import logging

from driver.web_driver import WebDriver
import configs.config as config


class Currency:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def change_currency_click(self):
        self._driver.find_element_by_css_selector('button[class="btn btn-link dropdown-toggle"]').click()

    def change_currency_to_euro(self):
        self._driver.find_element_by_css_selector('button[name="EUR"]').click()
        logging.info('currency change to euro on Currency page')

    def change_currency_to_pound_sterling(self):
        self._driver.find_element_by_css_selector('button[name="GBP"]').click()
        logging.info('currency change to pound sterling on Currency page')

    def change_currency_to_dollar(self):
        self._driver.find_element_by_css_selector('button[name="USD"]').click()
        logging.info('currency change to dollar on Currency page')

    def check_change(self):
        return self._driver.find_element_by_css_selector('button[class="btn btn-link dropdown-toggle"] strong').text
