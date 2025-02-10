{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Checkpoint 3: Web Scraping for Reviews"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Objective\n",
    "The goal of this task is to scrape product reviews from a given product URL, extract essential details such as review text, ratings, reviewer names, and dates, and save the results into a structured CSV file for further analysis."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Libraries Used\n",
    "- **requests**: To fetch HTML content of the product page.\n",
    "- **BeautifulSoup**: For parsing and extracting data from HTML.\n",
    "- **pandas**: To organize and save the extracted data.\n",
    "\n",
    "Install the required libraries using:\n",
    "```bash\n",
    "pip install requests beautifulsoup4 pandas\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "\n",
    "# Function to scrape reviews from a product URL\n",
    "def scrape_reviews(product_url):\n",
    "    # Send a GET request to the product page\n",
    "    headers = {\n",
    "        \"User-Agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36\"\n",
    "    }\n",
    "    response = requests.get(product_url, headers=headers)\n",
    "\n",
    "    # Parse the HTML content\n",
    "    soup = BeautifulSoup(response.content, \"html.parser\")\n",
    "\n",
    "    # Initialize lists to store extracted data\n",
    "    review_texts = []\n",
    "    ratings = []\n",
    "    reviewer_names = []\n",
    "    review_dates = []\n",
    "\n",
    "    # Extract reviews\n",
    "    for review in soup.select(\".review\"):\n",
    "        # Extract review text\n",
    "        text = review.select_one(\".review-text\").get_text(strip=True) if review.select_one(\".review-text\") else None\n",
    "        review_texts.append(text)\n",
    "\n",
    "        # Extract rating\n",
    "        rating = review.select_one(\".review-rating\").get_text(strip=True) if review.select_one(\".review-rating\") else None\n",
    "        ratings.append(rating)\n",
    "\n",
    "        # Extract reviewer name\n",
    "        name = review.select_one(\".review-author\").get_text(strip=True) if review.select_one(\".review-author\") else None\n",
    "        reviewer_names.append(name)\n",
    "\n",
    "        # Extract review date\n",
    "        date = review.select_one(\".review-date\").get_text(strip=True) if review.select_one(\".review-date\") else None\n",
    "        review_dates.append(date)\n",
    "\n",
    "    # Create a DataFrame to organize the scraped data\n",
    "    data = pd.DataFrame({\n",
    "        \"Review Text\": review_texts,\n",
    "        \"Rating\": ratings,\n",
    "        \"Reviewer Name\": reviewer_names,\n",
    "        \"Review Date\": review_dates\n",
    "    })\n",
    "\n",
    "    return data\n",
    "\n",
    "# Main function to scrape and save reviews\n",
    "product_url = input(\"Enter the product URL to scrape reviews: \").strip()\n",
    "\n",
    "# Scrape reviews\n",
    "reviews_data = scrape_reviews(product_url)\n",
    "\n",
    "# Save to CSV\n",
    "output_file = \"Reviews.csv\"\n",
    "reviews_data.to_csv(output_file, index=False)\n",
    "print(f\"Scraped reviews saved to {output_file}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Steps to Run the Script\n",
    "1. **Install Required Libraries**:\n",
    "   ```bash\n",
    "   pip install requests beautifulsoup4 pandas\n",
    "   ```\n",
    "2. **Run the Script**:\n",
    "   - Execute the code and provide a valid product URL when prompted.\n",
    "3. **Output**:\n",
    "   - The extracted reviews will be saved into a file named `Reviews.csv`.\n",
    "   - The file contains fields: Review Text, Rating, Reviewer Name, and Review Date."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Notes\n",
    "- The script works for static websites. For dynamic content, use tools like `selenium`.\n",
    "- Ensure the URL provided is from the target website and contains reviews."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
