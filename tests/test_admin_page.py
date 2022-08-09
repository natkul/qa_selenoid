from pages.admin_page import AdminPage
import allure
import logging


@allure.title('login admin page')
def test_admin_page(web_driver):
    logging.info(f"-------> Test '{test_admin_page.__name__}' started -------")
    admin_page = AdminPage(web_driver)
    admin_page.visit_admin_page()
    admin_page.input_username_field()
    admin_page.input_password_field()
    admin_page.click_submit_button()
    title = admin_page.get_panel_title()
    assert title == "Dashboard"
