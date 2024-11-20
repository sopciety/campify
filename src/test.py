import spotipy
from spotipy.oauth2 import SpotifyOAuth


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="3ec42338a5c64f6b9cb100f6adea9d3d",
                                               client_secret="00937c5117aa4a718dbae89085ae7506",
                                               redirect_uri="http://localhost:5000/callback",
                                               scope="user-library-read"))


results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])