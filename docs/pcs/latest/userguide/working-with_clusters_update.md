

# Updating a cluster in AWS PCS
<a name="working-with_clusters_update"></a>

AWS PCS lets you update cluster configurations after creation through the UpdateCluster API or console. You can modify cluster settings without rebuilding your infrastructure, which reduces operational overhead and minimizes interruptions.

## Benefits of cluster updates
<a name="update-cluster-benefits"></a>

Updating AWS PCS clusters lets you adapt HPC infrastructure to new requirements without service disruption. Configuration changes take minutes instead of the hour or more needed to rebuild clusters. This capability is important for production environments that require minimal downtime and for teams that need to adjust cluster settings as workload patterns change.

## Supported configuration changes
<a name="update-cluster-supported-settings"></a>

You can modify four main categories of settings:
+ **Scheduler version** - Update to a newer supported scheduler version. For more information, see [Updating the scheduler version of a cluster in AWS PCS](working-with_clusters_version_update.md).
+ **Accounting configuration** - Enable or disable managed accounting and configure retention settings.
+ **Scale-down behavior** - Adjust the `scaleDownIdleTime` parameter, which controls how long dynamic instances remain idle before AWS PCS automatically terminates them.
+ **Slurm custom settings** - Modify any of the supported Slurm settings that apply at the cluster level, including Prolog, Epilog, and SelectTypeParameters.

## Limitations
<a name="update-cluster-limitations"></a>

You cannot modify certain configurations after cluster creation. These include:
+ Security group configurations
+ VPC subnet selection
+ Cluster size
+ Cluster name

These settings are foundational to the cluster's architecture and require creating a new cluster to modify them. To update the scheduler version, see [Updating the scheduler version of a cluster in AWS PCS](working-with_clusters_version_update.md).

## Prerequisites for cluster updates
<a name="update-cluster-prerequisites"></a>

Before updating a cluster, ensure the following conditions are met:
+ Cluster must be in `ACTIVE`, `UPDATE_FAILED`, or `SUSPENDED` state
+ All associated resources (Queues, Compute Node Groups) must be in `ACTIVE` state
+ You must have appropriate IAM permissions for the UpdateCluster operation
+ No other update operations can be in progress

## Update process and job impact
<a name="update-cluster-process"></a>

During an update operation, compute nodes continue to run existing jobs even when the cluster controller becomes briefly unreachable. However, the system cannot accept new job submissions or make scheduling decisions during this period.

You can monitor cluster updates through both the console and API interfaces. The cluster will transition through the following states during an update:
+ `UPDATING` - Update in progress
+ `ACTIVE` - Update completed successfully
+ `UPDATE_FAILED` - Update encountered an error

## Billing during updates
<a name="update-cluster-billing"></a>

Standard hourly charges for your AWS PCS cluster continue during update operations. When you update a cluster to disable accounting, billing for the accounting feature stops as soon as the cluster enters the `UPDATING` state. When enabling accounting, billing doesn't begin until the cluster successfully completes the update and returns to the `ACTIVE` state.

**Topics**
+ [Benefits of cluster updates](#update-cluster-benefits)
+ [Supported configuration changes](#update-cluster-supported-settings)
+ [Limitations](#update-cluster-limitations)
+ [Prerequisites for cluster updates](#update-cluster-prerequisites)
+ [Update process and job impact](#update-cluster-process)
+ [Billing during updates](#update-cluster-billing)
+ [Update an AWS PCS cluster](working-with_clusters_update_procedure.md)
+ [Updating the scheduler version of a cluster in AWS PCS](working-with_clusters_version_update.md)
+ [Frequently asked questions about updating clusters in AWS PCS](working-with_clusters_update_faq.md)
+ [Troubleshooting AWS PCS cluster updates](working-with_clusters_update_troubleshooting.md)