# Cloud Homelab

A virtualized Linux environment for deploying and operating a containerized web application. The project uses Hyper-V, Ubuntu Server, Docker Compose, and Ansible, with a planned Azure deployment managed through Terraform.

The focus is on repeatable infrastructure configuration, network separation, least-privilege access, persistent data, and operational troubleshooting.

## System architecture

```text
Windows host (Hyper-V)
└── Ubuntu Server VM
    ├── SSH key authentication / UFW
    ├── Docker Compose network
    │   ├── Nginx reverse proxy     host TCP/80
    │   │   └── Flask + Gunicorn    internal TCP/5000
    │   │       └── PostgreSQL 17   internal TCP/5432
    │   │           └── Named data volume
    │   └── Container health checks and restart policies
    └── Ansible (server configuration work in progress)
```

Only Nginx publishes an application port to the Ubuntu host. Flask and PostgreSQL communicate through the Docker network using Compose service names. This is a LAN-only HTTP deployment, not a public-facing production service.

## Implemented components

**Ubuntu and host administration**
- Ubuntu Server VM running on Hyper-V, accessed using SSH keys.
- Linux permissions, systemd, UFW, package management, and log-based diagnostics.
- Host-level Nginx configuration from earlier testing, subsequently disabled to prevent a conflict with the Docker reverse proxy.

**Containerized application**
- Nginx routes HTTP traffic to a Flask application served by Gunicorn.
- PostgreSQL stores application records in a persistent Docker named volume.
- Compose defines service networking, startup dependencies, health checks, restart policies, and resource limits.
- Flask runs as a non-root user with dropped Linux capabilities, read-only root filesystem, restricted privilege escalation, and a writable temporary mount.
- Runtime values are supplied through a local `.env` file excluded from version control; `.env.example` documents the required keys.

**Configuration automation — in progress**
- Ansible inventory and configuration for the Ubuntu VM.
- Playbooks covering package management, system information, variables, templates, conditions, loops, and handlers.
- Ubuntu baseline configuration under development, followed by user/service management and application deployment.

The Ansible work is being developed locally; its deployment automation is not yet complete. See [implementation plan](docs/roadmap.md).

## Run the application locally

Prerequisites: Linux host with Docker Engine and the Docker Compose plugin installed.

```bash
cd app
cp .env.example .env
# Set local credentials in .env before starting.
docker compose config --quiet
docker compose up -d --build
docker compose ps
curl -i http://localhost/health
curl -i http://localhost/messages
```

The application currently expects the PostgreSQL `messages` table to exist. **Initializing a clean database is not yet fully automated**; `/messages` requires that schema and its data to be present. Git contains source and configuration, not database records or credentials.

A named volume persists database files across normal container recreation. Avoid `docker compose down -v` when that data needs to be preserved.

## Design and operations

| Area | Approach | Current limitation / next step |
| --- | --- | --- |
| Network exposure | Single Nginx entry point; private app and database ports | HTTPS not configured for external access |
| Application runtime | Gunicorn behind Nginx | Further deployment resilience testing pending |
| Data durability | Named PostgreSQL volume; manual logical backup practiced | Automated backup and tested restore still needed |
| Container security | Non-root Flask process, reduced privileges and filesystem writes | Image scanning and secret management not yet implemented |
| Automation | Ansible playbooks for repeatable host configuration | Fresh-VM provisioning and app deployment pending |
| Cloud | Azure selected for the next infrastructure environment | Terraform configuration and deployment pending |

## Documentation

- [Implementation plan](docs/roadmap.md)

## Planned Azure architecture

Use Terraform to provision a small Azure resource group, VNet/subnet, network security rules, and Linux VM suitable for the existing Compose application. Configure deployment through Ansible, apply least-privilege Azure RBAC, and add monitoring, budget controls, backup/restore validation, and a teardown procedure.

Azure is **planned**, not deployed. Advanced multi-node orchestration and AWS are outside the current project scope.
