# Updating a cluster in AWS PCS

AWS PCS lets you update cluster configurations after creation through the UpdateCluster API or console. You can modify cluster settings without rebuilding your infrastructure, which reduces operational overhead and minimizes interruptions.

## Benefits of cluster updates

Updating AWS PCS clusters lets you adapt HPC infrastructure to new requirements without service disruption. Configuration changes take minutes instead of the hour or more needed to rebuild clusters. This capability is important for production environments that require minimal downtime and for teams that need to adjust cluster settings as workload patterns change.

## Supported configuration changes

You can modify three main categories of settings:

- **Accounting configuration** - Enable or disable managed accounting and configure retention settings.
- **Scale-down behavior** - Adjust the `scaleDownIdleTime` parameter, which controls how long dynamic instances remain idle before AWS PCS automatically terminates them.
- **Slurm custom settings** - Modify any of the supported Slurm settings that apply at the cluster level, including Prolog, Epilog, and SelectTypeParameters.

## Limitations

You cannot modify certain configurations after cluster creation. These include:

- Security group configurations
- VPC subnet selection
- Cluster size
- Slurm version
- Cluster name

These settings are foundational to the cluster's architecture and require creating a new cluster to modify them.

## Prerequisites for cluster updates

Before updating a cluster, ensure the following conditions are met:

- Cluster must be in `ACTIVE`, `UPDATE_FAILED`, or `SUSPENDED` state
- All associated resources (Queues, Compute Node Groups) must be in `ACTIVE` state
- You must have appropriate IAM permissions for the UpdateCluster operation
- No other update operations can be in progress

## Update process and job impact

During an update operation, compute nodes continue to run existing jobs even when the cluster controller becomes briefly unreachable. However, the system cannot accept new job submissions or make scheduling decisions during this period.

You can monitor cluster updates through both the console and API interfaces. The cluster will transition through the following states during an update:

- `UPDATING` - Update in progress
- `ACTIVE` - Update completed successfully
- `UPDATE_FAILED` - Update encountered an error

## Billing during updates

Standard hourly charges for your AWS PCS cluster continue during update operations. When you update a cluster to disable accounting, billing for the accounting feature stops as soon as the cluster enters the `UPDATING` state. When enabling accounting, billing doesn't begin until the cluster successfully completes the update and returns to the `ACTIVE` state.

###### Topics

- [Update an AWS PCS cluster](working-with_clusters_update_procedure.md "working-with_clusters_update_procedure.md")
- [Frequently asked questions about updating clusters in AWS PCS](working-with_clusters_update_faq.md "working-with_clusters_update_faq.md")
- [Troubleshooting AWS PCS cluster updates](working-with_clusters_update_troubleshooting.md "working-with_clusters_update_troubleshooting.md")
