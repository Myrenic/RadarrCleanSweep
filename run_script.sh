#!/bin/bash

# Log the script start time
echo "$(date) - Running Radarr Clean Sweep script." >> /app/script_run.log

# Navigate to the app directory if necessary
cd /app

# Run the Python script
python3 main.py

# Log the completion time
echo "$(date) - Finished running Radarr Clean Sweep script." >> /app/script_run.log
