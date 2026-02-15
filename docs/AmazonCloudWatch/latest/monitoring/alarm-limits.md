# Limits

## General CloudWatch quotas

For information about general CloudWatch service quotas that apply to alarms, see [CloudWatch service quotas](cloudwatch_limits.md "cloudwatch_limits.md").

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

## Limits that apply to alarms based on connected data

sources

- When CloudWatch evaluates an alarm, it does so every minute, even if the period for the
  alarm is longer than one minute. For the alarm to work, the Lambda function must be
  able to return a list of timestamps starting on any minute, not only on multiples of
  the period length. These timestamps must be spaced one period length apart.

Therefore, if the data source queried by the Lambda can only return timestamps that
are multiples of the period length, the function should "re-sample" the fetched data
to match the timestamps expected by the `GetMetricData` request.

For example, an alarm with a five-minute period is evaluated every minute using
five-minute windows that shift by one minute each time. In this case:

    + For the alarm evaluation at 12:15:00, CloudWatch expects data points with timestamps
     of `12:00:00`, `12:05:00`, and `12:10:00`.
    + Then for the alarm evaluation at 12:16:00, CloudWatch expects data points with
     timestamps of `12:01:00`, `12:06:00`, and
     `12:11:00`.

- When CloudWatch evaluates an alarm, any data points returned by the Lambda function that
  don't align with the expected timestamps are dropped, and the alarm is evaluated using
  the remaining expected data points. For example, when the alarm is evaluated at
  `12:15:00` it expects data with timestamps of `12:00:00`,
  `12:05:00`, and `12:10:00`. If it receives data with
  timestamps of `12:00:00`, `12:05:00`, `12:06:00`, and
  `12:10:00`, the data from `12:06:00` is dropped and CloudWatch
  evaluates the alarm using the other timestamps.

Then for the next evaluation at `12:16:00`, it expects data with
timestamps of `12:01:00`, `12:06:00`, and `12:11:00`.
If it only has the data with timestamps of `12:00:00`,
`12:05:00`, and `12:10:00`, all of these data points are
ignored at 12:16:00 and the alarm transitions into the state according to how you
specified the alarm to treat missing data. For more information, see [Alarm evaluation](alarm-evaluation.md "alarm-evaluation.md").

- We recommend that you create these alarms to take actions when they transition to
  the `INSUFFICIENT_DATA` state, because several Lambda function failure use
  cases will transition the alarm to `INSUFFICIENT_DATA` regardless of the
  way that you set the alarm to treat missing data.
- If the Lambda function returns an error:
  - If there is a permission problem with calling the Lambda function, the alarm
    begins having missing data transitions according to how you specified the alarm to
    treat missing data when you created it.
  - Any other error coming from the Lambda function causes the alarm to transition
    to `INSUFFICIENT_DATA`.

- If the metric requested by the Lambda function has some delay so that the last data
  point is always missing, you should use a workaround. You can create an M out of N
  alarm or increase the evaluation period of the alarm. For more information about M out
  of N alarms, see [Alarm evaluation](alarm-evaluation.md "alarm-evaluation.md").
