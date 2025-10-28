# Create a CloudWatch alarm based on a Metrics

Insights query

A CloudWatch Metrics Insights query helps you
query metrics at scale using SQL-like syntax. You can create an alarm on any Metrics
Insights query, including queries that return multiple time series. This capability
significantly expands your monitoring options. When you create an alarm based on a Metrics
Insights query, the alarm automatically adjusts as resources are added to or removed from
your monitored group. Create the alarm once, and any resource that matches your query
definition and filters joins the alarm monitoring scope when its corresponding metric
becomes available. For multi-time series queries, each returned time series becomes a
contributor to the alarm, allowing for more granular and dynamic monitoring.

Here are two primary use cases for CloudWatch Metrics Insights alarms:

- Outlier Detection and Aggregate Monitoring

Create an alarm on a Metrics Insights query that returns a single aggregated time
series. This approach works well for dynamic alarms that monitor aggregated metrics
across your infrastructure or applications. For example, you can monitor the maximum CPU
utilization across all your instances, with the alarm automatically adjusting as you
scale your fleet.

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
clause splits your data into separate time series (for example, by instance ID), while
the `ORDER BY` clause ensures consistent and prioritized processing of these
time series during alarm evaluation.

## Limits that apply to alarms based on Metrics Insights queries

CloudWatch Metrics Insights alarms use queries to evaluate multiple metrics and time series simultaneously. These alarms have specific limits that affect how your queries are processed and what data is available for alarm evaluation.

CloudWatch Metrics Insights alarms have the following limits:

- **Account limit**: 200 alarms per account per Region
- **Data evaluation window**: Only the most recent 3 hours of data is used for alarm evaluation
  - Note: The alarm detail page can display up to 2 weeks of historical data for visualization

- **Transition rate limiting**: Alarms monitoring multiple time series are limited to 100 concurrent state transitions
- **Query processing limits**: These limits apply at different stages of query execution:
  - **Input processing**: A Metrics Insights query can process no more than 10,000 metrics. If your query matches more than 10,000 metrics (for example, across thousands of EC2 instances), the query will only process the first 10,000 metrics that it finds
  - **Output results**: If your processed query would normally return more than 500 result rows, CloudWatch caps the results at 500. Since alarms require an ORDER BY clause, you'll receive the 500 highest or lowest results based on your sorting configuration

Understanding these limits helps you design effective queries. For instance, if you're monitoring a large fleet, consider using more specific filters to stay within the 10,000 metric processing limit, or use aggregation functions to reduce the number of result rows returned.

For more information on Metrics Insights queries quotas and limits, see [Metrics Insights quotas](cloudwatch-metrics-insights-limits.md "cloudwatch-metrics-insights-limits.md").

## Prerequisites

Before creating a CloudWatch Metrics Insights alarm, ensure you have:

- Appropriate IAM permissions to create and manage CloudWatch alarms
- Metrics available in your AWS account for the resources you want to
  monitor
- Basic understanding of SQL query syntax
