# CloudWatch events and metrics from Amazon EMR

Use events and metrics to track the activity and health of an Amazon EMR cluster. Events are
useful for monitoring a specific occurrence within a cluster - for example, when a cluster
changes state from starting to running. Metrics are useful to monitor a specific value - for
example, the percentage of available disk space that HDFS is using within a cluster.

For more information about CloudWatch Events, see the [Amazon CloudWatch Events User Guide](../../../AmazonCloudWatch/latest/events.md "../../../AmazonCloudWatch/latest/events.md"). For more information about CloudWatch
metrics, see [Using Amazon CloudWatch
metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md") and [Creating Amazon CloudWatch
alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the _Amazon CloudWatch User Guide_.

###### Topics

- [Monitoring Amazon EMR metrics with CloudWatch](UsingEMR_ViewingMetrics.md "UsingEMR_ViewingMetrics.md")
- [Monitoring Amazon EMR events with CloudWatch](emr-manage-cloudwatch-events.md "emr-manage-cloudwatch-events.md")
- [Responding to CloudWatch events from Amazon EMR](emr-events-response.md "emr-events-response.md")
