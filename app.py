# streamlit app
import streamlit as st
import pickle as pk
import pandas as pd
import requests
import os

#If running locally

# from dotenv import load_dotenv
# load_dotenv()
# API_KEY = os.getenv('API_KEY')

#If deployed on Streamlit

API_KEY=st.secrets['API_KEY']

def fetch_poster(movie_id):
      url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

      headers = {
            "accept": "application/json",
             "Authorization": f"Bearer {API_KEY}"
                }

      
             
      response = requests.get(url, headers=headers)

      data=response.json()

      return "https://image.tmdb.org/t/p/original" + data['poster_path']
     
     


def recommend(movie):
     movie_index = movies[movies['title']==movie].index[0]
     distances= similarity[movie_index]
     movie_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x: x[1] )[1:6]

     recommended=[]  
     poster_list=[] 
     for i in movie_list:
         
        movie_id= movies.iloc[i[0]].id

        recommended.append(movies.iloc[i[0]].title)
        poster_list.append(fetch_poster(movie_id))
     
     return recommended,poster_list


st.title("Movie Recommender System")

movies_dict = pk.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity= pk.load(open('similarity_matrix.pkl','rb'))

option_selected = st.selectbox(
   'Select the movie for Recommendation',
    (movies.title))

st.write('You selected:', option_selected)

if st.button("Recommend"):

    recommended_list ,recommended_poster_list= recommend(option_selected)
    
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
       st.write(recommended_list[0])
       st.image(recommended_poster_list[0])

    with col2:
       st.write(recommended_list[1])
       st.image(recommended_poster_list[1])

    with col3:
       st.write(recommended_list[2])
       st.image(recommended_poster_list[2])


    with col4:
       st.write(recommended_list[3])
       st.image(recommended_poster_list[3])

    with col5:
       st.write(recommended_list[4])
       st.image(recommended_poster_list[4])

 



