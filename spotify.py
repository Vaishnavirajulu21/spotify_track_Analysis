import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt

# Set up Spotify API credentials
 
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id = 'f9629daec6054588b6c069a221de0dc6',
    client_secret = 'c5fc68646fe94d8fb10bda9c3ad81ace'    
))

#track url

track_url = 'https://open.spotify.com/track/7qiZfU4dY1lWllzX7mPBI3'

#extract track id directly from url using regex

track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

#print(track_id)

track = sp.track(track_id)
# print(track)

#Extract Metadata

track_data  ={
    'Track Name': track['name'],
    'Artist': track['artists'][0]['name'],
    'Album': track['album']['name'],
    'Popularity': track['popularity'],
    'Duration (minutes)': track['duration_ms'] / 60000
}


print(track_data)
# metadata
print(f"\ntrack name:{track_data['Track Name']}")
print(f"Artist:{track_data['Artist']}")
print(f"Album':{track_data['Album']}")
print(f"Popularity:{track_data['Popularity']}")
print(f"Duration:{track_data['Duration (minutes)']}")


#convert metadata to dataframe
df = pd.DataFrame([track_data])
print("\nTrack Data as DataFrame:")
print(df)


#convert that into csv
df.to_csv("spotify_track_data.csv",index=False)


# Visualize track data
features = ['Popularity', 'Duration (minutes)']
values = [track_data['Popularity'], track_data['Duration (minutes)']]

plt.figure(figsize=(8, 5))
plt.bar(features, values, color='skyblue', edgecolor='black')
plt.title(f"Track Metadata for '{track_data['Track Name']}'")
plt.ylabel('Value')
plt.show()

