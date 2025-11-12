# 🎧 Spotilytics – Spotify Data Analytics Dashboard  

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey?logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?logo=mysql)
![Spotify API](https://img.shields.io/badge/Spotify-API-green?logo=spotify)
![Render](https://img.shields.io/badge/Deployed%20on-Render-blueviolet?logo=render)

---

## 🌐 Live Demo  
🚀 **View Live:** [Spotify Track Analysis Dashboard](https://spotify-track-analysis-1.onrender.com/)  

> Analyze, visualize, and explore your favorite Spotify tracks in real time!

---

## 🧠 Overview  
**Spotilytics** is an interactive **Spotify Data Analysis Dashboard** built using **Flask**, **MySQL**, and **Chart.js**.  
It connects with the **Spotify API** to fetch live track data, store it in a MySQL database, and visualize it through a modern, interactive dashboard.

🎯 **Core Functions:**
- Fetch Spotify track data (name, artist, album, popularity, duration)
- Store details securely in **MySQL**
- Track user searches using **SQLite**
- Visualize trends and insights with **Chart.js**

---

## ⚙️ Tech Stack  

| Component | Technology |
|------------|-------------|
| **Frontend** | HTML, CSS, Bootstrap, Chart.js |
| **Backend** | Flask (Python) |
| **Database** | MySQL + SQLite |
| **API** | Spotify Web API |
| **Deployment** | Render |

---

## 🚀 Features  

- 🎵 **Spotify Integration** – Fetch real-time data using Spotify’s Web API  
- 💾 **MySQL Storage** – Store song metadata (artist, album, duration, popularity)  
- 📊 **Interactive Dashboard** – Visualize your data dynamically using Chart.js  
- 🕒 **Track History** – Maintain a search history of queried tracks  
- 🌐 **Deployed Live** – Hosted on Render for global access  

---

## 🛠️ Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Vaishnavirajulu21/spotify_track_Analysis.git
cd spotify_track_Analysis
```

### 2️⃣ Create and Activate Virtual Environment  
```bash
python -m venv env
env\Scripts\activate   # (Windows)
```

### 3️⃣ Install Required Packages  
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables  
Create a `.env` file in the root directory:
```
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=spotify_db
```

### 5️⃣ Run the Application  
```bash
python app.py
```

Then open the browser and visit 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📊 Dashboard Preview  

Your dashboard includes powerful visualizations such as:
- 🎶 Top Tracks by Popularity  
- 📈 Average Duration per Artist  
- 🎤 Most Searched Artists  

🔗 **Live App:** [https://spotify-track-analysis-1.onrender.com/](https://spotify-track-analysis-1.onrender.com/)

---

## 🌍 Deployment on Render  

1. Add **gunicorn** to your `requirements.txt`  
2. Set **Start Command** in Render:
   ```
   gunicorn app:app
   ```
3. Add Environment Variables in Render Dashboard:
   ```
   SPOTIFY_CLIENT_ID=your_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
   MYSQL_HOST=your_host
   MYSQL_USER=your_user
   MYSQL_PASSWORD=your_password
   MYSQL_DB=spotify_db
   ```
4. Deploy and enjoy your live Spotify analytics dashboard 🎉  

---

## 🧰 Dependencies  

- Flask  
- spotipy  
- mysql-connector-python  
- pandas  
- python-dotenv  
- gunicorn  
 

---

## ⚡ System Flow  

```
[Spotify API] → Fetch Track Data
        ↓
 [Flask Backend] → Process and Transform Data
        ↓
 [MySQL Database] → Store Track Details
        ↓
 [Frontend] → Visualize Insights
```

---

## 👩‍💻 Author  

**💻Vaishnavi Varatharajulu**  
🎓 Biomedical Engineer | 💻 Data Analyst | 🤖 Python Developer

🌱 Passionate about Data Analytics, Machine Learning, and Intelligent Applications.

🌐 GitHub
