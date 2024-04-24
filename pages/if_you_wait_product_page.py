from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class IfYouWaitProductPage(BasePage):
    _url = "https://demo.nopcommerce.com/if-you-wait-donation"
    __add_to_wishlist = (By.ID, "add-to-wishlist-button-35")
    __wishlist_label = (By.CSS_SELECTOR, ".wishlist-label")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self._url)

    def add_wishlist(self):
        super()._click(self.__add_to_wishlist)
        super()._click(self.__wishlist_label)
