import pandas as pd

def headline_length_statistics(data):
    data['headline_length'] = data['headline'].apply(len)
    return data['headline_length'].describe()

def count_articles_by_publisher(data):
    return data['publisher'].value_counts()

def analyze_publication_dates(data):
    # Specify the date format
    date_format = "%Y-%m-%d %H:%M:%S"
    data['publication_date'] = pd.to_datetime(data['date'], format=date_format, errors='coerce')
    return data['publication_date'].dt.date.value_counts().sort_index()
# Example Usage:
# headline_stats = headline_length_statistics(analyst_data)
# publisher_counts = count_articles_by_publisher(analyst_data)
# publication_trends = analyze_publication_dates(analyst_data)
