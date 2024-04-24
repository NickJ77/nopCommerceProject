from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ContactFormPage(BasePage):
    _url = "https://demo.nopcommerce.com/contactus"
    __name_field = (By.XPATH, "//input[@id='FullName']")
    __email_field = (By.ID, "Email")
    __enquiry_field = (By.ID, "Enquiry")
    __submit_button = (By.XPATH, "//button[@name='send-email']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self._url)

    def input_contact_details(self, name: str, email: str, enquiry: str):
        super()._type(self.__name_field, name)
        super()._type(self.__email_field, email)
        super()._type(self.__enquiry_field, enquiry)
        super()._click(self.__submit_button)
