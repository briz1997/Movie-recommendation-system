import streamlit as st
import pickle
import joblib

st.title("Movie recommendation")
with open('movies.pickel','rb') as m:
    movies = pickle.load(m)

similarty = joblib.load("similarty.joblib")

movies__name = movies['title'].values

def recommend(name_movie):
  movie_index = movies[movies['title'] == name_movie].index[0]
  recommendation = similarty[movie_index]
  movie_list = sorted(enumerate(recommendation),reverse=True,key=lambda x:x[1])[1:6]
  
  recommend_movies = []
  for i in movie_list:
    recommend_movies.append(movies.iloc[i[0]].title)

  return recommend_movies

name_movie = st.selectbox("Select movie name",movies__name)

if st.button("Recommend"):
    r = recommend(name_movie)
    st.write("recomendation movies ")

    for i in r:
       st.write(i)

