FROM python:3.8-slim

WORKDIR /app

COPY main.py ./
COPY run_script.sh ./

# Ensure the script is executable
RUN chmod +x run_script.sh

# Run main.py at container startup
RUN python3 main.py

# Setup cron job to run every hour
RUN apt-get update && apt-get install -y cron \
    && echo "0 * * * * /app/run_script.sh" | crontab -

# Run cron in the foreground
CMD ["cron", "-f"]
