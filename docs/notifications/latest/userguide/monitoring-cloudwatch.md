# Monitoring AWS User Notifications with Amazon CloudWatch

You can monitor AWS User Notifications using CloudWatch, which collects raw data and processes it into
readable, near real-time metrics. CloudWatch keeps these statistics for 15 months so that you can
access historical information and gain perspective on how your web application or service
performs. You can also set alarms that watch for certain thresholds, and send notifications or
take actions when those thresholds are met. For more information, see the
[Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

## Enabling CloudWatch Metrics

Amazon CloudWatch metrics are enabled by default.

## Available metrics and dimensions

The following are the metrics and dimensions that User Notifications sends to Amazon CloudWatch.

The `AWS/Notifications` namespace includes the following metrics.

| Metric                   | Description                                                            |
| ------------------------ | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ServiceEventsThrottled` | The number of throttled events. Units: Count                           | User Notifications sends the following dimensions to CloudWatch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Dimension                | Description                                                            |
| ---                      | ---                                                                    |
| `Service, EventType`     | This dimension filters the data you request by service and event type. | ## Viewing User Notifications metrics You can view metrics in the CloudWatch console. The console provides a fine-grained and customizable display of your resources, as well as the number of running tasks in a service. ### Viewing User Notifications metrics in the CloudWatch console You can see a detailed view of User Notifications metrics in the CloudWatch console. You can tailor your view in the CloudWatch console to suit your needs. For more information about CloudWatch, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md"). ###### To view metrics in the CloudWatch console 1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/"). 2. In the **Metrics** section in the left navigation, choose **Notifications**. 3. Choose the metrics to view. |
