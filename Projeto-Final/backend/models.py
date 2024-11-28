from pydantic import BaseModel
from typing import List, Optional

class Movie(BaseModel):
    """
    Representa um filme com informações básicas.
    """
    movieId: int
    title: str
    genres: str

class Recommendation(BaseModel):
    """
    Representa uma recomendação de filme para um usuário.
    """
    movieId: int
    title: str
    avg_rating: float

class MoviesResponse(BaseModel):
    """
    Representa a resposta ao listar filmes.
    """
    movies: List[Movie]

class RecommendationsResponse(BaseModel):
    """
    Representa a resposta ao listar recomendações de filmes.
    """
    recommendations: List[Recommendation]
