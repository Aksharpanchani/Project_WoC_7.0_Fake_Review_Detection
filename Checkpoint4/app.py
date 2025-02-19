from flask import Flask, render_template, request
import joblib
from scraper import scrape_reviews
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the trained pipeline (vectorizer + model)
try:
    pipeline = joblib.load('model.pkl')
except Exception as e:
    pipeline = None
    print(f"Error loading model: {e}")

@app.route('/')
def home():
    """
    Render the homepage with the input form.
    """
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Analyze reviews from the provided product URL.
    """
    if not pipeline:
        return render_template('index.html', error="Model not loaded properly!")
    
    product_url = request.form['product_url']
    
    try:
        # Define selectors for the target website (Update based on real structure)
        selectors = {
            "review_selector": ".review",
            "text_selector": ".review-text",
            "rating_selector": ".review-rating",
            "author_selector": ".review-author",
            "date_selector": ".review-date"
        }

        # Scrape reviews with selectors
        reviews_df = scrape_reviews(product_url, **selectors)
        if reviews_df.empty:
            return render_template('index.html', error="No reviews found! Try another URL.")

        # Classify reviews using the loaded pipeline
        # Classify reviews using the loaded pipeline
        reviews = []
        for text in reviews_df['Review Text'].dropna():  # Drop missing values
            probability = pipeline.predict_proba([text])[0][1] * 100  # Get probability
            prediction = 'Real' if probability > 70 else 'Fake'  # Apply 70% threshold

            reviews.append({
                'text': text,
                'prediction': prediction,
                'probability': round(probability, 2)
            })

        return render_template('index.html', results=reviews)


    except Exception as e:
        return render_template('index.html', error=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
