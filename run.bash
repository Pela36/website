#!/bin/bash

# Stop and remove any existing container with the same name
if [ "$(docker ps -aq -f name=website-container)" ]; then
    echo "Stopping and removing existing container..."
    docker stop website-container
    docker rm website-container
fi

# Run the Docker container with port mapping
echo "Running Docker container..."
docker run -d -p 5000:5000 --name website-container my-website

# Scrape the local IPv4 address
LOCAL_IPV4=$(hostname -I | awk '{print $1}')

# Output the address to access the website
echo "Website is running at http://$LOCAL_IPV4:5000"
