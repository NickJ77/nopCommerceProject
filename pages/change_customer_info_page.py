from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ChangeCustomerInfoPage(BasePage):
    _url = "https://demo.nopcommerce.com/customer/info"
    __email_address_field = (By.ID, "Email")
    __password_field = (By.ID, "Password")
    __login_button = (By.CSS_SELECTOR, ".button-1.login-button")
    __gender = (By.CSS_SELECTOR, ".female")
    __dropdown_1 = (By.XPATH, "//select[@name='DateOfBirthDay']")
    __dropdown_2 = (By.XPATH, "//select[@name='DateOfBirthMonth']")
    __dropdown_3 = (By.XPATH, "//select[@name='DateOfBirthYear']")
    __save_button = (By.ID, "save-info-button")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self._url)

    def execute_login(self, email: str, password: str):
        super()._type(self.__email_address_field, email)
        super()._type(self.__password_field, password)
        super()._click(self.__login_button)

    def change_gender(self):
        super()._click(self.__gender)

    def select_option_from_dropdown(self, index):
        super().select_dropdown_option_by_index(self.__dropdown_1, index)
        super().select_dropdown_option_by_index(self.__dropdown_2, index)
        super().select_dropdown_option_by_index(self.__dropdown_3, index)

    def click_save(self):
        super()._click(self.__save_button)

    def get_gender_name(self):
        return super()._get_text(self.__gender)
