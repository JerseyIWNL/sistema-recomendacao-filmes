import streamlit as st
import requests
import pandas as pd

API_URL = "http://backend:8000"

st.title("Sistema de Recomendação de Filmes")

option = st.selectbox("Escolha uma funcionalidade", ["Filtrar Filmes", "Recomendações"])

if option == "Filtrar Filmes":
    genre = st.text_input("Gênero")
    limit = st.slider("Número de filmes", 1, 100, 10)
    if st.button("Buscar"):
        response = requests.get(f"{API_URL}/movies", params={"genre": genre, "limit": limit})
        st.write(pd.DataFrame(response.json()["movies"]))

if option == "Recomendações":
    user_id = st.number_input("ID do Usuário", min_value=1, step=1)
    limit = st.slider("Número de recomendações", 1, 100, 10)
    if st.button("Recomendar"):
        response = requests.get(f"{API_URL}/recommend", params={"user_id": user_id, "limit": limit})
        st.write(pd.DataFrame(response.json()["recommendations"]))
