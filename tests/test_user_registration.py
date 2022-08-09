import logging

from pages.user_registration_page import UserRegistration
import allure


@allure.title('registration page')
def test_user_registration_page(web_driver):
    logging.info(f"-------> Test '{test_user_registration_page.__name__}' started -------")
    user_page = UserRegistration(web_driver)
    user_page.visit_user_page()
    title = user_page.get_account_title()
    assert title == "Register Account"
    user_page.first_name_field()
    user_page.password_field()
    user_page.telephone_field()
    user_page.continue_button()
