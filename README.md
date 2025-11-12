<project>
  <header>
    <title>🎧 Spotilytics – Spotify Data Analytics Dashboard</title>
    <badges>
      <badge>![Python](https://img.shields.io/badge/Python-3.9-blue)</badge>
      <badge>![Flask](https://img.shields.io/badge/Flask-Framework-green)</badge>
      <badge>![MySQL](https://img.shields.io/badge/MySQL-Database-orange)</badge>
      <badge>![SpotifyAPI](https://img.shields.io/badge/Spotify-API-brightgreen)</badge>
      <badge>![Render](https://img.shields.io/badge/Deployed%20on-Render-purple)</badge>
    </badges>
  </header>

  <section id="overview">
    <title>📊 Overview</title>
    <p>
      Spotilytics is an interactive <strong>Spotify Data Analytics Dashboard</strong> built using 
      Flask, MySQL, and the Spotify API. It allows users to fetch track data such as
      <em>Track Name, Artist, Album, Popularity, Duration</em>, and <em>Album Cover</em>.
      The data is stored securely in a MySQL database and visualized through a dashboard 
      for trend analysis and insights.
    </p>
  </section>

  <section id="features">
    <title>✨ Features</title>
    <list>
      <item>🎵 Fetch real-time Spotify track data via Spotify API</item>
      <item>💾 Store all data securely in a MySQL database</item>
      <item>📈 Analyze track popularity and artist trends</item>
      <item>🖼️ Save album covers and track metadata</item>
      <item>☁️ Hosted on Render with auto-deployment</item>
    </list>
  </section>

  <section id="tech-stack">
    <title>🧩 Tech Stack</title>
    <list>
      <item><strong>Backend:</strong> Flask (Python)</item>
      <item><strong>Database:</strong> MySQL</item>
      <item><strong>API:</strong> Spotify Web API via Spotipy</item>
      <item><strong>Frontend:</strong> HTML, CSS, js</item>
      <item><strong>Deployment:</strong> Render Cloud</item>
    </list>
  </section>

  <section id="installation">
    <title>⚙️ Installation</title>
    <steps>
      <step>1️⃣ Clone the repository:
        <code>git clone https://github.com/Vaishnavirajulu21/spotify_track_Analysis.git</code>
      </step>
      <step>2️⃣ Create and activate virtual environment:
        <code>python -m venv env && env\Scripts\activate</code>
      </step>
      <step>3️⃣ Install dependencies:
        <code>pip install -r requirements.txt</code>
      </step>
      <step>4️⃣ Create a <strong>.env</strong> file and add:
        <code>
          SPOTIFY_CLIENT_ID=your_client_id<br/>
          SPOTIFY_CLIENT_SECRET=your_client_secret<br/>
          MYSQL_HOST=localhost<br/>
          MYSQL_USER=root<br/>
          MYSQL_PASSWORD=your_password<br/>
          MYSQL_DB=spotify_db
        </code>
      </step>
      <step>5️⃣ Run the Flask app:
        <code>python app.py</code>
      </step>
    </steps>
  </section>

  <section id="database">
    <title>🗄️ Database Schema</title>
    <table>
      <tr><th>Column</th><th>Type</th><th>Description</th></tr>
      <tr><td>id</td><td>INT</td><td>Primary key (auto-increment)</td></tr>
      <tr><td>track_name</td><td>VARCHAR(255)</td><td>Track title</td></tr>
      <tr><td>artist</td><td>VARCHAR(255)</td><td>Artist name</td></tr>
      <tr><td>album</td><td>VARCHAR(255)</td><td>Album name</td></tr>
      <tr><td>popularity</td><td>INT</td><td>Popularity score</td></tr>
      <tr><td>duration_minutes</td><td>FLOAT</td><td>Track length in minutes</td></tr>
      <tr><td>album_cover</td><td>VARCHAR(255)</td><td>Album image URL</td></tr>
      <tr><td>url</td><td>VARCHAR(255)</td><td>Spotify track URL</td></tr>
    </table>
  </section>

  <section id="deployment">
    <title>🚀 Deployment</title>
    <p>
      This project is deployed on <strong>Render</strong>.<br/>
      To deploy your own version:
    </p>
    <steps>
      <step>1️⃣ Connect your GitHub repository to Render.</step>
      <step>2️⃣ Add environment variables from your local <code>.env</code> file in Render’s dashboard.</step>
      <step>3️⃣ Add <code>gunicorn</code> to <code>requirements.txt</code>.</step>
      <step>4️⃣ Set the start command as:
        <code>gunicorn app:app</code>
      </step>
    </steps>
  </section>

  <section id="preview">
    <title>🌐 Live Preview</title>
    <p>
      🔗 <a href="https://your-render-app-url.onrender.com">Live Dashboard on Render</a>
    </p>
  </section>

  <section id="conclusion">
    <title>💬 Conclusion</title>
    <p>
      Spotilytics simplifies the process of gathering, storing, and analyzing Spotify data.
      With the power of Flask, MySQL, and Render, it provides a seamless platform for
      understanding track trends and musical insights 🎶.
    </p>
  </section>
</project>

