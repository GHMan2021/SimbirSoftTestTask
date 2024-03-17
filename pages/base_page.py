from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.config import WAIT_TIMEOUT


class BasePage:
    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, timeout=WAIT_TIMEOUT, poll_frequency=1)

    def open(self) -> None:
        self.driver.get(self.url)

    def element_is_visible(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator: tuple[str, str]) -> list[WebElement]:
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator: tuple[str, str]) -> list[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def remove_footer(self) -> None:
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('fixedban').style.display='none';")

    def select_date_by_text(self, locator: tuple[str, str], value: str) -> None:
        select = Select(self.element_is_present(locator))
        select.select_by_visible_text(value)

    def select_date_item_from_list(self, locator: tuple[str, str], value: str) -> None:
        item_list = self.elements_are_present(locator)
        for item in item_list:
            if item.text == value:
                item.click()
                break
