from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class SortingShoes(BasePage):
    _url = "https://demo.nopcommerce.com/shoes"
    __sort_by_price = (By.XPATH, "//option[contains(text(),'Price: High to Low')]")
    __price_text = (By.XPATH, "//option[contains(text(),'Price: High to Low')]")
    __sort_by_color = (By.ID, "attribute-option-15")
    __color_text = (By.XPATH, "//label[@for='attribute-option-15']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self._url)

    def click_sorting(self):
        super()._click(self.__sort_by_price)
        super()._click(self.__sort_by_color)

    def get_sort_by_price_text(self):
        return super()._get_text(self.__price_text)

    def get_sort_by_color_text(self):
        return super()._get_text(self.__color_text)
