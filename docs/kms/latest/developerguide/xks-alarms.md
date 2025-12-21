# Create CloudWatch alarms for external key stores

You can create Amazon CloudWatch alarms based on external key store metrics to notify
you when a metric value exceeds a threshold you specified. The alarm can send the
message to an [Amazon Simple Notification Service (Amazon SNS)
topic](../../../sns/latest/dg/sns-create-topic.md "../../../sns/latest/dg/sns-create-topic.md") or an [Amazon EC2
Auto Scaling policy](../../../autoscaling/ec2/userguide/as-scale-based-on-demand.md#as-how-scaling-policies-work "../../../autoscaling/ec2/userguide/as-scale-based-on-demand.md#as-how-scaling-policies-work"). For detailed information about CloudWatch alarms, see [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the _Amazon CloudWatch User Guide_.

Before creating an Amazon CloudWatch alarm, you need an Amazon SNS topic. For details, see [Creating an Amazon SNS topic](../../../sns/latest/dg/sns-create-topic.md "../../../sns/latest/dg/sns-create-topic.md") in the
_Amazon CloudWatch User Guide_.

###### Topics

- [Create an alarm for certificate
  expiration](#cert-expire-alarm "#cert-expire-alarm")
- [Create an alarm for response
  timeout](#latency-alarm "#latency-alarm")
- [Create an alarm for retryable
  errors](#retryable-errors-alarm "#retryable-errors-alarm")
- [Create an alarm for
  non-retryable errors](#nonretryable-errors-alarm "#nonretryable-errors-alarm")

## Create an alarm for certificate

expiration

This alarm uses the [XksProxyCertificateDaysToExpire](monitoring-cloudwatch.md#metric-xks-proxy-certificate-days-to-expire "monitoring-cloudwatch.md#metric-xks-proxy-certificate-days-to-expire") metric that AWS KMS
publishes to CloudWatch to record the anticipated expiration of the TLS certificate
associated with your external key store proxy endpoint. You cannot create a single
alarm for all external key stores in your account or an alarm for external key
stores that you might create in the future.

We recommend setting the alarm to alert you 10 days before your certificate is set
to expire, but you should set the threshold that best fits your needs.

**Create the alarm**

Follow the instructions in [Create a
CloudWatch alarm based on a static threshold](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md") using the following required
values. For other fields, accept the default values and provide names as requested.

| Field          | Value                                                                                                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Select metric  | Choose **KMS**, then choose **XKS<br>Proxy Certificate Metrics**.<br>Select the check box next to the<br>`XksProxyCertificateName` that you want to<br>monitor.<br>Then choose **Select metric**. |
| Statistic      | Minimum                                                                                                                                                                                           |
| Period         | 5 minutes                                                                                                                                                                                         |
| Threshold type | Static                                                                                                                                                                                            |
| Whenever ...   | Whenever \*_XksProxyCertificateDaysToExpire_<br>• is<br>`Lower` than `10`.                                                                                                                        |

## Create an alarm for response

timeout

This alarm uses the [XksProxyLatency](monitoring-cloudwatch.md#metric-xks-proxy-latency "monitoring-cloudwatch.md#metric-xks-proxy-latency") metric that AWS KMS publishes to CloudWatch
to record the number of milliseconds it takes for an external key store proxy to
respond to an AWS KMS request. You cannot create a single alarm for all external key
stores in your account or an alarm for external key stores that you might create in
the future.

AWS KMS expects the external key store proxy to respond to each request within 250
milliseconds. We recommend setting an alarm to alert you when your external key
store proxy takes longer than 200 milliseconds to respond, but you should set the
threshold that best fits your needs.

**Create the alarm**

Follow the instructions in [Create a
CloudWatch alarm based on a static threshold](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md") using the following required
values. For other fields, accept the default values and provide names as requested.

| Field          | Value                                                                                                                                                                           |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Select metric  | Choose **KMS**, then choose **XKS<br>Proxy Latency Metrics**.<br>Select the check box next to the `KmsOperation`<br>that you want to monitor.<br>Then choose **Select metric**. |
| Statistic      | Average                                                                                                                                                                         |
| Period         | 5 minutes                                                                                                                                                                       |
| Threshold type | Static                                                                                                                                                                          |
| Whenever ...   | Whenever \*_XksProxyLatency_<br>• is<br>`Greater` than `200`.                                                                                                                   |

## Create an alarm for retryable

errors

This alarm uses the [XksProxyErrors](monitoring-cloudwatch.md#metric-xks-proxy-errors "monitoring-cloudwatch.md#metric-xks-proxy-errors") metric that AWS KMS publishes to CloudWatch to
record the number of exceptions related to AWS KMS requests to your external key store
proxy. You cannot create a single alarm for all external key stores in your account
or an alarm for external key stores that you might create in the future.

Retryable errors will lower your reliability percentage and can indicate
networking errors. We recommend setting an alarm to alert you when more than five
retryable errors are recorded in a one minute period, but you should set the
threshold that best fits your needs.

Follow the instructions in [Create a
CloudWatch alarm based on a static threshold](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md") using the following required
values. For other fields, accept the default values and provide names as requested.

| Field          | Value                                                                                                                                                                                                                                         |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Select metric  | Choose the **Query\*<br>• tab.<br>Choose `AWS/KMS` for<br>**Namespace**.<br>Enter `SUM(XksProxyErrors)` for **Metric<br>name**.<br>Enter `ErrorType = Retryable` for **Filter<br>by**.<br>Choose **Run**. Then choose **Select<br>metric\*\*. |
| Label          | `Retryable errors`                                                                                                                                                                                                                            |
| Period         | 1 minute                                                                                                                                                                                                                                      |
| Threshold type | Static                                                                                                                                                                                                                                        |
| Whenever ...   | Whenever \*_q1_<br>• is `Greater` than<br>`5`.                                                                                                                                                                                                |

## Create an alarm for

non-retryable errors

This alarm uses the [XksProxyErrors](monitoring-cloudwatch.md#metric-xks-proxy-errors "monitoring-cloudwatch.md#metric-xks-proxy-errors") metric that AWS KMS publishes to CloudWatch to
record the number of exceptions related to AWS KMS requests to your external key store
proxy. You cannot create a single alarm for all external key stores in your account
or an alarm for external key stores that you might create in the future.

Non-retryable errors can indicate a problem with the configuration of your
external key store. We recommend setting an alarm to alert you when more than five
non-retryable errors are recorded in a one minute period, but you should set the
threshold that best fits your needs.

Follow the instructions in [Create a
CloudWatch alarm based on a static threshold](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md") using the following required
values. For other fields, accept the default values and provide names as requested.

| Field          | Value                                                                                                                                                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Select metric  | Choose the **Query\*<br>• tab.<br>Choose `AWS/KMS` for<br>**Namespace**.<br>Enter `SUM(XksProxyErrors)` for **Metric<br>name**.<br>Enter `ErrorType = Non-retryable` for<br>**Filter by**.<br>Choose **Run**. Then choose **Select<br>metric\*\*. |
| Label          | `Non-retryable errors`                                                                                                                                                                                                                            |
| Period         | 1 minute                                                                                                                                                                                                                                          |
| Threshold type | Static                                                                                                                                                                                                                                            |
| Whenever ...   | Whenever \*_q1_<br>• is `Greater` than<br>`5`.                                                                                                                                                                                                    |
