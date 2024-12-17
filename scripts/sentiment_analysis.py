import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import ngrams
from collections import Counter

# Ensure required NLTK resources are downloaded
nltk.download('vader_lexicon')
nltk.download('punkt') 
nltk.download('stopwords')

# Load the CSV file
df = pd.read_csv('E:\\EDUCATION\\Kifiya_AI_Mastery_Program\\W1Data\\Data\\raw_analyst_ratings.csv\\dateFormatted.csv')

# Display the first few rows of the DataFrame
print("Initial Data:")
print(df.head())

# Sentiment Analysis
sia = SentimentIntensityAnalyzer()

# Function to categorize sentiment
def categorize_sentiment(score):
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis
df['sentiment_score'] = df['headline'].apply(lambda x: sia.polarity_scores(x)['compound'])
df['sentiment'] = df['sentiment_score'].apply(categorize_sentiment)

# Display the DataFrame with sentiments
print("\nSentiment Analysis Results:")
print(df[['headline', 'sentiment_score', 'sentiment']].head())

# Keyword Extraction using TF-IDF
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_features=20)
tfidf_matrix = tfidf_vectorizer.fit_transform(df['headline'])
keywords = tfidf_vectorizer.get_feature_names_out()
tfidf_array = tfidf_matrix.toarray()
keywords_scores = pd.DataFrame(tfidf_array, columns=keywords)

# Sum the scores for each keyword
total_scores = keywords_scores.sum().sort_values(ascending=False)

print("\nTop Keywords:")
print(total_scores.head(10))

# Common Phrases Extraction (Bigrams)
def extract_bigrams(headlines):
    bigrams = []
    for headline in headlines:
        tokens = nltk.word_tokenize(headline.lower())
        bigrams.extend(list(ngrams(tokens, 2)))
    return bigrams

# Extract bigrams from headlines
bigrams = extract_bigrams(df['headline'])

# Count the frequency of each bigram
bigram_freq = Counter(bigrams)

# Display the most common bigrams
common_bigrams = bigram_freq.most_common(10)
print("\nCommon Phrases (Bigrams):")
print(common_bigrams)

<<<<<<< HEAD
# Save the results to a new CSV file if needed
=======
#Save the results to a new CSV file if needed
>>>>>>> task-1
df.to_csv('E:\\EDUCATION\\Kifiya_AI_Mastery_Program\\W1Data\\Data\\raw_analyst_ratings.csv\\output_with_sentiment.csv', index=False)
print("\nResults saved to 'output_with_sentiment.csv'.")