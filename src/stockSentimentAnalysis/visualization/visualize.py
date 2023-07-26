import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.metrics import ConfusionMatrixDisplay
from nltk.corpus import stopwords
from joblib import load
from clean_text import load_and_process_data

def create_word_cloud(data):
    # Create a word cloud of the news headlines
    text = ' '.join(data['Combined_News'])
    wordcloud = WordCloud(stopwords=stopwords.words('english')).generate(text)

    # Display the word cloud
    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def plot_label_distribution(data):
    # Plot the distribution of the labels
    plt.figure(figsize=(6, 6))
    data['Label'].value_counts().plot(kind='bar')
    plt.title('Distribution of Labels')
    plt.xlabel('Label')
    plt.ylabel('Count')
    plt.show()

def plot_confusion_matrix(model_filepath, test_filepath):
    # Load the model and test data
    model = load(model_filepath)
    test_data = load_and_process_data(test_filepath)

    # Make predictions on the test data
    predictions = model.predict(test_data['Combined_News'])

    # Plot the confusion matrix
    cm = confusion_matrix(test_data['Label'], predictions)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    disp.plot()
    plt.show()

# Usage
# filepath = 'path_to_your_data_file'
# data = load_and_process_data(filepath)
# create_word_cloud(data)
# plot_label_distribution(data)
# model_filepath = 'path_to_your_saved_model'
# test_filepath = 'path_to_your_test_data'
# plot_confusion_matrix(model_filepath, test_filepath)
