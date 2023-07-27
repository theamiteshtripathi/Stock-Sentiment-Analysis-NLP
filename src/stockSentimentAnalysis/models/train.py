from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from joblib import dump
from src.stockSentimentAnalysis.preprocessing.clean_text import load_and_process_data

def train_model(filepath):
    # Load and process the data
    data = load_and_process_data(filepath)
    
    # Split the data into training and test sets
    train, test = train_test_split(data, test_size=0.2, random_state=42)
    
    # Define the model pipeline
    model_pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=5000,ngram_range=(1,3))),
        ('chi2', SelectKBest(chi2, k=1200)),
        ('clf', RandomForestClassifier())
    ])
    
    # Fit the model
    model_pipeline.fit(train["Combined_News"], train["Label"])
    
    # Save the model
    dump(model_pipeline, 'models/model.joblib')

# Usage
# filepath = 'path_to_your_data_file'
# train_model(filepath)
