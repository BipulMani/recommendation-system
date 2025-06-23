from fastapi import APIRouter, HTTPException
from models.request_models import RecommendRequest
from services.loader import load_assets
from services.recommender import recommend
from typing import Dict

router = APIRouter()
embeddings, kmeans, mappings, movies_df = load_assets("assets/")

@router.post("/recommend")
def get_recommendations(req: RecommendRequest):
    try:
        print("Liked movies:", req.liked_movies)

        recommendations = recommend(req.liked_movies, embeddings, mappings, movies_df)

        print("Recommendations:", recommendations)

        if not recommendations:
            raise HTTPException(status_code=404, detail="No recommendations found.")

        return {"recommendations": recommendations}

    except Exception as e:
        print("Exception occurred:", str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")

