import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

class SpotifyHandler:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv('SPOTIFY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
            redirect_uri=os.getenv('SPOTIFY_REDIRECT_URI'),
            scope='user-top-read user-library-read'
        ))

    def get_top_artists(self, limit=20):
        return self.sp.current_user_top_artists(limit=limit)

    def get_top_tracks(self, limit=20):
        return self.sp.current_user_top_tracks(limit=limit)

    def get_track_features(self, track_ids):
        return self.sp.audio_features(track_ids)

    def analyze_user_profile(self):
        # Get top tracks and their audio features
        top_tracks = self.get_top_tracks(limit=50)
        track_ids = [track['id'] for track in top_tracks['items']]
        audio_features = self.get_track_features(track_ids)

        # Calculate average energy and valence
        energy_sum = sum(feat['energy'] for feat in audio_features if feat)
        valence_sum = sum(feat['valence'] for feat in audio_features if feat)
        avg_energy = energy_sum / len(audio_features)
        avg_valence = valence_sum / len(audio_features)

        # Get dominant genres from top artists
        top_artists = self.get_top_artists(limit=20)
        genres = {}
        for artist in top_artists['items']:
            for genre in artist['genres']:
                genres[genre] = genres.get(genre, 0) + 1

        dominant_genres = sorted(genres.items(), key=lambda x: x[1], reverse=True)[:5]

        return {
            'energy': avg_energy,
            'mood': avg_valence,
            'dominant_genres': [genre[0] for genre in dominant_genres]
        }