import pandas as pd
import matplotlib.pyplot as plt
#from statsmodels.tsa.seasonal import seasonal_decompose
#from statsmodels.tsa.stattools import adfuller

# Load the data
data = pd.read_csv('E:\\EDUCATION\\Kifiya_AI_Mastery_Program\\W1Data\\Data\\raw_analyst_ratings.csv\\output_with_sentiment.csv')

# Parse dates with dayfirst parameter
data['date'] = pd.to_datetime(data['date'], dayfirst=True)

# Set date as index
data.set_index('date', inplace=True)

# Visualize the data
plt.figure(figsize=(12, 6))
plt.plot(data['sentiment_score'], label='Sentiment Score')  # Use the appropriate column
plt.title('Financial News Sentiment Over Time')
plt.xlabel('Date')
plt.ylabel('Sentiment Score')
plt.grid()
plt.legend()
plt.savefig('../financial_news_sentiment.png')  # Save the plot as a PNG file
plt.show()

# Descriptive statistics
stats = data.describe()
print(stats)
stats.to_csv('../descriptive_statistics.csv')  # Save statistics to CSV
'''
# Check for missing values
missing_values = data.isnull().sum()
print(missing_values)

# Decompose the time series
decomposition = seasonal_decompose(data['sentiment_score'], model='additive')  # Use the appropriate column
plt.figure(figsize=(12, 8))
decomposition.plot()
plt.savefig('time_series_decomposition.png')  # Save decomposition plot
plt.show()

# Correlation analysis
correlation_matrix = data.corr()
print(correlation_matrix)
correlation_matrix.to_csv('correlation_matrix5.csv')  # Save correlation matrix to CSV

# Stationarity check
result = adfuller(data['sentiment_score'])  # Use the appropriate column
print('ADF Statistic:', result[0])
print('p-value:', result[1])

# Save findings to a text file
with open('findings5.txt', 'w') as f:
    f.write('ADF Statistic: {}\n'.format(result[0]))
    f.write('p-value: {}\n'.format(result[1]))
    f.write('\nDescriptive Statistics:\n')
    f.write(stats.to_string())
    f.write('\n\nCorrelation Matrix:\n')
    f.write(correlation_matrix.to_string())
    '''