# Alarms on CloudWatch Metrics Insights queries in CloudWatch

You can create alarms on Metrics Insights queries. This helps you have alarms that track
multiple resources without needing to be updated later. The query catches new resources and
resources that change. For example, you can create an alarm that watches the CPU utilization
of your fleet, and the alarm automatically evaluates new instances that you launch after
creating the alarm.

In a monitoring account that is set up for CloudWatch cross-account observability, your
Metrics Insights alarms can watch resources in source accounts and in the monitoring account
itself. For more information about how to limit your alarm queries to a specific account or
to group the results by account ID, see the `WHERE` and `GROUP BY`
sections in [Query components and syntax in
CloudWatch Metrics Insights](cloudwatch-metrics-insights-querylanguage.md "cloudwatch-metrics-insights-querylanguage.md").

**Using tags in alarm queries**

You can create alarms on Metrics Insights queries that use AWS resource tags to filter and group metrics. To use tags with alarms, on the [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/ "https://console.aws.amazon.com/connect/"), choose **Settings**. On the **CloudWatch Settings** page, under **Enable resource tags on telemetry**, choose
**Enable**.
Context-aware alarms monitor specific applications, environments, or teams automatically as resources change.

For example, you can create an alarm that monitors CPU utilization for all Amazon EC2 instances tagged with a specific application.

```
SELECT MAX(CPUUtilization) FROM "AWS/EC2" WHERE tag.Application = 'Orders' AND tag.Environment = 'Prod'
```

Tag-based alarms automatically adapt as you add or remove resources with matching tags, providing dynamic monitoring aligned with your operational structure.

###### Contents

- [Creating a Metrics Insights
  CloudWatch alarm](cloudwatch-metrics-insights-alarm-create.md "cloudwatch-metrics-insights-alarm-create.md")
