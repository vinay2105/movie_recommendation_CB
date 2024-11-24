import streamlit as st
import pickle
from model import recommend
movie_df = pickle.load(open("movie_df.pkl","rb"))
movie_list = movie_df["title"].unique()

st.title("MOVIE RECOMMENDATION WEBAPP (COLLABORATIVE_FILTERING)")

option = st.selectbox("Enter movie name", movie_list)
rating = st.slider(
    "Rate this movie",
    min_value=0.00,
    max_value=5.00,
    step=0.01,
    value=0.00
)

if st.button('recommend movies'):
    recommendation = recommend(option,rating)
    for i in recommendation:
        st.write(i)


