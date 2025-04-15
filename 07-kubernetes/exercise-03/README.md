# Lab 3: Managing Configurations with ConfigMaps

## Objective
In this lab, you will learn how to use ConfigMaps to manage configuration data in Kubernetes. You'll understand how to create ConfigMaps, inject them into pods, and handle configuration updates without rebuilding containers.

## Prerequisites
- Completed Lab 1 and 2 (Basic Pod and Deployment operations)
- A running Kubernetes cluster
- kubectl CLI tool installed and configured
- Basic understanding of YAML syntax

## Steps

### 1. Create a ConfigMap
First, create a file named `app-config.yaml` with the following content:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  # Simple key-value pairs
  APP_NAME: "MyApp"
  ENVIRONMENT: "development"
  
  # Configuration file content
  config.json: |
    {
      "database": {
        "host": "localhost",
        "port": 5432
      },
      "features": {
        "debug": true,
        "cache": true
      }
    }
```

Apply the ConfigMap:
```bash
kubectl apply -f app-config.yaml
```

### 2. Create a Deployment that Uses the ConfigMap
Create a file named `config-app-deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: config-app
  labels:
    app: config-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: config-app
  template:
    metadata:
      labels:
        app: config-app
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        # Inject environment variables from ConfigMap
        env:
        - name: APP_NAME
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: APP_NAME
        - name: ENVIRONMENT
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: ENVIRONMENT
        # Mount ConfigMap as a volume
        volumeMounts:
        - name: config-volume
          mountPath: /etc/app/config
      volumes:
      - name: config-volume
        configMap:
          name: app-config
```

### 3. Deploy the Application
Apply the deployment:
```bash
kubectl apply -f config-app-deployment.yaml
```

### 4. Verify the Configuration
Check that the ConfigMap was created:
```bash
kubectl get configmap app-config
```

Inspect the ConfigMap contents:
```bash
kubectl describe configmap app-config
```

### 5. Verify Configuration in the Pod
Get the pod name:
```bash
kubectl get pods
```

Check the environment variables:
```bash
kubectl exec <pod-name> -- env | grep APP
```

Verify the mounted configuration file:
```bash
kubectl exec <pod-name> -- cat /etc/app/config/config.json
```

### 6. Update the ConfigMap
Edit the ConfigMap:
```bash
kubectl edit configmap app-config
```

Or update it from a file:
```bash
kubectl apply -f app-config.yaml
```

### 7. Verify Configuration Updates
Check that the pod picked up the new configuration:
```bash
kubectl exec <pod-name> -- env | grep APP
kubectl exec <pod-name> -- cat /etc/app/config/config.json
```

### 8. Clean Up
When finished, delete the resources:
```bash
kubectl delete deployment config-app
kubectl delete configmap app-config
```

## Key Concepts

### ConfigMaps
- Store non-confidential data in key-value pairs
- Can contain entire configuration files
- Can be mounted as volumes or injected as environment variables
- Updates are automatically propagated to pods

### Configuration Management
- Separate configuration from container image
- Enable configuration changes without rebuilding containers
- Support different configurations for different environments
- Maintain configuration versioning

### Best Practices
- Use ConfigMaps for non-sensitive data
- Keep configurations in version control
- Use meaningful key names
- Document configuration options
- Consider using ConfigMap generators

## Learning Outcomes
- Understanding ConfigMaps and their purpose
- Creating and managing configuration data
- Injecting configurations into pods
- Handling configuration updates
- Following configuration management best practices

## Troubleshooting
Common issues and solutions:
1. ConfigMap not found:
   ```bash
   kubectl get configmap app-config
   kubectl describe configmap app-config
   ```

2. Configuration not updated:
   ```bash
   kubectl describe pod <pod-name>
   kubectl get events
   ```

3. Volume mount issues:
   ```bash
   kubectl exec <pod-name> -- ls -la /etc/app/config
   ```

## Additional Resources
- [Kubernetes ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
- [Configure Pods Using ConfigMaps](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)
- [ConfigMap Best Practices](https://kubernetes.io/docs/concepts/configuration/configmap/#configmap-best-practices)

