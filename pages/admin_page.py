import logging

from driver.web_driver import WebDriver
import configs.config as config


class AdminPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def visit_admin_page(self):
        url = config.URL + '/admin'
        self._driver.driver.get(url)
        logging.info('Open admin page.')

    def input_username_field(self):
        self._driver.get_url()
        self._driver.find_element_by_css_selector("input[name='username']").send_keys("user")

    def input_password_field(self):
        self._driver.find_element_by_css_selector("input[name='password']").send_keys("bitnami")

    def click_submit_button(self):
        self._driver.find_element_by_css_selector("button[type='submit']").click()
        logging.info('The admin user is logged in')

    def get_panel_title(self):
        logging.info('Checking the page title ')
        return self._driver.find_element_by_tag("h1").text
