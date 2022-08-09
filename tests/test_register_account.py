import logging

from pages.register_account_page import RegisterPage
import allure


@allure.title('register page')
def test_register_page(web_driver):
    logging.info(f"-------> Test '{test_register_page.__name__}' started -------")
    register = RegisterPage(web_driver)
    register.visit_register_page()
    register.input_first_name()
    register.input_last_name()
    register.input_email()
    register.input_telephone()
    register.input_password()
    register.input_confirm_password()
    register.click_checkbox_privacy_policy()
    url = register.click_button_continue()
    assert url is True
