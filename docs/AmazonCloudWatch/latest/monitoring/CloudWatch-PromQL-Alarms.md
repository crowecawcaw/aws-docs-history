# Using PromQL in alarms

You can create CloudWatch alarms that use PromQL queries to monitor your metrics. PromQL alarms
evaluate a PromQL expression and trigger alarm state changes based on the query results.

For information about alarm concepts, see [Concepts](alarm-concepts.md "alarm-concepts.md").

For information about alarm data queries, see [Alarm data queries](alarm-data-queries.md "alarm-data-queries.md").

For information about alarm actions, see [Alarm actions](alarm-actions.md "alarm-actions.md").

For information about alarm limits, see [Limits](alarm-limits.md "alarm-limits.md").

## Creating a PromQL alarm

You can create a PromQL alarm from the CloudWatch console, the AWS CLI, or the CloudWatch API.

###### To create a PromQL alarm from the console

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, **All alarms**.
3. Choose **Create alarm**.
4. Choose **Select metric**, then choose the **PromQL** tab.
5. Enter your PromQL query. The query must return a single time series for the alarm to evaluate.
6. Configure the alarm conditions, including the threshold, evaluation period, and datapoints to alarm.
7. Configure the alarm actions, such as Amazon SNS notifications.
8. Enter a name and description for the alarm, then choose **Create alarm**.

You can also create a PromQL alarm directly from [Running PromQL queries in Query Studio](CloudWatch-PromQL-QueryStudio.md "CloudWatch-PromQL-QueryStudio.md") after running a query that returns a single time series.

## Creating a CloudWatch alarm using PromQL for anomaly detection

You can create a PromQL alarm that triggers when a metric breaches an expected range
defined by statistical bounds. The alarm query combines upper and lower bounds into a
single expression that returns only the anomalous data points. Any time series returned
by the query is considered breaching.

The following example expression detects when an ad request metric exceeds 3 standard
deviations from the median over a 60-minute window:

```
1 * {"app.ads.ad_requests"} > quantile_over_time(0.5, {"app.ads.ad_requests"}[60m] offset 1m)
    + 3 * stddev_over_time({"app.ads.ad_requests"}[60m] offset 1m)
or
1 * {"app.ads.ad_requests"} < clamp_min(
    quantile_over_time(0.5, {"app.ads.ad_requests"}[60m] offset 1m)
    - 3 * stddev_over_time({"app.ads.ad_requests"}[60m] offset 1m),
0)
```

This expression works across multiple label values, so the alarm can track anomalies
across your entire fleet. Each breaching time series is tracked as a separate
contributor. For more information about how PromQL alarms evaluate contributors, see
[PromQL alarms](alarm-promql.md "alarm-promql.md").

You can adjust the multiplier and time window to match your metric's behavior. A
higher multiplier produces wider bounds with fewer false positives. A longer time window
smooths out short-term spikes. The `clamp_min` function prevents the lower
bound from going negative for metrics that can't have negative values.

For more information about building anomaly detection bands with PromQL, see [Anomaly detection using PromQL](anomaly_detection_promql.md "anomaly_detection_promql.md").
