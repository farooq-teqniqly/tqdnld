# Scroll-Scraper

Python library for automating scrolling and downloading web pages via Selenium. 
This is especially useful for pages that utilize infinite scrolling.

## Usage

### Download ChromeDriver

Download ChromeDriver from https://chromedriver.chromium.org/downloads. Choose the version that matches the Chrome
browser running on your system. Place the executable in the root of your Python project.

### Install Package

Install the package by running `pip install tq-scroll-scrape`.

### Use the Package

Here is sample code demonstrating how to download a page:

```python
from teqniqly.scroll_and_scrape import ScrollAndScrape

url = "https://www.espn.com/"
scroll_scraper = ScrollAndScrape()
scroll_scraper.download(url)
scroll_scraper.driver.close()
scroll_scraper.driver.quit()
```

This library will scroll the page until it reaches the end. The scroll height can be controlled
by passing the `scroll_by` kwarg. If omitted the value of `document.body.scrollHeight` is used.

To give items the chance to render, the library will wait before scrolling again. The wait time can
be controlled via the `sleep_after_scroll_seconds` parameter. If omitted, the default value is two seconds.

The example below scrolls the page by 500 pixels, waiting 5 seconds between each scroll.

```python
from teqniqly.scroll_and_scrape import ScrollAndScrape

url = "https://www.espn.com/"
downloader = ScrollAndScrape()
downloader.download(url, sleep_after_scroll_seconds=5, scroll_by=500)
downloader.driver.close()
downloader.driver.quit()
```

#### Post-download Processing
The `download` function accepts a callback that executes after the page is downloaded. The page
source is passed into the callback. The example below saves the downloaded page to an html file.

```python
from teqniqly.scroll_and_scrape import ScrollAndScrape


def save_file(source: str):
    with open("espn.html", "w") as file:
        file.write(source)


url = "https://www.espn.com/"
downloader = ScrollAndScrape()
downloader.download(url, save_file)
downloader.driver.close()
downloader.driver.quit()
```