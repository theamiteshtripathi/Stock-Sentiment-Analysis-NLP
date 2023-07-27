import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
import re

def clean_text(text):
    text = re.sub("[^a-zA-Z]", " ", text)
    text = text.lower()
    text = text.split()
    lemmatizer = WordNetLemmatizer()
    text = [lemmatizer.lemmatize(word) for word in text if not word in set(stopwords.words("english"))]
    text = " ".join(text)
    return text

def load_and_process_data(filepath):
    data = pd.read_csv(filepath, encoding='ISO-8859-1')
    data["Combined_News"] = data.filter(regex=("Top.*")).apply(lambda x: "".join(x.astype(str)), axis=1)
    data["Combined_News"] = data["Combined_News"].apply(clean_text)
    return data

# Usage
# filepath = 'path_to_your_data_file'
# data = load_and_process_data(filepath)
