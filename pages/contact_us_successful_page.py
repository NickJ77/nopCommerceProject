from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ContactUsSuccessfulPage(BasePage):
    _url = "https://demo.nopcommerce.com/contactus"
    __successful_message = (By.XPATH, "//div[contains(@class,'result')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_successful_response(self) -> str:
        return super()._get_text(self.__successful_message)
