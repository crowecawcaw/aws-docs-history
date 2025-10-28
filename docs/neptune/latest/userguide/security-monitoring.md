# Logging and monitoring usage and performance in Amazon Neptune

Amazon Neptune supports various methods for monitoring performance and usage:

- **Cluster status** – Check the health of a Neptune
  cluster's graph database engine. For more information, see [Check the Health Status of a Neptune Instance](access-graph-status.md "access-graph-status.md").
- **Amazon CloudWatch** – Neptune automatically sends metrics to
  CloudWatch and also supports CloudWatch Alarms. For more information, see [Monitoring Neptune Using Amazon CloudWatch](cloudwatch.md "cloudwatch.md").
- **Audit log files** – View, download, or watch
  database log files using the Neptune console. For more information, see [Using Audit Logs with Amazon Neptune Clusters](auditing.md "auditing.md").
- **Publishing logs to Amazon CloudWatch Logs** – You can configure a
  Neptune DB cluster to publish audit log data to a log group in Amazon CloudWatch Logs. With CloudWatch Logs, you
  can perform real-time analysis of the log data, use CloudWatch to create alarms and view metrics,
  and use CloudWatch Logs to store your log records in highly durable storage. For more information, see
  [Neptune CloudWatch Logs](cloudwatch-logs.md "cloudwatch-logs.md").
- **AWS CloudTrail** – Neptune supports API logging using CloudTrail.
  For more information, see [Logging Amazon Neptune API Calls with AWS CloudTrail](cloudtrail.md "cloudtrail.md").
- **Tagging** – Use tags to add metadata to your
  Neptune resources and track usage based on tags. For more information, see [Tagging Amazon Neptune resources](tagging.md "tagging.md").
