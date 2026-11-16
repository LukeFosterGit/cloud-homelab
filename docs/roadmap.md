# Implementation Plan

## Objective

Reproduce the existing local application and its host configuration in a second environment using infrastructure as code and deployment automation. Keep the same Nginx / Flask / PostgreSQL workload throughout the project so that changes in infrastructure and operations can be evaluated directly.

## Delivery milestones

| Milestone | State | Deliverable |
| --- | --- | --- |
| Ubuntu host and access controls | Implemented locally | SSH key access, firewall configuration, service diagnostics |
| Docker application | Implemented locally | HTTP through Nginx, internal service communication, persistent PostgreSQL data, health checks and container restrictions |
| Ansible host baseline | In progress | Packages, service account and permissions, services and security settings applied consistently |
| Ansible application deployment | Planned | Configure a clean Ubuntu VM and deploy the existing Compose stack without repeating manual setup |
| Deployment validation and recovery | Planned | Repeatable startup, idempotency checks, diagnosed failure scenarios, tested PostgreSQL restore |
| Microsoft administration integration | Planned | Focused PowerShell, Windows Server, and Entra ID/RBAC exercises relevant to host and Azure operations |
| Terraform and Azure network | Planned | Resource group, virtual network, subnet, network security controls, appropriately sized VM, least-privilege access |
| Azure operations | Planned | Application deployment, monitoring/logging, budget controls, backup/recovery test, and teardown |
| Documentation and handoff | Ongoing | Architecture, procedures, design tradeoffs, validation results, and known limitations |

## Current implementation priority

**Ansible host configuration.** Inventory, variable management, templating, handlers, and package tasks are established locally. The next task is to manage a dedicated service account, group, and restricted directory. Follow this with systemd, SSH/UFW changes performed with access safeguards, and deployment of the existing Compose application.

## Scope boundaries

The core system remains **one application, one automated local deployment, and one Azure deployment**. Complex Kubernetes orchestration, multiple cloud providers, high availability, and an expanded application catalog are not required for this implementation.

Any additional component should address a documented reliability, security, deployment, or operational requirement.
