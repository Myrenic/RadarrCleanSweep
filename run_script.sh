#!/bin/sh

# Log starting time
echo "$(date) - Starting Radarr Clean Sweep script." >> /app/logs/radarr_clean_sweep.log

# Execute the main script
python3 /app/main.py  # Adjust the path if necessary

# Log completion time
echo "$(date) - Radarr Clean Sweep script completed." >> /app/logs/radarr_clean_sweep.log
