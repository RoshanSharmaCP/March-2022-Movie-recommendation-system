import streamlit as st
import pickle
import pandas as pd
import numpy as np
import difflib
import requests



# fetch poster
def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e99974e75de5e11bfd9822b4aba4bd81&language=en-US'.format(movie_id))
    data=response.json()
    # print(data)
    # st.text(data)
    return 'https://image.tmdb.org/t/p/w500'+ data['poster_path']

# recommended movies
def recommend(movie):
    movie_name = movie
    list_of_all_titles= pd.DataFrame(movies_dict)['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    movies_data= movies
    close_match = find_close_match[0]
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    i = 1
    list_of_recommended_movies=[]
    recommended_movies_poster=[]

    for movie in sorted_similar_movies:
        index = movie[0]
        movie_id = movies_data.iloc[index, 4]



        title_from_index = movies_data[movies_data.index == index]['title'].values[0]
        if (i <= 5):
            list_of_recommended_movies.append(title_from_index)
            recommended_movies_poster.append(fetch_poster(movie_id))
            i += 1
    return list_of_recommended_movies,recommended_movies_poster

# changing movies dictionary to dataframe
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies =pd.DataFrame(movies_dict)
#  loading similartity scores/matrix
similarity=pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommendation system')
selected_movie_name = st.selectbox(
     'Enter a movie name.',
    movies['title'].values)

if st.button('Recommend'):
    # recommend(selected_movie_name)
    names, posters=recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

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




