import re
from playwright.sync_api import Page, expect

def test_vidjan_title(page: Page):
    page.goto("https://vidjan.onrender.com/")

    # Expect a title "Vidjan, The Top Movies!".
    expect(page).to_have_title(re.compile("Vidjan"))
