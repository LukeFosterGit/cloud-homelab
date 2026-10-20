# Docker Application Architecture

## Overview

A containerized web application built with Docker Compose to demonstrate networking, persistent storage, security hardening, and application deployment.

## Architecture

Client → Nginx → Flask/Gunicorn → PostgreSQL

**Nginx**
- Reverse proxy exposed on host port 80.
- Routes requests to Flask over Docker's internal network.

**Flask and Gunicorn**
- Python web application running on internal port 5000.
- Served by Gunicorn rather than Flask's development server.
- Provides `/health` and `/messages` endpoints.

**PostgreSQL**
- PostgreSQL 17 database running on internal port 5432.
- Stores application data in a persistent Docker named volume.

## Security Controls

- Non-root application user.
- Dropped Linux capabilities.
- Read-only Flask container filesystem.
- Temporary writable `/tmp` filesystem.
- Prevention of privilege escalation.
- CPU and memory limits.
- No direct host port exposure for Flask or PostgreSQL.

## Reliability

- Database and application health checks.
- Docker Compose startup dependencies.
- Container restart policies.
- Persistent PostgreSQL storage.

## Configuration

Database environment variables are loaded from a local `.env` file, which is excluded from Git.

An `.env.example` file documents the required configuration.

## Running the Application

From the `app/` directory:

1. Copy `.env.example` to `.env`.
2. Configure the database environment variables.
3. Run `docker compose up -d --build`.
4. Open `http://localhost/messages` on the Docker host.

## Future Improvements

- HTTPS and TLS certificates.
- Automated database backups and restore testing.
- Container vulnerability scanning.
- CI/CD.
- Ansible server configuration.
- Terraform infrastructure provisioning.
- AWS deployment.
