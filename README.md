# 🕷️ Trustpilot Vinted Scraper

A simple Python script that scrapes reviews of **Vinted Italy** from [Trustpilot](https://it.trustpilot.com/review/vinted.it) using `requests` and `BeautifulSoup`.

The goal is to demonstrate a clean and modular approach to basic web scraping — focusing on **code structure**, **error handling**, and **clarity**, rather than large-scale data extraction.

---

##  Overview

The scraper:
- Iteratively fetches review pages from Trustpilot  
- Parses reviewer name, title, text content, rating, and date  
- Handles missing fields gracefully  
- Prints the first few extracted reviews to the console  

This project is a concise example of how to organize a scraping pipeline using:
- `requests` for HTTP requests  
- `BeautifulSoup` for HTML parsing  
- Simple modular functions for clarity and maintainability  

---

## ⚙️ Requirements

Install dependencies before running the script:

```bash
pip install requests beautifulsoup4 lxml
```

## ▶️ Usage

Run the script from the command line:

python script/scraper.py


You can adjust parameters such as the number of pages to scrape or delay between requests directly in the main() function:

reviews = scrape_all_reviews(max_pages=10, delay=1)

## 📄 Example Output
```
[+] Successfully fetched page 1
[+] Page 1: found 20 reviews.
...
Total reviews scraped: 200

Mario Rossi - 5 stars
Ottimo servizio!
Transazione veloce e sicura.
```
---


## Project Structure
```
trustpilot-scraper/
│
├── script/
│   └── scraper.py          # Main scraping script
│
├── README.md
└── requirements.txt        # (Optional) Dependencies
```

Inside scraper.py:
```
fetch_page_html()     # Handles HTTP requests
parse_reviews()       # Parses reviews from a single page
scrape_all_reviews()  # Manages pagination and flow
main()                # Entry point
```

## Possible Extensions

This mini-project can easily be extended by:

Exporting reviews to a CSV or SQLite database

Performing basic sentiment analysis or word frequency analysis

Building a simple dashboard to visualize average ratings and review trends

These additions can turn it into a small data engineering or analytics project.

---
## 🪶 Notes

This script is for educational and portfolio purposes only.

Trustpilot’s website structure may change over time, which can affect scraping.

The scraper performs only read operations (no login or automation beyond HTTP requests).

Author: Roberto Chiaiese

License: MIT
