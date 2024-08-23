import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='module')
def driver() -> WebDriver:
    """Фикстура для создания экземпляра веб-драйвера Chrome.

    Returns:
        WebDriver: Экземпляр веб-драйвера для управления браузером Chrome.
    """
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()
