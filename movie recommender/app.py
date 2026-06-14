import streamlit as st
import pickle
import pandas as pd
def recommend(movie):
    
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    
    for i in movies_list:
        st.write(movies.iloc[i[0]].title) 

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

option=st.selectbox('Which kind of movie do you want to watch?',movies['title'].values)



if st.button('Recommend'):
    recommend(option)
    st.write(option)