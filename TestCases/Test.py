from playwright.sync_api import Page, expect
from Pages.Homepage import Homepage
from Pages.Basepage import Basepage


# @pytest.mark.skip
def test_basic(page: Page) -> None:  # TC1
    homepage = Homepage(page)
    homepage.go_to_homepage()
    homepage.leftsidebar_category_click(0)
    page.pause()