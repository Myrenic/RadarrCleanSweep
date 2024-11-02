# Use an appropriate base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy your script files
COPY main.py ./
COPY run_script.sh ./

# Install necessary dependencies (if any)
# RUN pip install requests  # Example, adjust as needed

# Make the script executable
RUN chmod +x run_script.sh

# Setup cron job to run every hour
RUN echo "0 * * * * /app/run_script.sh" | crontab -

# Run cron in the foreground
CMD ["cron", "-f"]
