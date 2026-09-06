

# Monitoring Amazon DocumentDB global clusters
<a name="global-clusters-monitor"></a>

Amazon DocumentDB (with MongoDB compatibility) integrates with CloudWatch so that you can gather and analyze operational metrics for your clusters. You can monitor these metrics using the CloudWatch console, the Amazon DocumentDB console, the AWS Command Line Interface (AWS CLI), or the CloudWatch API.

To monitor a global cluster, use the following CloudWatch metrics.


| Metric | Description | 
| --- | --- | 
| GlobalClusterReplicatedWriteIO | The average number of billed write I/O operations replicated from the cluster volume in the primary AWS Region to the cluster volume in a secondary AWS Region, reported at 5-minute intervals. The number of replicated ReplicatedWriteIOs to each secondary Region is the same as the number of in-Region VolumeWriteIOPs performed by the primary Region. | 
| GlobalClusterDataTransferBytes | The amount of data transferred from the primary cluster’s AWS Region to a secondary cluster’s AWS Region, measure in bytes. | 
| GlobalClusterReplicationLag | The amount of lag, in milliseconds, when replicating change events from the primary cluster’s AWS Region to a secondary cluster’s AWS Region | 

For more information on how to view these metrics, see [Viewing CloudWatch data](https://docs.aws.amazon.com/documentdb/latest/devguide/cloud_watch.html#cloud_watch-view_data).