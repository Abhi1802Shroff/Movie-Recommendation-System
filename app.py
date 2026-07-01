import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index=movies_list[movies_list.title==movie].index[0]
    distance=similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movie=[]
    recommended_movie_posters=[]
    for i in movie_list:
        movie_id=movies_list.iloc[i[0]].movie_id
        recommended_movie.append(movies_list.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie,recommended_movie_posters

similarity=pickle.load(open('similarity.pkl','rb'))

movies_list=pickle.load(open('movie.pkl','rb'))

movies=movies_list.title.values

st.title('Movie Recommender System')

selected_movie_name=st.selectbox('Select the movie of your choice',movies)

if st.button('Recommend'):
    names,poster=recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])