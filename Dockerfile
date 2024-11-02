FROM python:3.8-slim

WORKDIR /app

COPY main.py ./
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the script
CMD ["python3", "main.py"]
