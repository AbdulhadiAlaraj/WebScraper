# Project Overview
WebScraper is a Python-based tool designed to navigate and extract information from websites. It is built to be versatile and customizable through various parameters, allowing users to specify starting URLs, content selection criteria, and more. The tool utilizes Beautiful Soup for parsing HTML content and the Requests library for fetching web pages.

# Features
- **Customizable URL Navigation:** Start from any URL and follow links within the domain.
- **Pattern Matching:** Only visit and process pages that match a given regular expression pattern.
- **Content Selection:** Use CSS selectors to target specific content on each page.
- **Page Limit:** Control the maximum number of pages to visit to prevent excessive crawling.
- **Output to JSON:** Results are conveniently saved in a JSON file, including titles, URLs, and text content.

# Getting Started

## Prerequisites
Ensure you have the following installed:

- Python 3.6 or later
- requests
- beautifulsoup4
- lxml

Install the necessary packages using pip:
``` bash
pip install requests beautifulsoup4 lxml
```
or
``` bash
pip install -r requirements.txt
```
## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/AbdulhadiAlaraj/WebScraper.git
```
Navigate to the WebScraper directory:
```bash

cd WebScraper
```

## Configuration

Edit the config dictionary in the script to suit your scraping needs:
- **url:** The starting URL for scraping.
- **match:** The regular expression pattern for matching URLs to visit.
- **selector:** The CSS selector for the content of interest.
- **maxPagesToCrawl:** The maximum number of pages to visit.
- **outputFileName:** The name of the file where results will be saved.
Running the Scraper

Execute the script:

```bash
python scraper.py
```

Monitor the console output for progress. Results will be saved in the specified output file in JSON format.

## Usage Example

To scrape a blog for articles:
- Set url to the blog's homepage.
- Set match to the pattern that identifies article URLs.
- Set selector to target the article text or specific elements.
- Adjust maxPagesToCrawl to limit the number of articles.

## Known Issues and Limitations
- **Dynamic Content:** WebScraper does not handle JavaScript-generated content. It works best with static HTML pages.
- **Rate Limiting:** Users should implement their own rate limiting and respect the target website's robots.txt and terms of service.
- **Error Handling:** While basic error handling is included, more robust handling and logging might be necessary for extensive use.
