import spotipy
from spotipy.oauth2 import SpotifyOAuth
from random import sample

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='playlist-modify-public'))

emotion_to_keywords = {
    'happy': 'happy pop',
    'sad': 'sad slow',
    'angry': 'angry rock',
    'surprise': 'surprise electronic',
    'fear': 'fear dark',
    'disgust': 'disgust heavy',
    'neutral': 'neutral calm'
}

def generate_playlist(emotion):
    if emotion not in emotion_to_keywords:
        return None, "Invalid emotion"
    keywords = emotion_to_keywords[emotion]
    results = sp.search(q=keywords, type='track', limit=50)
    tracks = results['tracks']['items']
    if not tracks:
        return None, "No tracks found"
    track_uris = [track['uri'] for track in sample(tracks, min(20, len(tracks)))]
    user = sp.current_user()['id']
    playlist = sp.user_playlist_create(user, f"EmotionSync Playlist - {emotion}", public=True)
    sp.playlist_add_items(playlist['id'], track_uris)
    playlist_url = playlist['external_urls']['spotify']
    return playlist_url, None