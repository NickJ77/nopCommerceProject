import pytest

from pages.apparel_link_page import ApparelLinkPage


@pytest.mark.apparel
class TestApparelLinkPage:
    def test_apparel_page_title(self, driver):
        apparel_link_page = ApparelLinkPage(driver)
        apparel_link_page.open()
        apparel_link_page.click_apparel_link()
        apparel_link_page.get_page_header()
