import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=9c71d8c7ddf4f47ba73f1828d14cbaaa&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']
def reccommed(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=(lambda x: x[1]))[1:6]
    reccommened_movies=[]
    reccommened_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id
        #fetch poster from KPI

        reccommened_movies.append(movies.iloc[i[0]].title)
        reccommened_movies_poster.append(fetch_poster(movie_id))
    return reccommened_movies,reccommened_movies_poster

st.title('Movie Recommended System')
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))


selected_movies = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

if st.button('Recommend'):
    names,posters=reccommed(selected_movies)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])


# st.write('You selected:', option)