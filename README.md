# Fake Review Detection System

## Introduction

This project aims to develop a Fake Review Detection System using machine learning techniques to identify fraudulent or fake reviews from a dataset of user-generated reviews. By cleaning and preprocessing the data, the system can train various classification models to detect suspicious patterns in reviews, such as misleading ratings or over-exaggerated opinions.

## Checkpoint 1: Data Preprocessing

Checkpoint 1 focuses on cleaning and preprocessing the review data to prepare it for machine learning. The preprocessing steps include loading the data, cleaning, normalizing, tokenizing, removing stopwords, lemmatizing, and vectorizing the text. These steps ensure the data is structured and ready for model training.

### Steps Included:

1. **Loading Data**: Load the dataset containing the reviews into a pandas DataFrame.
2. **Data Cleaning**:  
   - Remove duplicate rows.  
   - Remove reviews with fewer than 5 words.  
   - Filter out reviews containing URLs.  
3. **Text Normalization**:  
   - Convert text to lowercase.  
   - Remove punctuation, special characters, and numbers to retain only meaningful words.  
4. **Tokenization**: Tokenize each review into individual words (tokens).  
5. **Stopword Removal**: Remove common stopwords (e.g., 'and', 'the', etc.) that do not contribute to meaningful analysis.  
6. **Lemmatization**: Convert words to their base or root form (e.g., 'running' becomes 'run').  
7. **Vectorization**: Transform the cleaned text into numerical format using TF-IDF vectorization, enabling machine learning algorithms to process the data.  
8. **Saving Cleaned Data**: Save the cleaned and preprocessed data to a new CSV file for further use in model training.  

## Checkpoint 2: Model Training Process

### Dataset Preparation:  
1. Load the preprocessed dataset created during the initial data preparation phase.  
2. Split the dataset into training and testing sets to evaluate the model's performance.

### Model Selection:  
Experiment with different classifiers such as Random Forest, SVM, and Logistic Regression to identify the best-performing model for the given data.

### Pipeline Creation:  
Construct pipelines to streamline the process of vectorization, transformation, and model application.

### Model Training:  
Train each model using the training dataset.

### Model Evaluation:  
1. Use the testing dataset to evaluate the model’s performance based on metrics such as accuracy, precision, recall, and F1 score.  
2. Compare the results of different models to choose the optimal one.

### Model Serialization:  
Save the trained models using serialization techniques (e.g., joblib) for future use.
