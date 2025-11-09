# Measuring Performance Between Your

Tape Gateway and AWS

Data throughput, data latency, and operations per second are measures that you can use
to understand how your application storage that is using your Tape Gateway is
performing. When you use the correct aggregation statistic, these values can be measured
by using the Storage Gateway metrics that are provided for you.

A _statistic_ is an aggregation of a metric over a specified period
of time. When you view the values of a metric in CloudWatch, use the `Average`
statistic for data latency (milliseconds), and use the `Samples` statistic
for input/output operations per second (IOPS). For more information, see [Statistics](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Statistic "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Statistic") in the _Amazon CloudWatch User Guide_.

The following table summarizes the metrics and the corresponding statistic you can use
to measure the throughput, latency, and IOPS between your Tape Gateway and AWS.

| Item of Interest       | How to Measure                                                                                                                                                                                                                                                                                                                      |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Latency                | Use the `ReadTime` and `WriteTime` metrics with<br>the `Average` CloudWatch statistic. For example, the<br>`Average` value of the `ReadTime` metric gives<br>you the latency per operation over the sample period of time.                                                                                                          |
| Throughput to AWS      | Use the `CloudBytesDownloaded` and<br>`CloudBytesUploaded` metrics with the `Sum`<br>CloudWatch statistic. For example, the `Sum` value of the<br>`CloudBytesDownloaded` metric over a sample period of 5<br>minutes divided by 300 seconds gives you the throughput from AWS to<br>the Tape Gateway as a rate in bytes per second. |
| Latency of data to AWS | Use the `CloudDownloadLatency` metric with the<br>`Average` statistic. For example, the<br>`Average` statistic of the<br>`CloudDownloadLatency` metric gives you the latency per<br>operation.                                                                                                                                      |

###### To measure the upload data throughput from a Tape Gateway to AWS

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose the **Metrics** tab.
3. Choose the **StorageGateway: Gateway Metrics** dimension, and
   find the Tape Gateway that you want to work with.
4. Choose the `CloudBytesUploaded` metric.
5. For **Time Range**, choose a value.
6. Choose the `Sum` statistic.
7. For **Period**, choose a value of 5 minutes or
   greater.
8. In the resulting time-ordered set of data points, divide each data point by
   the period (in seconds) to get the throughput at that sample period. For
   example, if the throughput from the Tape Gateway to AWS is 555,544,576 bytes
   for a given data point, and the period is 300 seconds, then the approximate
   throughput would be 1.85 megabytes per second.

###### To measure the data latency from a Tape Gateway to AWS

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose the **Metrics** tab.
3. Choose the **StorageGateway: GatewayMetrics** dimension, and
   find the Tape Gateway that you want to work with.
4. Choose the `CloudDownloadLatency` metric.
5. For **Time Range**, choose a value.
6. Choose the `Average` statistic.
7. For **Period**, choose a value of 5 minutes to match the
   default reporting time.
   The resulting time-ordered set of data points contains the latency in
   milliseconds.

###### To set an upper threshold alarm for a

Tape Gateway's throughput to AWS

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Create Alarm** to start the Create Alarm
   wizard.
3. Choose the **StorageGateway: Gateway Metrics** dimension, and
   find the Tape Gateway that you want to work with.
4. Choose the `CloudBytesUploaded` metric.
5. Define the alarm by defining the alarm state when the
   `CloudBytesUploaded` metric is greater than or equal to a
   specified value for a specified time. For example, you can define an alarm state
   when the `CloudBytesUploaded` metric is greater than 10 megabytes for
   60 minutes.
6. Configure the actions to take for the alarm state. For example, you can have
   an email notification sent to you.
7. Choose **Create Alarm**.

###### To set an upper threshold alarm for reading

data from AWS

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Create Alarm** to start the Create Alarm
   wizard.
3. Choose the **StorageGateway: Gateway Metrics** dimension, and
   find the Tape Gateway that you want to work with.
4. Choose the `CloudDownloadLatency` metric.
5. Define the alarm by defining the alarm state when the
   `CloudDownloadLatency` metric is greater than or equal to a
   specified value for a specified time. For example, you can define an alarm state
   when the `CloudDownloadLatency` is greater than 60,000 milliseconds
   for greater than 2 hours.
6. Configure the actions to take for the alarm state. For example, you can have
   an email notification sent to you.
7. Choose **Create Alarm**.
