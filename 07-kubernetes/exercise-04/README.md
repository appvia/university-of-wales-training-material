# Lab 4: Troubleshooting Kubernetes Deployments

## Objective
In this lab, you will learn how to diagnose and fix common issues in Kubernetes deployments. You'll understand how to use various kubectl commands to troubleshoot problems and interpret their outputs effectively.

## Prerequisites
- Completed Labs 1-3 (Basic Pod, Deployment, and ConfigMap operations)
- A running Kubernetes cluster
- kubectl CLI tool installed and configured
- Basic understanding of YAML syntax

## Steps

### 1. Create a Broken Deployment
First, create a file named `broken-deployment.yaml` with intentional errors:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: broken-app
  labels:
    app: broken-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: broken-app
  template:
    metadata:
      labels:
        app: broken-app
    spec:
      containers:
      - name: nginx
        image: nginx:non-existent-tag  # This image doesn't exist
        ports:
        - containerPort: 80
        env:
        - name: REQUIRED_VAR
          valueFrom:
            configMapKeyRef:
              name: non-existent-config  # This ConfigMap doesn't exist
              key: SOME_KEY
```

### 2. Apply the Broken Deployment
Apply the deployment with errors:
```bash
kubectl apply -f broken-deployment.yaml
```

### 3. Diagnose the Issues
Use various kubectl commands to diagnose the problems:

Check deployment status:
```bash
kubectl get deployments
kubectl get pods
```

Describe the deployment for detailed information:
```bash
kubectl describe deployment broken-app
```

Check pod events:
```bash
kubectl get events --sort-by='.lastTimestamp'
```

View pod logs (if any pods are created):
```bash
kubectl logs <pod-name>
```

### 4. Fix the Deployment
Create a corrected version in `fixed-deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: broken-app
  labels:
    app: broken-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: broken-app
  template:
    metadata:
      labels:
        app: broken-app
    spec:
      containers:
      - name: nginx
        image: nginx:latest  # Fixed image tag
        ports:
        - containerPort: 80
        env:
        - name: REQUIRED_VAR
          value: "default-value"  # Fixed environment variable
```

### 5. Apply the Fix
Apply the corrected deployment:
```bash
kubectl apply -f fixed-deployment.yaml
```

### 6. Verify the Fix
Check that the deployment is now working:
```bash
kubectl get deployments
kubectl get pods
kubectl describe deployment broken-app
```

### 7. Clean Up
When finished, delete the deployment:
```bash
kubectl delete deployment broken-app
```

## Key Concepts

### Common Deployment Issues
1. **Image Pull Errors**
   - Non-existent image tags
   - Private registry authentication issues
   - Network connectivity problems

2. **Configuration Issues**
   - Missing ConfigMaps or Secrets
   - Invalid environment variables
   - Incorrect resource requests/limits

3. **Resource Constraints**
   - Insufficient CPU/memory
   - Node capacity issues
   - Resource quotas

### Troubleshooting Commands
1. **kubectl get**
   - Quick status overview
   - Resource state verification
   - Pod status checking

2. **kubectl describe**
   - Detailed resource information
   - Event history
   - Configuration validation
   - Error messages

3. **kubectl logs**
   - Container stdout/stderr
   - Application errors
   - Runtime issues

4. **kubectl get events**
   - Cluster-wide events
   - Chronological issue tracking
   - System-level problems

### Troubleshooting Workflow
1. Check resource status
2. Examine detailed descriptions
3. Review relevant logs
4. Analyze cluster events
5. Apply fixes
6. Verify resolution

## Learning Outcomes
- Understanding common deployment issues
- Using kubectl commands effectively
- Interpreting error messages
- Following a systematic troubleshooting approach
- Applying fixes and verifying solutions

## Troubleshooting Guide
Common issues and their solutions:

1. **ImagePullBackOff**
   ```bash
   # Check image name and tag
   kubectl describe pod <pod-name>
   # Verify image exists in registry
   docker pull <image>:<tag>
   ```

2. **CrashLoopBackOff**
   ```bash
   # Check container logs
   kubectl logs <pod-name>
   # Verify environment variables
   kubectl describe pod <pod-name>
   ```

3. **Pending State**
   ```bash
   # Check resource constraints
   kubectl describe pod <pod-name>
   # Verify node capacity
   kubectl describe nodes
   ```

## Additional Resources
- [Kubernetes Troubleshooting](https://kubernetes.io/docs/tasks/debug/)
- [Debugging Applications](https://kubernetes.io/docs/tasks/debug-application-cluster/debug-application/)
- [Troubleshooting Guide](https://kubernetes.io/docs/tasks/debug-application-cluster/debug-application-introspection/)

