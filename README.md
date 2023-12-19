# Discover-Eternally

Spotify generates a Discover Weekly playlist every week with 30 newly recommened songs for you to listen to. After the week, those songs are gone forever and new songs populate the playlist! This program moves your Discover Weekly Spotify playlist into a "Discover Eternally" playlist every week so you will never miss a song.

## Installation

### Requirements

- Python 3.x
- Spotify Account
- Spotify Developer Credentials (Client ID, Client Secret)

### Dependencies Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/Discover-Eternally.git
    cd Discover-Eternally
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv myenv
    # Activate virtual environment
    # Windows
    myenv\Scripts\activate
    # Unix/macOS
    source myenv/bin/activate
    ```

3. Install required Python packages:

    ```bash
    pip install -r requirements.txt
    ```
    
## Configuration

### Spotify Developer Credentials

Ensure you have obtained your Spotify Developer credentials (Client ID and Client Secret) from the Spotify Developer Dashboard. Add these credentials to the `secrets.py` file as follows:

```python
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
SPOTIFY_USER_ID = 'your_spotify_user_id'
```

## Usage

### Running the Script

Ensure you have filled in the necessary credentials in the `secrets.py` file. Then, execute the script:

```bash
python spotify_playlist_sync.py
```

### Scheduling with Cron

To automate syncing your playlists, you can schedule the script to run periodically (weekly) using cron.

1. Open the cron jobs editor:

    ```bash
    crontab -e
    ```

2. Add a cron job entry to run the script weekly at a specified time:

    ```bash
    0 8 * * 1 /path/to/python /path/to/spotify_playlist_sync.py
    ```

This example schedules the script to run every Monday at 8 AM. Adjust the timing as needed.

## Contributing

Feel free to contribute by opening issues or submitting pull requests.
