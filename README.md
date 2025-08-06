# EmotionSync

**EmotionSync** is a real-time emotion recognition web application that uses **DeepFace** to detect your facial expression through webcam input. It then generates a custom 20-song Spotify playlist based on your mood with the help of the Spotify API.

This project is built with Python and Flask.

---

## Project Structure

| File/Folder              | Description                                      |
|--------------------------|--------------------------------------------------|
| `app.py`                 | Flask backend to run the web server              |
| `facial_analysis.py`     | Detects emotion using DeepFace and webcam        |
| `spotify_integration.py` | Creates emotion-based playlist using Spotify API |
| `templates/index.html`   | Home page with a start button                    |
| `templates/result.html`  | Result page showing detected emotion and playlist |
| `requirements.txt`       | Lists required Python packages                   |
| `README.md`              | Project documentation                            |

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/EmotionSync.git
cd EmotionSync
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Spotify Developer Setup

1. Visit [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Create an app and copy the **Client ID** and **Client Secret**
3. Set the redirect URI to:
```
http://localhost:8888/callback
```
4. In the terminal, set the environment variables:

**Windows:**
```bash
set SPOTIPY_CLIENT_ID=your_client_id
set SPOTIPY_CLIENT_SECRET=your_client_secret
set SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
```

**macOS/Linux:**
```bash
export SPOTIPY_CLIENT_ID=your_client_id
export SPOTIPY_CLIENT_SECRET=your_client_secret
export SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
```

Replace `your_client_id` and `your_client_secret` with your actual credentials.

---

## Running the Application

After configuring the environment variables, run the Flask app:

```bash
python app.py
```

Then open the following URL in your browser:

```
http://localhost:5000
```

---

## How It Works

1. The user clicks "Start Analysis" on the homepage.
2. The app activates the webcam and records video for 10 seconds.
3. DeepFace analyzes the captured frames to determine the dominant emotion.
4. The app uses the Spotify API to search for songs that match that emotion.
5. A public playlist of 20 songs is created on the user's Spotify account.
6. The playlist URL is shown on the results page.

---

## Features

- Real-time facial emotion recognition
- Automatic Spotify playlist creation based on emotion
- Webcam integration using OpenCV
- Simple and user-friendly Flask web interface
- Works with any Spotify account

---

## Requirements

- Python 3.7 or higher
- Webcam access
- Spotify Developer account

---

## Dependencies

```
deepface
opencv-python
spotipy
flask
tf-keras
```

---

## Notes

- The first time you run the app, DeepFace may take time to download the necessary models.
- If no face is detected during the 10-second capture, an error will be displayed.
- Spotify tracks may vary by region based on availability.
- You must be logged into your Spotify account when generating a playlist.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- DeepFace: https://github.com/serengil/deepface  
- Spotify API: https://developer.spotify.com/  
- Flask Framework: https://flask.palletsprojects.com/
