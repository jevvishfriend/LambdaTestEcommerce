from playwright.sync_api import Page


class Basepage:
    def __init__(self, page: Page):
        self.page = page
        # Navbar locators
        self._navbar_logo_btn = page.get_by_role("link", name="Poco Electro")
        self._navbar_categories_dpd = page.get_by_role("button", name="All Categories")
        self._navbar_searchbar = page.get_by_role("textbox", name="Search For Products")
        self._navbar_search_category_btn = page.get_by_role("button", name="All Categories")
        self._navbar_search_categories = page.locator("(//button[@class='btn dropdown-toggle'])")
        self._navbar_search_btn = page.get_by_role('button', name='Search')
        self._navbar_compare_btn = page.get_by_role("link", name="Compare", exact=True)
        self._navbar_wishlist_btn = page.get_by_role("link", name="Wishlist", exact=True)
        self._navbar_cart_btn = page.locator("#entry_217825")
        self._navbar_home_btn = page.get_by_role("link", name="Home")
        self._navbar_special_btn = page.get_by_role("link", name="Special Hot", exact=True)
        self._navbar_blog_btn = page.get_by_role("link", name="Blog", exact=True)
        self._navbar_mega_menu_btn = page.get_by_role("button", name="Mega Menu")
        self._navbar_addons_btn = page.get_by_role("button", name="AddOns Featured")
        self._navbar_my_account_btn = page.get_by_role("button", name="My account")
        #dd
        # Leftsidebar
        self._leftsidebar_category_open_btn = page.get_by_role("button", name="Shop by Category")
        self._leftsidebar_categories = page.locator("(//li[@class='nav-item'])") # all categories within the sidebar - chose category from 0 - 14
        self._leftsidebar_components_category = page.get_by_role("link", name="Components")
        self._leftsidebar_cameras = page.get_by_role("link", name="Cameras", exact=True)
        self._leftsidebar_phone_category = page.get_by_role("link", name="Phone, Tablets & Ipod")
        self._leftsidebar_software = page.get_by_role("link", name="Software", exact=True)
        self._leftsidebar_mp3players = page.get_by_role("link", name="MP3 Players", exact=True)
        self._leftsidebar_lapotop_and_notebooks_category = page.get_by_role("link", name="Laptops & Notebooks")
        self._leftsidebar_desktops_and_monitors = page.get_by_role("link", name="Desktops and Monitors")
        self._leftsidebar_printers_and_scanners = page.get_by_role("link", name="Printers & Scanners")
        self._leftsidebar_mice_and_trackballs = page.get_by_role("link", name="Mice and Trackballs")
        self._leftsidebar_fashion_and_accessories = page.get_by_role("link", name="Fashion and Accessories")
        self._leftsidebar_beaty_and_saloon = page.get_by_role("link", name="Beauty and Saloon")
        self._leftsidebar_autoparts_and_accessories = page.get_by_role("link", name="Autoparts and Accessories")
        self._leftsidebar_washing_machine = page.get_by_role("link", name="Washing machine")
        self._leftsidebar_gaming_consoles = page.get_by_role("link", name="Gaming consoles")
        self._leftsidebar_air_conditioner = page.get_by_role("link", name="Air conditioner")
        self._leftsidebar_web_cameras = page.get_by_role("link", name="Web Cameras")

    #category number from 0-14
    def leftsidebar_category_click(self, category_number: int):
        self._leftsidebar_category_open_btn.click()
        self._leftsidebar_categories.nth(category_number).click()
