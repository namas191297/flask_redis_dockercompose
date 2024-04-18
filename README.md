# Flask and Redis Counter Application

## Overview
This project is a simple Flask application that increments a counter every time the homepage is visited. The counter's state is managed by a Redis server. The application is designed to be run using Docker and Docker-compose, ensuring that both the Flask application and Redis server are correctly set up and linked without any manual configuration required.

## Prerequisites
Before you can run this project, you need to have the following software installed on your machine:

1. **Docker**: Docker is a platform that allows you to easily build, test, and deploy applications. Docker packages software into standardized units called containers that have everything the software needs to run including libraries, system tools, code, and runtime.
2. **Docker Compose**: Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services.

### Installing Docker
To install Docker, follow the instructions on the [official Docker website](https://docs.docker.com/get-docker/). This will vary depending on your operating system.

### Installing Docker Compose
Docker Compose typically comes with the Docker installation on Windows and Mac. For Linux, you might have to install it separately. You can find the instructions on the [official Docker Compose website](https://docs.docker.com/compose/install/).

## Installation
1. **Clone the Repository**: First, clone this repository to your local machine using:
   ```bash
   git clone <url_to_repository>
   ```
   Replace <url_to_repository> with the URL or path of your GitHub repository.
2. **Navigate to the Project Directory**: Once cloned, move into the project directory:
   ```bash
   cd <path_to_cloned_repository>
   ```

## Usage

To run the application, follow these steps:

1. **Start the Application**: Run the following command in the terminal:
   ```bash
   docker-compose up --build
   ```
   This command builds the images if they don't exist and starts the containers as specified in the docker-compose.yml file.
2. **Access the Application**: Open a web browser and visit http://127.0.0.1:5000. You should see the webpage displaying a counter that increments with each visit.
3. **Shut Down the Application**: To stop and remove the containers, use the following command:
   ```bash
   docker-compose down
   ```