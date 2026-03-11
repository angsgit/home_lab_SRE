# Homelab CI/CD Pipeline with Jenkins, Terraform, and K3s

This repository demonstrates a self-contained homelab setup for deploying and monitoring a Python application using **Jenkins, Terraform, Docker, and K3s (lightweight Kubernetes)**. The lab includes monitoring via **Prometheus** and **Grafana**.

---

## **Overview**

This setup runs entirely on a single Linux host using containers. Jenkins orchestrates the pipeline, Terraform provisions infrastructure containers, K3s runs your application Pods, and Prometheus/Grafana handle monitoring.


---

## **Pipeline Stages**

1. **Pipeline Trigger**  
   - Jenkins pipeline starts automatically via Git commit or manually.

2. **Terraform Stage**  
   - Jenkins spins up a **Terraform container**.  
   - Terraform provisions infrastructure containers:  
     - **K3s container** → lightweight Kubernetes cluster  
     - **Grafana container** → dashboards  
     - **Prometheus container** → metrics collection  
   - Terraform container exits after provisioning.

3. **K3s Stage**  
   - Jenkins ensures the **K3s container is running**.  
   - Sets up `kubectl` context to deploy applications.

4. **Application Build Stage**  
   - Jenkins builds the Python app Docker image.  
   - Pushes it to a local Docker registry or DockerHub.

5. **Kubernetes Deploy Stage**  
   - Jenkins applies Deployment + Service manifests to K3s.  
   - K3s creates Pods and manages their lifecycle, networking, and scaling.

6. **Monitoring Stage**  
   - Prometheus scrapes metrics from Python app Pods.  
   - Grafana reads Prometheus metrics and displays dashboards.

7. **Optional Tear-down Stage** *(Lab Only)*  
   - `terraform destroy` removes K3s, Grafana, and Prometheus containers.  
   - In production, this stage is skipped to keep the cluster and monitoring running continuously.

---

## **Technologies Used**

- **Docker**: container runtime  
- **Jenkins**: CI/CD orchestration  
- **Terraform**: infrastructure as code (provisions containers)  
- **K3s**: lightweight Kubernetes cluster  
- **Python**: sample application  
- **Prometheus**: metrics collection  
- **Grafana**: monitoring dashboards  

---

## **Usage**

1. Start Jenkins container on my host.  
2. Configure pipeline with this repo.  
3. Trigger pipeline:  
   - Jenkins will run Terraform container to provision infra.  
   - Build the Python app Docker image.  
   - Deploy app to K3s using manifests.  
   - Start monitoring via Prometheus/Grafana.  
4. *(Optional)* Tear down lab with `terraform destroy`.  

---

## **Notes**

- This setup is ideal for **learning CI/CD, Terraform, and Kubernetes** on a single host.  
- In production, the tear-down stage should be removed, and the cluster + monitoring should remain persistent.  
- All components run as Docker containers, making it portable and reproducible.

---
