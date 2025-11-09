# Using Amazon CloudWatch with HealthImaging

You can monitor AWS HealthImaging using CloudWatch, which collects raw data and processes it into
readable, near real-time metrics. These statistics are kept for 15 months, so you can use that
historical information and gain a better perspective on how your web application or service is
performing. You can also set alarms that watch for certain thresholds, and send notifications or
take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

###### Note

Metrics are reported for all HealthImaging APIs.

The following tables list the metrics and dimensions for HealthImaging. Each is presented as a
frequency count for a user-specified data range.

| Metrics    | Metrics                                                                                                                                                                                                         | Description |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Call Count | The number of calls to APIs. This can be reported either for the account or a<br>specified data store.<br>Units: Count<br>Valid Statistics: Sum, Count<br>Dimensions: Operation, data store ID, data store type |

You can get metrics for HealthImaging with the AWS Management Console, the AWS CLI, or the CloudWatch API. You can use
the CloudWatch API through one of the Amazon AWS Software Development Kits (SDKs) or the CloudWatch API
tools. The HealthImaging console displays graphs based on the raw data from the CloudWatch API.

You must have the appropriate CloudWatch permissions to monitor HealthImaging with CloudWatch. For more
information, see [Identity and access
management for CloudWatch](../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md "../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md") in the _CloudWatch User Guide_.

## Viewing HealthImaging metrics

###### To view metrics (CloudWatch console)

1. Sign in to the AWS Management Console and open the [CloudWatch
   console](https://console.aws.amazon.com/cloudwatch/home "https://console.aws.amazon.com/cloudwatch/home").
2. Choose **Metrics**, choose **All Metrics**, and then
   choose **AWS/Medical Imaging**.
3. Choose the dimension, choose a metric name, then choose **Add to
   graph**.
4. Choose a value for the date range. The metric count for the selected date range is
   displayed in the graph.

## Creating an alarm using CloudWatch

A CloudWatch alarm watches a single metric over a specified time period, and performs one or
more actions: sending a notification to an Amazon Simple Notification Service (Amazon SNS) topic or Auto Scaling policy. The
action or actions are based on the value of the metric relative to a given threshold over a
number of time periods that you specify. CloudWatch can also send you an Amazon SNS message when the
alarm changes state.

CloudWatch alarms invoke actions only when the state changes and has persisted for the period
you specify. For more information, see [Using CloudWatch
alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md").
