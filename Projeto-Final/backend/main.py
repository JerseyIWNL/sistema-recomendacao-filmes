from fastapi import FastAPI, Query
from backend.db import get_connection

app = FastAPI()

@app.get("/movies")
def list_movies(genre: str = Query(None), limit: int = 10):
    """
    Lista filmes por gênero.
    """
    conn = get_connection()
    query = "SELECT movieId, title, genres FROM movies"
    filters = []
    if genre:
        filters.append(f"genres LIKE '%{genre}%'")
    if filters:
        query += " WHERE " + " AND ".join(filters)
    query += f" LIMIT {limit}"
    result = conn.execute(query).fetchall()
    return {"movies": [dict(row) for row in result]}

@app.get("/recommend")
def recommend_movies(user_id: int, limit: int = 10):
    """
    Retorna filmes recomendados para um usuário.
    """
    conn = get_connection()
    query = f"""
        SELECT m.movieId, m.title, AVG(r.rating) as avg_rating
        FROM ratings r
        JOIN movies m ON r.movieId = m.movieId
        WHERE r.userId = {user_id}
        GROUP BY m.movieId
        ORDER BY avg_rating DESC
        LIMIT {limit};
    """
    result = conn.execute(query).fetchall()
    return {"recommendations": [dict(row) for row in result]}
