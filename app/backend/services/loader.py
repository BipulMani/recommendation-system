import numpy as np
import pandas as pd
import joblib
import pickle
import os

def load_assets(assets_path: str = None):
    base_path = os.path.dirname(__file__)
    if assets_path is None:
        assets_path = os.path.abspath(os.path.join(base_path, "../../assets/"))

    embeddings = np.load(os.path.join(assets_path, "movie_embeddings.npy"))
    kmeans = joblib.load(os.path.join(assets_path, "kmeans_model.pkl"))
    mappings = pickle.load(open(os.path.join(assets_path, "mappings.pkl"), "rb"))
    movies_df = pd.read_csv(os.path.join(assets_path, "movies.csv"))

    return embeddings, kmeans, mappings, movies_df
