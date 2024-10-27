#!/bin/bash

# Build the Docker image
docker build -t my-website .

# Stop and remove any existing container with the same name
if [ "$(docker ps -aq -f name=website-container)" ]; then
    echo "Stopping and removing existing container..."
    docker stop website-container
    docker rm website-container
fi

# Run the Docker container with port mapping
docker run -d -p 5000:5000 --name website-container my-website
