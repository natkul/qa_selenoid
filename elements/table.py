from driver.web_driver import WebDriver


class Table:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def get_column(self, index):
        return self._driver.find_elements_by_css_selector('tbody tr td')[index]

    def click_column(self):
        self.get_column(0).click()

    def get_name(self):
        return self.get_column(2).text

    def check_table_empty(self):
        return self.get_column(0).text
