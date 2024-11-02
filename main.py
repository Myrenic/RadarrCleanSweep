import os
import requests
import logging
from datetime import datetime, timedelta
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def delete_old_movies(radarr_url, radarr_api_key, days_threshold):
    """Deletes movies older than the specified threshold from Radarr."""
    # Make API call to Radarr
    response = requests.get(f"{radarr_url}/api/v3/movie", headers={"X-Api-Key": radarr_api_key})
    response.raise_for_status()
    
    current_date = datetime.utcnow()
    threshold_date = current_date - timedelta(days=days_threshold)
    
    for movie in response.json():
        added_date = datetime.strptime(movie.get("added"), '%Y-%m-%dT%H:%M:%SZ')
        if added_date < threshold_date:
            delete_response = requests.delete(f"{radarr_url}/api/v3/movie/{movie['id']}", headers={"X-Api-Key": radarr_api_key})
            if delete_response.status_code == 200:
                logger.info(f"Deleted movie: {movie['title']} (ID: {movie['id']})")
            else:
                logger.error(f"Failed to delete movie: {movie['title']} (ID: {movie['id']}), Status Code: {delete_response.status_code}")

def main():
    logger.info("Starting Radarr Clean Sweep script.")
    
    # Retrieve environment variables
    radarr_url = os.getenv("RADARR_URL")
    radarr_api_key = os.getenv("RADARR_API_KEY")
    sleep_duration = int(os.getenv('SLEEP_DURATION', 3600))
    days_threshold = int(os.getenv("DAYS", 60))

    if not radarr_url or not radarr_api_key:
        logger.error("RADARR_URL and RADARR_API_KEY must be set.")
        return

    try:
        delete_old_movies(radarr_url, radarr_api_key, days_threshold)
        logger.info("Radarr Clean Sweep script completed.")
    except requests.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logger.error(f"An unexpected error occurred: {err}")

    logger.info(f"Sleeping for {sleep_duration} seconds...")
    time.sleep(sleep_duration)

if __name__ == "__main__":
    main()
