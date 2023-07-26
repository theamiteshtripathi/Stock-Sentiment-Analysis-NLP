# -*- coding: utf-8 -*-
"""Stock Sentiment Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12XYOHnegjJWiTU2OCmy4pdfj_5e4vkl1

## Stock Sentiment Analysis using News Headlines
"""

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from google.colab import files

uploaded = files.upload()

df=pd.read_csv('Data.csv', encoding = "ISO-8859-1")

df.head()

# Check the shape of the dataset
print("Number of rows: ", df.shape[0])
print("Number of columns: ", df.shape[1])

# Check the distribution of labels
sns.countplot(x='Label', data=df)
plt.title('Distribution of Labels in the Dataset')
plt.show()

# Check if there are any missing values
missing_values = df.isnull().sum().sum()
print("Number of missing values in the dataset: ", missing_values)

# Replace missing values with an empty string
df = df.fillna('')

# Check if there are any missing values left
missing_values = df.isnull().sum().sum()
print("Number of missing values in the dataset: ", missing_values)

# Download the necessary NLTK data
nltk.download('stopwords')
nltk.download('wordnet')

# Create a lemmatizer object
lemmatizer = WordNetLemmatizer()

# Define the set of stopwords
stopwords_set = set(stopwords.words('english'))

# Initialize an empty list to hold the cleaned headlines
cleaned_headlines = []

# Loop over each row in the dataframe
for index, row in df.iterrows():
    # Join all the headlines into a single string
    joined_headlines = ' '.join(str(x) for x in row[2:])

    # Convert the headlines to lower case
    lower_headlines = joined_headlines.lower()

    # Split the headlines into words
    words = lower_headlines.split()

    # Remove stopwords and lemmatize the words
    cleaned_words = [lemmatizer.lemmatize(word) for word in words if word not in stopwords_set]

    # Join the cleaned words back into a single string and add it to the list
    cleaned_headline = ' '.join(cleaned_words)
    cleaned_headlines.append(cleaned_headline)

# Replace the old headlines with the cleaned headlines in the dataframe
df['Cleaned Headlines'] = cleaned_headlines

# Display the first few rows of the dataframe
df.head()

"""we move on to the feature extraction step. We will experiment with different feature extraction methods. We will start with CountVectorizer as in the original code, but we'll also try TF-IDF (Term Frequency-Inverse Document Frequency). TF-IDF is a statistic that reflects how important a word is to a document in a collection or corpus."""

from sklearn.feature_extraction.text import CountVectorizer

# Create a new DataFrame for the features
features = df.copy()

# Split the data into training and test sets
train = features[features['Date'] < '20150101']
test = features[features['Date'] > '20141231']

# Implement BAG OF WORDS
countvector = CountVectorizer(ngram_range=(2,2))
traindataset = countvector.fit_transform(train['Cleaned Headlines'])
test_dataset = countvector.transform(test['Cleaned Headlines'])

traindataset, test_dataset

"""TF-IDF (Term Frequency-Inverse Document Frequency) is another method that represents text data in terms of a matrix. However, instead of just counting the number of times each word appears in each document, it assigns a weight to each word in each document. This weight is the product of two terms: the term frequency (the count of the word in the document) and the inverse document frequency (the log of the total number of documents divided by the number of documents that contain the word). The idea is to give higher weight to words that are more unique to a document."""

from sklearn.feature_extraction.text import TfidfVectorizer

# Implement TF-IDF
tfidfvector = TfidfVectorizer(ngram_range=(2,2))
traindataset_tfidf = tfidfvector.fit_transform(train['Cleaned Headlines'])
test_dataset_tfidf = tfidfvector.transform(test['Cleaned Headlines'])

traindataset_tfidf, test_dataset_tfidf

"""Now that we've extracted features from the text, the next step is to train a machine learning model on these features. In the original code, a RandomForest Classifier was used. We'll start with that, but also consider other models for comparison.

Let's proceed with the RandomForest Classifier using the Bag of Words features. We'll train the model and then evaluate its performance on the test set. We'll use accuracy as the evaluation metric for now, but later we'll also consider other metrics like Precision, Recall, and F1-score.
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Implement RandomForest Classifier
randomclassifier=RandomForestClassifier(n_estimators=200, criterion='entropy')
randomclassifier.fit(traindataset, train['Label'])

# Predict for the Test Dataset
predictions = randomclassifier.predict(test_dataset)

# Evaluation
matrix = confusion_matrix(test['Label'], predictions)
score = accuracy_score(test['Label'], predictions)
report = classification_report(test['Label'], predictions)

matrix, score, report

# Implement RandomForest Classifier
randomclassifier=RandomForestClassifier(n_estimators=200, criterion='entropy')
randomclassifier.fit(traindataset_tfidf, train['Label'])

# Predict for the Test Dataset
predictions_tfidf = randomclassifier.predict(test_dataset_tfidf)

# Evaluation
matrix_tfidf = confusion_matrix(test['Label'], predictions_tfidf)
score_tfidf = accuracy_score(test['Label'], predictions_tfidf)
report_tfidf = classification_report(test['Label'], predictions_tfidf)

matrix_tfidf, score_tfidf, report_tfidf

from sklearn.linear_model import LogisticRegression

# Implement Logistic Regression
logreg = LogisticRegression()
logreg.fit(traindataset, train['Label'])

# Predict for the Test Dataset
predictions_logreg = logreg.predict(test_dataset)

# Evaluation
matrix_logreg = confusion_matrix(test['Label'], predictions_logreg)
score_logreg = accuracy_score(test['Label'], predictions_logreg)
report_logreg = classification_report(test['Label'], predictions_logreg)

matrix_logreg, score_logreg, report_logreg

# Implement Logistic Regression with TF-IDF
logreg.fit(traindataset_tfidf, train['Label'])

# Predict for the Test Dataset
predictions_logreg_tfidf = logreg.predict(test_dataset_tfidf)

# Evaluation
matrix_logreg_tfidf = confusion_matrix(test['Label'], predictions_logreg_tfidf)
score_logreg_tfidf = accuracy_score(test['Label'], predictions_logreg_tfidf)
report_logreg_tfidf = classification_report(test['Label'], predictions_logreg_tfidf)

matrix_logreg_tfidf, score_logreg_tfidf, report_logreg_tfidf

from sklearn.naive_bayes import MultinomialNB

# Implement Multinomial Naive Bayes
nb = MultinomialNB()
nb.fit(traindataset, train['Label'])

# Predict for the Test Dataset
predictions_nb = nb.predict(test_dataset)

# Evaluation
matrix_nb = confusion_matrix(test['Label'], predictions_nb)
score_nb = accuracy_score(test['Label'], predictions_nb)
report_nb = classification_report(test['Label'], predictions_nb)

matrix_nb, score_nb, report_nb

# Implement Multinomial Naive Bayes with TF-IDF
nb.fit(traindataset_tfidf, train['Label'])

# Predict for the Test Dataset
predictions_nb_tfidf = nb.predict(test_dataset_tfidf)

# Evaluation
matrix_nb_tfidf = confusion_matrix(test['Label'], predictions_nb_tfidf)
score_nb_tfidf = accuracy_score(test['Label'], predictions_nb_tfidf)
report_nb_tfidf = classification_report(test['Label'], predictions_nb_tfidf)

matrix_nb_tfidf, score_nb_tfidf, report_nb_tfidf

# Create a dataframe to hold the results
results = pd.DataFrame({
    'Model': ['Random Forest (BoW)', 'Random Forest (TF-IDF)', 'Logistic Regression (BoW)', 'Logistic Regression (TF-IDF)', 'Multinomial NB (BoW)', 'Multinomial NB (TF-IDF)'],
    'Accuracy': [score, score_tfidf, score_logreg, score_logreg_tfidf, score_nb, score_nb_tfidf]
})

# Display the results
results

# Create plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Accuracy', y='Model', data=results)

plt.xlabel('Accuracy', size=15)
plt.ylabel('Model', size=15)
plt.title('Model Comparison - Accuracy', size=15)
plt.tick_params(axis='x', labelsize=10)
plt.tick_params(axis='y', labelsize=10)

plt.show()

from sklearn.feature_selection import SelectKBest, chi2

# Define the feature selection
selector = SelectKBest(chi2, k=1000)

# Fit the feature selection
selector.fit(traindataset, train['Label'])

# Transform the datasets
traindataset_reduced = selector.transform(traindataset)
test_dataset_reduced = selector.transform(test_dataset)

traindataset_reduced.shape, test_dataset_reduced.shape

# Implement RandomForest Classifier
randomclassifier=RandomForestClassifier(n_estimators=200, criterion='entropy')
randomclassifier.fit(traindataset_reduced, train['Label'])

# Predict for the Test Dataset
predictions_reduced = randomclassifier.predict(test_dataset_reduced)

# Evaluation
matrix_reduced = confusion_matrix(test['Label'], predictions_reduced)
score_reduced = accuracy_score(test['Label'], predictions_reduced)
report_reduced = classification_report(test['Label'], predictions_reduced)

matrix_reduced, score_reduced, report_reduced

# Implement Logistic Regression with reduced features
logreg.fit(traindataset_reduced, train['Label'])

# Predict for the Test Dataset
predictions_logreg_reduced = logreg.predict(test_dataset_reduced)

# Evaluation
matrix_logreg_reduced = confusion_matrix(test['Label'], predictions_logreg_reduced)
score_logreg_reduced = accuracy_score(test['Label'], predictions_logreg_reduced)
report_logreg_reduced = classification_report(test['Label'], predictions_logreg_reduced)

matrix_logreg_reduced, score_logreg_reduced, report_logreg_reduced

# Implement Multinomial Naive Bayes with reduced features
nb.fit(traindataset_reduced, train['Label'])

# Predict for the Test Dataset
predictions_nb_reduced = nb.predict(test_dataset_reduced)

# Evaluation
matrix_nb_reduced = confusion_matrix(test['Label'], predictions_nb_reduced)
score_nb_reduced = accuracy_score(test['Label'], predictions_nb_reduced)
report_nb_reduced = classification_report(test['Label'], predictions_nb_reduced)

matrix_nb_reduced, score_nb_reduced, report_nb_reduced

# Add the new results to the previous results dataframe
results_reduced = pd.DataFrame({
    'Model': ['Random Forest (BoW, Reduced)', 'Logistic Regression (BoW, Reduced)', 'Multinomial NB (BoW, Reduced)'],
    'Accuracy': [score_reduced, score_logreg_reduced, score_nb_reduced]
})

results_all = pd.concat([results, results_reduced], ignore_index=True)

# Display the results
results_all

# Create plot for all models including the ones with reduced features
plt.figure(figsize=(10, 6))
sns.barplot(x='Accuracy', y='Model', data=results_all)

plt.xlabel('Accuracy', size=15)
plt.ylabel('Model', size=15)
plt.title('Model Comparison - Accuracy', size=15)
plt.tick_params(axis='x', labelsize=10)
plt.tick_params(axis='y', labelsize=10)

plt.show()

"""Ensemble Modelling"""

from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier

# Instantiate the base models
classifier1 = RandomForestClassifier(random_state=1)
classifier2 = LogisticRegression()
classifier3 = MultinomialNB()

# Define a list called base_models to store all the base models
base_models = [('RandomForest', classifier1),
               ('LogisticRegression', classifier2),
               ('MultinomialNB', classifier3)]

# Initialize the Stacking Classifier with the base models
stacking_model = StackingClassifier(estimators=base_models, final_estimator=LogisticRegression())

# Fit the model to the training data
stacking_model.fit(traindataset_reduced, train['Label'])

# Evaluate the model on the test data
stacking_score = stacking_model.score(test_dataset_reduced, test['Label'])

print('Stacking Classifier Accuracy: ', stacking_score)

from sklearn.model_selection import GridSearchCV

# Define a parameter grid for the final estimator
param_grid = {
    'final_estimator__C': [0.1, 1.0, 10.0],
    'final_estimator__penalty': ['l2', 'none']
}

# Initialize the GridSearchCV
grid_search = GridSearchCV(estimator=stacking_model, param_grid=param_grid, cv=5)

# Fit the GridSearchCV to the training data
grid_search.fit(traindataset_reduced, train['Label'])

# Print the best parameters and the best score
print('Best Parameters:', grid_search.best_params_)
print('Best Score:', grid_search.best_score_)

# Evaluate the model on the test data
test_score = grid_search.score(test_dataset_reduced, test['Label'])

print('Test Accuracy: ', test_score)

from sklearn.metrics import classification_report, confusion_matrix

# Generate predictions on the test data
test_preds = grid_search.predict(test_dataset_reduced)

# Print the classification report
print(classification_report(test['Label'], test_preds))

# Print the confusion matrix
print(confusion_matrix(test['Label'], test_preds))




