import pytest

from pages.create_account_page import CreateAccountPage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage


class TestLogin:
    @pytest.mark.login
    @pytest.mark.positive
    def test_create_account_success(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        account_creation_page = CreateAccountPage(driver)
        login_page.go_to_create_account_page()
        account_creation_page.create_account("Neka", "Fig", "nekafig115@laymro.com", "12345678", "12345678")

    @pytest.mark.login
    @pytest.mark.positive
    def test_customers_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("nekafig115@laymro.com", "12345678")
        logged_in_page = MyAccountPage(driver)
        assert logged_in_page.header == "My account - Customer info"
        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL is not the same as expected"
        assert logged_in_page.is_logout_button_displayed(), "Logout button should be present"
