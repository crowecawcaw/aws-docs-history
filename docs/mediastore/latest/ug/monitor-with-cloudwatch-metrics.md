End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Monitoring AWS Elemental MediaStore with

Amazon CloudWatch metrics

You can monitor AWS Elemental MediaStore using CloudWatch, which collects raw data and
processes it into readable metrics. CloudWatch
keeps statistics are kept for 15 months so that you can access historical
information and gain a better perspective on how your web application or service is
performing. You can also set alarms that watch for certain thresholds, and send
notifications or take actions when those thresholds are met. For more information,
see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

For AWS Elemental MediaStore, you might want to watch `BytesDownloaded` and
send an email to yourself when that metric reaches a certain threshold.

###### To view metrics using the CloudWatch console

Metrics are grouped first by the service namespace, and then by the various
dimension combinations within each namespace.

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. Under **All metrics**, choose the
   **AWS/MediaStore** namespace.
4. Choose the metric dimension to view the metrics. For example, choose
   `Request metrics by container` to view metrics for the
   different types of requests that have been sent to the container.

###### To view metrics using the AWS CLI

- At a command prompt, use the following command:

```
aws cloudwatch list-metrics --namespace "AWS/MediaStore"
```

## AWS Elemental MediaStore metrics

The following table lists metrics that AWS Elemental MediaStore sends to CloudWatch.

###### Note

To view metrics, you must [add a
metric policy](policies-metric-add.md#policies-metric-add.title "policies-metric-add.md#policies-metric-add.title") to the container to allow MediaStore to send
metrics to Amazon CloudWatch.

| Metric            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RequestCount`    | The total number of HTTP requests made to a MediaStore<br>container, separated by operation type (`Put`,<br>`Get`, `Delete`,<br>`Describe`, `List`).<br>Units: Count<br>Valid dimensions:<br>• Container name<br>• Object group name<br>• Request type<br>Valid statistics: Sum                                                                                                                                                                                                                                                                                                                                      |
| `4xxErrorCount`   | The number of HTTP requests made to MediaStore that<br>resulted in a 4xx error.<br>Units: Count<br>Valid dimensions:<br>• Container name<br>• Object group name<br>• Request type<br>Valid statistics: Sum                                                                                                                                                                                                                                                                                                                                                                                                           |
| `5xxErrorCount`   | The number of HTTP requests made to MediaStore that<br>resulted in a 5xx error.<br>Units: Count<br>Valid dimensions:<br>• Container name<br>• Object group name<br>• Request type<br>Valid statistics: Sum                                                                                                                                                                                                                                                                                                                                                                                                           |
| `BytesUploaded`   | The number of bytes uploaded for requests made to a<br>MediaStore container, where the request includes a<br>body.<br>Units: Bytes<br>Valid dimensions:<br>• Container name<br>• Object group name<br>Valid statistics: Average (bytes per request), Sum (bytes<br>per period), Sample Count, Min (same as P0.0), Max (same as<br>p100), any percentile between p0.0 and p99.9                                                                                                                                                                                                                                       |
| `BytesDownloaded` | The number of bytes downloaded for requests made to a<br>MediaStore container, where the response includes a<br>body.<br>Units: Bytes<br>Valid dimensions:<br>• Container name<br>• Object group name<br>Valid statistics: Average (bytes per request), Sum (bytes<br>per period), Sample Count, Min (same as P0.0), Max (same as<br>p100), any percentile between p0.0 and p99.9                                                                                                                                                                                                                                    |
| `TotalTime`       | The number of milliseconds that the request was in flight<br>from the server's perspective. This value is measured from<br>the time that MediaStore receives your request, to the time that<br>it sends the last byte of the response. This value is<br>measured from the server's perspective because measurements<br>made from the client's perspective are affected by network<br>latency.<br>Units: Milliseconds<br>Valid dimensions:<br>• Container name<br>• Object group name<br>• Request type<br>Valid statistics: Average, Min (same as P0.0), Max (same<br>as p100), any percentile between p0.0 and p100 |
| `TurnaroundTime`  | The number of milliseconds that MediaStore spent<br>processing your request. This value is measured from the<br>time that MediaStore receives the last byte of your request, to<br>the time that it sends the first byte of the<br>response.<br>Units: Milliseconds<br>Valid dimensions:<br>• Container name<br>• Object group name<br>• Request type<br>Valid statistics: Average, Min (same as P0.0), Max (same<br>as p100), any percentile between p0.0 and p100                                                                                                                                                  |
| `ThrottleCount`   | The number of HTTP requests made to MediaStore that were throttled.<br>Units: Count<br>Valid dimensions:<br>• Container name<br>• Object group name<br>• Request type<br>Valid statistics: Sum                                                                                                                                                                                                                                                                                                                                                                                                                       |
