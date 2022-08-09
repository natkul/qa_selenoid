from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from configs.config import TIMEOUT_STEP, MAX_TIMEOUT


class WebDriver:

    def __init__(self, driver):
        self.driver = driver

    def driver_init(self):
        self.driver.maximize_window()
        self.driver = self.driver

    def allert_accept(self):
        return self.driver.switch_to.alert.accept()

    def get_url(self):
        return self.driver.current_url

    def __custom_find(self, method, elem, timeout):
        sleep(TIMEOUT_STEP)
        try:
            element = WebDriverWait(self.driver, timeout, TIMEOUT_STEP).until(EC.presence_of_element_located(
                (method, elem)))
            return element
        except TimeoutException as e:
            print(e)
            return None

    def __custom_find_all_elements(self, method, elem, timeout):
        sleep(TIMEOUT_STEP)
        try:
            element = WebDriverWait(self.driver, timeout, TIMEOUT_STEP).until(EC.presence_of_all_elements_located(
                (method, elem)))
            return element
        except TimeoutException as e:
            print(e)
            return None

    def find_element_by_css_selector(self, elem, timeout=MAX_TIMEOUT):
        return self.__custom_find(By.CSS_SELECTOR, elem, timeout)

    def find_elements_by_css_selector(self, elem, timeout=MAX_TIMEOUT):
        return self.__custom_find_all_elements(By.CSS_SELECTOR, elem, timeout)

    def find_element_by_tag(self, elem, timeout=MAX_TIMEOUT):
        return self.__custom_find(By.TAG_NAME, elem, timeout)

    def find_element_by_id(self, elem, timeout=MAX_TIMEOUT):
        return self.__custom_find(By.ID, elem, timeout)
