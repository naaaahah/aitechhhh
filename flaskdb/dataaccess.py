import sqlite3

def add_track(title, artist, tempo, intensity, has_lyrics, language, URL):
    conn = sqlite3.connect('music_recommendation.db')
    c = conn.cursor()
    c.execute('INSERT INTO tracks (title, artist, tempo, intensity, has_lyrics, language, URL) VALUES (?, ?, ?, ?, ?, ?, ?)',
              (title, artist, tempo, intensity, has_lyrics, language, URL))
    conn.commit()
    conn.close()

def add_user(age, gender, preferred_tempo, preferred_intensity, preferred_lyrics, preferred_language):
    conn = sqlite3.connect('music_recommendation.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (age, gender, preferred_tempo, preferred_intensity, preferred_lyrics, preferred_language) VALUES (?, ?, ?, ?, ?, ?)',
              (age, gender, preferred_tempo, preferred_intensity, preferred_lyrics, preferred_language))
    conn.commit()
    conn.close()

