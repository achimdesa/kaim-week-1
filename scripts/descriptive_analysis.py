import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the CSV file
df = pd.read_csv('E:\\EDUCATION\\Kifiya_AI_Mastery_Program\\W1Data\\Data\\raw_analyst_ratings.csv\\output_with_sentiment.csv')


# Convert 'publication_date' to datetime, specifying the correct format
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y', errors='coerce')

# Check for any NaT values
print("\nCheck for any invalid dates (NaT values):")
print(df[df['date'].isna()])

# Display the first few rows of the DataFrame
print("Initial Data:")
print(df.head())

# Descriptive Statistics for Textual Lengths
# Calculate the length of each headline
df['headline_length'] = df['headline'].apply(len)

# Obtain basic statistics for headline lengths
headline_length_stats = df['headline_length'].describe()
print("\nDescriptive Statistics for Headline Lengths:")
print(headline_length_stats)

# Count the number of articles per publisher
articles_per_publisher = df['publisher'].value_counts()
print("\nNumber of Articles per Publisher:")
print(articles_per_publisher)

# Analyzing Publication Dates
# Ensure 'publication_date' is in datetime format
df['date'] = pd.to_datetime(df['date'])

# Count articles per day
articles_per_day = df['date'].value_counts().sort_index()
print("\nNumber of Articles Published per Day:")
print(articles_per_day)
########
# Ensure articles_per_day is sorted by date
articles_per_day = articles_per_day.sort_index()

# Create the plot
plt.figure(figsize=(16, 6))  # Increase figure size
plt.plot(articles_per_day.index, articles_per_day.values, marker='o', linestyle='-')

# Set the title and labels
plt.title('Number of Articles Published Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Articles')

# Set major ticks to every 2 weeks or use MonthLocator
plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))  
# Format the x-axis labels
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Manually set ticks every 14 days
plt.xticks(articles_per_day.index[::14], rotation=45) 

# Automatically format the x-axis date labels
plt.gcf().autofmt_xdate()

# Add a grid for better readability
plt.grid()

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
'''
plt.figure(figsize=(12, 6))
plt.plot(articles_per_day.index, articles_per_day.values, marker='o', linestyle='-')
plt.title('Number of Articles Published Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45)

# Set x-axis major locator and formatter
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Set locator to major ticks every day
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Format for the date

plt.tight_layout()
plt.grid()
plt.show()
'''
'''
# Make sure to sort the articles_per_day by date
articles_per_day = articles_per_day.sort_index()

plt.figure(figsize=(12, 6))
plt.plot_date(articles_per_day.index, articles_per_day.values, marker='o', linestyle='-')
plt.title('Number of Articles Published Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid()
plt.show()
'''