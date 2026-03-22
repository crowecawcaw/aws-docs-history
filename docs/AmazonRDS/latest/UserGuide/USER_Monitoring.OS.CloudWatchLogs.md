# Viewing OS metrics using CloudWatch Logs

After you have enabled Enhanced Monitoring for your DB instance or Multi-AZ DB cluster, you can view the metrics for it
using CloudWatch Logs, with each log stream representing a single DB instance or DB cluster being monitored. The log stream identifier is the
resource identifier (`DbiResourceId`) for the DB instance or DB cluster.

###### To view Enhanced Monitoring log data

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. If necessary, choose the AWS Region that your DB instance or Multi-AZ DB cluster is in. For more information, see [Regions and endpoints](../../../general/latest/gr/index.md "../../../general/latest/gr/index.md") in the
   _Amazon Web Services General Reference_.
3. Choose **Logs** in the navigation pane.
4. Choose **RDSOSMetrics** from the list of log groups.

In a Multi-AZ DB instance deployment, log files with `-secondary` appended to the name are
for the Multi-AZ standby replica.

![Multi-AZ standby replica log file](images/enhanced-monitoring-cloudwatch-secondary.png) 5. Choose the log stream that you want to view from the list of log streams.
