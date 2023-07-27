# 📈 Stock Sentiment Analysis 📰

![Banner Image](https://img.freepik.com/free-vector/global-business-background-with-stock-chart-blue-tone_53876-117483.jpg?w=1380&t=st=1690413977~exp=1690414577~hmac=d11431c141fd5b375ba1c3e8adfed0f86aab1ca2912f3c04fc96c78ef027034a)

Welcome to the Stock Sentiment Analysis project! This project uses Natural Language Processing (NLP) techniques to analyze news headlines and predict the impact on stock market movements.

## 🎯 Project Goal

The goal of this project is to predict whether the stock market will increase or decrease based on news headlines using machine learning algorithms.

## 📚 Dataset

The dataset used in this project is the [Daily News for Stock Market Prediction](https://www.kaggle.com/aaron7sun/stocknews) dataset from Kaggle.

## 🧰 Requirements

The dependencies for this project are listed in the `environment.yaml` file. To install these dependencies, run the following command:

```bash
conda env create -f environment.yml
```

## 🚀 Usage

To run the entire project, use the following command:

```bash
python main.py --headline "Your headline text here" --visualize
```

Replace `"Your headline text here"` with the actual headline text that you want to predict.

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

## 📝 License

This project is licensed under the MIT License.

---






