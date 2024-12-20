import pandas as pd

def calculate_daily_returns(df):
    df['Daily Return'] = df['Close'].pct_change()
    return df

def calculate_correlation(sentiment_df, stock_df):
    correlation = sentiment_df['Sentiment'].corr(stock_df['Daily Return'])
    return correlation
