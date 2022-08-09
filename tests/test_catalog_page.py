import logging

from pages.catalog_page import CatalogPage
import allure


@allure.title('catalog page')
def test_catalog_page(web_driver):
    logging.info(f"-------> Test '{test_catalog_page.__name__}' started -------")
    catalog_page = CatalogPage(web_driver)
    catalog_page.visit_catalog_page()
    catalog_page.add_to_wish_list()
    catalog_page.view_phones_by_list()
    subtitle = catalog_page.get_subtitle_phones()
    assert subtitle == "Phones & PDAs"
    catalog_page.img_product_htc()
    link = catalog_page.product_compare_link()
    assert link == "Product Compare (0)"
