import os
import re
import pandas as pd
import mysql.connector
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Spotify API Authentication
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
))

# MySQL Database Connection
db_config = {
    'host': os.getenv("MYSQL_HOST"),
    'user': os.getenv("MYSQL_USER"),
    'password': os.getenv("MYSQL_PASSWORD"),
    'database': os.getenv("MYSQL_DB")
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Read track URLs from file
file_path = "track_urls.txt"
with open(file_path, 'r') as file:
    track_urls = file.readlines()

all_track = []

for track_url in track_urls:
    track_url = track_url.strip()
    try:
        track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)
        track = sp.track(track_id)

        track_data = {
            'Track Name': track['name'],
            'Artist': track['artists'][0]['name'],
            'Album': track['album']['name'],
            'Popularity': track['popularity'],
            'Duration (minutes)': track['duration_ms'] / 60000,
            'URL': track['external_urls']['spotify'],
            'Album Cover': track['album']['images'][0]['url'] if track['album']['images'] else None
        }

        all_track.append(track_data)

        insert_query = """
        INSERT INTO spotify_tracks (track_name, artist, album, popularity, duration_minutes,url,album_cover)
        VALUES (%s, %s, %s, %s, %s, %s,%s)
        """
        cursor.execute(insert_query, (
            track_data['Track Name'],
            track_data['Artist'],
            track_data['Album'],
            track_data['Popularity'],
            track_data['Duration (minutes)'],
            track_data['URL'],
            track_data['Album Cover']
            
        ))
        connection.commit()

        print(f"Inserted: {track_data['Track Name']} by {track_data['Artist']}")

    except Exception as e:
        print(f"Error processing URL: {track_url}, Error: {e}")

df = pd.DataFrame(all_track)
df.to_csv("track5.csv", index=False)
print("✅ Data saved to 'track1.csv'")


# Close the connection
cursor.close()
connection.close()

print("All tracks have been processed and inserted into the database.")
