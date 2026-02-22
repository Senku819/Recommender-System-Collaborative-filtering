import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import os
import sys
import numpy as np
# Manual implementation of cosine similarity
def manual_cosine_similarity(matrix):
    # Matrix Dot Product (A . B)
    # We multiply the matrix by its Transpose (T)
    dot_product = np.dot(matrix, matrix.T)
    
    # Calculate Magnitude (Norm) for each user row
    # axis=1 means "across the row"
    norms = np.linalg.norm(matrix, axis=1)
    
    # Outer product of norms (NormA * NormB for every pair)
    norm_matrix = np.outer(norms, norms)
    
    # Division (A . B) / (|A| * |B|)
    # Add a tiny number (1e-9) to avoid dividing by zero errors
    similarity = dot_product / (norm_matrix + 1e-9)
    
    return similarity


# Ensure the working directory is set correctly
os.chdir(sys.path[0])   


# Load the raw CSV files
ratings = pd.read_csv(r"ml-latest-small/ratings.csv")
movies = pd.read_csv(r'ml-latest-small/movies.csv')

# Combine them so we have Movie Titles instead of just IDs
df = pd.merge(ratings, movies, on='movieId')

# Create a big table: Index (Rows) = Users, Columns = Movies
user_movie_matrix = df.pivot_table(index='userId', columns='title', values='rating')

# Fill empty spots (NaN) with 0
matrix_norm = user_movie_matrix.fillna(0)

# Calculate how similar every user is to every other user
user_similarity = manual_cosine_similarity(matrix_norm)

# Turn it into a readable table
user_sim_df = pd.DataFrame(user_similarity, index=matrix_norm.index, columns=matrix_norm.index)
def get_recommendations(target_user_id, k=10):
    # A. FIND TWINS: Get similarity scores for our target user
    sim_scores = user_sim_df[target_user_id].sort_values(ascending=False)
    
    # Pick the top 'k' most similar people (skipping index 0 because that's the user themselves)
    top_k_users = sim_scores.iloc[1:k+1]
    
    # B. GET THEIR RATINGS: Get the movie ratings from these 'k' twins
    similar_users_ratings = matrix_norm.loc[top_k_users.index]
    
    # C. PREDICT: Calculate Weighted Average
    # (Rating * Similarity Score) -> Higher similarity means their vote counts more
    weighted_ratings = similar_users_ratings.T.dot(top_k_users)
    sum_of_weights = top_k_users.sum()
    
    # Final Score formula
    predicted_ratings = weighted_ratings / sum_of_weights
    
    # D. FILTER: Remove movies the target user has already watched
    # We only want NEW recommendations
    target_user_ratings = matrix_norm.loc[target_user_id]
    already_seen = target_user_ratings[target_user_ratings > 0].index
    recommendations = predicted_ratings.drop(already_seen)
    
    # Return the top 10 highest scores
    return recommendations.sort_values(ascending=False).head(10)
# Example usage
# Get recommendations for a specific user
picked_userid = 42
#   Get top k(changable) recommendations
top_recs = get_recommendations(picked_userid, k=10)
#   Print them out
print(f"{'='*40}")
print(f"Top recommendations for User {picked_userid}:")
print(f"{'='*40}\n")

for movie, score in top_recs.items():
    print(f"{movie}: {score:.2f}")
