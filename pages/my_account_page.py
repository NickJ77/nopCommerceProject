from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class MyAccountPage(BasePage):
    _url = "https://demo.nopcommerce.com/customer/info"
    __header = (By.CSS_SELECTOR, ".page-title")
    __log_out_button = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self._url

    @property
    def header(self) -> str:
        return super()._get_text(self.__header)

    def is_logout_button_displayed(self) -> bool:
        return super()._is_displayed(self.__log_out_button)
