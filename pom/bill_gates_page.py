import allure
from base.selenium_base import SeleniumBase
from selenium.common.exceptions import TimeoutException


class BillGates(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)  # To be able to use parent's class methods
        self.url = f"https://ru.wikipedia.org/wiki/Bill_Gates"
        driver.get(self.url)
        driver.implicitly_wait(10)
        self.__bill_face = ('//*[@src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Visit_of_Bill_Gates'
                            '%2C_Chairman_of_Breakthrough_Energy_Ventures%2C_to_the_European_Commission_5_%28cropped'
                            '%29.jpg/267px-Visit_of_Bill_Gates%2C_Chairman_of_Breakthrough_Energy_Ventures'
                            '%2C_to_the_European_Commission_5_%28cropped%29.jpg"]')
        self.__context_main = ".toctext"
        self.__paragraph = "mw-headline"

    @allure.step('Check Bill Gates picture')
    def check_bill_gates_face(self):
        return self.is_visible('xpath', self.__bill_face, "Bill Gate's face")

    @allure.step('Get the text of main and sub context paragraphs')
    def get_context_data(self) -> list:
        context_elements = self.are_visible('css', self.__context_main, "All main context elements")
        context_text = []
        for i in context_elements:
            context_text.append(i.text)
        return context_text

    @allure.step('Get the data from page according to context')
    def get_data_for_context(self):
        list_of_titles = self.get_context_data()
        try:
            for i in list_of_titles:
                locator_on_the_page = f"//*[@class = '{self.__paragraph}' and contains(text(), '{i}')]"
                self.is_present('xpath', locator_on_the_page, f'locator for {i}')
                return True
        except TimeoutException:
            return AssertionError
