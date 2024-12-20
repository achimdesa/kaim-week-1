import pandas as pd

def analyze_publication_frequency(data):
    date_format = "%Y-%m-%d %H:%M:%S"
    data['publication_date'] = pd.to_datetime(data['date'], format=date_format, errors='coerce')
    return data.groupby(data['publication_date'].dt.date).size()

# Example Usage:
# publication_freq = analyze_publication_frequency(analyst_data)

