import os
from dotenv import load_dotenv
import base64
from requests import post, get
import json
import re

load_dotenv()

# app.secret_key = '543de345-512a-4a6b-b9b6-12f50b29d491'


client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# BASE URLS
TOKEN_BASE_URL = 'https://accounts.spotify.com/api/token'
ARTIST_BASE_URL = 'https://api.spotify.com/v1/search?'
TOP_SONGS_BASE_URL = 'https://api.spotify.com/v1/artists'


class SpotifyAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None

    def get_token(self):
        auth_string = f"{self.client_id}:{self.client_secret}"
        au_bytes = auth_string.encode('utf-8')
        auth_base64 = str(base64.b64encode(au_bytes), 'utf-8')

        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}
        result = post(TOKEN_BASE_URL, headers=headers, data=data)
        json_result = json.loads(result.content)
        self.token = json_result["access_token"]
        return self.token

    def get_aut_header(self):
        if not self.token:
            self.get_token()
        return {"Authorization": "Bearer " + self.token}

    def search_for_artist(self, artistname):
        headers = self.get_aut_header()
        query = f"q={artistname}&type=artist&tlimit=1"
        
        query_url = ARTIST_BASE_URL + query
        result = get(query_url, headers=headers)
        json_result = json.loads(result.content)['artists']['items']

        if len(json_result) == 0:
            print("No artist with this name exists...")
            return None
        return json_result[0]

    def get_songs_by_artist(self, artist_id, country):
        url = f"{TOP_SONGS_BASE_URL}/{artist_id}/top-tracks?country={country}"
        headers = self.get_aut_header()
        result = get(url, headers=headers)
        json_result = json.loads(result.content)['tracks']
        return json_result
    


# Exemplo de uso:
# spotify_api = SpotifyAPI(client_id, client_secret)
# artist = spotify_api.search_for_artist("Metallica")
# print(artist['name'])
# if artist:
#     artist_id = artist['id']
#     songs = spotify_api.get_songs_by_artist(artist_id, "US")
    
# for idx, song in enumerate(songs):
#     print(f"{idx + 1}. {song['name']}. {song['album']['release_date']}")


# def processing_json_top10(artist, json_result):
#     artist_name = artist['name']
#     artist_id = artist['id']

#     top10_data = []
#     for i, item in enumerate(json_result):
#         song_name = re.sub(r'\b(Remaster(ed)?|\(Remaster(ed)?\)|Deluxe.*|\(Deluxe.*\)|Box Set|\(Box Set\))\b', '', item['name'], flags=re.IGNORECASE)
#         album_name = re.sub(r'\b(Remaster(ed)?|\(Remaster(ed)?\)|Deluxe.*|\(Deluxe.*\)|Box Set|\(Box Set\))\b', '', item['album']['name'], flags=re.IGNORECASE)
#         release_date = item['album']['release_date']
#         top10_rank = i + 1  # Assume que a contagem começa do 1
    
#         # Remover parênteses restantes após a substituição
#         song_name = song_name.replace("(", "").replace(")", "")
#         album_name = album_name.replace("(", "").replace(")", "")

#         song_data = {
#             'id': artist_id,
#             'name_artist': artist_name,
#             'top10_rank': top10_rank,
#             'song_name': song_name.strip(),
#             'album_name': album_name.strip(),
#             'release_date': release_date
#         }

#         top10_data.append(song_data)

#     return top10_data

# print(processing_json_top10(artist, songs))

        
    





# token2 = get_token()
# # print(token)

# print("\n")
# musico ="Megadeth"

# result = search_for_artist(token2, musico)
# print(result['name'])
# aritst_id = result['id']
# songs = get_songs_by_artitst(token2, aritst_id, "BR")
# print(songs)


# for idx, song in enumerate(songs):
#     print(f"{idx + 1}. {song['name']}. {song['album']['release_date']}")

# teste_request(base_url, token2)