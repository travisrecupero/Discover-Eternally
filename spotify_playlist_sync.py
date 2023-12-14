import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException
from secrets import CLIENT_ID, CLIENT_SECRET, SPOTIFY_USER_ID

def get_playlist_id(sp, user_id, playlist_name):
    playlists = sp.user_playlists(user_id)
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            return playlist['id']
    return None

def create_playlist(sp, user_id, playlist_name):
    try:
        print(f"Creating '{playlist_name}' playlist...")
        playlist = sp.user_playlist_create(user_id, playlist_name)
        playlist_id = playlist['id']
        print(f"'{playlist_name}' playlist created successfully!")
        return playlist_id
    except SpotifyException as e:
        print(f"Error creating '{playlist_name}' playlist: {e}")
        return None

def main():
    # Authenticate
    scope = "playlist-modify-public"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri='http://localhost:8888/callback'))

    # Get tracks from Discover Weekly
    discover_weekly_id = 'YOUR_DISCOVER_WEEKLY_PLAYLIST_ID'
    try:
        results = sp.playlist_tracks(discover_weekly_id)
    except SpotifyException as e:
        print(f"Error retrieving tracks from Discover Weekly: {e}")
        exit()

    # Get or create "Discover Eternally" playlist
    playlist_name = "Discover Eternally"
    user_id = SPOTIFY_USER_ID
    discover_eternally_id = get_playlist_id(sp, user_id, playlist_name)
    if not discover_eternally_id:
        discover_eternally_id = create_playlist(sp, user_id, playlist_name)

    # Add tracks to "Discover Eternally" playlist
    tracks_to_add = [track['track']['uri'] for track in results['items']]
    if discover_eternally_id:
        try:
            sp.playlist_add_items(discover_eternally_id, tracks_to_add)
            print("Tracks added to 'Discover Eternally' playlist!")
        except SpotifyException as e:
            print(f"Error adding tracks to 'Discover Eternally' playlist: {e}")
            exit()
    else:
        print("Failed to create or retrieve the playlist. Exiting.")
        exit()

if __name__ == "__main__":
    main()