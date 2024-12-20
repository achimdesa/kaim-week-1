import pandas as pd

def load_analyst_data(file_path='../Data/raw_analyst_ratings/raw_analyst_ratings.csv'):
    return pd.read_csv(file_path)

def load_stock_data(stock_file_path):
    return pd.read_csv(stock_file_path)

# Example Usage:
# analyst_data = load_analyst_data()
# stock_data = load_stock_data('Data/yfinance_data/AAPL_historical_data.csv')
