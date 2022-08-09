import pytest
import allure
import logging
from pages.admin_page import AdminPage
import configs.config as config
from driver.web_driver import WebDriver
from selenium import webdriver
import os


def pytest_addoption(parser):
    logging.basicConfig(filename=f'{os.path.dirname(os.path.realpath(__file__))}/myapp.log', level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(filename)s %(message)s')
    parser.addoption("--url", action="store", default="http://192.168.220.130:8081")
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="192.168.220.130")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--browser_version", default="102.0")
    parser.addoption("--timeout_step", default="0.5")
    parser.addoption("--max_timeout", default="10")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--browser_version")
    timeout_step = request.config.getoption("--timeout_step")
    max_timeout = request.config.getoption("--max_timeout")
    vnc = request.config.getoption("--vnc")
    url = request.config.getoption("--url")
    config.URL = url
    config.TIMEOUT_STEP = timeout_step
    config.MAX_TIMEOUT = max_timeout
    print(version)
    if executor == "local":
        caps = {'goog:chromeOptions': {}}

    else:
        executor_url = f'http://{executor}:4444/wd/hub/'

        caps = {
            "browserName": browser,
            "browserVersion": version,
            "screenResolution": "1280x720",
            "name": "Natalia",
            "selenoid:options": {
                "sessionTimeout": "60s",
                "enableVNC": vnc,
            },
            'acceptSslCerts': True,
            'acceptInsecureCerts': True,
            'timeZone': 'Europe/Moscow',
            'goog:chromeOptions': {}
        }

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )

        driver.maximize_window()

    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    try:
        if rep.when == 'call' and rep.failed:
            if 'browser' in item.fixturenames:
                web_browser = item.funcargs['browser']
                allure.attach(
                    web_browser.get_screenshot_as_png(),
                    name='screenshot',
                    attachment_type=allure.attachment_type.PNG
                )
            else:
                logging.info('Failed to get screenshot')

    except Exception as exception:
        logging.info(f'Failed to take screenshot: {exception}')


@pytest.fixture
def login(web_driver):
    login = AdminPage(web_driver)
    login.visit_admin_page()
    login.input_username_field()
    login.input_password_field()
    login.click_submit_button()
    config.TOKEN = 'YQxanueqnGrEvVHMhLlmvakOxsYcbuJM'
    return web_driver


@pytest.fixture
def web_driver(browser):
    wd = WebDriver(browser)
    return wd
