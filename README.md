# Logodot

## Project Description

A free web app to serve simple logos upon a few color and font preferences.

## Purpose

To teach myself containerization (Docker) and Kubernetes deployments. I chose Logodot for this because I believe that containerizing the logo-serving API and frontend web app will improve the performance of the app under high load. This is primarily because image-processing is resource-intensive and could potentially interfere with the speed of serving web pages.

## Stack

- Python
- Flask
- React & Antd
- Python Image Library (PIL)
- Git & Github
- Docker & Dockerhub
- Kubernetes & Google Cloud Platform

## Setup

### Docker Setup

1. Start Docker `docker-machine start default && docker-machine env && @FOR /f "tokens=*" %i IN ('docker-machine env') DO @%i`

### Frontend

Build Docker image: `cd frontend-app && docker build . -t ${your_dockerhub_username_here}/logodot-frontend`
Push to Dockerhub: `docker push ${your_dockerhub_username_here}/logodot-frontend`

### Generator

Build Docker image: `cd logo-generator && docker build . -t ${your_dockerhub_username_here}/logodot-generator`
Push to Dockerhub: `docker push ${your_dockerhub_username_here}/logodot-generator`