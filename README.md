# 📈 Stock Sentiment Analysis 💹
This repository contains the code for a stock sentiment analysis project. It uses Natural Language Processing (NLP) techniques and Machine Learning (ML) models to predict the sentiment of stock market news headlines. The prediction can be either positive (stock price will increase) or negative (stock price will decrease).

![Banner Image](https://img.freepik.com/free-vector/global-business-background-with-stock-chart-blue-tone_53876-117483.jpg?w=1380&t=st=1690413977~exp=1690414577~hmac=d11431c141fd5b375ba1c3e8adfed0f86aab1ca2912f3c04fc96c78ef027034a)

## 🎯 Project Goal
The goal of this project is to predict whether the stock market will increase or decrease based on news headlines using machine learning algorithms.

## 📚 Dataset
The dataset used in this project is the [Daily News for Stock Market Prediction](https://www.kaggle.com/aaron7sun/stocknews) dataset from Kaggle.

## 🛠️ Installation
1. Clone this repository:
   ```
   git clone https://github.com/theamiteshtripathi/Stock-Sentiment-Analysis.git
   ```
2. Change into the project directory:
   ```
   cd Stock-Sentiment-Analysis
   ```
3. Install the required dependencies:
   ```
   conda env create -f environment.yml
   ```

## 📚 How to Use
The main script is `main.py` and it takes several command line arguments:
- `--data`: The path to the data file.
- `--headline`: A headline to predict the sentiment of.
- `--visualize`: Whether to visualize the results.

### Train a Model
To train a new model with your data, use the `--data` argument:
```bash
python3 main.py --data "/path/to/your/data.csv"
```

### Make a Prediction
To make a prediction on a specific headline, use the `--headline` argument. The model will be loaded from `models/model.joblib`. If this file doesn't exist, the script will try to train a new model, which requires the `--data` argument:
```bash
python3 main.py --headline "Your headline here"
```

### Visualize the Results
To visualize the results of the training or prediction, use the `--visualize` argument. This argument requires either the `--data` or `--headline` argument:
```bash
python3 main.py --data "/path/to/your/data.csv" --visualize
python3 main.py --headline "Your headline here" --visualize
```

## 📂 Project Structure
```
stockSentimentAnalysis/
|--- environment.yml
|--- README.md
|--- run.py
|--- src/
|    |--- __init__.py
|    |--- models/
|    |    |--- __init__.py
|    |    |--- train.py
|    |    |--- evaluate.py
|    |    |--- predict.py
|    |--- preprocessing/
|    |    |--- __init__.py
|    |    |--- clean_text.py
|    |--- visualization/
|    |    |--- __init__.py
|    |    |--- visualize.py
|--- data/
|--- models/
|--- config/
|    |--- __init__.py
|    |--- configuration.py
```

## 📈 Results
The final model achieved an accuracy of 82% on the test data.

## 📜 License
This project is licensed under the terms of the MIT license.

## 👥 Contribution
Contributions are welcome! Please make a pull request in this repository.

## 🤝 Contact
For any queries, please feel free to reach out to me at [theamiteshtripathi@gmail.com](theamiteshtripathi@gmail.com).
