# kaim-week-1
# EDA and Analysis Project

This repository contains three tasks focused on Exploratory Data Analysis (EDA) and analysis of stock data and analyst data. The project is divided into three tasks, each with its own focus and set of functionalities.

## Task 1: Stock Data EDA and Analysis

### Overview

In this task, we perform EDA on historical stock data for various companies. The analysis includes calculating financial indicators, visualizing the data, and analyzing portfolio metrics.

### Files

- **`eda_task_1.ipynb`**: The Jupyter notebook for Task 1.
- **`scripts/data_loader.py`**: Module to load stock data.
- **`scripts/data_preparation.py`**: Module to calculate financial indicators.
- **`scripts/data_visualization.py`**: Module to visualize the indicators.
- **`scripts/calculate_financial_metrics.py`**: Module to calculate portfolio metrics.

### Steps

1. **Load Stock Data**: Import and load historical stock data for AAPL, AMZN, GOOG, META, MSFT, NVDA, and TSLA.
2. **Calculate Indicators**: Apply financial indicators to the stock data.
3. **Visualize Indicators**: Plot the indicators to understand their impact on the stock prices.
4. **Prepare Portfolio Data**: Create a portfolio from the selected stocks.
5. **Calculate Metrics**: Analyze the portfolio using financial metrics.

## Task 2: Analyst Data EDA and Analysis

### Overview

In this task, we perform EDA on analyst data, which includes headline analysis, sentiment analysis, topic modeling, time series analysis, and publisher analysis.

### Files

- **`eda_task_2.ipynb`**: The Jupyter notebook for Task 2.
- **`scripts/data_loader.py`**: Module to load analyst data.
- **`scripts/descriptive_statistics.py`**: Module for descriptive statistics.
- **`scripts/sentiment_analysis.py`**: Module for sentiment analysis.
- **`scripts/topic_modeling.py`**: Module for topic modeling.
- **`scripts/time_series_analysis.py`**: Module for time series analysis.
- **`scripts/publisher_analysis.py`**: Module for publisher analysis.

### Steps

1. **Load Analyst Data**: Import and load analyst data.
2. **Descriptive Statistics**: Analyze headline lengths and publisher article counts.
3. **Sentiment Analysis**: Perform sentiment analysis on headlines.
4. **Topic Modeling**: Identify topics within the headlines.
5. **Time Series Analysis**: Analyze publication frequency over time.
6. **Publisher Analysis**: Investigate contributions by publishers and domains.

## Task 3: Correlation Analysis Between News Sentiment and Stock Returns

### Overview

In this task, we analyze the correlation between daily sentiment from news headlines and stock returns for selected companies. The task involves aligning dates between the news and stock datasets, performing sentiment analysis, calculating daily stock returns, and analyzing correlations.

### Files

- **`task_3_eda.ipynb`**: The Jupyter notebook for Task 3.
- **`scripts/data_loader.py`**: Module to load stock and news data.
- **`scripts/calculate_daily_returns.py`**: Module to calculate daily stock returns.
- **`scripts/sentiment_analysis.py`**: Module to calculate sentiment scores.
- **`scripts/correlation_analysis.py`**: Module to perform correlation analysis.

### Steps

1. **Load Data**: Import both stock and news datasets.
2. **Calculate Daily Stock Returns**: Compute daily returns for each stock.
3. **Perform Sentiment Analysis**: Analyze the sentiment of news headlines.
4. **Merge Datasets**: Align news and stock data by date.
5. **Correlation Analysis**: Calculate the correlation between daily sentiment scores and stock returns.

## Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook
- Required Python packages listed in `requirements.txt`

### Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:achimdesa/week-1.git
   cd week-1
Install the required Python packages:
bash

pip install -r requirements.txt
Run the Jupyter notebooks:


jupyter notebook
Contributing
Feel free to contribute to this project by submitting issues or pull requests.
