import pandas as pd
import talib

def load_stock_data(file_path):
    return pd.read_csv(file_path)

# def calculate_technical_indicators(df):
#     df['SMA'] = talib.SMA(df['Close'], timeperiod=20)
#     df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
#     return df


def calculate_indicators(data):
    data['SMA_20'] = talib.SMA(data['Close'], timeperiod=20)
    data['RSI'] = talib.RSI(data['Close'], timeperiod=14)
    data['MACD'], data['MACD_signal'], data['MACD_hist'] = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    return data



def normalize_dates(news_data, stock_data):
    # Convert 'date' columns to datetime with explicit format
    news_data['date'] = pd.to_datetime(news_data['date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
    stock_data['Date'] = pd.to_datetime(stock_data['Date'], format='%Y-%m-%d', errors='coerce')
    
    # Align dates
    news_data['date'] = news_data['date'].dt.date
    stock_data['Date'] = stock_data['Date'].dt.date
    
    return news_data, stock_data

def merge_news_stock_data(news_data, stock_data):
    # Merge news and stock data on date
    merged_data = pd.merge(news_data, stock_data, left_on='date', right_on='Date', how='inner')
    return merged_data
