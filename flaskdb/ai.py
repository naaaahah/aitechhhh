from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import sqlite3

# データベースからデータを読み込む
conn = sqlite3.connect('music_recommendation.db')
tracks_df = pd.read_sql_query("SELECT * FROM tracks", conn)
users_df = pd.read_sql_query("SELECT * FROM users", conn)
conn.close()

# データの前処理
def preprocess_data(tracks_df, users_df):
    # カテゴリカルデータのエンコーディング
    tracks_df = pd.get_dummies(tracks_df, columns=['intensity', 'language'])
    users_df = pd.get_dummies(users_df, columns=['preferred_intensity', 'preferred_language'])
    
    # ユーザーデータと曲データを結合
    combined_df = users_df.merge(tracks_df, how='cross')
    
    return combined_df

combined_df = preprocess_data(tracks_df, users_df)

# 特徴量とターゲットに分ける
X = combined_df[['age', 'preferred_tempo', 'preferred_lyrics', 'preferred_intensity_high', 'preferred_intensity_low', 'preferred_intensity_medium', 'preferred_language_English', 'preferred_language_Japanese','preferred_language_Korean', 'tempo', 'has_lyrics', 'intensity_high', 'intensity_low', 'intensity_medium', 'language_English', 'language_Japanese', 'language_Korean']]
y = combined_df['title']

# 決定木モデルを訓練
model = DecisionTreeClassifier()
model.fit(X, y)

# 新しいユーザーの推薦を行う関数
def recommend_track(age, gender, preferred_tempo, preferred_intensity, preferred_lyrics, preferred_language):
    input_data = {
        'age': [age],
        'preferred_tempo': [preferred_tempo],
        'preferred_lyrics': [preferred_lyrics],
        'preferred_intensity_high': [1 if preferred_intensity == 'High' else 0],
        'preferred_intensity_low': [1 if preferred_intensity == 'Low' else 0],
        'preferred_intensity_medium': [1 if preferred_intensity == 'Mid' else 0],
        'preferred_language_English': [1 if preferred_language == 'English' else 0],
        'preferred_language_Japanese': [1 if preferred_language == 'Japanese' else 0],
        'preferred_language_Korean': [1 if preferred_language == 'Korean' else 0],
        'tempo': [preferred_tempo],
        'has_lyrics': [preferred_lyrics],
        'intensity_high': [1 if preferred_intensity == 'High' else 0],
        'intensity_low': [1 if preferred_intensity == 'Low' else 0],
        'intensity_medium': [1 if preferred_intensity == 'Mid' else 0],
        'language_English': [1 if preferred_language == 'English' else 0],
        'language_Japanese': [1 if preferred_language == 'Japanese' else 0],
        'language_Korean': [1 if preferred_language == 'Korean' else 0]
    }
    input_df = pd.DataFrame(input_data)
    prediction = model.predict(input_df)
    return prediction[0]

# 例として推薦を実行
print(recommend_track(25, 'Female', 110, 'medium', True, 'English'))
