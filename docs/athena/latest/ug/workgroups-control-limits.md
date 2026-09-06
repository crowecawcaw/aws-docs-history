

# Use CloudWatch and EventBridge to monitor queries and control costs
<a name="workgroups-control-limits"></a>

Workgroups allow you to set data usage control limits per query or per workgroup, set up alarms when those limits are exceeded, and publish query metrics to CloudWatch.

In each workgroup, you can:
+ Configure **Data usage controls** per query and per workgroup, and establish actions that will be taken if queries breach the thresholds.
+ View and analyze query metrics, and publish them to CloudWatch. If you create a workgroup in the console, the setting for publishing the metrics to CloudWatch is selected for you. If you use the API operations, you must [enable publishing the metrics](athena-cloudwatch-metrics-enable.md). When metrics are published, they are displayed under the **Metrics** tab in the **Workgroups** panel. Metrics are disabled by default for the primary workgroup. 

## Video
<a name="athena-cloudwatch-metrics-video"></a>

The following video shows how to create custom dashboards and set alarms and triggers on metrics in CloudWatch. You can use pre-populated dashboards directly from the Athena console to consume these query metrics.

[![AWS Videos](http://img.youtube.com/vi/x1V_lhkdKCg/0.jpg)](http://www.youtube.com/watch?v=x1V_lhkdKCg)


**Topics**
+ [Video](#athena-cloudwatch-metrics-video)
+ [Enable query metrics](athena-cloudwatch-metrics-enable.md)
+ [Monitor query metrics with CloudWatch](query-metrics-viewing.md)
+ [Monitor usage metrics with CloudWatch](monitoring-athena-usage-metrics.md)
+ [Monitor query events with EventBridge](athena-events.md)
+ [Configure data usage controls](workgroups-setting-control-limits-cloudwatch.md)