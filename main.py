import os
import requests
import logging
from datetime import datetime, timedelta

# Set up logging to console only
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(ch)

def main():
    logger.info("Starting Radarr Clean Sweep script.")

    # Retrieve environment variables
    radarr_url = os.getenv("RADARR_URL")
    radarr_api_key = os.getenv("RADARR_API_KEY")
    days_threshold = int(os.getenv("DAYS", 60))

    if not radarr_url or not radarr_api_key:
        logger.error("RADARR_URL and RADARR_API_KEY must be set.")
        return

    # Make API call to Radarr
    try:
        response = requests.get(f"{radarr_url}/api/v3/movie", headers={"X-Api-Key": radarr_api_key})
        response.raise_for_status()  # Raise an error for bad responses
        movies = response.json()

        # Current date for comparison
        current_date = datetime.utcnow()
        threshold_date = current_date - timedelta(days=days_threshold)

        for movie in movies:
            added_date = datetime.strptime(movie.get("added"), '%Y-%m-%dT%H:%M:%SZ')  # Correct date format
            if added_date < threshold_date:
                # Logic to delete the movie
                movie_id = movie['id']
                delete_response = requests.delete(f"{radarr_url}/api/v3/movie/{movie_id}", headers={"X-Api-Key": radarr_api_key})
                if delete_response.status_code == 200:
                    logger.info(f"Deleted movie: {movie['title']} (ID: {movie_id})")
                else:
                    logger.error(f"Failed to delete movie: {movie['title']} (ID: {movie_id}), Status Code: {delete_response.status_code}")

        logger.info("Radarr Clean Sweep script completed.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
