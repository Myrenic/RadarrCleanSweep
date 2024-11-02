import os
import requests
from datetime import datetime, timedelta
import sys

# Set Radarr URL and API Key from environment variables
RADARR_URL = os.getenv("RADARR_URL")
RADARR_API_KEY = os.getenv("RADARR_API_KEY")
DAYS_BEFORE_DELETION = os.getenv("DAYS_BEFORE_DELETION", 60)  # Default to 60 days if not set

# Check if the required environment variables are set
if not RADARR_URL or not RADARR_API_KEY:
    print("Error: RADARR_URL and RADARR_API_KEY must be set.")
    sys.exit(1)

# Convert the days to an integer
try:
    days_before_deletion = int(DAYS_BEFORE_DELETION)
except ValueError:
    print("Error: DAYS_BEFORE_DELETION must be an integer.")
    sys.exit(1)

def get_movies():
    url = f"{RADARR_URL}/api/v3/movie"
    headers = {
        "X-Api-Key": RADARR_API_KEY
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movies: {e}")
        return []

def delete_movie(movie_id):
    url = f"{RADARR_URL}/api/v3/movie/{movie_id}"
    headers = {
        "X-Api-Key": RADARR_API_KEY
    }
    
    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        print(f"Deleted movie ID: {movie_id}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error deleting movie ID {movie_id}: {e}")

def main():
    movies = get_movies()
    threshold_date = datetime.now() - timedelta(days=days_before_deletion)
    
    for movie in movies:
        added_date = datetime.strptime(movie.get("added"), '%Y-%m-%dT%H:%M:%SZ')  # Adjusted format
        if added_date < threshold_date:
            delete_movie(movie.get("id"))

if __name__ == "__main__":
    main()
