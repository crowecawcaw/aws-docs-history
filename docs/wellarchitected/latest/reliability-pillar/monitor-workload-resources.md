# Monitor workload resources

Logs and metrics are powerful tools to gain insight into the
health of your workload. You can configure your workload to
monitor logs and metrics and send notifications when thresholds
are crossed or significant events occur. Monitoring allows your
workload to recognize when low-performance thresholds are crossed
or failures occur, so it can recover automatically in response.

Monitoring is critical to ensure that you are meeting your
availability requirements. Your monitoring needs to effectively
detect failures. The worst failure mode is the “silent” failure,
where the functionality is no longer working, but there is no way
to detect it except indirectly. Your customers know before you do.
Alerting when you have problems is one of the primary reasons you
monitor. Your alerting should be decoupled from your systems as
much as possible. If your service interruption removes your
ability to alert, you will have a longer period of interruption.

At AWS, we instrument our applications at multiple levels. We
record latency, error rates, and availability for each request,
for all dependencies, and for key operations within the process.
We record metrics of successful operation as well. This allows us
to see impending problems before they happen. We don’t just
consider average latency. We focus even more closely on latency
outliers, like the 99.9th and 99.99th percentile. This is because
if one request out of 1,000 or 10,000 is slow, that is still a
poor experience. Also, although your average may be acceptable, if
one in 100 of your requests causes extreme latency, it will
eventually become a problem as your traffic grows.

Monitoring at AWS consists of four distinct phases:

1. Generation — Monitor all components for the workload
2. Aggregation — Define and calculate metrics
3. Real-time processing and alarming — Send notifications and automate responses
4. Storage and Analytics

###### Best practices

- [REL06-BP01 Monitor all components for the workload
  (Generation)](rel_monitor_aws_resources_monitor_resources.md "rel_monitor_aws_resources_monitor_resources.md")
- [REL06-BP02 Define and calculate metrics (Aggregation)](rel_monitor_aws_resources_notification_aggregation.md "rel_monitor_aws_resources_notification_aggregation.md")
- [REL06-BP03 Send notifications (Real-time processing and
  alarming)](rel_monitor_aws_resources_notification_monitor.md "rel_monitor_aws_resources_notification_monitor.md")
- [REL06-BP04 Automate responses (Real-time processing and
  alarming)](rel_monitor_aws_resources_automate_response_monitor.md "rel_monitor_aws_resources_automate_response_monitor.md")
- [REL06-BP05 Analyze logs](rel_monitor_aws_resources_storage_analytics.md "rel_monitor_aws_resources_storage_analytics.md")
- [REL06-BP06 Regularly review monitoring scope and
  metrics](rel_monitor_aws_resources_review_monitoring.md "rel_monitor_aws_resources_review_monitoring.md")
- [REL06-BP07 Monitor end-to-end tracing of requests through your
  system](rel_monitor_aws_resources_end_to_end.md "rel_monitor_aws_resources_end_to_end.md")
