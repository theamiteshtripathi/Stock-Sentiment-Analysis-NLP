from joblib import load
from clean_text import clean_text

def predict(model_filepath, text):
    # Load the model
    model = load(model_filepath)

    # Clean the text
    cleaned_text = clean_text(text)

    # Make the prediction
    prediction = model.predict([cleaned_text])

    return prediction

# Usage
# model_filepath = 'path_to_your_saved_model'
# text = 'Your raw text input here'
# prediction = predict(model_filepath, text)
