import logging

from pages.product_card_page import ProductPage
import allure


@allure.title('catalog page')
def test_catalog_page(web_driver):
    logging.info(f"-------> Test '{test_catalog_page.__name__}' started -------")
    product_page = ProductPage(web_driver)
    product_page.visit_product_page()
    title = product_page.get_title_phones()
    assert title == "HTC Touch HD"
    product_page.input_quantity_field()
    product_page.add_to_card()
    tab = product_page.review_tab()
    assert tab == "Reviews (0)"
    product_page.input_name_field()
