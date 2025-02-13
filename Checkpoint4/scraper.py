import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import time
from random import choice

# Configure logging
logging.basicConfig(level=logging.INFO)

# List of User-Agents to rotate
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/92.0"
]

def scrape_reviews(product_url, **selectors):
    """
    Scrape reviews from a product page using dynamically provided selectors.
    """
    headers = {
        "User-Agent": choice(USER_AGENTS),  # Random User-Agent to prevent blocking
        "Accept-Language": "en-US,en;q=0.9"
    }
    session = requests.Session()

    try:
        logging.info(f"Fetching {product_url}...")
        response = session.get(product_url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching the page: {e}")
        return pd.DataFrame()

    time.sleep(3)  # Shortened wait time to optimize scraping
    soup = BeautifulSoup(response.content, "html.parser")
    review_selector = selectors.get("review_selector", ".review")
    reviews = soup.select(review_selector)

    if not reviews:
        logging.warning("No reviews found! HTML structure might have changed.")
        return pd.DataFrame()

    review_texts, ratings, reviewer_names, review_dates = [], [], [], []

    for review in reviews:
        review_texts.append(extract_text(review, selectors.get("text_selector", ".review-text")))
        ratings.append(clean_rating(extract_text(review, selectors.get("rating_selector", ".review-rating"))))
        reviewer_names.append(extract_text(review, selectors.get("author_selector", ".review-author")))
        review_dates.append(extract_text(review, selectors.get("date_selector", ".review-date")))

    return pd.DataFrame({
        "Review Text": review_texts,
        "Rating": ratings,
        "Reviewer Name": reviewer_names,
        "Review Date": review_dates
    })

def extract_text(element, selector):
    """Helper function to safely extract text from an element."""
    if not selector:
        return None
    found_element = element.select_one(selector)
    return found_element.get_text(strip=True) if found_element else None

def clean_rating(rating):
    """Clean and extract numeric value from the rating text."""
    if rating:
        try:
            return float(rating.split()[0])
        except (ValueError, AttributeError):
            return None
    return None
