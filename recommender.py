import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("assessments.csv")

# Combine text fields
assessment_texts = (
    df['name'] + " " +
    df['description'] + " " +
    df['test_type']
).tolist()

# Create TF-IDF vectors
vectorizer = TfidfVectorizer()

assessment_vectors = vectorizer.fit_transform(assessment_texts)

# Recommendation function
def recommend_assessments(query, top_k=5):

    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        assessment_vectors
    )[0]

    top_indices = similarities.argsort()[::-1][:top_k]

    results = []

    for idx in top_indices:

        row = df.iloc[idx]

        results.append({
            "name": row['name'],
            "url": row['url'],
            "remote_support": row['remote_support'],
            "adaptive_support": row['adaptive_support'],
            "duration": row['duration'],
            "test_type": row['test_type'],
            "score": float(similarities[idx])
        })

    return results