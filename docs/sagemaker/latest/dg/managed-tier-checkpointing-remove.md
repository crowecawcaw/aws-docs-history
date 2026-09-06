

# Removing managed tiered checkpointing
<a name="managed-tier-checkpointing-remove"></a>

This section explains how to disable managed tiered checkpointing when you no longer need it.

To disable managed tiered checkpointing, use the [`update-cluster`](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/update-cluster.html) AWS CLI to update your cluster configuration:

```
aws sagemaker update-cluster \
    --cluster-name {{cluster-name}} \
    --tiered-storage-config '{ "Mode": "Disable" }'
```

This removes the memory management daemon from your cluster. The daemon is implemented as a standard Kubernetes DaemonSet and follows standard Kubernetes lifecycle management.