import argparse
from joblib import load
from src.stockSentimentAnalysis.preprocessing.clean_text import load_and_process_data
from src.stockSentimentAnalysis.models.train import train_model
from src.stockSentimentAnalysis.models.evaluate import evaluate_model
from src.stockSentimentAnalysis.models.predict import predict_headline_sentiment
from src.stockSentimentAnalysis.visualization.visualize import visualize_results

def main(args):
    data = None
    model = None
    X_test = None
    y_test = None

    # Load and preprocess the data if a data file is provided
    if args.data:
        print("Loading and preprocessing data...")
        data = load_and_process_data(args.data)

    # Train the model if data is loaded
    if data is not None:
        print("Training model...")
        model, X_test, y_test = train_model(data)

    # Evaluate the model if it's trained
    if model is not None and data is not None:
        print("Evaluating model...")
        evaluate_model(model, X_test, y_test)

    # Make a prediction if a headline is provided
    if args.headline:
        # If a model is not trained, load it from the saved model file
        if model is None:
            print("Loading model...")
            model = load('models/model.joblib')
        print("Making a prediction...")
        prediction = predict_headline_sentiment(model, args.headline)
        print(f"The predicted sentiment of the headline is: {prediction}")

    # Visualize the results if the --visualize argument is provided and a model is trained
    if args.visualize and model is not None and data is not None:
        print("Visualizing results...")
        visualize_results(data, model, X_test, y_test)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the Stock Sentiment Analysis project.')
    parser.add_argument('--headline', type=str, help='A headline to predict the sentiment of.')
    parser.add_argument('--visualize', action='store_true', help='Whether to visualize the results.')
    parser.add_argument('--data', type=str, help='Path to the data file.')
    args = parser.parse_args()
    main(args)
