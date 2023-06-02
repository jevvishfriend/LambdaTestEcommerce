from playwright.sync_api import Page
from Pages.Basepage import Basepage

url_home = 'https://ecommerce-playground.lambdatest.io/'


class Homepage(Basepage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.carrousel = page.locator("(//div[@class='carousel-inner'])[1]")

    def go_to_homepage(self):
        self.page.goto(url_home)
