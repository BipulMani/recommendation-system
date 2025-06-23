from pydantic import BaseModel
from typing import List

class RecommendRequest(BaseModel):
    liked_movies: List[str]