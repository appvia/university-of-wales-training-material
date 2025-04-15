# Lab 2: Scaling Your Application

## Objective
In this lab, you will learn how to create and manage Kubernetes Deployments, scale applications horizontally, and perform basic deployment operations. You'll understand the differences between Pods and Deployments, and how to handle application scaling.

## Prerequisites
- Completed Lab 1 (Basic Pod operations)
- A running Kubernetes cluster
- kubectl CLI tool installed and configured
- Basic understanding of YAML syntax

## Steps

### 1. Create a Deployment Manifest
First, create a file named `nginx-deployment.yaml` with the following content:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
```

### 2. Deploy the Application
Apply the deployment manifest:
```bash
kubectl apply -f nginx-deployment.yaml
```

### 3. Verify the Deployment
Check the status of your deployment:
```bash
kubectl get deployments
kubectl get pods
```

### 4. Scale the Deployment
Scale the deployment to 3 replicas:
```bash
kubectl scale deployment nginx-deployment --replicas=3
```

Verify the scaling:
```bash
kubectl get pods
```

You should now see 3 pods running with names like `nginx-deployment-xxxxx-yyyy`.

### 5. Test Load Balancing
Create a service to expose the deployment:
```bash
kubectl expose deployment nginx-deployment --type=NodePort
```

Access the application:
```bash
kubectl port-forward service/nginx-deployment 8080:80
```

Visit `http://localhost:8080` multiple times to see the load balancing in action.

### 6. Update the Deployment
Update the nginx image to a specific version:
```bash
kubectl set image deployment/nginx-deployment nginx=nginx:1.19
```

Monitor the rollout:
```bash
kubectl rollout status deployment/nginx-deployment
```

### 7. Rollback Changes
If needed, rollback to the previous version:
```bash
kubectl rollout undo deployment/nginx-deployment
```

### 8. Clean Up
When finished, delete the deployment and service:
```bash
kubectl delete deployment nginx-deployment
kubectl delete service nginx-deployment
```

## Key Concepts

### Deployments vs Pods
- **Pods**: Basic unit of deployment in Kubernetes
- **Deployments**: Higher-level abstraction that manages multiple pods
  - Provides declarative updates
  - Handles pod replication
  - Manages rolling updates
  - Supports rollbacks

### Scaling
- Horizontal scaling adds more pod replicas
- Kubernetes automatically distributes traffic across pods
- Scaling can be done manually or automatically (HPA)

### Rolling Updates
- Zero-downtime updates
- Gradual replacement of pods
- Automatic rollback on failure
- Configurable update strategy

## Learning Outcomes
- Understanding Deployments and their benefits
- Managing application scaling
- Performing rolling updates
- Handling rollbacks
- Working with Services for load balancing

## Troubleshooting
Common issues and solutions:
1. Pods not starting:
   ```bash
   kubectl describe deployment nginx-deployment
   kubectl describe pod <pod-name>
   ```

2. Scaling issues:
   ```bash
   kubectl get events
   kubectl describe deployment nginx-deployment
   ```

3. Update failures:
   ```bash
   kubectl rollout history deployment/nginx-deployment
   kubectl rollout undo deployment/nginx-deployment
   ```

## Additional Resources
- [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Scaling Applications](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#scaling-a-deployment)
- [Rolling Updates](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-update-deployment)

