from flask import Flask, render_template
from facial_analysis import analyze_emotion_from_webcam
from spotify_integration import generate_playlist

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    emotion, error = analyze_emotion_from_webcam()
    if error:
        return render_template('result.html', error=error)
    playlist_url, error = generate_playlist(emotion)
    if error:
        return render_template('result.html', error=error)
    return render_template('result.html', emotion=emotion, playlist_url=playlist_url)

if __name__ == '__main__':
    app.run(debug=True)