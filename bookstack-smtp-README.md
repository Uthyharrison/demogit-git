
BookStack Docker Deployment (Production Ready)

# This deployment provides a Docker-based setup for running BookStack with:
- MySQL as (database)
- SMTP support for sending email notifications (e.g. password reset)
- Persistent data storage via Docker volumes
- Health checks & restart policies for reliability


 # Project Structure

bookstack/
─ docker-compose.yml # Defines BookStack and MySQL services
─ .env # Contains environment-specific variables

# BookStack Deployment with Docker Compose & SMTP Integration

This repository contains a production-ready setup for deploying **BookStack** using Docker Compose, with SMTP configuration for email notifications and password reset functionality. The configuration ensures a smooth and scalable deployment with persistent storage, health checks, and easy-to-use environment variable management.


# Overview

BookStack is an easy-to-use platform for creating documentation, knowledge bases, and wikis. This setup allows you to deploy BookStack quickly in a production environment using Docker Compose, ensuring seamless email functionality via SMTP for user interactions like notifications and password reset



# Architecture

The solution uses Docker Compose to manage the deployment of BookStack, along with the required configuration for persistent storage and email functionality. It includes:

- **BookStack Service:** Main application container.
- **Database Service (MySQL):** Persistent storage for all BookStack data.
- **SMTP Settings:** Configured via `.env` file for easy SMTP setup.

# How It Works

1. **Docker Compose** orchestrates both the BookStack application and MySQL database containers.
2. **Environment Variables** defined in `.env` file handle SMTP configuration and other settings.
3. **Persistent Storage** is enabled using Docker volumes, ensuring data is not lost on restarts.
4. **Health Checks & Restart Policies** ensure BookStack and its dependencies are always running and healthy.



# How to Deploy

# 1. Clone the Repository
- git clone https://git.edusuc.net/WEBFORX/infrastructure-tools.git
- cd into the folder infrastructure-tools i cloned from the repo which consist of the code
- i make a directory called bookstack and move the file that contains the code there, i did some modification to suit what i want to achieve.
