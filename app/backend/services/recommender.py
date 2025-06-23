import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def find_movie_ids_from_titles(movies_df, titles):
    matched_ids = []
    for title in titles:
        movies_match = movies_df[movies_df["title"].str.contains(title, case=False, na=False)]
        if not movies_match.empty:
            matched_ids.append(movies_match.iloc[0]["movieId"])
    return matched_ids

def recommend(liked_titles, embeddings, mappings, movies_df):
    k = 30
    movieIdToIdx = mappings["movieIdToIdx"]
    idxToMovieId = mappings["idxToMovieId"]

    liked_ids = find_movie_ids_from_titles(movies_df, liked_titles)
    liked_ids = [int(mid) for mid in liked_ids]

    liked_indices = [movieIdToIdx[mid] for mid in liked_ids if mid in movieIdToIdx]
    if not liked_indices:
        return []

    liked_vectors = embeddings[liked_indices]
    user_profile = np.mean(liked_vectors, axis=0).reshape(1, -1)

    similarities = cosine_similarity(user_profile, embeddings)[0]
    top_indices = similarities.argsort()[-k:][::-1]

    recommended_movieIds = [idxToMovieId[i] for i in top_indices]
    recommended_titles = movies_df[movies_df["movieId"].isin(recommended_movieIds)]["title"].tolist()

    return recommended_titles
