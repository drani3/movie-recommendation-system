import pandas as pd
import numpy as np
import streamlit as st
import pickle
import requests

st.title("Movie recommender")

df = pickle.load(open('movies.pkl' , 'rb'))
movie_list = df['title']

option = st.selectbox('Movie Name' , (movie_list))


def fetch_poster(movie_id):

    request = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=79d9db440722b3d924ac9430bd0ea52f'.format(movie_id))
    data = request.json()
    return 'https://image.tmdb.org/t/p/original' + data['poster_path']

    
if st.button('Search similar movies'):
    similar_movies = df[df['title'] == option]['similar'].iloc[0]


    col1 , col2 , col3 , col4 , col5 = st.columns(5)
    with col1:
        st.markdown(similar_movies[0][0], unsafe_allow_html=True)
        st.image(fetch_poster(similar_movies[0][1]))
    with col2:
        st.markdown(similar_movies[1][0], unsafe_allow_html=True)
        st.image(fetch_poster(similar_movies[1][1]))
    with col3:
        st.markdown(similar_movies[2][0], unsafe_allow_html=True)
        st.image(fetch_poster(similar_movies[2][1]))
    with col4:
        st.markdown(similar_movies[3][0], unsafe_allow_html=True)
        st.image(fetch_poster(similar_movies[3][1]))
    with col5:
        st.markdown(similar_movies[4][0], unsafe_allow_html=True)
        st.image(fetch_poster(similar_movies[4][1]))


    





