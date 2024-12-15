
import pandas as pd
import talib
import matplotlib.pyplot as plt
import yfinance as yf

# Load stock price data from CSV files
def load_data(file_paths):
    dataframes = []
    for file_path in file_paths:
        df = pd.read_csv(file_path)
        dataframes.append(df)
    return pd.concat(dataframes, ignore_index=True)

# Apply TA-Lib indicators
def apply_ta_indicators(df):
    df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
    df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    df['MACD'], df['MACD_SIGNAL'], _ = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    return df

# Retrieve financial metrics from yfinance
def get_financials(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    return ticker.financials

# Visualize stock data and indicators
def visualize_data(df):
    plt.figure(figsize=(14, 7))
    plt.plot(df['Close'], label='Close Price', color='blue')
    plt.plot(df['SMA_20'], label='20-Day SMA', color='orange')
    plt.plot(df['SMA_50'], label='50-Day SMA', color='green')
    plt.title('Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

    plt.figure(figsize=(14, 5))
    plt.plot(df['RSI'], label='RSI', color='purple')
    plt.axhline(70, linestyle='--', alpha=0.5, color='red')
    plt.axhline(30, linestyle='--', alpha=0.5, color='green')
    plt.title('Relative Strength Index')
    plt.show()

# Main function
def main():
    # Define your CSV file paths here
    file_paths = [
        'E:\\EDUCATION\\Kifiya_AI_Mastery_Program\\W1Data\\Data\\yfinance_data\\AAPL.csv',
        'E:\\EDUCATION\\Kifiya_AI_Mastery_Program\\W1Data\\Data\\yfinance_data\\AMZN.csv',
        'E:\\EDUCATION\\Kifiya_AI_Mastery_Program\\W1Data\\Data\\yfinance_data\\GOOG.csv',
        #'path/to/stock2.csv',
        # Add more file paths as needed
    ]
    
    # Load data
    all_stocks = load_data(file_paths)

    # Ensure 'Date' column is in datetime format
    all_stocks['Date'] = pd.to_datetime(all_stocks['Date'])
    all_stocks.set_index('Date', inplace=True)

    # Apply TA-Lib indicators
    all_stocks = apply_ta_indicators(all_stocks)

    # Retrieve financial metrics
    financials = get_financials('AAPL')  # Replace with your stock ticker
    print(financials)

    # Visualize the data
    visualize_data(all_stocks)

if __name__ == "__main__":
    main()