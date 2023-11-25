import pytest
import allure
from pom.bill_gates_page import BillGates
from allure_commons.types import AttachmentType


@pytest.mark.usefixtures("setup")
@allure.epic("Bill Gate's wiki testing ")
class TestBillGates:
    @allure.story("Test of Bill Gates page picture")
    @allure.severity("Normal")
    def test_bills_photo(self):
        page = BillGates(self.driver)
        try:
            assert page.check_bill_gates_face()
        except AssertionError or Exception as e:
            with allure.step("Failed to load Bill Gate's picture"):
                allure.attach(self.driver.get_screenshot_as_png(), name='Failed_bill_gates_picture',
                              attachment_type=AttachmentType.PNG)
                raise e

    @allure.story("Test of containing context in main text")
    @allure.severity("Normal")
    def test_accordance_of_context(self):
        page = BillGates(self.driver)
        try:
            assert page.get_data_for_context()
        except AssertionError or Exception as e:
            with allure.step("Page text doesn't contain context"):
                allure.attach(self.driver.get_screenshot_as_png(), name='Failed_context',
                              attachment_type=AttachmentType.PNG)
                raise e