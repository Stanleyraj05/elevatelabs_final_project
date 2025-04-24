
# 🚀 Kubernetes-Based Canary Deployment with K3s and Istio

## 📌 Objective
Simulate modern canary deployments by deploying two versions of an application on K3s and managing traffic using Istio. Route 80% of the traffic to the stable version and 20% to the canary version, observe performance, and roll back or promote accordingly.

---

## 🧱 Architecture

```
Client
  |
Ingress Gateway (Istio)
  |
VirtualService (Traffic Split: 80% v1, 20% v2)
  |
Service (my-app)
  |
Deployments
  ├── v1 (Stable)
  └── v2 (Canary)
```

---

## 🛠️ Tools & Technologies

- [K3s](https://k3s.io/) (Lightweight Kubernetes)
- [Istio](https://istio.io/) (Service Mesh)
- Docker (Containerization)
- Node.js/Python (Sample App)
- Helm (Optional - for packaging)
- Prometheus & Grafana (Optional - Observability)
- kubectl / curl for manual testing

---

## 📁 Project Structure

```
.
├── deployment-v1.yaml          # Deployment for version v1 (stable)
├── deployment-v2.yaml          # Deployment for version v2 (canary)
├── service.yaml                # Kubernetes Service
├── gateway.yaml                # Istio Gateway
├── destination-rule.yaml       # Istio DestinationRule for version routing
├── virtual-service.yaml        # Istio VirtualService for traffic split
└── README.md                   # Project documentation
```

---

## ⚙️ Prerequisites

- A working K3s cluster (or local K3d setup)
- Istio installed and configured in the cluster
- kubectl configured to access your cluster
- Docker installed
- (Optional) Prometheus and Grafana set up for metrics

---

## 🚀 Setup Instructions

1. **Deploy the Stable and Canary Versions**

```bash
kubectl apply -f deployment-v1.yaml
kubectl apply -f deployment-v2.yaml
```

2. **Expose the Application via Kubernetes Service**

```bash
kubectl apply -f service.yaml
```

3. **Apply Istio Routing Components**

```bash
kubectl apply -f destination-rule.yaml
kubectl apply -f gateway.yaml
kubectl apply -f virtual-service.yaml
```

4. **Find External IP**

```bash
kubectl get svc -n istio-system
```

Use this IP to access the application.

---

## 📊 Monitoring Strategy

### Option 1: Manual Curl Logs

```bash
for i in {1..20}; do curl http://<EXTERNAL-IP>/; done
kubectl logs -l version=v1
kubectl logs -l version=v2
```

You should see ~16 logs in v1 and ~4 in v2 if the split is 80/20.

### Option 2: Prometheus & Grafana (Recommended)

- Use Istio's default metrics:
  - `istio_requests_total`
  - `istio_request_duration_seconds`
- Build dashboards by filtering `destination_version` labels.

---

## 🧠 Canary Deployment Strategy

### Initial Setup

- Deploy two versions of the application:
  - **v1 (Stable)**: `replicas: 3`
  - **v2 (Canary)**: `replicas: 1`
- Expose both via a shared `Service`
- Use Istio `DestinationRule` to define subsets:
  
```yaml
subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
```

- Route traffic using `VirtualService`:

```yaml
- destination:
    host: my-app
    subset: v1
  weight: 80
- destination:
    host: my-app
    subset: v2
  weight: 20
```

---

## ✅ Promotion Criteria

Promote v2 only if:

- No increase in error rate
- Stable response time and performance
- All features work as expected

To promote, change weight to 100% for v2:

```yaml
- destination:
    host: my-app
    subset: v2
  weight: 100
```

---

## ❌ Rollback Plan

If performance issues are detected in v2:

- Route all traffic back to v1:

```yaml
- destination:
    host: my-app
    subset: v1
  weight: 100
```

- Optionally delete or scale down the v2 deployment.

---

## ✅ Deliverables

- ✅ K3s deployment YAMLs (`deployment-v1.yaml`, `deployment-v2.yaml`)
- ✅ Istio configuration files (`gateway.yaml`, `destination-rule.yaml`, `virtual-service.yaml`)
- ✅ Canary Deployment Strategy (this `README.md`)
- ✅ Monitoring steps (logs or metrics via curl, Prometheus/Grafana)
