# Lab 1: Deploying Your First Pod

## Objective
In this lab, you will learn how to deploy your first Kubernetes pod using kubectl and YAML manifests. You'll understand basic pod operations and how to interact with your deployed application.

## Prerequisites
- A running Kubernetes cluster (local or cloud-based)
- kubectl CLI tool installed and configured
- Basic understanding of YAML syntax

## Steps

### 1. Create a Pod Manifest
First, create a file named `nginx-pod.yaml` with the following content:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
  - name: nginx
    image: nginx:latest
    ports:
    - containerPort: 80
```

### 2. Deploy the Pod
Use kubectl to create the pod using the YAML manifest:
```bash
kubectl apply -f nginx-pod.yaml
```

### 3. Verify Pod Status
Check the status of your pod:
```bash
kubectl get pods
```

You should see your nginx-pod in the list. The status should change to "Running" once the container is fully started.

### 4. Investigate Pod Details
Get detailed information about your pod:
```bash
kubectl describe pod nginx-pod
```

This command will show you:
- Pod IP address
- Container status
- Events related to the pod
- Resource requests and limits
- Volume mounts (if any)

### 5. Access the Pod
To access the nginx web server running in your pod, use port forwarding:
```bash
kubectl port-forward nginx-pod 8080:80
```

Now you can access the nginx welcome page by opening:
```
http://localhost:8080
```

### 6. Clean Up
When you're done, delete the pod:
```bash
kubectl delete pod nginx-pod
```

## Learning Outcomes
- Understanding basic pod concepts
- Working with YAML manifests
- Using kubectl commands for pod management
- Accessing applications running in pods
- Basic troubleshooting with kubectl describe

## Troubleshooting
If your pod is not starting:
1. Check the pod status with `kubectl get pods`
2. Use `kubectl describe pod nginx-pod` to see detailed error messages
3. Check container logs with `kubectl logs nginx-pod`
4. Verify your cluster is running with `kubectl cluster-info`

## Additional Resources
- [Kubernetes Pod Documentation](https://kubernetes.io/docs/concepts/workloads/pods/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [YAML Syntax Guide](https://yaml.org/spec/1.2/spec.html)

