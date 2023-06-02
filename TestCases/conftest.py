import pytest

from playwright.sync_api import Page
from Pages import Homepage

@pytest.fixture
def homepage(page: Page) -> Homepage:
    return homepage(page)

