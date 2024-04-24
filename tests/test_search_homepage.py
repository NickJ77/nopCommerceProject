import pytest

from pages.product_listing_page import ProductPage
from pages.search_home_page import SearchHomePage


class TestSearchHomePage:

    @pytest.mark.homepage
    def test_successful_product_search(self, driver):
        search_home_page = SearchHomePage(driver)
        search_home_page.open()
        search_home_page.search_item("Apple MacBook Pro 13-inch")
        product_page = ProductPage(driver)
        assert search_home_page.is_submit_button_displayed(), "Submit button should be displayed"
        assert product_page.expected_url() == product_page.current_url, "Actual URL doesn't match expected"
        assert product_page.product_name() == "Apple MacBook Pro 13-inch"
        assert product_page.is_cart_button_displayed(), "Cart button should be visible"
