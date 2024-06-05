import sqlite3

def add_track(title, artist, tempo, intensity, has_lyrics, language):
    conn = sqlite3.connect('music_recommendation.db')
    c = conn.cursor()
    c.execute('INSERT INTO tracks (title, artist, tempo, intensity, has_lyrics, language) VALUES (?, ?, ?, ?, ?, ?)',
              (title, artist, tempo, intensity, has_lyrics, language))
    conn.commit()
    conn.close()

def add_user(age, gender, preferred_tempo, preferred_intensity, preferred_lyrics, preferred_language):
    conn = sqlite3.connect('music_recommendation.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (age, gender, preferred_tempo, preferred_intensity, preferred_lyrics, preferred_language) VALUES (?, ?, ?, ?, ?, ?)',
              (age, gender, preferred_tempo, preferred_intensity, preferred_lyrics, preferred_language))
    conn.commit()
    conn.close()

# 例としてデータを追加
add_track('Song A', 'Artist 1', 120, 'high', True, 'English')
add_track('Song B', 'Artist 2', 90, 'low', False, 'Japanese')
add_user(25, 'Female', 110, 'medium', True, 'English')
