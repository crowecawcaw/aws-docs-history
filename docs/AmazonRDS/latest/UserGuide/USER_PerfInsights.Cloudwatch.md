# Amazon CloudWatch metrics for Amazon RDS Performance Insights

Performance Insights automatically publishes some metrics to Amazon CloudWatch. The same data can be
queried from Performance Insights, but having the metrics in CloudWatch makes it easy to add CloudWatch
alarms. It also makes it easy to add the metrics to existing CloudWatch Dashboards.

| Metric                   | Description                                                                                                                                                                                |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| DBLoad                   | The number of active sessions for the database. Typically, you want the data for the average number of active sessions.<br>In Performance Insights, this data is queried as `db.load.avg`. |
| DBLoadCPU                | The number of active sessions where the wait event type is CPU. In Performance Insights, this data is queried as `db.load.avg`,<br>filtered by the wait event type `CPU`.                  |
| DBLoadNonCPU             | The number of active sessions where the wait event type is not CPU.                                                                                                                        |
| DBLoadRelativeToNumVCPUs | The ratio of the DB load to the number of virtual CPUs for the database.                                                                                                                   |

###### Note

These metrics are published to CloudWatch only if there is load on the DB instance.

You can examine these metrics using the CloudWatch console, the AWS CLI, or the CloudWatch API. You can
also examine other Performance Insights counter metrics using a special metric math
function. For more information, see [Querying other Performance Insights counter metrics in CloudWatch](#USER_PerfInsights.Cloudwatch.ExtraMetrics "#USER_PerfInsights.Cloudwatch.ExtraMetrics").

For example, you can get the statistics for the `DBLoad` metric by running the [get-metric-statistics](../../../cli/latest/reference/cloudwatch/get-metric-statistics.md "../../../cli/latest/reference/cloudwatch/get-metric-statistics.md") command.

```
aws cloudwatch get-metric-statistics \
    --region us-west-2 \
    --namespace AWS/RDS \
    --metric-name DBLoad  \
    --period 60 \
    --statistics Average \
    --start-time 1532035185 \
    --end-time 1532036185 \
    --dimensions Name=DBInstanceIdentifier,Value=db-loadtest-0
```

This example generates output similar to the following.

```
{
		"Datapoints": [
		{
		"Timestamp": "2021-07-19T21:30:00Z",
		"Unit": "None",
		"Average": 2.1
		},
		{
		"Timestamp": "2021-07-19T21:34:00Z",
		"Unit": "None",
		"Average": 1.7
		},
		{
		"Timestamp": "2021-07-19T21:35:00Z",
		"Unit": "None",
		"Average": 2.8
		},
		{
		"Timestamp": "2021-07-19T21:31:00Z",
		"Unit": "None",
		"Average": 1.5
		},
		{
		"Timestamp": "2021-07-19T21:32:00Z",
		"Unit": "None",
		"Average": 1.8
		},
		{
		"Timestamp": "2021-07-19T21:29:00Z",
		"Unit": "None",
		"Average": 3.0
		},
		{
		"Timestamp": "2021-07-19T21:33:00Z",
		"Unit": "None",
		"Average": 2.4
		}
		],
		"Label": "DBLoad"
		}

```

For more information about CloudWatch, see [What is Amazon CloudWatch?](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") in the _Amazon CloudWatch User Guide_.

## Querying other Performance Insights counter metrics in CloudWatch

###### Note

If you enable the Advanced mode of Database Insights, Amazon RDS publishes Performance Insights counter metrics to Amazon CloudWatch. With Database Insights, you don't need to use the `DB_PERF_INSIGHTS` metric math function. You can use the CloudWatch Database Insights dashboard to search, query, and set alarms for Performance Insights counter metrics.

You can query, alarm, and graphs on RDS Performance Insights metrics from CloudWatch.
You can access information about your
DB instance by using the `DB_PERF_INSIGHTS` metric math function for CloudWatch.
This function allows you to use the Performance Insights metrics
that are not directly reported to CloudWatch to create a new time series.

You can use the new Metric Math function by clicking on the **Add Math** drop-down menu in the **Select metric** screen in the CloudWatch console.
You can use it to create alarms and graphs on Performance Insights metrics or on combinations of CloudWatch and Performance Insights metrics,
including high-resolution alarms for sub-minute metrics.
You can also use the function programmatically by including the Metric Math expression in a [`get-metric-data`](../../../cli/latest/reference/cloudwatch/get-metric-data.md "../../../cli/latest/reference/cloudwatch/get-metric-data.md") request.
For more information, see [Metric math syntax and functions](../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md#metric-math-syntax-functions-list "../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md#metric-math-syntax-functions-list") and
[Create an alarm on Performance Insights counter metrics from an AWS database](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_alarm_database_performance_insights.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_alarm_database_performance_insights.md").
