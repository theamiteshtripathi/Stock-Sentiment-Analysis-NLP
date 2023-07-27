from src.stockSentimentAnalysis.preprocessing.clean_text import clean_text
from sklearn.feature_extraction.text import CountVectorizer

def predict_headline_sentiment(model, headline):
    """
    Make a prediction on the sentiment of a headline using a trained model.

    Parameters:
    model (object): The trained model
    headline (str): The headline to predict the sentiment of

    Returns:
    str: The predicted sentiment of the headline
    """

    # Clean the text
    cleaned_headline = clean_text(headline)

    # Make the prediction
    prediction = model.predict([cleaned_headline])

    return 'Positive' if prediction == 1 else 'Negative'

