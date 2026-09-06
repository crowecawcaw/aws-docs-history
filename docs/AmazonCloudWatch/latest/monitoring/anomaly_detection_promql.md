# Anomaly detection using PromQL

You can build anomaly detection bands for any Prometheus-compatible metric by using
standard PromQL functions such as `quantile_over_time`,
`stddev_over_time`, and `avg_over_time`. This approach computes a
baseline and adds or subtracts a scaled standard deviation to define upper and lower bounds
that adapt to your metric's natural patterns.

This works for any metric that returns a float value, such as CPU usage, request latency,
or error counts. For information about ingesting metrics using OpenTelemetry, see [OpenTelemetry](CloudWatch-OpenTelemetry-Sections.md "CloudWatch-OpenTelemetry-Sections.md").

## Defining upper and lower bounds

To define an expected range for a metric, compute a baseline using the median or average
over a time window, then add and subtract a multiple of the standard deviation. The
multiplier controls sensitivity—higher values produce wider bands with fewer false
positives, while lower values catch smaller deviations.

The following example creates an upper bound for an ad request metric using a 60-minute
window and a multiplier of 3:

```
quantile_over_time(0.5, {"app.ads.ad_requests"}[60m] offset 1m)
  + 3 * stddev_over_time({"app.ads.ad_requests"}[60m] offset 1m)
```

The following example creates the corresponding lower bound. The `clamp_min`
function prevents the lower bound from going negative for metrics that can't have negative
values:

```
clamp_min(
    quantile_over_time(0.5, {"app.ads.ad_requests"}[60m] offset 1m)
    - 3 * stddev_over_time({"app.ads.ad_requests"}[60m] offset 1m),
0)
```

You can graph both bounds together in CloudWatch Query Studio to visualize the expected range
for your metric. For more information, see [Running PromQL queries in Query Studio](CloudWatch-PromQL-QueryStudio.md "CloudWatch-PromQL-QueryStudio.md").

## Detecting breaches

To detect when a metric is outside its expected range, combine both bounds into a single
query. The following expression returns only the data points where the metric value exceeds
the upper bound or falls below the lower bound:

```
1 * {"app.ads.ad_requests"} > quantile_over_time(0.5, {"app.ads.ad_requests"}[60m] offset 1m)
    + 3 * stddev_over_time({"app.ads.ad_requests"}[60m] offset 1m)
or
1 * {"app.ads.ad_requests"} < clamp_min(
    quantile_over_time(0.5, {"app.ads.ad_requests"}[60m] offset 1m)
    - 3 * stddev_over_time({"app.ads.ad_requests"}[60m] offset 1m),
0)
```

This query works across multiple label values, so you can detect anomalies across your
entire fleet in a single query. You can use this expression to create a PromQL alarm that
triggers when any time series breaches the expected range. For more information, see [Creating a CloudWatch alarm using PromQL for anomaly detection](CloudWatch-PromQL-Alarms.md#promql_alarm_anomaly_detection "CloudWatch-PromQL-Alarms.md#promql_alarm_anomaly_detection").
