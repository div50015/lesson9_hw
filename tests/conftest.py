import pytest
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = 1900
    browser.config.window_height = 900
    options = webdriver.ChromeOptions()
    browser.config.driver = options

    yield

    browser.close()