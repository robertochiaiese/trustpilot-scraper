# 🕷️ Trustpilot Vinted Scraper

A simple Python script that scrapes reviews of **Vinted Italy** from [Trustpilot](https://it.trustpilot.com/review/vinted.it) using `requests` and `BeautifulSoup`.

The goal is to demonstrate a clean and modular approach to basic web scraping — focusing on **code structure**, **error handling**, and **clarity**, rather than large-scale data extraction.

---

## 🧠 Overview

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
