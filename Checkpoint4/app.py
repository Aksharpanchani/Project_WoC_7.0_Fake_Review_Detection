from flask import Flask, render_template, request
import joblib
from scraper import scrape_reviews  # Import your Checkpoint 3 scraper

app = Flask(__name__)

# Load ML model (replace with your actual model)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    product_url = request.form['product_url']
    
    try:
        # Scrape reviews
        reviews_df = scrape_reviews(product_url)
        if reviews_df.empty:
            return render_template('index.html', error="No reviews found!")

        # Classify reviews
        reviews = []
        for text in reviews_df['Review Text']:
            prediction = model.predict([text])[0]  # Replace with your model's predict method
            probability = model.predict_proba([text])[0][1] * 100  # Adjust for your model
            reviews.append({
                'text': text,
                'prediction': 'Real' if prediction == 1 else 'Fake',
                'probability': round(probability, 2)
            })

        return render_template('index.html', results=reviews)

    except Exception as e:
        return render_template('index.html', error=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)