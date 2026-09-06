

# CloudWatch events and metrics from Amazon EMR
<a name="emr-manage-cluster-cloudwatch"></a>

Use events and metrics to track the activity and health of an Amazon EMR cluster. Events are useful for monitoring a specific occurrence within a cluster - for example, when a cluster changes state from starting to running. Metrics are useful to monitor a specific value - for example, the percentage of available disk space that HDFS is using within a cluster.

For more information about CloudWatch Events, see the [Amazon CloudWatch Events User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/). For more information about CloudWatch metrics, see [Using Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) and [Creating Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

**Topics**
+ [Monitoring Amazon EMR metrics with CloudWatch](UsingEMR_ViewingMetrics.md)
+ [Monitoring Amazon EMR events with CloudWatch](emr-manage-cloudwatch-events.md)
+ [Responding to CloudWatch events from Amazon EMR](emr-events-response.md)