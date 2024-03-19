import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver

from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver() -> WebDriver:
    """Фикстура для создания экземпляра веб-драйвера Chrome.

    Returns:
        WebDriver: Экземпляр веб-драйвера для управления браузером Chrome.
    """
    chrome_options = webdriver.ChromeOptions()
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()
