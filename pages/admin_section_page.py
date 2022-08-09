import logging

from driver.web_driver import WebDriver
import configs.config as config
import random
from elements.table import Table


class AdminSection(Table):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._driver = driver
        self.product_name = None

    def visit_section_page(self):
        url = config.URL + '/admin'
        self._driver.driver.get(url)

    def product_tab(self):
        self._driver.find_element_by_css_selector("a[href='#collapse1']").click()
        self._driver.find_element_by_css_selector("a[href *= 'catalog/product&user_token']").click()
        logging.info('Open products page.')

    def new_product_button_click(self):
        self._driver.find_element_by_css_selector("a[data-original-title='Add New']").click()

    def input_name_product(self):
        self._driver.find_element_by_css_selector("input[id='input-name1']").send_keys(
            "test_product" + str(random.randint(0, 100000)))
        self.product_name = self._driver.find_element_by_css_selector("input[id='input-name1']").get_property('value')
        return self.product_name

    def input_meta_tag_title(self):
        self._driver.find_element_by_css_selector("input[id='input-meta-title1']").send_keys("test_title")

    def tab_data_click(self):
        self._driver.find_element_by_css_selector("a[href='#tab-data']").click()

    def input_model(self):
        self._driver.find_element_by_css_selector('input[id="input-model"]').send_keys("test_model")

    def save_product_button_click(self):
        self._driver.find_element_by_css_selector('button[data-original-title="Save"').click()

    def filter_product(self):
        self._driver.find_element_by_css_selector('input[id="input-name"]').send_keys(self.product_name)

    def apply_filter(self):
        self._driver.find_element_by_css_selector('button[id="button-filter"]').click()

    def choose_product(self):
        product = Table(self._driver)
        product.click_column()
        logging.info(f'The created product is selected')

    def delete_product(self):
        table = Table(self._driver)
        self._driver.find_element_by_css_selector('button[data-original-title="Delete"]').click()
        self._driver.allert_accept()
        text = table.check_table_empty()
        assert text == 'No results!'
        logging.info(f'Product successfully deleted.')

    def add_products(self):
        table = Table(self._driver)
        self.new_product_button_click()
        name = self.input_name_product()
        assert name == self.product_name
        self.input_meta_tag_title()
        self.tab_data_click()
        self.input_model()
        self.save_product_button_click()
        self.filter_product()
        self.apply_filter()
        text = table.get_name()
        assert text == self.product_name
        logging.info(f'Product {name} successfully added.')
