import pandas as pd
import streamlit as st
import pickle
import requests
import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load API key from secrets
API_KEY = st.secrets["tmdb_api_key"]


@st.cache_data
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

        response = requests.get(url)
        data = response.json()

        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

    except:
        return "https://via.placeholder.com/500x750?text=Poster+Not+Available"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)

        recommended_movies_posters.append(fetch_poster(movie_id))

        time.sleep(0.3)

    return recommended_movies, recommended_movies_posters


# Load Data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

cv = CountVectorizer(max_features=5000, stop_words='english')

vectors = cv.fit_transform(movies['tags']).toarray()

similarity = cosine_similarity(vectors)

# UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Movie Name?",
    movies['title'].values
)

if st.button('Recommend'):

    names, posters = recommend(selected_movie_name)

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