import matplotlib.pyplot as plt

def plot_indicators(data, stock_name):
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data['Close'], label='Close Price')
    plt.plot(data.index, data['SMA_20'], label='20-Day SMA')
    plt.plot(data.index, data['RSI'], label='RSI', color='orange')
    plt.plot(data.index, data['MACD'], label='MACD', color='purple')
    plt.plot(data.index, data['MACD_signal'], label='MACD Signal', color='red')
    plt.title(f'{stock_name} - Technical Indicators')
    plt.legend()
    plt.show()