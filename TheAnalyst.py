from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright










# Prototype. Scrapes all statistics.
"""
# URL can be any individual match page from https://theanalyst.com/
url = ["https://theanalyst.com/opta-football-match-centre?competitionId=2kwbbcootiqqgmrzs6o5inle5&seasonId=6pdwluctev9iebv00r4qqukno&matchId=4sbvntlrcii2yfgkq0rdnd1xw"
]

# Store html (value) with corresponding url (key)
html = {
}

# Replace a generic part of the URL to get to Opta's data widgets
def to_dataviz(url):
    return url.replace(
        "https://theanalyst.com/opta-football-match-centre",
        "https://dataviz.theanalyst.com/opta-football-match-centre/",
    )

def scrape(urls):
    with sync_playwright() as p:

        # Use handle p to open a new browser page
        browser = p.chromium.launch()
        page = browser.new_page()

        # Check for "Opta-Outer", the tag that contains data, before adding the html to dict
        for url in urls:
            page.goto(to_dataviz(url))
            page.wait_for_selector("td.Opta-Outer", timeout=15000)
            html[url] = page.content()
        browser.close()

def clean(pages):
    cleaned = {}
    for url, page_html in pages.items():

        # Soup is a searchable object that is the HTML of a url
        soup = BeautifulSoup(page_html, "html.parser")

        rows = []

        # Clean all cells in all rows
        for tr in soup.find_all("tr"):
            cells = [td.get_text(strip=True) for td in tr.find_all("td")]

            # Skip rows with no cells
            if cells:
                rows.append(cells)

        cleaned[url] = rows
    return cleaned

# def filter(cleaned):
   # filtered = {}
   # for url, rows in cleaned.items():

# Test
scrape(url)
print(clean(html))
"""
