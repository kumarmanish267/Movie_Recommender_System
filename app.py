import streamlit as st  # open source app framework
import pickle  # for serializing and de-serializing python object structures
import pandas as pd  # used to analyze data
import requests  # for requesting poster path
import typing_extensions
from annotated_text import annotated_text  # for designing
from streamlit_option_menu import option_menu
n

st.set_page_config(layout="wide")  # layout of page

# Headings and description

st.title('Movie Recommender System')

annotated_text(("Don't know which movies matches your favourite movie? Don't worry!"
                " Just feed your favourite movie here and we will recommend you the related movies.", "", "605C41"))
st.text("")
des_text = '<p style="font-size: 20px; color: White;">Get recommendations for movies like?</p>'
st.markdown(des_text, unsafe_allow_html=True)

# loading dataframes
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)  # This is our dataframe

similarity = pickle.load(open('similarity.pkl', 'rb'))  # This is our similarity dataframe

# What similarity dataframe contains?
# We have 5000 coordinates for each movie. We can visualize it as a 5000 dimensional system and
# each movie as a vector in this 5000 dimensional system.

# To measure closeness of a movie, we can either calcualte euclidean distance between two vectors
# or the angle between two vectors.

# We will not use euclidean distance because euclidean distance fails when we have high dimensions.
# So we will use cosine distance. Less the angle between two vectors,
# closer they are, and thus they will be considered similar.

# We already have a function to accomplish this task.

# cosine_similarity function calculates cosine of angle of each movie with every other movie.
# The result is stored in similarity matrix
# similarity will be a 2D matrix with number of rows and columns equal to the number of movies


# choosing the movie we want recommendation for
selected_movie_name = st.selectbox('', movies['title'].values)

# Thus function makes request to the API and fetches path of the movie poster


@st.experimental_singleton
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=4d5ad5333bb6ddac989968480b52ff26&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


# This function is for recommendation of the movie

# To obtain movie list we use enumerate function. The enumerate() method adds a counter to an iterable and
# returns it (the enumerate object). By default iterator starts from 0

# To sort the movies I used the function sorted(). It has time complexity nlog(n) [Best possible time complexity]

# Syntax of sorted() is sorted(iterable, key=None, reverse=False)

# reverse (Optional) - If True, the sorted list is reversed (or sorted in descending order).
# Defaults to False if not provided.
# key (Optional) - A function that serves as a key for the sort comparison. Defaults to None.


# By default, sorted() sorts the list in ascending order, but I want list to be sorted in descending order.
# To do this I used reverse=True

# We must note that here we are sorting pairs, as each movie has got its counter in the first place, so sorting would
# be done on the basis of counters.

# But we want to sort the movie list on the basis of cosine of angle between the movie vectors.
# To do this we use (key=lambda x:x[1])

# We use [1:26] to obtain top 25 movies
# The output contains the movies from most similar to the least similar


@st.experimental_singleton
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # Fetches index
    distances = similarity[movie_index]  # Fetches the cosine distance list of the selected movie with very other movie
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:26]
    # Gives top 25 most similar movies

    recommended_movies = []  # Empty list, names of similar movies will be appended in it
    recommended_movies_posters = []  # Empty list, names of similar movies will be appended in it
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id  # Fetches id of movie
        # fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)  # Appending in the list
        recommended_movies_posters.append(fetch_poster(movie_id))  # Appending in the list

    return recommended_movies, recommended_movies_posters


if st.button('Recommend'):  # Displaying the result
    
    names, posters = recommend(selected_movie_name)  # function recommend will take the selected movie name
    # Using layouts and containers for displaying the result

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

    cols1, cols2, cols3, cols4, cols5 = st.columns(5)

    with cols1:
        st.text(names[5])
        st.image(posters[5])

    with cols2:
        st.text(names[6])
        st.image(posters[6])

    with cols3:
        st.text(names[7])
        st.image(posters[7])

    with cols4:
        st.text(names[8])
        st.image(posters[8])

    with cols5:
        st.text(names[9])
        st.image(posters[9])

    coll1, coll2, coll3, coll4, coll5 = st.columns(5)

    with coll1:
        st.text(names[10])
        st.image(posters[10])

    with coll2:
        st.text(names[11])
        st.image(posters[11])

    with coll3:
        st.text(names[12])
        st.image(posters[12])

    with coll4:
        st.text(names[13])
        st.image(posters[13])

    with coll5:
        st.text(names[14])
        st.image(posters[14])

    coss1, coss2, coss3, coss4, coss5 = st.columns(5)

    with coss1:
        st.text(names[15])
        st.image(posters[15])

    with coss2:
        st.text(names[16])
        st.image(posters[16])

    with coss3:
        st.text(names[17])
        st.image(posters[17])

    with coss4:
        st.text(names[18])
        st.image(posters[18])

    with coss5:
        st.text(names[19])
        st.image(posters[19])

    cool1, cool2, cool3, cool4, cool5 = st.columns(5)

    with cool1:
        st.text(names[20])
        st.image(posters[20])

    with cool2:
        st.text(names[21])
        st.image(posters[21])

    with cool3:
        st.text(names[22])
        st.image(posters[22])

    with cool4:
        st.text(names[23])
        st.image(posters[23])

    with cool5:
        st.text(names[24])
        st.image(posters[24])
