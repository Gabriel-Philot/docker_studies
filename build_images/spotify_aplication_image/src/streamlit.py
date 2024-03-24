import streamlit as st
from main import main_pipe, postgress_pipe, query_data

# Global variable (this one for this use wil be fixed)

table = "persist_top10_data"

st.title("Spotify TOP 10 Artist Songs 🎶")


artist_name = st.text_input("Write the name of an artist of your choice:")
country = st.selectbox("Select a country:",["BR","US","GB"])

if artist_name:
    if st.button("Seach 10 TOP Songs"):
        df = main_pipe(artist_name, country)
        st.write(df)
        st.write("### Data wil be persisted PostgreSQL DB")

        st.write("⚡ OBS: Data wil be persisted with Update/Insert method to avoid duplicates")
        message = postgress_pipe(df, table)
        html = "<span style='color:green'>{}</span>".format(message)
        st.write(html, unsafe_allow_html=True)

    
        st.title("All the data from the DB")
        query = "SELECT * FROM persist_top10_data"
        df = query_data(query)
        num_rows = df.shape[0]
        st.write(f"Number of rows in database table: {num_rows}")
        st.write(df)


else :
  st.write("")


sql_query = st.text_input("Enter SQL query to retrieve data from the table: *persist_top10_data*")
        
query_exemple = "select name_artist, top10_rank, song_name, album_name FROM persist_top10_data WHERE album_name = 'Roots'"
st.write(f"Query exemple:")
st.write(query_exemple)
if sql_query:
  df = query_data(sql_query)
  st.write(df)

