from flask import Flask, request, render_template
from flaskdb.ai import recommend_track

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    age = int(request.form['age'])
    gender = request.form['gender']
    preferred_tempo = int(request.form['preferred_tempo'])
    preferred_intensity = request.form['preferred_intensity']
    preferred_lyrics = request.form['preferred_lyrics'] == 'True'
    preferred_language = request.form['preferred_language']
    recommended_track = recommend_track(age, gender, preferred_tempo, preferred_intensity, preferred_lyrics, preferred_language)
    return f"The recommended track is: {recommended_track}"

if __name__ == '__main__':
    app.run(debug=True)
