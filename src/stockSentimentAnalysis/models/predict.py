from joblib import load
from src.stockSentimentAnalysis.preprocessing.clean_text import clean_text

def predict(model_filepath, text):
    # Load the model
    model = load(model_filepath)

    # Clean the text
    cleaned_text = clean_text(text)

    # Make the prediction
    prediction = model.predict([cleaned_text])

    return prediction

def predict_headline_sentiment(model_filepath, headline):
    # Load the trained model
    model = load(model_filepath)

    # Preprocess the headline
    cleaned_headline = clean_text(headline)

    # Convert the cleaned headline to a pandas series
    cleaned_headline_series = pd.Series(cleaned_headline)

    # Use the model to predict the sentiment of the headline
    prediction = model.predict(cleaned_headline_series)

    return prediction[0]

# Usage
# model_filepath = 'path_to_your_saved_model'
# text = 'Your raw text input here'
# prediction = predict(model_filepath, text)
