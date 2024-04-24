from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://demo.nopcommerce.com/login?ReturnUrl=%2Fcustomer%2Finfo"
    __email_address_field = (By.ID, "Email")
    __password_field = (By.ID, "Password")
    __login_button = (By.CSS_SELECTOR, ".button-1.login-button")
    __error_message_1 = (By.ID, "Email-error")
    __error_message_2 = (By.XPATH, "//li[normalize-space()='No customer account found']")
    __register_link = By.CSS_SELECTOR, ".button-1.register-button"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)  # super().__init class referring to base page or parent class

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, email: str, password: str):
        super()._type(self.__email_address_field,
                      email)  # super().type=(basepage method) self.__email_address_field=(locator) email_address=value
        super()._type(self.__password_field,
                      password)  # super().type=(basepage method) self.__password_field=(locator) password=value
        super()._click(self.__login_button)  # super().click=(basepage method) self.__login_button=(locator)

    def get_error_message(self) -> str:  # no value parameter needed because you're not typing anything
        return super()._get_text(self.__error_message_1, time=5)

    def get_second_error_message(self):
        return super()._get_text(self.__error_message_2, time=5)

    def go_to_create_account_page(self):
        super()._click(self.__register_link)
