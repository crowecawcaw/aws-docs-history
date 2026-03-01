# Use CloudWatch and EventBridge to monitor queries and control costs

Workgroups allow you to set data usage control limits per query or per workgroup, set up
alarms when those limits are exceeded, and publish query metrics to CloudWatch.

In each workgroup, you can:

- Configure **Data usage controls** per query and per workgroup,
  and establish actions that will be taken if queries breach the thresholds.
- View and analyze query metrics, and publish them to CloudWatch. If you create a
  workgroup in the console, the setting for publishing the metrics to CloudWatch is selected
  for you. If you use the API operations, you must [enable publishing the metrics](athena-cloudwatch-metrics-enable.md "athena-cloudwatch-metrics-enable.md").
  When metrics are published, they are displayed under the
  **Metrics** tab in the **Workgroups** panel.
  Metrics are disabled by default for the primary workgroup.

## Video

The following video shows how to create custom dashboards and set alarms and triggers
on metrics in CloudWatch. You can use pre-populated dashboards directly from the Athena console
to consume these query metrics.

###### Topics

- [Enable query metrics](athena-cloudwatch-metrics-enable.md "athena-cloudwatch-metrics-enable.md")
- [Monitor query metrics with CloudWatch](query-metrics-viewing.md "query-metrics-viewing.md")
- [Monitor usage metrics with CloudWatch](monitoring-athena-usage-metrics.md "monitoring-athena-usage-metrics.md")
- [Monitor query events with EventBridge](athena-events.md "athena-events.md")
- [Configure data usage controls](workgroups-setting-control-limits-cloudwatch.md "workgroups-setting-control-limits-cloudwatch.md")
