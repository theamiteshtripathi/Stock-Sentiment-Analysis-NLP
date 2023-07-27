from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from joblib import load
from src.stockSentimentAnalysis.preprocessing.clean_text import load_and_process_data

def evaluate_model(model, X_test, y_test):
    # Make predictions on the test data
    predictions = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, predictions)
    print(f"Test Accuracy: {accuracy}")
    
    # Print the classification report
    print(classification_report(y_test, predictions))
    
    # Print the confusion matrix
    print(confusion_matrix(y_test, predictions))


# Usage
# model_filepath = 'path_to_your_saved_model'
# test_filepath = 'path_to_your_test_data'
# evaluate_model(model_filepath, test_filepath)
