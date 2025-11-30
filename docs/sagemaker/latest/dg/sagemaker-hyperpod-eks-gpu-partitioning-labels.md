# Node Lifecycle and Labels

Amazon SageMaker HyperPod performs deep health checks on cluster instances during the creation and update of HyperPod clusters before GPU partitioning begins. HyperPod health-monitoring agent continuously monitors the health status of GPU partitioned instances.

## MIG Configuration States

Nodes with GPU partition configuration go through several states:

- **Pending** - Node is being configured with a MIG profile
- **Configuring** - GPU Operator is applying MIG partitioning
- **Success** - GPU partitioning completed successfully
- **Failed** - GPU partitioning encountered an error

## Monitoring Node States

```
# Check node health status
kubectl get nodes -l sagemaker.amazonaws.com/node-health-status=Schedulable

# Monitor MIG configuration progress
kubectl get node `NODE_NAME` -o jsonpath='{.metadata.labels.nvidia\.com/mig\.config\.state}'

# Check for configuration errors
kubectl describe node `NODE_NAME` | grep -A 5 "Conditions:"
```

## Custom Labels and Taints

You can manage MIG configuration with custom labels and taints to label your GPU partitions and apply them across instances:

```
{
  "KubernetesConfig": {
    "Labels": {
      "nvidia.com/mig.config": "all-2g.10gb",
      "task-type": "inference",
      "environment": "production"
    },
    "Taints": [
      {
        "Key": "gpu-task",
        "Value": "mig-enabled",
        "Effect": "NoSchedule"
      }
    ]
  }
}
```
