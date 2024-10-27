# Website Deployment with Docker

This repository contains a Dockerized Flask application that includes registration and login functionalities. The setup is designed for easy deployment using two scripts: `install.bash` for building the Docker image and `run.bash` for running the container.

## Getting Started

Follow these steps to clone the repository, set up the environment, and run the application.

### Prerequisites

- Ensure that **Docker** is installed and running on your machine.
  
  ```bash
   sudo apt update
   sudo apt install -y docker-ce docker-ce-cli containerd.io

### Installation

1. **Clone the repository**:
   
   ```bash
   git clone https://github.com/Pela36/website
   
2. **Navigate to the project directory**:

    ```bash
    cd website

3. **Make the scripts executable**:
   
    ```bash
    chmod +x install
    
4. **Run the installer**"
   
     ```bash
    ./install

### **Website should already be running, if not you can**:

1. Run the website
   
    ```bash
    ./run.bash

### **Stop the website by running**:

1. **This command**:
   
    ```bash
    docker stop website-container


    
