# Monitoring your metric streams with CloudWatch metrics

Metric streams emit CloudWatch metrics about their health and operation in the
`AWS/CloudWatch/MetricStreams` namespace. The following metrics are
emitted. These metrics are emitted with a `MetricStreamName` dimension and
with no dimension. You can use the metrics with no dimensions to see aggregated metrics
for all of your metric streams. You can use the metrics with the
`MetricStreamName` dimension to see the metrics about only that metric
stream.

For all of these metrics, values are emitted only for metric streams
that are in the **Running** state.

| Metric              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `MetricUpdate`      | The number of metric updates sent to the metric stream. If no metric<br>updates are streamed during a time period, this metric is not emitted during<br>that time period.<br>If you stop the metric stream, this metric stops being emitted until<br>the metric stream is started again.<br>Valid Statistic: `Sum`<br>Units: None                                                                                                                                       |
| `TotalMetricUpdate` | This is calculated as **MetricUpdate + a number based on additional<br>statistics that are being streamed**.<br>For each unique namespace and metric name combination, streaming 1-5 additional<br>statistics adds 1 to the `TotalMetricUpdate`, streaming 6-10 additional statistics<br>adds 2 to `TotalMetricUpdate`, and so on.<br>Valid Statistic: `Sum`<br>Units: None                                                                                             |
| `PublishErrorRate`  | The number of unrecoverable errors that occur when<br>putting data into the Firehose delivery stream. If no errors occur during a time period,<br>this metric is not emitted during that time period.<br>If you stop the metric stream, this metric stops being emitted until<br>the metric stream is started again.<br>Valid Statistic: `Average` to see the rate<br>of metric updates unable to be written. This value will be<br>between 0.0 and 1.0.<br>Units: None |
