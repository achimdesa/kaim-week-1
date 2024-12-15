import pandas as pd
import talib
#import pynance
from pynance import PyNance
import matplotlib.pyplot as plt
import os

# Step 1: Load and Prepare the Data from CSV Files
def load_data(tickers, folder_path):
    combined_data = pd.DataFrame()
    for ticker in tickers:
        file_path = os.path.join(folder_path, f"{ticker}.csv")  
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Ticker'] = ticker  # Add ticker column for identification
        combined_data = pd.concat([combined_data, df], ignore_index=True)
    return combined_data

# Step 2: Apply TA-Lib Indicators
def apply_indicators(df):
    df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
    df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    return df

# Step 3: Calculate Financial Metrics using PyNance
def calculate_metrics(tickers):
    metrics = []
    for ticker in tickers:
        stock = PyNance(ticker)
        metrics.append({
            'Ticker': ticker,
            'P/E Ratio': stock.pe,
            'Market Cap': stock.market_cap,
            'Dividend Yield': stock.dividend_yield,
            'Revenue': stock.revenue,
            'Net Income': stock.net_income
        })
    return pd.DataFrame(metrics)

# Step 4: Visualize the Data
def plot_indicators(ticker, df):
    plt.figure(figsize=(14, 7))

    # Plot Closing Price and Moving Averages
    plt.subplot(2, 1, 1)
    plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
    plt.plot(df['Date'], df['SMA_20'], label='20-Day SMA', color='red')
    plt.plot(df['Date'], df['SMA_50'], label='50-Day SMA', color='green')
    plt.title(f'{ticker} Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()

    # Plot RSI
    plt.subplot(2, 1, 2)
    plt.plot(df['Date'], df['RSI'], label='RSI', color='purple')
    plt.axhline(70, linestyle='--', color='red')
    plt.axhline(30, linestyle='--', color='green')
    plt.title(f'{ticker} RSI')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Main function to execute the steps
def main():
    tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'MET']
    #folder_path = 'E:\EDUCATION\Kifiya_AI_Mastery_Program\W1Data\Data\yfinance_data'  
    folder_path = r'E:\EDUCATION\Kifiya_AI_Mastery_Program\W1Data\Data\yfinance_data'
    # Load and prepare data
    combined_data = load_data(tickers, folder_path)

    # Apply TA-Lib indicators
    combined_data = combined_data.groupby('Ticker').apply(apply_indicators)

    # Calculate financial metrics
    metrics_df = calculate_metrics(tickers)
    print(metrics_df)

    # Visualize data for each ticker
    for ticker in tickers:
        ticker_data = combined_data[combined_data['Ticker'] == ticker]
        plot_indicators(ticker, ticker_data)

if __name__ == "__main__":
    main()