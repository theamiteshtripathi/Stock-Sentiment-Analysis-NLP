import argparse
from preprocessing.clean_text import clean_text, load_and_process_data
from models.train import train_model
from models.evaluate import evaluate_model
from models.predict import predict_headline_sentiment
from visualization.visualize import visualize_results
from config.configuration import Config

def main(args):
    # Load and preprocess the data
    print("Loading and preprocessing data...")
    data = load_and_process_data(Config.RAW_DATA_DIR)
    cleaned_data = clean_text(data)

    # Train the model
    print("Training model...")
    model = train_model(cleaned_data)

    # Evaluate the model
    print("Evaluating model...")
    evaluate_model(model, cleaned_data)

    # Make a prediction
    if args.headline:
        print("Making a prediction...")
        prediction = predict_headline_sentiment(model, args.headline)
        print(f"The predicted sentiment of the headline is: {prediction}")

    # Visualize the results
    if args.visualize:
        print("Visualizing results...")
        visualize_results(model, cleaned_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the Stock Sentiment Analysis project.')
    parser.add_argument('--headline', type=str, help='A headline to predict the sentiment of.')
    parser.add_argument('--visualize', action='store_true', help='Whether to visualize the results.')
    args = parser.parse_args()
    main(args)
