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

- A default of 200 alarms using the Metrics Insights query per account per Region
- Only the latest 3 hours of data can be used for evaluating the alarm's conditions.
  However, you can visualize up to two weeks of data on the alarm's detail page
  graph
- Alarms evaluating multiple time series will limit the rate of concurrent transitions
  to 100
  - Assuming the query retrieves 150 time series:
    - If there are fewer than 100 contributors in ALARM (for example 95), the `StateReason`
      will be "95 out of 150 time series evaluated to ALARM"
    - If there are more than 100 contributors in ALARM, for example 105, the `StateReason`
      will be "100+ time series evaluated to ALARM"

  - Furthermore, based on the size of the Alarm contributor data, the `StateReason` can be
    truncated to display fewer time series data. Assuming we truncate to 85 contributors,
    the `StateReason` will be:
    - If there are fewer than 100 contributors in ALARM (for example 95) - truncated to 85,
      the `StateReason` will be "85+ out of 150 time series evaluated to ALARM".
    - If there are more than 100 contributors in ALARM (for example 105) - truncated to 85,
      the `StateReason` will be "85+ time series evaluated to ALARM".

- Metrics Insights limits on the maximum number of time series analyzed or returned
  apply
- During alarm evaluation, the `EvaluationState` will be set to
  `PARTIAL_DATA` for the following limits:
  - If the Metrics Insights query returns more than 500 time series.
  - If the Metrics Insights query matches more than 10,000 metrics.

For more information on CloudWatch service quotas and limits, see [CloudWatch Metrics Insights service
quotas](cloudwatch-metrics-insights-limits.md "cloudwatch-metrics-insights-limits.md").

## Missing Data in CloudWatch Metrics Insights alarms

**Alarms based on Metrics Insights queries that aggregate to a
single time series**

The missing data scenarios and their effects upon alarm evaluation are the same as a standard
metric alarm in terms of the configured missing data treatment. See, [metric alarm missing data](AlarmThatSendsEmail.md#alarms-and-missing-data "AlarmThatSendsEmail.md#alarms-and-missing-data").

**Alarms based on Metrics Insights queries that produce multiple time series**

Missing data scenarios for Metrics Insights alarms occur when:

- Individual datapoints within a time series are not present.
- One or more time series disappear when evaluating upon multiple time series.
- No time series are retrieved by the query.

Missing data scenarios affect the alarm evaluation in the following manner:

- For the evaluation of a time series, the treat missing data treatment is applied for individual
  datapoints within the time series. For example, if 3 datapoints were queried for the time series but
  only 1 was received, 2 datapoints would follow the configured missing data configuration.
- If a time series is not retrieved by the query anymore, it will transition to `OK` no matter
  the treat missing data treatment. Alarm actions associated with the `OK` transition at the
  contributor level are executed and the `StateReason` specifies that the aforementioned
  contributor was not found with the message, "No data was returned for this contributor".
  The state of the alarm will depend on the state of the other contributors that were
  retrieved by the query.
- At alarm level, if the query returns an empty result (no time series at all), the treat missing
  data treatment is applied. For example, if the treat missing data was set as `BREACHING`,
  the alarm will transition to `ALARM`.

## Prerequisites

Before creating a CloudWatch Metrics Insights alarm, ensure you have:

- Appropriate IAM permissions to create and manage CloudWatch alarms
- Metrics available in your AWS account for the resources you want to monitor
- Basic understanding of SQL query syntax
