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

def scrape_reviews(product_url, review_selector=".review", text_selector=".review-text", 
                   rating_selector=".review-rating", author_selector=".review-author", 
                   date_selector=".review-date"):
    """
    Scrape reviews from a product page using the provided selectors.
    """
    headers = {
        "User-Agent": choice(USER_AGENTS)  # Random User-Agent to prevent blocking
    }

    session = requests.Session()

    try:
        logging.info(f"Fetching {product_url}...")
        response = session.get(product_url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching the page: {e}")
        return pd.DataFrame()

    time.sleep(5)  # Wait to prevent blocking
    soup = BeautifulSoup(response.content, "html.parser")
    reviews = soup.select(review_selector)

    if not reviews:
        logging.warning("No reviews found! HTML structure might have changed.")
        return pd.DataFrame()

    review_texts, ratings, reviewer_names, review_dates = [], [], [], []

    for review in reviews:
        text = review.select_one(text_selector)
        rating = review.select_one(rating_selector)
        name = review.select_one(author_selector)
        date = review.select_one(date_selector)

        review_texts.append(text.get_text(strip=True) if text else None)
        ratings.append(clean_rating(rating.get_text(strip=True)) if rating else None)
        reviewer_names.append(name.get_text(strip=True) if name else None)
        review_dates.append(date.get_text(strip=True) if date else None)

    return pd.DataFrame({
        "Review Text": review_texts,
        "Rating": ratings,
        "Reviewer Name": reviewer_names,
        "Review Date": review_dates
    })

def clean_rating(rating):
    """
    Clean and extract numeric value from the rating text.
    """
    if rating:
        try:
            return float(rating.split()[0])
        except (ValueError, AttributeError):
            return None
    return None
