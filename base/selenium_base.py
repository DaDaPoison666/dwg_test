from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from urllib.parse import urlparse


class SeleniumBase:
    """Base methods to use in POM"""
    def __init__(self, driver):
        self.driver = driver  # initialise webdriver
        self.wait = WebDriverWait(self.driver, 15) # Default timing to load locator on the page

    @staticmethod
    def __get_selenium_by(find_by: str) -> str:
        """Prepare locators to be found using css as the easiest and the fastest and xpath as the most accurate"""
        find_by = find_by.lower()
        locating = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH
        }
        return locating[find_by]

    def get_current_page_url(self) -> str:
        self.driver.implicitly_wait(20)  # Give time to page to load
        url = urlparse(self.driver.current_url)
        return url.path

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Method returns WebElement if it is visible at the page"""
        return self.wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                               locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Method returns WebElement if it is presented in DOM"""
        return self.wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def is_clickable(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Method returns WebElement if it is clickable"""
        return self.wait.until(ec.element_to_be_clickable((self.__get_selenium_by(find_by), locator)), locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> list:
        """Returns list of elements if they are visible at the page"""
        return self.wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                               locator_name)