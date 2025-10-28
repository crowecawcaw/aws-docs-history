# Troubleshooting custom Slurm settings in AWS PCS

If you encounter errors when creating or updating AWS PCS resources with Slurm custom settings, you can use logging to diagnose and resolve the issues.

## Troubleshooting incompatible Slurm custom settings

**Problem:** You receive an error message similar to the following when performing cluster, compute node group, or queue operations:

```
{OPERATION} failed. The Slurm custom settings of the cluster might be incompatible. Check the settings and try again.
```

This error can occur with the following operations:

- CreateCluster
- CreateComputeNodeGroup
- UpdateComputeNodeGroup
- CreateQueue
- UpdateQueue

**Solution:** Enable logging to understand the specific issue and troubleshoot the incompatible settings.

###### To troubleshoot incompatible Slurm custom settings

1. Create the cluster if it doesn't exist yet, or ensure your existing cluster is in a state where logging can be enabled.
2. Enable logging for your cluster. For detailed instructions, see [Logging and monitoring for AWS PCS](monitoring-overview.md "monitoring-overview.md").

###### Note

Logging can be enabled once the cluster is in creation. 3. Review the logs to identify the specific Slurm configuration issue causing the incompatibility. 4. Correct the incompatible custom settings based on the log information and retry the operation.

For information about supported Slurm custom settings, see:

- [Custom Slurm settings for AWS PCS clusters](slurm-custom-settings-cluster.md "slurm-custom-settings-cluster.md")
- [Custom Slurm settings for AWS PCS compute node groups](slurm-custom-settings-cng.md "slurm-custom-settings-cng.md")
- [Custom Slurm settings for AWS PCS queues](slurm-custom-settings-queue.md "slurm-custom-settings-queue.md")
