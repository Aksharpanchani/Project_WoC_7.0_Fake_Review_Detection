# Fake Review Detection System

## Introduction

This project aims to develop a Fake Review Detection System, which uses machine learning techniques to identify fraudulent or fake reviews from a dataset of user-generated reviews. By cleaning and preprocessing the data, the system can train various classification models to detect suspicious patterns in reviews, such as misleading ratings or over-exaggerated opinions.

## Checkpoint 1: Data Preprocessing

Checkpoint 1 focuses on cleaning and preprocessing the review data to prepare it for machine learning. The preprocessing steps include loading the data, cleaning, normalizing, tokenizing, removing stopwords, lemmatizing, and vectorizing the text. These steps help in ensuring that the data is structured and ready for model training.

### Steps Included:

1. **Loading Data**: Loading the dataset containing the reviews into a pandas DataFrame.
   
2. **Data Cleaning**: 
   - Removal of duplicate rows.
   - Removal of reviews with fewer than 5 words.
   - Filtering out reviews containing URLs.

3. **Text Normalization**: 
   - Convert text to lowercase.
   - Remove punctuation, special characters, and numbers to retain only meaningful words.

4. **Tokenization**: 
   - Tokenize each review into individual words (tokens).

5. **Stopword Removal**: 
   - Remove common stopwords (e.g., 'and', 'the', etc.) that do not contribute to meaningful analysis.

6. **Lemmatization**: 
   - Convert words to their base or root form (e.g., 'running' becomes 'run').

7. **Vectorization**: 
   - Convert the cleaned text into a numerical format using TF-IDF vectorization, which transforms the text into vectors that can be used by machine learning algorithms.

8. **Saving Cleaned Data**: 
   - Save the cleaned and preprocessed data to a new CSV file for further use in model training.
