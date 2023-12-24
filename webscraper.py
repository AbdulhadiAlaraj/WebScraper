import re
import json
import requests
from urllib.parse import urljoin, urlparse, urlunparse
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self, config):
        self.start_url = config["url"]
        self.match_pattern = config["match"]
        self.selector = config["selector"]
        self.max_pages = config["maxPagesToCrawl"]
        self.output_file = config["outputFileName"]
        self.visited = set()

    def fetch_url(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def parse_links(self, html, base_url):
        soup = BeautifulSoup(html, 'lxml')
        for link in soup.find_all('a', href=True):
            href = link['href']
            if re.match(self.match_pattern, href) or re.match(self.match_pattern, urljoin(base_url, href)):
                full_url = urljoin(base_url, href)
                if full_url not in self.visited:
                    yield full_url

    def normalize_url(self, url):
        """Normalize the URL by removing the fragment."""
        parsed_url = urlparse(url)
        return urlunparse(parsed_url._replace(fragment=""))

    def parse_links(self, html, base_url):
        soup = BeautifulSoup(html, 'lxml')
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(base_url, href)
            normalized_url = self.normalize_url(full_url)
            if re.match(self.match_pattern, normalized_url) and normalized_url not in self.visited:
                yield normalized_url

    def scrape(self):
        pages_to_visit = [self.normalize_url(self.start_url)]
        results = []

        while pages_to_visit and len(self.visited) < self.max_pages:
            url = pages_to_visit.pop(0)
            normalized_url = self.normalize_url(url)
            if normalized_url in self.visited:
                continue

            print(f"Scraping {normalized_url}")
            self.visited.add(normalized_url)
            html = self.fetch_url(normalized_url)

            if html:
                soup = BeautifulSoup(html, 'lxml')
                content = soup.select(self.selector)
                text_content = ' '.join([c.get_text(separator=' ', strip=True) for c in content])  # Extract text from the content
                title = soup.title.string if soup.title else url

                results.append({
                    "title": title,
                    "url": url,
                    "html": text_content  # Changed 'content' to 'text_content'
                })


                links = self.parse_links(html, url)
                pages_to_visit.extend(links)

        with open(self.output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)

        print(f"Scraping complete. Data written to {self.output_file}")


if __name__ == "__main__":
    config = {
        "url": "https://example.com",  # Replace with your starting URL
        "match": "https://example.com/docs/*",  # Replace with your URL match pattern
        "selector": ".content",  # Replace with your CSS selector
        "maxPagesToCrawl": 50,
        "outputFileName": "output.json",
    }

    scraper = WebScraper(config)
    scraper.scrape()
