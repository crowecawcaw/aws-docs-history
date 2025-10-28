# Definition of a metric for MediaConnect datapoints

AWS Elemental MediaConnect collects data that is the basis for metrics. It collects these _datapoints_ every second and sends them immediately to
Amazon CloudWatch. You can use CloudWatch to generate _metrics_
for these datapoints.

A metric is a collection of datapoints that has had an aggregation (a _statistic_) applied and that has a _period_ and a _time
range_. For example, you can request the Dropped packets metric as an
average (the statistic) for a 1 minute period over 10 minutes (the time range). This
result of this request is 10 metrics (because the range divided by the period is
10).

## Period

Most MediaConnect metrics have a _high resolution
period_, which means that the minimum period is one second. MediaConnect Gateway
metrics are the only metrics not available in a high resolution period.

## Time range

Each period has a _maximum time range_. For
example, if you specify 1 day as the time range, you won't be able to retrieve
metrics with a 10 second period.

| Period                          | Maximum time range            |
| ------------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 second                        | The last 3 hours              |
| 5 seconds                       |                               | 10 seconds                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 30 seconds                      |
| 60 seconds                      | The last 360 hours (15 days)  |
| 300 seconds (5 minutes)         | The last 1512 hours (63 days) |
| 900 seconds (15 minutes)        |
| 3600 seconds (1 hour) or longer | The last 455 days (15 months) | Periods don't have a _minimum time range_. But there is a point where the statistic you apply becomes meaningless if you have a low period. For example, assume that you set the period to one second. This means that CloudWatch retrieves one datapoint. You can't obtain an average, a minimum or a maximum on one datapoint. However, this doesn't mean that the metric is meaningless. Instead, the metric is for the raw datapoint, with no statistic. ## Maximum storage time Metrics are available for the last 15 months. Make sure that you specify a period that allows the time range that you want. |
