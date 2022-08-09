import logging

from driver.web_driver import WebDriver
import configs.config as config


class CatalogPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def visit_catalog_page(self):
        url = config.URL + '/smartphone'
        self._driver.driver.get(url)
        logging.info('Open catalog page.')

    def get_subtitle_phones(self):
        return self._driver.find_element_by_tag("h2").text

    def product_compare_link(self):
        return self._driver.find_element_by_css_selector("a[href$='compare']").text

    def img_product_htc(self):
        self._driver.find_element_by_css_selector("a[href$='htc-touch-hd'] img[class='img-responsive']")
        logging.info('Checking the existence of the img product htc element on catalog page')

    def view_phones_by_list(self):
        self._driver.find_element_by_id("list-view")
        logging.info('Checking the existence of the view phones by list element on catalog page')

    def add_to_wish_list(self):
        self._driver.find_element_by_css_selector("div[class='button-group']")
        logging.info('Checking the existence of the wish list element on catalog page')
