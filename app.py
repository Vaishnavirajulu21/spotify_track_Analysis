from flask import Flask, render_template, jsonify, request
import csv
import sqlite3
from datetime import datetime
import math

app = Flask(__name__)

# -------------------------
# DATABASE SETUP
# -------------------------
conn = sqlite3.connect('search_history.db', check_same_thread=False)
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS history")
conn.commit()

c.execute('''
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_name TEXT,
    artist TEXT,
    album TEXT,
    album_cover TEXT,
    popularity INTEGER,  
    duration REAL,
    url TEXT ,  
    search_time TEXT
)
''')
conn.commit()

# -------------------------
# HELPER FUNCTIONS
# -------------------------
def read_tracks_csv():
    tracks = []
    with open('track1.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                tracks.append({
                    'song_name': row['Track Name'],
                    'artist': row['Artist'],
                    'album': row['Album'],
                    'popularity': int(row['Popularity']),
                    'duration': round(float(row['Duration (minutes)']), 2),
                    'url':row['URL'],
                    'album_cover': row['Album Cover']
                })
            except Exception as e:
                print(f"Skipping row due to error: {e}")
    return tracks

def add_to_history(track):

    search_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Check if this track is already in history
    c.execute('''
        SELECT id FROM history 
        WHERE song_name=? AND artist=? AND album=?
    ''', (track['song_name'], track['artist'], track['album']))
    exists = c.fetchone()

    if exists:
        # Optionally, update the search_time if you want the latest search to appear first
        c.execute('''
            UPDATE history
            SET search_time=?
            WHERE id=?
        ''', (search_time, exists[0]))
    else:
        # Insert new record if not exists
        c.execute('''
            INSERT INTO history (song_name, artist, album, album_cover, popularity, duration,url,search_time)
            VALUES (?, ?, ?, ?, ?, ?, ?,?)
        ''', (
            track['song_name'],
            track['artist'],
            track['album'],
            track['album_cover'],
            int(track['popularity']),
            float(track['duration']),
            track['url'],
            search_time
        ))

    conn.commit()

    conn.commit()

def get_history_page(page=1, per_page=10):
    offset = (page - 1) * per_page
    c.execute('SELECT COUNT(*) FROM history')
    total_records = c.fetchone()[0]
    total_pages = math.ceil(total_records / per_page)

    c.execute('''
        SELECT * FROM history ORDER BY search_time DESC LIMIT ? OFFSET ?
    ''', (per_page, offset))
    rows = c.fetchall()
    history = []
    for idx, row in enumerate(rows):
        history.append({
            'sno': offset + idx + 1,
            'song_name': row[1],
            'artist': row[2],
            'album': row[3],
            'album_cover': row[4],
            'popularity': row[5],
            'duration': row[6],
            'url': row[7],
            'search_time': row[8]
        })
    return {'history': history, 'total_pages': total_pages, 'current_page': page}

# -------------------------
# ROUTES
# -------------------------
@app.route('/')
def index():
    tracks = read_tracks_csv()
    return render_template('index.html', tracks=tracks)

@app.route('/track/<song_name>')
def track_detail(song_name):
    tracks = read_tracks_csv()  # read CSV every time
    track = next((t for t in tracks if t.get('song_name', '').lower() == song_name.lower()), None)
    if track:
        # Save to history when user visits detail page
        add_to_history(track)
        return render_template('track_detail.html', track=track)
    return f"Track '{song_name}' not found", 404

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/tracks')
def tracks_api():
    tracks = read_tracks_csv()
    return jsonify(tracks)

@app.route('/save_search', methods=['POST'])
def save_search():
    track = request.json
    if track and track.get('song_name'):  # check key exists
        add_to_history(track)
        return jsonify({'status': 'success'})
    return jsonify({'status': 'failed', 'message': 'Invalid track data'}), 400

@app.route('/search_history')
def search_history_api():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    history_data = get_history_page(page, per_page)
    return jsonify(history_data)

# -------------------------
# RUN APP
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)
