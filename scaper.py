import requests
from bs4 import BeautifulSoup
from time import sleep


def fetch_page_html(page: int) -> str | None:
    """Fetch HTML of a given Trustpilot review page for Vinted."""
    url = f"https://it.trustpilot.com/review/vinted.it?page={page}"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print(f"[!] Failed to retrieve page {page} (status {response.status_code})")
        return None

    print(f"[+] Successfully fetched page {page}")
    return response.text


def parse_reviews(html: str) -> list[dict]:
    """Parse reviews from a Trustpilot HTML page."""
    soup = BeautifulSoup(html, "lxml")
    review_cards = soup.find_all("div", attrs={"data-testid": "service-review-card-v2"})
    reviews = []

    for card in review_cards:
        try:
            reviewer = card.find("span", class_=lambda x: x and "consumerName" in x).text.strip()
        except AttributeError:
            reviewer = "Unknown"

        try:
            title = card.find("h2").text.strip()
        except AttributeError:
            title = ""

        try:
            content = card.find("p").text.strip()
        except AttributeError:
            content = ""

        try:
            date_review = card.find(
                "span",
                class_=lambda x: x and "Badge_badgeText" in x
            ).text.strip()
        except AttributeError:
            date_review = ""

        try:
            stars = card.find("img", class_=lambda x: x and "StarRating" in x)["alt"].split()[1]
        except Exception:
            stars = "N/A"

        reviews.append({
            "reviewer": reviewer,
            "title": title,
            "content": content,
            "date": date_review,
            "stars": stars
        })

    return reviews


def scrape_all_reviews(max_pages: int = 5, delay: int = 2) -> list[dict]:
    """Scrape multiple pages of Trustpilot reviews for Vinted."""
    all_reviews = []

    for page in range(1, max_pages + 1):
        html = fetch_page_html(page)
        if not html:
            break

        reviews = parse_reviews(html)
        if not reviews:
            print(f"[i] No reviews found on page {page}. Stopping.")
            break

        print(f"[+] Page {page}: found {len(reviews)} reviews.")
        all_reviews.extend(reviews)

        sleep(delay)

    return all_reviews


def main():
    reviews = scrape_all_reviews(max_pages=10, delay=1)

    print(f"\nTotal reviews scraped: {len(reviews)}\n")
    for r in reviews[:5]:  # show just first 5
        print(f"{r['reviewer']} - {r['stars']} stars")
        print(f"{r['title']}\n{r['content']}\n---")


if __name__ == "__main__":
    main()

