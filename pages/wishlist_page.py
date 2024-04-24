from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class Wishlist(BasePage):
    _url = "https://demo.nopcommerce.com/wishlist"
    __page_title = (By.XPATH, "//h1[contains(text(),'Wishlist')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def header(self) -> str:
        return super()._get_text(self.__page_title)
