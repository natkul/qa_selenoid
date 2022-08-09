import logging

from pages.home_page import MainPage
import allure


@allure.title('main page')
def test_main_page(web_driver):
    logging.info(f"-------> Test '{test_main_page.__name__}' started -------")
    main_page = MainPage(web_driver)
    main_page.visit_home_page()
    main_page.img_opencart()
    main_page.get_trash_button()
    main_page.get_search_field()
    main_page.get_swiper_button_next()
    subtitle = main_page.get_subtitle_featured()
    assert subtitle == "Featured"
