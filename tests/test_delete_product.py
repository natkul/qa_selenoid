import logging

from pages.admin_section_page import AdminSection
import allure


@allure.title('add product')
def test_add_product(login):
    logging.info(f"-------> Test '{test_add_product.__name__}' started -------")
    product = AdminSection(login)
    product.product_tab()
    product.add_products()
    product.choose_product()
    product.delete_product()
