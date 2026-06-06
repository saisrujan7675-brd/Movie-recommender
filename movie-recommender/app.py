import streamlit as st
from model import recommend
import pandas as pd

movies = pd.read_csv("movies.csv")

st.title("🎬 Movie Recommendation System")

movie = st.selectbox(
    "Choose a Movie",
    movies["title"].tolist()
)

if st.button("Recommend"):
    results = recommend(movie)

    st.subheader("Recommended Movies")

    for r in results:
        st.write("👉", r)