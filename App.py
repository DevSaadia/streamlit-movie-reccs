import streamlit as st
from recommendations import recommend 
import json 
import asyncio
import pandas as pd

df = pd.read_csv('titles_and_posters.csv')
movie_list = df['title'].tolist()

st.title("Movie Recommendation System")
# st.write("Type in an exact movie name and press enter.")
# movie = st.text_input("Enter the movie name", autocomplete= "Her"

# )
movie = st.selectbox("Select a movie", movie_list)
# audio_value = st.audio_input("Record a voice message")

# if audio_value:
#     st.audio(audio_value)


if movie:
    async def get_recommendations():
        return await recommend(movie)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    recc = loop.run_until_complete(get_recommendations())
    st.write("Recommended Movies: ")
    for each in recc['recommended_movies']:
        st.write(each)



# movie_list = [
#     "The Matrix", "Inception", "The Dark Knight", "Interstellar", 
#     "The Lord of the Rings", "The Shawshank Redemption", "The Godfather",
#     "Pulp Fiction", "Forrest Gump", "The Lion King", "The Avengers"
# ]
# st.selectbox("Select a movie", movie_list)
# # User types a movie name
# user_input = st.text_input("Enter a movie name:")

# # Filter the movie list based on input
# filtered_movies = [movie for movie in movie_list if user_input.lower() in movie.lower()]

# # Suggest movies that match the input
# selected_movie = st.selectbox("",options=filtered_movies)

# st.write("You selected:", selected_movie)