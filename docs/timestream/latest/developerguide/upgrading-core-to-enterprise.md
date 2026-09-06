

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Upgrade from Core to Enterprise edition
<a name="upgrading-core-to-enterprise"></a>

You can upgrade an existing InfluxDB 3 Core cluster to Enterprise edition to gain access to features such as multi-node deployments, long-term data retention, and dedicated compaction.

**Important**  
Upgrading from Core to Enterprise is a **one-way operation**. Once a cluster is upgraded to Enterprise, it cannot be reverted to Core edition.

## Prerequisites and requirements
<a name="core-to-enterprise-prerequisites"></a>
+ **First-time Enterprise activation**: If this is the first time you are activating an Enterprise license on your AWS account, the upgrade must be performed through the AWS Management Console. This one-time console activation enables Enterprise capabilities for your account.
+ **Subsequent operations**: After the initial console activation, your account is enabled for Enterprise. You can then upgrade additional Core clusters to Enterprise or deploy new Enterprise clusters using the AWS CLI, API, or the AWS Management Console.

## Upgrade using the AWS Management Console
<a name="core-to-enterprise-console"></a>

1. Sign in to the AWS Management Console and open the Timestream for InfluxDB console.

1. In the navigation pane, choose **InfluxDB Databases**.

1. Select the Core cluster you want to upgrade.

1. Choose **Modify**.

1. For **Edition**, select **Enterprise**.

1. Review the changes and choose **Modify cluster**.

## What happens during the upgrade
<a name="core-to-enterprise-what-happens"></a>

When you upgrade a Core cluster to Enterprise:

1. **Cluster restart**: The cluster restarts to apply the Enterprise engine configuration.

1. **Node configuration**: Depending on your cluster node count, the cluster will be configured as either:
   + A single-node Enterprise cluster (all-in-one: writer, reader, and compactor on one node)
   + A multi-node Enterprise cluster with a dedicated compactor (for clusters with 3 or more nodes)

1. **Data compaction**: Your existing data will be gradually compacted in the background by the Enterprise compaction engine. The cluster remains usable during this process.

**Note**  
The time required for data compaction to catch up depends on the volume of existing data, the cluster size, instance size, and the available CPU and memory headroom relative to your current workload.

**Important**  
**Capacity considerations for compaction after upgrade**  
**Single-node clusters**: When upgrading a Core single-node cluster to Enterprise, the compactor runs on the same node as the writer and reader. Because Core does not include a compactor, all existing data must be compacted after the upgrade. This requires additional CPU and memory capacity beyond what your current workload uses. If the node does not have sufficient headroom, compaction may compete with your read and write workloads, potentially impacting performance. Consider scaling up to a larger instance type (for example, from `db.influx.xlarge` to `db.influx.2xlarge`) before or immediately after the upgrade to give the compactor the resources it needs. You can scale back down after compaction catches up.
**Multi-node (3-node) clusters**: When upgrading to a 3-node Enterprise cluster, a dedicated compactor node is provisioned. However, the full benefits of Enterprise—such as optimized query performance from compacted data—will not be realized until the compactor finishes processing all pre-existing data. The time this takes depends on the volume of data already in the database, the current running workload, and the instance size and configuration of the compactor node.

**Tuning compaction performance**: To help the compactor process existing data faster, you can adjust the following Enterprise-only parameters in your parameter group:
+ `compaction-max-num-files-per-plan` – Increase this value to allow the compactor to process more files per compaction cycle. For example, increase from the default of 500 to 1000–5000 on larger instances (db.influx.4xlarge and above). See [`compaction-max-num-files-per-plan`](compaction-max-num-files-per-plan.md) for recommended values by instance size.
+ `compaction-check-interval` – Reduce from the default of 10 seconds to 5 seconds on db.influx.4xlarge and above to make the compactor evaluate work more frequently.

For single-node clusters, scaling up the instance type is the most effective way to give the compactor more capacity, since all roles share the same node's resources. For multi-node clusters, the dedicated compactor node uses the same instance class as the other nodes, so scaling the cluster's instance type also increases compactor capacity. For full details on compaction parameters, see [Category 4: Compaction](compaction-parameters.md).

## Considerations
<a name="core-to-enterprise-considerations"></a>
+ This is a one-way upgrade. You **cannot** downgrade from Enterprise to Core.
+ Plan the upgrade during a period of lower activity to allow the compaction process sufficient CPU and memory headroom to catch up.
+ **Single-node clusters**: Consider temporarily scaling up to a larger instance type before upgrading to ensure the compactor has enough CPU and memory to compact existing data without impacting your workload.
+ **Multi-node clusters**: Expect a transition period after upgrading where the compactor is processing all pre-existing data. Full Enterprise performance benefits are realized after compaction completes. The duration depends on data volume, workload intensity, and instance size.
+ You can speed up post-upgrade compaction by increasing `compaction-max-num-files-per-plan` and reducing `compaction-check-interval` in your parameter group. See [Category 4: Compaction](compaction-parameters.md) for details.
+ After upgrading, you can take advantage of Enterprise features such as [Scaling a cluster](multi-node-scaling.md) to scale your cluster horizontally.