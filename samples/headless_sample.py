"""
Scroll and Scrape headless sample.
"""

import os.path

from tq_scroll_scrape.scroll_and_scrape import ScrollAndScrape


def save_file(source: str):
    filename = os.path.join(os.getcwd(), "headless_sample.html")

    with open(filename, "w") as file:
        file.write(source)


url = "https://www.espn.com"
driver_path = os.path.join(os.getcwd(), "../", "chromedriver.exe")
scroll_scraper = ScrollAndScrape(driver_path, headless=True)
scroll_scraper.download(url, save_file, sleep_after_scroll_seconds=2, scroll_by=1000)
scroll_scraper.driver.close()
scroll_scraper.driver.quit()
