from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ApparelLinkPage(BasePage):
    _url = "https://demo.nopcommerce.com/"
    __ApparelLink = (By.LINK_TEXT, "Apparel")
    __page_header = (By.XPATH, "//h1[contains(text(),'Apparel')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self._url)

    def click_apparel_link(self):
        super()._click(self.__ApparelLink)

    def get_page_header(self):
        return super()._get_text(self.__page_header)
