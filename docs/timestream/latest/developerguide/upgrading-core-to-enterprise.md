For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Upgrade from Core to Enterprise edition

You can upgrade an existing InfluxDB 3 Core cluster to Enterprise edition to gain access to
features such as multi-node deployments, long-term data retention, and dedicated compaction.

###### Important

Upgrading from Core to Enterprise is a **one-way operation**.
Once a cluster is upgraded to Enterprise, it cannot be reverted to Core edition.

## Prerequisites and requirements

- **First-time Enterprise activation**: If this is the first
  time you are activating an Enterprise license on your AWS account, the upgrade must be
  performed through the AWS Management Console. This one-time console activation enables Enterprise
  capabilities for your account.
- **Subsequent operations**: After the initial console
  activation, your account is enabled for Enterprise. You can then upgrade additional Core
  clusters to Enterprise or deploy new Enterprise clusters using the AWS CLI, API, or the
  AWS Management Console.

## Upgrade using the AWS Management Console

1. Sign in to the AWS Management Console and open the Timestream for InfluxDB console.
2. In the navigation pane, choose **InfluxDB Databases**.
3. Select the Core cluster you want to upgrade.
4. Choose **Modify**.
5. For **Edition**, select **Enterprise**.
6. Review the changes and choose **Modify cluster**.

## What happens during the upgrade

When you upgrade a Core cluster to Enterprise:

1. **Cluster restart**: The cluster restarts to apply the
   Enterprise engine configuration.
2. **Node configuration**: Depending on your cluster node
   count, the cluster will be configured as either:
   - A single-node Enterprise cluster (all-in-one: writer, reader, and compactor on one
     node)
   - A multi-node Enterprise cluster with a dedicated compactor (for clusters with 3 or
     more nodes)

3. **Data compaction**: Your existing data will be gradually
   compacted in the background by the Enterprise compaction engine. The cluster remains usable
   during this process.

###### Note

The time required for data compaction to catch up depends on the volume of existing data,
the cluster size, instance size, and the available CPU and memory headroom relative to your
current workload.

## Considerations

- This is a one-way upgrade. You **cannot** downgrade from
  Enterprise to Core.
- Plan the upgrade during a period of lower activity to allow the compaction process
  sufficient CPU and memory headroom to catch up.
- After upgrading, you can take advantage of Enterprise features such as
  [Scaling a cluster](multi-node-scaling.md "multi-node-scaling.md") to scale your cluster horizontally.
