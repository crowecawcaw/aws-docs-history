# Monitor the Kinesis Producer Library with

Amazon CloudWatch

The [Amazon Kinesis Producer Library](../../../kinesis/latest/dev/developing-producers-with-kpl.md "../../../kinesis/latest/dev/developing-producers-with-kpl.md") (KPL) for Amazon Kinesis Data Streams publishes custom Amazon CloudWatch metrics on your
behalf. You can view these metrics by navigating to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/") and choosing
**Custom Metrics**. For more information about custom metrics, see
[Publish Custom Metrics](../../../AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.md "../../../AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.md") in
the _Amazon CloudWatch User Guide_.

There is a nominal charge for the metrics uploaded to CloudWatch by the KPL; specifically,
Amazon CloudWatch Custom Metrics and Amazon CloudWatch API Requests charges apply. For
more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"). Local metrics gathering does not incur CloudWatch
charges.

###### Topics

- [Metrics, dimensions, and namespaces](#kpl-metrics "#kpl-metrics")
- [Metric level and granularity](#kpl-metrics-granularity "#kpl-metrics-granularity")
- [Local access and Amazon CloudWatch upload](#kpl-metrics-local-upload "#kpl-metrics-local-upload")
- [List of metrics](#kpl-metrics-list "#kpl-metrics-list")

## Metrics, dimensions, and namespaces

You can specify an application name when launching the KPL, which is then used
as part of the namespace when uploading metrics. This is optional; the KPL
provides a default value if an application name is not set.

You can also configure the KPL to add arbitrary additional dimensions to the
metrics. This is useful if you want finer-grained data in your CloudWatch metrics. For
example, you can add the hostname as a dimension, which then allows you to identify
uneven load distributions across your fleet. All KPL configuration settings are
immutable, so you can't change these additional dimensions after the KPL instance
is initialized.

## Metric level and granularity

There are two options to control the number of metrics uploaded to CloudWatch:

_metric level_

This is a rough gauge of how important a metric is. Every metric is
assigned a level. When you set a level, metrics with levels below that
are not sent to CloudWatch. The levels are `NONE`,
`SUMMARY`, and `DETAILED`. The default setting
is `DETAILED`; that is, all metrics. `NONE` means
no metrics at all, so no metrics are actually assigned to that
level.

_granularity_

This controls whether the same metric is emitted at additional levels
of granularity. The levels are `GLOBAL`, `STREAM`,
and `SHARD`. The default setting is `SHARD`, which
contains the most granular metrics.

When `SHARD` is chosen, metrics are emitted with the stream
name and shard ID as dimensions. In addition, the same metric is also
emitted with only the stream name dimension, and the metric without the
stream name. This means that, for a particular metric, two streams with
two shards each will produce seven CloudWatch metrics: one for each shard, one
for each stream, and one overall; all describing the same statistics but
at different levels of granularity. For an illustration, see the
following diagram.

The different granularity levels form a hierarchy, and all the metrics
in the system form trees, rooted at the metric names:

```
MetricName (GLOBAL):           Metric X                    Metric Y
                                  |                           |
                           -----------------             ------------
                           |               |             |          |
StreamName (STREAM):    Stream A        Stream B      Stream A   Stream B
                           |               |
                        --------        ---------
                        |      |        |       |
ShardID (SHARD):     Shard 0 Shard 1  Shard 0 Shard 1
```

Not all metrics are available at the shard level; some are stream
level or global by nature. These are not produced at the shard level,
even if you have enabled shard-level metrics (`Metric Y` in
the preceding diagram).

When you specify an additional dimension, you must provide values for
`tuple:<DimensionName, DimensionValue,
 Granularity>`. The granularity is used to determine where
the custom dimension is inserted in the hierarchy: `GLOBAL`
means that the additional dimension is inserted after the metric name,
`STREAM` means it's inserted after the stream name, and
`SHARD` means it's inserted after the shard ID. If
multiple additional dimensions are given per granularity level, they are
inserted in the order given.

## Local access and Amazon CloudWatch upload

Metrics for the current KPL instance are available locally in real time; you can
query the KPL at any time to get them. The KPL locally computes the sum,
average, minimum, maximum, and count of every metric, as in CloudWatch.

You can get statistics that are cumulative from the start of the program to the
present point in time, or using a rolling window over the past _N_ seconds, where _N_
is an integer between 1 and 60.

All metrics are available for upload to CloudWatch. This is especially useful for
aggregating data across multiple hosts, monitoring, and alarming. This functionality
is not available locally.

As described previously, you can select which metrics to upload with the _metric level_ and _granularity_ settings. Metrics that are not uploaded are available
locally.

Uploading data points individually is untenable because it could produce millions
of uploads per second, if traffic is high. For this reason, the KPL aggregates
metrics locally into 1-minute buckets and uploads a statistics object to CloudWatch one
time per minute, per enabled metric.

## List of metrics

| Metric                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `UserRecordsReceived`                             | Count of how many logical user records were received by the<br>KPL core for put operations. Not available at shard<br>level.<br>Metric level: Detailed<br>Unit: Count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `UserRecordsPending`                              | Periodic sample of how many user records are currently<br>pending. A record is pending if it is either currently buffered<br>and waiting to be sent, or sent and in-flight to the backend<br>service. Not available at shard level.<br>The KPL provides a dedicated method to retrieve this metric<br>at the global level for customers to manage their put<br>rate.<br>Metric level: Detailed<br>Unit: Count                                                                                                                                                                                                                                                                                        |
| `UserRecordsPut`                                  | Count of how many logical user records were put successfully.<br>The KPL outputs a zero for failed records. This allows the average to give the success rate, the count to give the total attempts, and the difference between the count and sum to give the failure count.<br>Metric level: Summary<br>Unit: Count                                                                                                                                                                                                                                                                                                                                                                                  |
| `UserRecordsDataPut`                              | Bytes in the logical user records successfully put.<br>Metric level: Detailed<br>Unit: Bytes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `KinesisRecordsPut`                               | Count of how many Kinesis Data Streams records were put successfully (each<br>Kinesis Data Streams record can contain multiple user records).<br>The KPL outputs a zero for failed records. This allows the<br>average to give the success rate, the count to give the total<br>attempts, and the difference between the count and sum to give<br>the failure count.<br>Metric level: Summary<br>Unit: Count                                                                                                                                                                                                                                                                                         |
| `KinesisRecordsDataPut`                           | Bytes in the Kinesis Data Streams records.<br>Metric level: Detailed<br>Unit: Bytes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `ErrorsByCode`                                    | Count of each type of error code. This introduces an<br>additional dimension of `ErrorCode`, in addition to<br>the normal dimensions such as `StreamName` and<br>`ShardId`. Not every error can be traced to a<br>shard. The errors that cannot be traced are only emitted at<br>stream or global levels. This metric captures information about<br>such things as throttling, shard map changes, internal failures,<br>service unavailable, timeouts, and so on.<br>Kinesis Data Streams API errors are counted one time per Kinesis Data Streams record.<br>Multiple user records within a Kinesis Data Streams record do not generate<br>multiple counts.<br>Metric level: Summary<br>Unit: Count |
| `AllErrors`                                       | This is triggered by the same errors as **Errors by Code**, but does not distinguish between<br>types. This is useful as a general monitor of the error rate<br>without requiring a manual sum of the counts from all the<br>different types of errors.<br>Metric level: Summary<br>Unit: Count                                                                                                                                                                                                                                                                                                                                                                                                      |
| `RetriesPerRecord`                                | Number of retries performed per user record. Zero is emitted<br>for records that succeed in one try.<br>Data is emitted at the moment a user record finishes (when it<br>either succeeds or can no longer be retried). If record<br>time-to-live is a large value, this metric may be significantly<br>delayed.<br>Metric level: Detailed<br>Unit: Count                                                                                                                                                                                                                                                                                                                                             |
| `BufferingTime`                                   | The time between a user record arriving at the KPL and<br>leaving for the backend. This information is transmitted back to<br>the user on a per-record basis, but is also available as an<br>aggregated statistic.<br>Metric level: Summary<br>Unit: Milliseconds                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `Request Time`                                    | The time it takes to perform<br>`PutRecordsRequests`.<br>Metric level: Detailed<br>Unit: Milliseconds                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `User Records per Kinesis Record`                 | The number of logical user records aggregated into a single<br>Kinesis Data Streams record.<br>Metric level: Detailed<br>Unit: Count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `Amazon Kinesis Records per<br>PutRecordsRequest` | The number of Kinesis Data Streams records aggregated into a single<br>`PutRecordsRequest`. Not available at shard<br>level.<br>Metric level: Detailed<br>Unit: Count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `User Records per<br>PutRecordsRequest`           | The total number of user records contained within a<br>`PutRecordsRequest`. This is roughly equivalent<br>to the product of the previous two metrics. Not available at<br>shard level.<br>Metric level: Detailed<br>Unit: Count                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
