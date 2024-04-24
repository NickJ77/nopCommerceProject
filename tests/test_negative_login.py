import pytest

from pages.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("email, password, expected_error_message",
                             [("john123@laymro.com", "12345678", "No customer account found"),
                              ("nekafig115@laymro.com", "987654321", "No customer account found")])
    def test_negative_login(self, driver, email, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(email, password)
        assert login_page.get_second_error_message() == expected_error_message, "Error message is not expected"
