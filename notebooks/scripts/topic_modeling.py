from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pandas as pd

# Function to perform topic modeling
def perform_topic_modeling(headlines, num_topics=5, num_top_words=10):
    # Vectorize the text data (convert to document-term matrix)
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    dtm = vectorizer.fit_transform(headlines)
    
    # Perform Latent Dirichlet Allocation (LDA) to find topics
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(dtm)
    
    # Print the top words in each topic
    print("Top words per topic:")
    feature_names = vectorizer.get_feature_names_out()
    for topic_idx, topic in enumerate(lda.components_):
        print(f"\nTopic {topic_idx + 1}:")
        print(" ".join([feature_names[i] for i in topic.argsort()[:-num_top_words - 1:-1]]))
    
    return lda, vectorizer

