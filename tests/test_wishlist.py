import pytest

from pages.if_you_wait_product_page import IfYouWaitProductPage
from pages.wishlist_page import Wishlist


class TestWishlist:

    @pytest.mark.wishlist
    def test_wishlist(self, driver):
        if_you_wait_product_page = IfYouWaitProductPage(driver)
        if_you_wait_product_page.open()
        if_you_wait_product_page.add_wishlist()
        added_to_wishlist = Wishlist(driver)
        assert added_to_wishlist.header() == "Wishlist"
