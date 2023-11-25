from base.selenium_base import SeleniumBase
import allure
from selenium.common.exceptions import TimeoutException


class WikiPage(SeleniumBase):
    @allure.step('Load page + locators')
    def __init__(self, driver, lang=''):
        super().__init__(driver)  # To be able to use parent's class methods
        self.url = f"https://{lang}wikipedia.org/"
        driver.get(self.url)
        driver.implicitly_wait(10)
        self.__search_field = "#searchInput"  # Using locators in the page class for easy access
        self.__search_button = "#search-form > fieldset > button"
        self.__failed_search = ".mw-search-nonefound"

    @allure.step('Use the search field')
    def search_data(self, data: str):
        """Use the search field"""
        search_field = self.is_visible('css', self.__search_field, 'Search field')
        return search_field.send_keys(data)

    @allure.step('Submit search result')
    def submit_by_enter(self):
        return self.is_visible('css', self.__search_field, 'Search field').submit()

    @allure.step('Push the search button')
    def push_search_btn(self):
        """Push the search button"""
        button = self.is_clickable('css', self.__search_button, 'Search button')
        return button.click()

    @allure.step('Check failed search')
    def check_failed_search_result(self):
        try:
            self.is_present('css', self.__failed_search, 'Check if there is no result in DOM')
            return "No such person"
        except TimeoutException:
            return "Person has got wiki page"



