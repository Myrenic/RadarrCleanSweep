# Use the official Python image as a base
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the main script into the container
COPY main.py .

# Command to run the script
CMD ["python", "main.py"]
