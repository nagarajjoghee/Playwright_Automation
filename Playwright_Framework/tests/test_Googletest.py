import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("AI TEST")