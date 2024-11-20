from flask import Flask, redirect, request, session, url_for
from spotify_handler import SpotifyHandler
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key

@app.route('/')
def index():
    return '''
        <h1>Welcome to Campify!</h1>
        <a href="/login">Login with Spotify</a>
    '''

@app.route('/login')
def login():
    try:
        spotify_handler = SpotifyHandler()
        auth_url = spotify_handler.sp.auth_manager.get_authorize_url()
        print(f"Generated auth URL: {auth_url}")  # Debug print
        return redirect(auth_url)
    except Exception as e:
        print(f"Login error: {str(e)}")
        return f"Error during login: {str(e)}", 500

@app.route('/callback')
def callback():
    print("\n=== CALLBACK ROUTE HIT ===")
    print(f"Request args: {dict(request.args)}")
    
    try:
        # Check for Spotify errors
        if 'error' in request.args:
            error = request.args.get('error')
            print(f"Spotify returned an error: {error}")
            return f"Spotify authorization error: {error}", 400

        # Get authorization code
        code = request.args.get('code')
        if not code:
            print("Authorization code not provided in callback")
            return "Authorization code missing", 400

        print(f"Authorization code received: {code}")

        # Exchange authorization code for access token
        spotify_handler = SpotifyHandler()
        token_info = spotify_handler.sp.auth_manager.get_access_token(code)
        
        if not token_info:
            print("Failed to retrieve token info")
            return "Error: Failed to retrieve access token", 400

        print(f"Token info retrieved: {token_info}")

        # Save token info in session
        session['token_info'] = token_info
        print(f"Session after token retrieval: {dict(session)}")

        # Redirect to profile page
        return redirect(url_for('profile'))
    except Exception as e:
        print(f"Callback error: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return f"Error during callback: {str(e)}", 500


@app.route('/profile')
def profile():
    print("\n=== PROFILE DEBUG ===")
    print(f"Session data: {dict(session)}")
    
    if 'token_info' not in session:
        print("No token info in session")
        return redirect(url_for('login'))
    
    try:
        spotify_handler = SpotifyHandler()

        # Ensure the token is valid and refresh if necessary
        token_info = spotify_handler.get_token(session)
        print(f"Valid token info: {token_info}")

        user_profile = spotify_handler.analyze_user_profile()
        print(f"User profile: {user_profile}")
        
        return f'''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Your Campify Profile</title>
                <style>
                    body {{ font-family: Arial; padding: 20px; }}
                    .meter {{ 
                        background: #eee;
                        border-radius: 8px;
                        height: 20px;
                        margin: 10px 0;
                    }}
                    .meter-fill {{
                        background: #1DB954;
                        height: 100%;
                        border-radius: 8px;
                        width: {user_profile['energy'] * 100}%;
                    }}
                </style>
            </head>
            <body>
                <h1>Your Music Profile</h1>
                <h2>Energy Level: {user_profile['energy'] * 100:.1f}%</h2>
                <div class="meter">
                    <div class="meter-fill"></div>
                </div>
                <h2>Mood: {user_profile['mood'] * 100:.1f}%</h2>
                <div class="meter">
                    <div class="meter-fill" style="width: {user_profile['mood'] * 100}%"></div>
                </div>
                <h2>Top Genres:</h2>
                <ul>
                    {''.join(f'<li>{genre}</li>' for genre in user_profile['dominant_genres'])}
                </ul>
            </body>
            </html>
        '''
    except Exception as e:
        print(f"Profile error: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return f"Error loading profile: {str(e)}", 500

    
    
@app.route('/generate-campsite')
def generate_campsite():
    spotify_handler = SpotifyHandler()
    user_profile = spotify_handler.analyze_user_profile()
    
    # Determine camping theme based on music profile
    theme = determine_theme(user_profile)
    
    return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
            </style>
        </head>
        <body>
            <h1>Your Personalized Campsite</h1>
            <div>
                <h2>Your Theme: {theme['name']}</h2>
                <p>{theme['description']}</p>
                
                <!-- Placeholder for campsite visualization -->
                <div id="campsite-view">
                    <p>Campsite visualization coming soon!</p>
                </div>
            </div>
        </body>
        </html>
    '''

def determine_theme(profile):
    energy = profile['energy']
    mood = profile['mood']
    
    if energy > 0.7:
        return {
            'name': 'Adventure Camp',
            'description': 'Your high-energy music suggests you\'re ready for an adventure!'
        }
    elif mood > 0.7:
        return {
            'name': 'Happy Valley Camp',
            'description': 'Your upbeat music taste reflects a bright and cheerful camping experience.'
        }
    else:
        return {
            'name': 'Chill Forest Camp',
            'description': 'Your music suggests you\'d enjoy a peaceful, relaxing camping experience.'
        }
    


if __name__ == '__main__':
    app.run(debug=True)