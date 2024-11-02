#!/bin/bash

# Log the script start time to console
echo "$(date) - Running Radarr Clean Sweep script."

# Navigate to the app directory if necessary
cd /app

# Run the Python script
python3 main.py

# Log the completion time to console
echo "$(date) - Finished running Radarr Clean Sweep script."
