import pandas as pd

def calculate_daily_returns(df):
    if isinstance(df, pd.DataFrame):
        if 'Close' in df.columns:
            df['daily_return'] = df['Close'].pct_change()
            return df
        else:
            print("Column 'Close' not found in DataFrame.")
    elif isinstance(df, pd.Series):
        return df.pct_change()  # Handle Series directly
    else:
        raise TypeError("Input must be a DataFrame or Series.")

def calculate_correlation(daily_sentiment, stock_data):
    # Merge sentiment and stock data on date
    merged_data = pd.merge(daily_sentiment, stock_data[['Date', 'daily_return']], left_on='date', right_on='Date')
    
    # Calculate correlation
    correlation = merged_data['sentiment'].corr(merged_data['daily_return'])
    return correlation

