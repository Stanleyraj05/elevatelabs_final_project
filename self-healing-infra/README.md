# 🛡️ Self-Healing Infrastructure with Prometheus, Alertmanager & Ansible

## 🚀 Project Objective
Automatically detect and recover from service failures using monitoring, alerting, and automation.

## 🧰 Stack
- 🔍 Prometheus: Service monitoring
- 🚨 Alertmanager: Alert routing
- 📦 Docker: Container orchestration
- ⚙️ Ansible: Automation & recovery
- 🐚 Shell Script: Webhook action
- 🌐 NGINX: Sample application

## 📂 Folder Structure
```
self-healing-infra/
├── ansible/              # Ansible automation
├── prometheus/           # Prometheus config & rules
├── alertmanager/         # Alertmanager config
├── webhook/              # Webhook + Flask server
├── docker-compose.yml    # Docker stack
└── README.md             # Documentation
```

## 🧪 How It Works
1. NGINX is monitored by Prometheus via Node Exporter.
2. If NGINX is detected down, Prometheus fires an alert.
3. Alertmanager routes the alert to a webhook.
4. The webhook runs an Ansible playbook to auto-restart NGINX.
5. Logs are stored for audit and visibility.

## 🛠️ Setup Instructions
```bash
# Step 1: Start infrastructure
docker-compose up -d

# Step 2: Simulate failure (stop NGINX manually)
docker stop $(docker ps -q --filter ancestor=nginx)

# Step 3: Observe auto-healing
# Prometheus will detect downtime, Alertmanager triggers webhook,
# Webhook calls Ansible which restarts NGINX

# Step 4: Logs
cat /tmp/webhook.log
cat /tmp/ansible.log
```

## ✅ Deliverables
- Prometheus Config
- Alert Rules
- Alertmanager Webhook
- Ansible Playbook
- Auto-Healing Demo Logs