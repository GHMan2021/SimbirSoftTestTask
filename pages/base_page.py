from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.config import WAIT_TIMEOUT


class BasePage:
    """Базовый класс для всех страниц.

    Attributes
    ----------
    driver
        Экземпляр WebDriver, используемый для взаимодействия с браузером.
    url
        URL, с которой будет работать экземпляр страницы.
    wait
        Экземпляр WebDriverWait, используемый для ожидания элементов на странице.
    """

    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, timeout=WAIT_TIMEOUT, poll_frequency=1)

    def open(self) -> None:
        """Открывает URL страницы в браузере."""
        self.driver.get(self.url)

    def element_is_visible(self, locator: tuple[str, str]) -> WebElement:
        """Ожидает и возвращает видимый элемент на странице.

        Args:
            locator (tuple[str, str]): Кортеж (by, value) для локатора элемента.

        Returns:
            WebElement: Элемент, который становится видимым.

        Raises:
            TimeoutException: Если элемент не становится видимым в течение времени ожидания.
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator: tuple[str, str]) -> list[WebElement]:
        """Ожидает и возвращает список видимых элементов на странице.

        Args:
            locator (tuple[str, str]): Кортеж (by, value) для локатора элементов.

        Returns:
            list[WebElement]: Список элементов, которые становятся видимыми.

        Raises:
            TimeoutException: Если элементы не становятся видимыми в течение времени ожидания.
        """
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator: tuple[str, str]) -> WebElement:
        """Ожидает и возвращает присутствующий элемент на странице.

        Args:
            locator (tuple[str, str]): Кортеж (by, value) для локатора элементов.

        Returns:
            list[WebElement]: Элемент, который присутствует на странице.

        Raises:
            TimeoutException: Если элементы не становятся видимыми в течение времени ожидания.
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator: tuple[str, str]) -> list[WebElement]:
        """Ожидает и возвращает список присутствующих элементов на странице.

        Args:
            locator (tuple[str, str]): Кортеж (by, value) для локатора элементов.

        Returns:
            list[WebElement]: Список элементов, которые присутствуют на странице.

        Raises:
            TimeoutException: Если элементы не становятся видимыми в течение времени ожидания.
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def remove_footer(self) -> None:
        """Удаляет футер со страницы."""
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('fixedban').style.display='none';")

    def select_date_by_text(self, locator: tuple[str, str], value: str) -> None:
        """Выбирает дату из выпадающего списка по видимому тексту.

        Args:
            locator (tuple[str, str]): Кортеж (by, value) для локатора элемента.
            value (str): Текст для выбора.

        Raises:
            TimeoutException: Если элемент не появится на странице в течение времени ожидания.
            NoSuchElementException: Если элемент не будет найден на странице.
        """
        select = Select(self.element_is_present(locator))
        select.select_by_visible_text(value)

    def select_date_item_from_list(self, locator: tuple[str, str], value: str) -> None:
        """Выбирает элемент из списка по его значению.

        Args:
            locator (tuple[str, str]): Кортеж (by, value) для локатора списка элементов.
            value (str): Значение элемента, который нужно выбрать.

        Raises:
            TimeoutException: Если элементы не появятся на странице в течение времени ожидания.
            NoSuchElementException: Если элементы не будут найдены на странице.
        """
        item_list = self.elements_are_present(locator)
        for item in item_list:
            if item.text == value:
                item.click()
                break
