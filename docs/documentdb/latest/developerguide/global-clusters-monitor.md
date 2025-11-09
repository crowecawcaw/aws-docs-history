# Monitoring Amazon DocumentDB global clusters

Amazon DocumentDB (with MongoDB compatibility) integrates with CloudWatch so that you can gather and
analyze operational metrics for your clusters. You can monitor these metrics using the CloudWatch
console, the Amazon DocumentDB console, the AWS Command Line Interface (AWS CLI), or the CloudWatch API.

To monitor a global cluster, use the following CloudWatch metrics.

| Metric                           | Description                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GlobalClusterReplicatedWriteIO` | The average number of billed write I/O operations replicated from the<br>cluster volume in the primary AWS Region to the cluster volume in a secondary<br>AWS Region, reported at 5-minute intervals. The number of replicated<br>`ReplicatedWriteIOs` to each secondary region is the same as the<br>number of in-region `VolumeWriteIOPs` performed by the primary<br>region. |
| `GlobalClusterDataTransferBytes` | The amount of data transferred from the primary cluster’s AWS Region to a<br>secondary cluster’s AWS Region, measure in bytes.                                                                                                                                                                                                                                                  |
| `GlobalClusterReplicationLag`    | The amount of lag, in milliseconds, when replicating change events from the<br>primary cluster’s AWS Region to a secondary cluster’s AWS Region                                                                                                                                                                                                                                 |

For more information on how to view these metrics, please see [Viewing CloudWatch data](cloud_watch.md#cloud_watch-view_data "cloud_watch.md#cloud_watch-view_data").
