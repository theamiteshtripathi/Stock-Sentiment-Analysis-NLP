from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from joblib import load
from src.stockSentimentAnalysis.preprocessing.clean_text import load_and_process_data

def evaluate_model(model_filepath, test_filepath):
    # Load the model
    model = load(model_filepath)

    # Load and process the test data
    test_data = load_and_process_data(test_filepath)

    # Make predictions on the test data
    predictions = model.predict(test_data['Combined_News'])

    # Calculate and print the accuracy
    accuracy = accuracy_score(test_data['Label'], predictions)
    print(f'Accuracy: {accuracy}')

    # Print the classification report
    print(classification_report(test_data['Label'], predictions))

    # Print the confusion matrix
    print(confusion_matrix(test_data['Label'], predictions))

# Usage
# model_filepath = 'path_to_your_saved_model'
# test_filepath = 'path_to_your_test_data'
# evaluate_model(model_filepath, test_filepath)
