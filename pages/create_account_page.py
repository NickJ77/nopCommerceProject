from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class CreateAccountPage(BasePage):
    _url = "https://demo.nopcommerce.com/register?returnUrl=%2F"
    __gender = (By.ID, 'gender-male')
    __first_name = (By.ID, 'FirstName')
    __last_name = (By.ID, 'LastName')
    __email_input = (By.ID, 'Email')
    __password = (By.ID, 'Password')
    __confirm_password = (By.ID, 'ConfirmPassword')
    __register_button = (By.ID, 'register-button')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self._url)

    def create_account(self, first_name: str, last_name: str, email: str, password: str, confirm_password: str):
        super()._click(self.__gender)
        super()._type(self.__first_name, first_name)
        super()._type(self.__last_name, last_name)
        super()._type(self.__email_input, email)
        super()._type(self.__password, password)
        super()._type(self.__confirm_password, confirm_password)
        super()._click(self.__register_button)

