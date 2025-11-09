Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Performance metrics in the CloudWatch

console

When working with Amazon Redshift metrics in the CloudWatch console, keep a couple of things in
mind:

- Query and load performance data is only available in the Amazon Redshift
  console.
- Some Metrics in the CloudWatch have different units than those used in the Amazon Redshift
  console. For example, `WriteThroughput` is displayed in GB/s (as
  compared to Bytes/s in CloudWatch), which is a more relevant unit for the typical
  storage space of a node.
  When working with Amazon Redshift metrics in the CloudWatch console, command line tools, or an
  Amazon SDK, keep these concepts in mind:

1. First, specify the metric dimension to work with. A dimension is a name-value
   pair that helps you to uniquely identify a metric. The dimensions for Amazon Redshift
   are `ClusterIdentifier` and `NodeID`. In the CloudWatch console,
   the `Redshift Cluster` and `Redshift Node` views are
   provided to easily select cluster and node-specific dimensions. For more
   information about dimensions, see [Dimensions](../../../AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.md#Dimension "../../../AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.md#Dimension") in
   the _CloudWatch Developer Guide_.
2. Then, specify the metric name, such as `ReadIOPS`.
   The following table summarizes the types of Amazon Redshift metric dimensions that are
   available to you. Depending on the metric, data is available in either 1-minute or
   5-minute intervals at no charge. For more information, see [Amazon Redshift metrics](metrics-listing.md#redshift-metrics "metrics-listing.md#redshift-metrics").

| CloudWatch namespace | Dimension           | Description                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AWS/Redshift`       | `NodeID`            | Filters requested data that is specific to the nodes of a cluster.<br>`NodeID` is either "Leader", "Shared", or "Compute-N"<br>where N is 0, 1, ... for the number of nodes in the cluster.<br>"Shared" means that the cluster has only one node, that is the<br>leader node and compute node are combined.                                                                                                                               |
| `AWS/Redshift`       | `ClusterIdentifier` | Filters requested data that is specific to the cluster. Metrics<br>that are specific to clusters include `HealthStatus`,<br>`MaintenanceMode`, and<br>`DatabaseConnections`. General metrics for this<br>dimension (for example, `ReadIOPS`) that are also metrics<br>of nodes represent an aggregate of the node metric data. Take care<br>in interpreting these metrics because they aggregate behavior of<br>leader and compute nodes. |

Working with gateway and volume metrics is similar to working with other service
metrics. Many of the common tasks are outlined in the CloudWatch documentation, including the
following:

- [View available
  metrics](../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md "../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md")
- [Get statistics for a
  metric](../../../AmazonCloudWatch/latest/monitoring/getting-metric-statistics.md "../../../AmazonCloudWatch/latest/monitoring/getting-metric-statistics.md")
- [Creating CloudWatch
  alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
