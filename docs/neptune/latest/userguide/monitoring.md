# Monitoring Amazon Neptune resources

Amazon Neptune supports various methods for monitoring database performance and usage:

- **Instance status** – Check the health of a Neptune
  cluster's graph database engine, find out what version of the engine is installed,
  and obtain other instance-related information using the [instance
  status API](access-graph-status.md "access-graph-status.md").
- **Graph summary API** – The [graph summary API](neptune-graph-summary.md "neptune-graph-summary.md") lets you quickly get a
  high-level understanding of your graph data size and content.

###### Note

Because the graph summary API relies on [DFE
statistics](neptune-dfe-statistics.md "neptune-dfe-statistics.md"), it's only available when statistics are enabled, which
is not the case on T3 and T4g instance types.

- **Amazon CloudWatch** – Neptune automatically sends metrics to
  CloudWatch and also supports CloudWatch Alarms. For more information, see [Monitoring Neptune Using Amazon CloudWatch](cloudwatch.md "cloudwatch.md").
- **Audit log files** – View, download, or watch
  database log files using the Neptune console. For more information, see [Using Audit Logs with Amazon Neptune Clusters](auditing.md "auditing.md").
- **Publishing logs to Amazon CloudWatch Logs** –
  You can configure a Neptune DB cluster to publish audit log data to a log group in
  Amazon CloudWatch Logs. With CloudWatch Logs, you can perform real-time analysis of the log data, use
  CloudWatch to create alarms and view metrics, and use CloudWatch Logs to store your log records
  in highly durable storage. See [Neptune CloudWatch Logs](cloudwatch-logs.md "cloudwatch-logs.md").
- **AWS CloudTrail** – Neptune supports API logging using CloudTrail.
  For more information, see [Logging Amazon Neptune API Calls with AWS CloudTrail](cloudtrail.md "cloudtrail.md").
- **Event notification subscriptions** –
  Subscribe to Neptune events to stay informed about what is happening. For more information, see [Using Neptune Event Notification](events.md "events.md").
- **Tagging** – Use tags to add metadata to your
  Neptune resources and track usage based on tags. For more information, see [Tagging Amazon Neptune resources](tagging.md "tagging.md").

###### Topics

- [Check the Health Status of a Neptune Instance](access-graph-status.md "access-graph-status.md")
- [Monitoring Neptune Using Amazon CloudWatch](cloudwatch.md "cloudwatch.md")
- [Using Audit Logs with Amazon Neptune Clusters](auditing.md "auditing.md")
- [Publishing Neptune Logs to Amazon CloudWatch Logs](cloudwatch-logs.md "cloudwatch-logs.md")
- [Enabling Amazon CloudWatch Logs for a Neptune notebook](notebook-logs.md "notebook-logs.md")
- [Using Amazon Neptune slow-query logging](slow-query-logs.md "slow-query-logs.md")
- [Logging Amazon Neptune API Calls with AWS CloudTrail](cloudtrail.md "cloudtrail.md")
- [Using Neptune Event Notification](events.md "events.md")
- [Tagging Amazon Neptune resources](tagging.md "tagging.md")
