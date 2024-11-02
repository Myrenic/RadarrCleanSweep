# RadarrCleanSweep

A lightweight Dockerized script that automatically deletes movies from your Radarr library that have not been watched for a specified period. 

## Features

- **Automatic Deletion**: Configurable time frame for deleting unwatched movies.
- **Dockerized**: Easy to deploy and run in any environment with Docker.
- **Environment Variables**: Easily configure your Radarr instance and API key.

## Getting Started

### Prerequisites

- Docker installed on your machine.

### Installation



``` docker-compose
version: '3.8'

services:
  radarrcleansweep:
    image: ghcr.io/myrenic/radarrcleansweep:latest
    restart: unless-stopped
    environment:
      - RADARR_URL=http://radarr:7878/
      - RADARR_API_KEY=UseYourApiKeyHere
      - DAYS=60
    volumes:
      - ./data:/app/data  # Adjust volume mapping as needed

```
