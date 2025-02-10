import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from random import uniform
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Function to scrape reviews from a product URL
def scrape_reviews(product_url, review_selector=".review", text_selector=".review-text", 
                   rating_selector=".review-rating", author_selector=".review-author", 
                   date_selector=".review-date"):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(product_url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return pd.DataFrame()

    soup = BeautifulSoup(response.content, "html.parser")
    reviews = soup.select(review_selector)

    review_texts = []
    ratings = []
    reviewer_names = []
    review_dates = []

    for review in reviews:
        # Extract review text
        text = review.select_one(text_selector).get_text(strip=True) if review.select_one(text_selector) else None
        review_texts.append(text)

        # Extract and clean rating
        rating = review.select_one(rating_selector).get_text(strip=True) if review.select_one(rating_selector) else None
        ratings.append(clean_rating(rating))

        # Extract reviewer name
        name = review.select_one(author_selector).get_text(strip=True) if review.select_one(author_selector) else None
        reviewer_names.append(name)

        # Extract review date
        date = review.select_one(date_selector).get_text(strip=True) if review.select_one(date_selector) else None
        review_dates.append(date)

    return pd.DataFrame({
        "Review Text": review_texts,
        "Rating": ratings,
        "Reviewer Name": reviewer_names,
        "Review Date": review_dates
    })

# Function to clean rating data
def clean_rating(rating):
    if rating:
        try:
            return float(rating.split()[0])
        except (ValueError, AttributeError):
            return None
    return None

# Main function to scrape and save reviews
def main():
    product_url = input("Enter the product URL to scrape reviews: ").strip()
    output_file = "Reviews.csv"

    # Define selectors (customize for the target website)
    selectors = {
        "review_selector": ".review",
        "text_selector": ".review-text",
        "rating_selector": ".review-rating",
        "author_selector": ".review-author",
        "date_selector": ".review-date"
    }

    # Scrape reviews
    reviews_data = scrape_reviews(product_url, **selectors)

    if reviews_data.empty:
        logging.error("No reviews scraped. Check the URL or selectors.")
        return

    # Save to CSV
    if os.path.exists(output_file):
        logging.warning(f"{output_file} already exists. Appending data.")
        existing_data = pd.read_csv(output_file)
        reviews_data = pd.concat([existing_data, reviews_data], ignore_index=True)

    reviews_data.to_csv(output_file, index=False)
    logging.info(f"Scraped reviews saved to {output_file}")

if __name__ == "__main__":
    main()