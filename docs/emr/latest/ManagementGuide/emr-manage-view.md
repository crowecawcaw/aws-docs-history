# View and monitor an Amazon EMR cluster as it performs work

Amazon EMR provides several tools you can use to gather information about your cluster. You
can access information about the cluster from the console, the CLI or programmatically.
The standard Hadoop web interfaces and log files are available on the primary node. You
can also use monitoring services such as CloudWatch and
Ganglia to track the performance of your cluster.

Application history is also available from the console using the "persistent"
application UIs for Spark History Server starting with Amazon EMR 5.25.0. With Amazon
EMR 6.x, persistent YARN timeline server, and Tez user interfaces are also available.
These services are hosted off-cluster, so you can access application history for 30 days
after the cluster terminates, without the need for a SSH connection or web proxy. See
[View application
history](emr-cluster-application-history.md "emr-cluster-application-history.md").

###### Topics

- [View Amazon EMR cluster status and details](emr-manage-view-clusters.md "emr-manage-view-clusters.md")
- [Enhanced step debugging with Amazon EMR](emr-enhanced-step-debugging.md "emr-enhanced-step-debugging.md")
- [View Amazon EMR application history](emr-cluster-application-history.md "emr-cluster-application-history.md")
- [View Amazon EMR log files](emr-manage-view-web-log-files.md "emr-manage-view-web-log-files.md")
- [View cluster instances in Amazon EC2](UsingEMR_Tagging.md "UsingEMR_Tagging.md")
- [CloudWatch events and metrics from Amazon EMR](emr-manage-cluster-cloudwatch.md "emr-manage-cluster-cloudwatch.md")
- [View cluster application metrics using Ganglia with Amazon EMR](ViewingGangliaMetrics.md "ViewingGangliaMetrics.md")
- [Logging AWS EMR API calls using
  AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [EMR Observability Best Practices](emr-metrics-observability.md "emr-metrics-observability.md")
