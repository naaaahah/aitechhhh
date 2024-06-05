import sqlite3

def init_db():
    conn = sqlite3.connect('music_recommendation.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tracks
                 (id INTEGER PRIMARY KEY, title TEXT, artist TEXT, tempo INTEGER, intensity TEXT, has_lyrics BOOLEAN, language TEXT, URL TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, age INTEGER, gender TEXT, preferred_tempo INTEGER, preferred_intensity TEXT, preferred_lyrics BOOLEAN, preferred_language TEXT)''')
    conn.commit()
    conn.close()

init_db()
