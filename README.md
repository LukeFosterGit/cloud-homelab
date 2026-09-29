#Cloud Architechture Homelab

A homelab project created to learn and showcase Linux, networking, automation, containers, IaC, and cloud architecture.

## Current Progress 

- Ubuntu Server deployed using Hyper-V
- SSH key authentication configured
- UFW Configured and activated
- Nginx web server deployed
- Bash health check script created
- Automated health check with systemd service and timer

## Docker

- Docker images and containers
- Dockerfiles
- Image tags and versioning
- Image layers and build cache
- Container lifecycle
- Port publishing
- Docker bridge networking
- Docker daemon and Unix socket permissions
- Building and replacing immutable containers

### Web Container  

The custom image is defined in: 
'docker/web/Dockerfile'

The container serves a simple web page through Nginx and is published
on port 8080 of the Ubuntu host.
