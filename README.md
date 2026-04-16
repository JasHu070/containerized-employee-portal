# Dockerized Employee Management System

## Overview
A multi-container employee management web application built using Docker Compose. The project uses Flask as the backend application, Nginx as a reverse proxy, and SQLite for persistent employee data storage.

## Tech Stack
- Docker
- Docker Compose
- Flask (Python)
- Nginx
- SQLite
- HTML / CSS

## Architecture
Browser -> Nginx -> Flask App -> SQLite Database File -> Docker Volume

## Features
- Add employee records
- Persistent data using Docker volumes
- Reverse proxy with Nginx
- Container healthchecks
- Restart policies
- Multi-container orchestration

## Project Structure
employee-docker-project/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
├── nginx/
│   └── default.conf
├── docker-compose.yml
├── Dockerfile
└── README.md

## How to Run

```bash
docker compose up --build -d
