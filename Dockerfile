FROM python:3.8-slim

WORKDIR /app

COPY main.py ./
COPY run_script.sh ./
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure the script is executable
RUN chmod +x run_script.sh

# Run main.py at container startup
RUN python3 main.py

# Setup cron job to run every hour
RUN apt-get update && apt-get install -y cron \
    && echo "0 * * * * /app/run_script.sh" | crontab -

# Run cron in the foreground
CMD ["cron", "-f"]




# Copy the main script into the container
COPY main.py .

# Command to run the script
CMD ["python", "main.py"]
