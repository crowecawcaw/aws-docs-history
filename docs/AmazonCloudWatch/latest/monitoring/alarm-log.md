# Log alarms

A Log Alarm monitors the results of a CloudWatch Logs Insights query that runs on a schedule using
a [Scheduled Query](../logs/ScheduledQueries.md "../logs/ScheduledQueries.md"). The alarm
applies an aggregation expression to the query results to produce a numeric value, and when
that aggregated value breaches a configured threshold, the alarm transitions to
`ALARM` state and runs configured actions.

Unlike metric alarms that require metric filters as an intermediate step, Log Alarms
evaluate directly on log data using the same Logs Insights query language you use for ad-hoc
analysis.

## How Log Alarms work

The following steps describe how a Log Alarm works:

1. You create a Log Alarm with a query, aggregation expression, schedule, and
   threshold.
2. CloudWatch automatically creates an AWS managed Scheduled Query that runs your query on the
   specified schedule.
3. Each query execution produces aggregated results (a single value or multiple
   contributor values).
4. CloudWatch evaluates the aggregated results against your threshold using M-out-of-N
   evaluation on recent query executions.
5. If the threshold is breached, the alarm transitions to `ALARM` state
   and runs your configured actions (such as Amazon SNS notifications).

###### Note

Log Alarms evaluate the last N query executions. The alarm transitions to
`ALARM` when M of those N executions breach the threshold.

To create a Log Alarm, see [Create a Log Alarm](Alarm-On-Logs.md#Create_Log_Alarm "Alarm-On-Logs.md#Create_Log_Alarm").

## Managed Scheduled Query lifecycle

When you create a Log Alarm, CloudWatch automatically creates an AWS managed Scheduled Query
that runs your query on the specified schedule. You do not need to create the Scheduled
Query separately.

The AWS managed Scheduled Query has the following characteristics:

- It is visible in the CloudWatch Logs console under Scheduled Queries.
- You cannot modify it directly. To change the query or its configuration, update the Log Alarm.
- CloudWatch deletes the AWS managed Scheduled Query when you delete the alarm.

## Log Alarm configuration

A Log Alarm is configured with the following parameters:

- **QueryString** is the CloudWatch Logs Insights query to run.
- **LogGroupIdentifiers** are the log groups to query. Specify
  either log group names or log group ARNs.
- **ScheduledQueryRoleARN** is the ARN of the IAM role that allows
  CloudWatch Logs to run the scheduled query on your behalf.
- **AggregationExpression** defines how query results are
  aggregated into a numeric value for threshold evaluation.
- **ScheduleExpression** defines how frequently the query runs (for
  example, `rate(5 minutes)`).
- **StartTimeOffset** defines the lookback window in seconds for
  each query execution.
- **EndTimeOffset** defines the end of the query time range as an
  offset in seconds from the current time.
- **ComparisonOperator** is how aggregated results are compared to
  the threshold. Valid values: `GreaterThanThreshold`,
  `GreaterThanOrEqualToThreshold`, `LessThanThreshold`,
  `LessThanOrEqualToThreshold`.
- **Threshold** is the numeric value to compare against.
- **QueryResultsToEvaluate** is the number of recent query
  executions to evaluate (N in M-out-of-N).
- **QueryResultsToAlarm** is the number of breaching results
  required to trigger `ALARM` (M in M-out-of-N).
- **TreatMissingData** defines how missing query results are
  treated during evaluation.

For the full list of parameters and creation instructions, see [Create a Log Alarm](Alarm-On-Logs.md#Create_Log_Alarm "Alarm-On-Logs.md#Create_Log_Alarm").

## Logs query

The Log Alarm query is a CloudWatch Logs Insights query that selects and filters the log data to
evaluate. The query runs on the log groups specified in `LogGroupIdentifiers`
over the time range defined by `StartTimeOffset` and
`EndTimeOffset`.

The query uses [CloudWatch Logs Insights query
syntax](../logs/CWL_QuerySyntax.md "../logs/CWL_QuerySyntax.md"). For guidelines on writing efficient queries for Log Alarms, see [Best practices and troubleshooting](#log-alarm-best-practices "#log-alarm-best-practices").

## Aggregation expressions

The aggregation expression defines how CloudWatch summarizes query results into a numeric
value for threshold evaluation. The expression uses the same syntax as the
`stats` command in CloudWatch Logs Insights.

The syntax for an aggregation expression is as follows:

```
statistic_func_expression [by field1, field2, ...] [| sort asc|desc]
```

You can specify only a single aggregation expression. The following table lists the
supported aggregation functions.

| Function     | Description                           | Example          |
| ------------ | ------------------------------------- | ---------------- |
| `count(*)`   | Count of all matched log lines.       | `count(*)`       |
| `avg(field)` | Average value of the specified field. | `avg(duration)`  |
| `sum(field)` | Sum of the specified field.           | `sum(bytesSent)` |
| `min(field)` | Minimum value of the specified field. | `min(latency)`   |
| `max(field)` | Maximum value of the specified field. | `max(latency)`   |

The `bin()` function is not supported in the aggregation expression
`by` clause. However, you can use `bin()` in the query string
itself.

## Multi-contributor alarms

When you include a `by` clause in your aggregation expression, the alarm
evaluates each unique combination of field values (called a _contributor_)
independently. The alarm transitions to `ALARM` state if any contributor
breaches the threshold.

For example, the following expression groups error counts by service name:

```
count(*) by serviceName
```

Each unique value of `serviceName` is evaluated independently against the
threshold. If any service exceeds the threshold in M out of N query executions, the alarm
enters `ALARM` state.

The following limits apply to multi-contributor alarms:

- Maximum 5 fields in the `by` clause.
- Maximum 500 contributor results returned per query execution.
- Maximum 100 contributors tracked in `ALARM` state
  simultaneously.

By default, contributors are sorted alphabetically and only the first 500 are returned
per query execution. To sort contributors by their aggregated value instead, specify
`| sort asc` or `| sort desc` in your aggregation expression (for
example, `avg(latency) by serviceName | sort desc`). Value-based sorting ensures
that the most significant contributors are evaluated first when the total number exceeds 500.

For multi-contributor alarms, Amazon SNS and Lambda actions run at the contributor level
(once per breaching contributor). Systems Manager OpsItem actions run at the alarm level.

###### Note

Systems Manager Incident Manager and investigation actions are not
supported for Log Alarms.

If a contributor disappears from query results (for example, an ephemeral resource is
terminated), that contributor transitions to `OK` state regardless of the
missing data treatment setting.

## Missing data treatment

Missing data occurs when a scheduled query execution does not produce a value that can
be evaluated against the threshold. This happens in the following cases:

**No logs present** — The log group contains no log events
in the query time range.

**Query returns no applicable results** — Logs are present
but the aggregation expression cannot produce a value. This happens when:

- Matching query results were not present as per the query filter.
- The field referenced in the aggregation expression was not present in the query
  results. For example, `count(error-codes)` where
  `error-codes` does not exist in the returned log events.

Note that `count(*)` on an empty result set returns 0, which is a valid
datapoint and is not treated as missing.

You can configure how the alarm treats missing data using the
`TreatMissingData` parameter. The following table describes the available
options.

| Value          | Behavior                                                       |
| -------------- | -------------------------------------------------------------- |
| `missing`      | Treat the datapoint as missing. This is the default.           |
| `notBreaching` | Treat the missing datapoint as not breaching the threshold.    |
| `breaching`    | Treat the missing datapoint as breaching the threshold.        |
| `ignore`       | Ignore the missing datapoint and evaluate only available data. |

## Evaluation states

In addition to the standard `OK`, `ALARM`, and
`INSUFFICIENT_DATA` states, Log Alarms can report the following evaluation
states in the `EvaluationState` field. These states provide additional context
about why the alarm is in its current state.

| State                | Description                                                                                                                                                                                                                                                                                                                             |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `EVALUATION_FAILURE` | A transient CloudWatch service issue prevented evaluation. This can occur when the<br>service experiences issues in evaluating query results due to service errors, or<br>when some (but not all) query results failed. The alarm transitions to<br>`INSUFFICIENT_DATA`. We recommend manual monitoring until the issue is<br>resolved. |
| `EVALUATION_ERROR`   | A client configuration error prevented evaluation. This can occur due to<br>insufficient permissions, an invalid query, or when all query results have failed.<br>The alarm transitions to `INSUFFICIENT_DATA` immediately. Refer to the<br>`StateReason` field for details.                                                            |
| `PARTIAL_DATA`       | The query returned the maximum 500 contributor groups but more matched. The<br>alarm evaluates the available contributors, but results might be<br>incomplete.                                                                                                                                                                          |

## Alarm update

When you update the query, aggregation expression, schedule, or log groups of a Log
Alarm, the alarm transitions to `INSUFFICIENT_DATA` until sufficient new
datapoints are collected. Changes to the threshold or M-out-of-N values do not trigger
this reset.

## Actions and notifications

Log Alarms support the following actions:

- Amazon SNS notifications
- Lambda function invocations
- Systems Manager OpsItem creation

For the full actions support matrix, see [Alarm actions](alarm-actions.md "alarm-actions.md").

When a Log Alarm transitions state, the action notification includes the following
information:

- Standard alarm configuration change information (alarm name, description,
  configuration details).
- State change information (new state, state reason, timestamp).
- Amazon SNS email notifications also include a deep link to the CloudWatch Logs Insights console
  showing the full query results.

The following example shows an Amazon SNS email notification for a single-value Log Alarm
(without a `BY` clause):

```
{
    "AlarmName": "HighErrorCount",
    "NewStateValue": "ALARM",
    "NewStateReason": "Threshold Crossed: 3 out of the last 5 query results [142.0 (10/06/26 12:15:00), 135.0 (10/06/26 12:10:00), 120.0 (10/06/26 12:05:00)] were greater than the threshold (100.0) (minimum 3 datapoints for OK -> ALARM transition).",
    "NewStateReasonData": {
        "version": "1.0",
        "queryDate": "2026-06-10T12:15:30.000+0000",
        "threshold": 100.0,
        "queryResultsToEvaluate": 5,
        "queryResultsToAlarm": 3,
        "results": [
            {
                "queryResultId": "scheduled-query-execution-id-3",
                "status": "COMPLETE",
                "timestamp": "2026-06-10T12:15:00.000+0000",
                "value": 142.0
            }
            // Additional results...
        ]
    },
    "StateChangeTime": "2026-06-10T12:15:30.000+0000",
    "OldStateValue": "OK"
    // Additional fields...
}
```

The following example shows an Amazon SNS email notification for a multi-contributor Log Alarm
(with a `BY` clause). Each breaching contributor generates a separate
notification:

```
{
    "AlarmName": "EndpointLatency",
    "NewStateValue": "ALARM",
    "NewStateReason": "5 out of 10 contributors evaluated to ALARM",
    "StateChangeTime": "2026-06-10T12:20:15.000+0000",
    "OldStateValue": "OK",
    "AlarmContributorId": "a1b2c3d4e5f6g7h8",
    "AlarmContributorAttributes": {
        "endpoint": "/api/orders"
    }
    // Additional fields...
}
```

### Including log lines in notifications

You can optionally include raw query result log lines in alarm notifications by setting
the `ActionLogLineCount` parameter to a value between 1 and 50. These are the
underlying log events on which the aggregation expression is evaluated, not the aggregated
values. The default value is 0, which means no log lines are included.

###### Note

Log lines are included only in Amazon SNS email notifications. Lambda actions do not
include log lines in their payloads.

###### Important

Including log lines in notifications might expose sensitive data from your logs in
Amazon SNS messages. Review your log content before you enable this
feature.

To include log lines, the log lines role must have the
`logs:GetQueryResults` permission. The number of log lines included in a
notification is limited by the requested count, the total results available, and the
Amazon SNS payload size limit.

## Best practices and troubleshooting

### Best practices

**Query optimization**

- Test queries manually in CloudWatch Logs Insights before using them in a Log Alarm to verify
  performance and expected results.
- Use filter commands early in your query to reduce the volume of data
  processed.
- Limit query time ranges (StartTimeOffset) to avoid timeouts with high-volume log
  groups.
- Use field indexes to optimize query performance.

**Schedule planning**

- Choose a schedule frequency that allows queries to complete before the next
  execution. For high-volume log groups, use longer intervals (for example, 10 minutes
  instead of 5).
- Account for log ingestion delays when setting StartTimeOffset. A small gap between
  EndTimeOffset and the current time helps avoid evaluating incomplete data.
- Spread out Log Alarm schedules across your account to avoid hitting Scheduled Query
  concurrency limits. Concurrent query executions across your account cannot exceed 100.
  Factor in this quota when creating multiple Log Alarms with overlapping
  schedules.

**Threshold tuning**

- Start with higher QueryResultsToEvaluate (N) values to reduce alarm noise from
  transient spikes.
- For sparse events (such as errors that rarely occur), set TreatMissingData to
  `notBreaching` to keep the alarm in OK state when no logs match.
- For continuous signals (such as traffic logs), consider setting TreatMissingData to
  `breaching` to detect when expected log data stops arriving.

**Multi-contributor design**

- Choose meaningful fields for the BY clause that represent distinct resources or
  dimensions you want to monitor independently.
- Be aware that only the first 500 contributors are returned per query execution. If
  you expect more, narrow your query or use fewer BY clause fields.
- Use the `| sort desc` or `| sort asc` suffix in your
  aggregation expression to prioritize the highest or lowest values based on your
  comparison operator when the 500 contributor limit is reached.

### Troubleshooting

**Alarm stays in INSUFFICIENT\_DATA**

| Possible cause                                   | Resolution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scheduled query execution role lacks permissions | Verify the role has `logs:StartQuery`,<br>`logs:StopQuery`, `logs:GetQueryResults`, and<br>`logs:DescribeLogGroups` permissions scoped to the correct log<br>groups.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Log group does not exist or was deleted          | Verify the log group ARNs in the alarm configuration are correct and<br>accessible.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Recently created or updated alarm                | After creation or configuration update, the alarm remains in<br>INSUFFICIENT\_DATA until enough query executions complete to satisfy the M-out-of-N<br>evaluation window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Scheduled query is not running                   | Check the AWS managed Scheduled Query in the CloudWatch Logs console to verify it is<br>executing on schedule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Aggregation field not present in query results   | The field referenced in the aggregation expression must be present in the<br>query results. For example, if your aggregation is `avg(latency)`,<br>make sure the query produces a `latency` field. If the field is not<br>present, the result is treated as missing data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Log ingestion delay                              | A scheduled query can only evaluate log events that have been ingested<br>by the time it runs. `StartTimeOffset` and `EndTimeOffset`<br>define the query window relative to execution time T —<br>[T − StartTimeOffset, T − EndTimeOffset] — but they do not account for<br>ingestion delay. If events are still being ingested for the window you query, the<br>query runs before they are available and skips them.<br>Use `EndTimeOffset` to shift the window back far enough that<br>ingestion is complete for the entire range.<br>Example: Suppose logs take up to 2 minutes to become queryable after the<br>events occur.<br>• `StartTimeOffset=60, EndTimeOffset=0` — window [T−60s, T].<br>The window ends at execution time, so recent events are not yet ingested<br>and are missed.<br>• `StartTimeOffset=180, EndTimeOffset=120` — window<br>[T−180s, T−120s]. The window ends 2 minutes in the past, by which point<br>all events are ingested and evaluable. |

**Alarm shows EVALUATION\_ERROR**

This indicates a client configuration issue. Check the StateReason field for details.
Common causes:

- Invalid or malformed query syntax.
- Insufficient permissions on the scheduled query execution role.
- All query executions failed (for example, log group permissions revoked).

**Alarm shows EVALUATION\_FAILURE**

This indicates a transient CloudWatch service issue. The alarm automatically recovers when
the issue resolves. If it persists beyond a few minutes, check the CloudWatch service health
dashboard.

**Alarm shows PARTIAL\_DATA**

The query returned the maximum 500 contributor groups but more matched. The alarm
evaluates available contributors, but results might be incomplete. Consider narrowing your
query or reducing the number of BY clause fields.

**Log lines not appearing in notifications**

- Verify `ActionLogLineCount` is set to a value between 1 and 50.
- Verify the log lines role has `logs:GetQueryResults` permission scoped
  to the correct log groups.
- Log lines are included only in Amazon SNS email notifications. Other action types do
  not include log lines.
- Queries using `unmask()` cannot include log lines in notifications
  (rejected at creation time).

For additional best practices on query optimization, monitoring, and authorization, see
[Scheduled Queries
best practices](../logs/scheduled-queries-best-practices.md "../logs/scheduled-queries-best-practices.md") in the _Amazon CloudWatch Logs User Guide_.
