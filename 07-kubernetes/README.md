# Kubernetes Labs

## Prerequisites

- kubectl CLI tool installed and configured
- wayfinder cli (for authentication into the cluster) 

```bash
curl -fsSLo ./wf.tgz https://storage.googleapis.com/wayfinder-releases/v2.9.7/wf-cli-darwin-amd64.tar.gz && tar -xzf ./wf.tgz -C . && rm ./wf.tgz
sudo mv ./wf-cli-darwin-amd64 /usr/local/bin/wf
```

- Basic understanding of YAML syntax
- Completed previous labs in sequence (each lab builds upon the previous ones)

> A Kubernetes cluster will be provided in the lab environment

## Lab Structure

The labs are designed to be completed in sequence:

1. Lab 1: Basic Pod operations
2. Lab 2: Deployments and scaling
3. Lab 3: ConfigMaps and configuration management
4. Lab 4: Troubleshooting and debugging

## Getting Started

### Login to the Cluster

After installing the wayfinder cli, open a terminal and run the following commands:

```bash
wf login -a https://api.wfdemo.appvia.io
wf access env test <your-name>
```
