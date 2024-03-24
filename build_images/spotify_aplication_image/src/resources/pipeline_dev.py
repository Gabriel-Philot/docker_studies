from spotifyapi import SpotifyAPI, client_id, client_secret
from process import transform_json_top10, transform_types
from postgress import PostgresDb, user_postegress, pass_postegress, host_postegress, db_postegress

# USED FOR TESTING OUT API + DEV DB INTEGRATION

def main_pipe(artist_name, country):
    spotifyApi = SpotifyAPI(client_id, client_secret)
    artist = spotifyApi.search_for_artist(artist_name)
    if artist:
        songs = spotifyApi.get_songs_by_artist(artist['id'], country)
        
        top10 = transform_json_top10(artist, songs)
        top10_df = transform_types(top10)

        return top10_df
    else:
        print(f"No artist found with name {artist_name}")


def postgress_pipe(df, table):
    db = PostgresDb(host_postegress, db_postegress, user_postegress, pass_postegress)
    db.connect()
    db.create_update_table(df, table)

    return "Data persisted to Postgres table successfully."

def query_data(query):
    db = PostgresDb(host_postegress, db_postegress, user_postegress, pass_postegress)
    db.connect()
    return db.run_query(query)



if __name__ == '__main__':

    arstist_name = 'Gojira'
    country = 'BR'
    
    df = main_pipe(arstist_name, country)

    table = "persist_artist_top10_data"

    db = PostgresDb(host_postegress, db_postegress, user_postegress, pass_postegress)
    db.connect()
    db.create_update_table(df, table)
    
    







