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
  radarr-clean-sweep:
    image: radarr-clean-sweep
    build:
      context: .
    environment:
      RADARR_URL: ${RADARR_URL}
      RADARR_API_KEY: ${RADARR_API_KEY}
    restart: unless-stopped
```
