from flask import Flask, redirect, request, session, url_for
from .spotify_handler import SpotifyHandler

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key

@app.route('/')
def index():
    return '''
        <h1>Welcome to Campify!</h1>
        <a href="/login">Login with Spotify</a>
    '''

@app.route('/login')
def login():
    spotify_handler = SpotifyHandler()
    return redirect(spotify_handler.sp.auth_manager.get_authorize_url())

@app.route('/callback')
def callback():
    try:
        spotify_handler = SpotifyHandler()
        code = request.args.get('code')
        if not code:
            return "Error: No code provided", 400
            
        session['token_info'] = spotify_handler.sp.auth_manager.get_access_token(code)
        return redirect(url_for('profile'))
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/profile')
def profile():
    spotify_handler = SpotifyHandler()
    try:
        user_profile = spotify_handler.analyze_user_profile()
        
        # Convert the profile data into HTML with some basic styling
        html = f'''
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
                    .profile-card {{ background: #f5f5f5; padding: 20px; border-radius: 8px; }}
                    .meter {{ background: #e0e0e0; height: 20px; border-radius: 10px; overflow: hidden; }}
                    .meter-fill {{ background: #1DB954; height: 100%; }}
                </style>
            </head>
            <body>
                <h1>Your Campify Profile</h1>
                <div class="profile-card">
                    <h2>Music Energy Level</h2>
                    <div class="meter">
                        <div class="meter-fill" style="width: {user_profile['energy'] * 100}%"></div>
                    </div>
                    <p>{user_profile['energy'] * 100:.1f}%</p>
                    
                    <h2>Music Mood</h2>
                    <div class="meter">
                        <div class="meter-fill" style="width: {user_profile['mood'] * 100}%"></div>
                    </div>
                    <p>{user_profile['mood'] * 100:.1f}%</p>
                    
                    <h2>Your Top Genres</h2>
                    <ul>
                        {''.join(f'<li>{genre}</li>' for genre in user_profile['dominant_genres'])}
                    </ul>
                </div>
                
                <div style="margin-top: 20px;">
                    <a href="/generate-campsite">Generate Your Campsite →</a>
                </div>
            </body>
            </html>
        '''
        return html
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)