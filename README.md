# Automated Cloud Infrastructure Deployment Pipeline

A CI/CD pipeline that automatically provisions and manages Azure cloud
infrastructure using Terraform, Docker, Kubernetes, Ansible, Prometheus,
and Grafana. Every push to the main branch triggers a full deployment.

## What this project does

- Pushes to GitHub trigger a GitHub Actions workflow automatically
- Terraform provisions Azure resources (Resource Group, VNet, Storage)
- A Python Flask app is containerised with Docker and deployed on Kubernetes
- Ansible handles configuration management across environments
- Prometheus collects metrics and Grafana displays them on a live dashboard

## Tools used

| Tool             | Purpose                        |
|------------------|--------------------------------|
| Terraform        | Infrastructure as Code (IaC)   |
| GitHub Actions   | CI/CD pipeline automation      |
| Microsoft Azure  | Cloud infrastructure           |
| Docker           | Containerisation               |
| Kubernetes       | Container orchestration        |
| Ansible          | Configuration management       |
| Prometheus       | Metrics collection             |
| Grafana          | Monitoring dashboards          |

## Project structure

```
cloud-infra-pipeline/
├── terraform/        Infrastructure as Code — Azure resources
├── app/              Python Flask app + Dockerfile
├── kubernetes/       Deployment and Service YAML files
├── ansible/          Configuration management playbooks
├── monitoring/       Prometheus and Grafana setup
└── .github/
    └── workflows/    GitHub Actions pipeline
```

## Screenshots

*(To be added after build is complete)*

## Author

Atefor Lesley Nkezi
[LinkedIn](https://www.linkedin.com/in/atefor-lesley-nkezi-6a3760250)
[GitHub](https://github.com/lesley237)
