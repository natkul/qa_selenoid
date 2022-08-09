import logging

from pages.home_page import MainPage
from pages.currency import Currency
import allure


@allure.title('currency change')
def test_change_to_euro(web_driver):
    logging.info(f"-------> Test '{test_change_to_euro.__name__}' started -------")
    main_page = MainPage(web_driver)
    main_page.visit_home_page()
    currency = Currency(web_driver)
    currency.change_currency_click()
    currency.change_currency_to_euro()
    euro = currency.check_change()
    assert euro == "€"


def test_change_to_pound(web_driver):
    logging.info(f"-------> Test '{test_change_to_pound.__name__}' started -------")
    main_page = MainPage(web_driver)
    main_page.visit_home_page()
    currency = Currency(web_driver)
    currency.change_currency_click()
    currency.change_currency_to_pound_sterling()
    pound = currency.check_change()
    assert pound == "£"


def test_change_to_dollar(web_driver):
    logging.info(f"-------> Test '{test_change_to_dollar.__name__}' started -------")
    main_page = MainPage(web_driver)
    main_page.visit_home_page()
    currency = Currency(web_driver)
    currency.change_currency_click()
    currency.change_currency_to_dollar()
    dollar = currency.check_change()
    assert dollar == "$"
