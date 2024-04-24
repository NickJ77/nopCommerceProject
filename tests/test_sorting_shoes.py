import pytest

from pages.sorting_shoes import SortingShoes


class TestSortingShoes:

    @pytest.mark.sortingshoes
    def test_sorting_shoes_by_price(self, driver):
        sorting_shoes = SortingShoes(driver)
        sorting_shoes.open()
        sorting_shoes.click_sorting()
        sorting_shoes.get_sort_by_price_text()
        assert sorting_shoes.get_sort_by_price_text() == "Price: High to Low"

    @pytest.mark.sortingshoes
    def test_sorting_shoes_by_color(self, driver):
        sorting_shoes = SortingShoes(driver)
        sorting_shoes.open()
        sorting_shoes.click_sorting()
        sorting_shoes.get_sort_by_color_text()
        assert (sorting_shoes.get_sort_by_color_text() == "Red")
