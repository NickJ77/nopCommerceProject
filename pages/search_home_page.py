from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class SearchHomePage(BasePage):
    _url = "https://demo.nopcommerce.com/"
    __search_field = (By.ID, "small-searchterms")
    __submit_button = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self._url)

    def search_item(self, search: str):
        super()._type(self.__search_field, search)
        super()._click(self.__submit_button)

    def is_submit_button_displayed(self):
        return super()._is_displayed(self.__submit_button)
