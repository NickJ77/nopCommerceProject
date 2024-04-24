import pytest

from pages.contact_form_page import ContactFormPage
from pages.contact_us_successful_page import ContactUsSuccessfulPage


class TestContactForm:

    @pytest.mark.contact
    def test_contact_form(self, driver):
        contact_form_page = ContactFormPage(driver)
        contact_form_page.open()
        contact_form_page.input_contact_details("Neka Fig ", "nekafig115@laymro.com",
                                                "I am requesting a refund on a recent order.")
        successful_submission = ContactUsSuccessfulPage(driver)
        assert successful_submission.get_successful_response().__contains__("Your enquiry has been successfully sent "
                                                                            "to the store owner.")
