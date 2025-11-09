# Create a CloudWatch alarm based on a Metrics

Insights query

A CloudWatch Metrics Insights query helps you
query metrics at scale using SQL-like syntax. You can create an alarm on any Metrics Insights
query, including queries that return multiple time series. This capability significantly
expands your monitoring options. When you create an alarm based on a Metrics Insights query,
the alarm automatically adjusts as resources are added to or removed from your monitored
group. Create the alarm once, and any resource that matches your query definition and filters
joins the alarm monitoring scope when its corresponding metric becomes available. For
multi-time series queries, each returned time series becomes a contributor to the alarm,
allowing for more granular and dynamic monitoring.

Here are two primary use cases for CloudWatch Metrics Insights alarms:

- Outlier Detection and Aggregate Monitoring

Create an alarm on a Metrics Insights query that returns a single aggregated time
series. This approach works well for dynamic alarms that monitor aggregated metrics across
your infrastructure or applications. For example, you can monitor the maximum CPU
utilization across all your instances, with the alarm automatically adjusting as you scale
your fleet.

To create an aggregate monitoring alarm, use this query structure:

```
SELECT FUNCTION(metricName)
FROM SCHEMA(...)
WHERE condition;
```

- Per-Resource Fleet Monitoring

Create an alarm that monitors multiple time series, where each time series functions
as a contributor with its own state. The alarm activates when any contributor enters the
ALARM state, triggering resource-specific actions. For example, monitor database
connections across multiple RDS instances to prevent connection rejections.

To monitor multiple time series, use this query structure:

```
SELECT AVG(DatabaseConnections)
FROM AWS/RDS
WHERE condition
GROUP BY DBInstanceIdentifier
ORDER BY AVG() DESC;
```

When creating multi-time series alarms, you must include two key clauses in your
query:

    + A `GROUP BY` clause that defines how to structure the time series and
     determines how many time series the query will produce
    + An `ORDER BY` clause that establishes a deterministic sorting of your
     metrics, enabling the alarm to evaluate the most important signals first

These clauses are essential for proper alarm evaluation. The `GROUP BY`
clause splits your data into separate time series (for example, by instance ID), while the
`ORDER BY` clause ensures consistent and prioritized processing of these time
series during alarm evaluation.

## Limits that apply to alarms based on Metrics Insights queries

When working with CloudWatch Metrics Insights alarms, be aware of these functional
limits:

- 200 alarms using this syntax per account per Region
- Only the latest 3 hours of data can be used for evaluating the alarm's conditions.
  However, you can visualize up to two weeks of data on the alarm's detail page
  graph
- Alarms evaluating multiple time series will limit the rate of concurrent transitions
  to 100
- Metrics Insights limits on the maximum number of time series analyzed or returned
  apply

For more information on CloudWatch service quotas and limits, see [CloudWatch service
quotas](cloudwatch_limits.md "cloudwatch_limits.md").

## Prerequisites

Before creating a CloudWatch Metrics Insights alarm, ensure you have:

- Appropriate IAM permissions to create and manage CloudWatch alarms
- Metrics available in your AWS account for the resources you want to monitor
- Basic understanding of SQL query syntax
