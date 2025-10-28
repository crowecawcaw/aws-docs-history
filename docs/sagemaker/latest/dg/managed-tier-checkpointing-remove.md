# Removing managed tiered

checkpointing

This section explains how to disable managed tiered checkpointing when you no longer need
it.

To disable managed tiered checkpointing, use the [`update-cluster`](../../../cli/latest/reference/sagemaker/update-cluster.md "../../../cli/latest/reference/sagemaker/update-cluster.md")
AWS CLI to update your cluster configuration:

```
aws sagemaker update-cluster \
    --cluster-name `cluster-name` \
    --tiered-storage-config '{ "Mode": "Disable" }'
```

This removes the memory management daemon from your cluster. The daemon is implemented as
a standard Kubernetes DaemonSet and follows standard Kubernetes lifecycle management.
