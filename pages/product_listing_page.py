from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ProductPage(BasePage):
    _url = "https://demo.nopcommerce.com/search?q=Apple+MacBook+Pro+13-inch"
    __product = (By.LINK_TEXT, "Apple MacBook Pro 13-inch")
    __cart_button = (By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def expected_url(self) -> str:
        return self._url

    def product_name(self):
        return super()._get_text(self.__product)

    def is_cart_button_displayed(self):
        return super()._is_displayed(self.__cart_button)
