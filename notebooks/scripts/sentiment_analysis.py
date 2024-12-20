import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download('vader_lexicon')

def perform_sentiment_analysis(headlines):
    analyzer = SentimentIntensityAnalyzer()
    sentiments = []
    for headline in headlines:
        sentiment_score = analyzer.polarity_scores(headline)
        sentiments.append({
            'headline': headline,
            'sentiment': sentiment_score['compound'],  # Overall sentiment score
            'positive': sentiment_score['pos'],
            'neutral': sentiment_score['neu'],
            'negative': sentiment_score['neg']
        })
    return pd.DataFrame(sentiments)
def perform_sentiment_analysis2(headlines):
    sia = SentimentIntensityAnalyzer()
    sentiments = headlines.apply(lambda x: sia.polarity_scores(x)['compound'])
    return sentiments

def aggregate_daily_sentiment(news_data):
    # Aggregate sentiment by date
    daily_sentiment = news_data.groupby('date')['sentiment'].mean().reset_index()
    return daily_sentiment