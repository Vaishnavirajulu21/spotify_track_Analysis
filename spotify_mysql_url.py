import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import mysql.connector
import pandas as pd


# Set up Spotify API credentials
 
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id = 'f9629daec6054588b6c069a221de0dc6',
    client_secret = 'c5fc68646fe94d8fb10bda9c3ad81ace'    
))




# MySQL Database Connection
db_config = {
    'host': 'localhost',           # Change to your MySQL host
    'user': 'root',       # Replace with your MySQL username
    'password': 'Vaishu@28',   # Replace with your MySQL password
    'database': 'spotify_db'       # Replace with your database name
}

# Connect to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Read track URLs from file
file_path = "track_urls.txt"
with open(file_path, 'r') as file:
    track_urls = file.readlines()

all_track = []
# Process each URL
for track_url in track_urls:
    track_url = track_url.strip()  # Remove whitespace
    try:
        # Extract track ID from URL
        track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

        # Fetch track details from Spotify API
        track = sp.track(track_id)

        # Extract metadata
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

        # Insert data into MySQL
        insert_query = """
        INSERT INTO spotify_tracks (track_name, artist, album, popularity, duration_minutes, album_cover,url)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
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
        
        print(track['album']['images'])

    except Exception as e:
        print(f"Error processing URL: {track_url}, Error: {e}")

# Save to CSV
df = pd.DataFrame(all_track)
df.to_csv("track1.csv", index=False)
print("✅ Data saved to 'spotify_track_data3.csv'")



# Close the connection
cursor.close()
connection.close()

print("All tracks have been processed and inserted into the database.")
