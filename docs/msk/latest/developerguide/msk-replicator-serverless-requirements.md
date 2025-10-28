# Supported MSK Serverless cluster

configuration

- MSK Serverless supports replication of these topic configurations for MSK Serverless target clusters during topic creation: `cleanup.policy`, `compression.type`, `max.message.bytes`, `retention.bytes`, `retention.ms`.
- MSK Serverless supports only these topic configurations during topic configuration sync: `compression.type`, `max.message.bytes`, `retention.bytes`, `retention.ms`.
- Replicator uses 83 compacted partitions on target MSK Serverless clusters. Make sure that target MSK Serverless clusters have a sufficient number of compacted partitions. See [MSK Serverless quota](limits.md#serverless-quota "limits.md#serverless-quota").

## Cluster configuration changes

- It’s recommended that you do not turn tiered storage on or off after the MSK Replicator has been created. If your target cluster is not tiered, then MSK won’t copy the tiered storage configurations, regardless of whether your source cluster is tiered or not. If you turn on tiered storage on the target cluster after Replicator is created, the Replicator needs to be recreated. If you want to copy data from a non-tiered to a tiered cluster, you should not copy topic configurations. See [Enabling and disabling
  tiered storage on an existing topic](msk-enable-disable-topic-tiered-storage-cli.md "msk-enable-disable-topic-tiered-storage-cli.md").
- Don’t change cluster configuration settings after MSK Replicator creation. Cluster configuration settings are validated during MSK Replicator creation. To avoid problems with the MSK Replicator, don’t change the following settings after the MSK Replicator is created.
  - Change MSK cluster to t3 instance type.
  - Change service execution role permissions.
  - Disable MSK multi-VPC private connectivity.
  - Change the attached cluster resource-based policy.
  - Change cluster security group rules.
