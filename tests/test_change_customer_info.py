import pytest

from pages.change_customer_info_page import ChangeCustomerInfoPage


class TestCustomerInformation:

    @pytest.mark.customers
    def test_change_customers_info(self, driver):
        change_customers_info_page = ChangeCustomerInfoPage(driver)
        change_customers_info_page.open()
        change_customers_info_page.execute_login("nekafig115@laymro.com", "12345678")
        change_customers_info_page.change_gender()
        change_customers_info_page.select_option_from_dropdown("2")
        change_customers_info_page.select_option_from_dropdown("5")
        change_customers_info_page.select_option_from_dropdown("8")
        change_customers_info_page.click_save()
        assert change_customers_info_page.get_gender_name() == "Female", "Gender is not correct"
