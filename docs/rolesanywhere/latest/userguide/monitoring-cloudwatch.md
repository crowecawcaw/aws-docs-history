# Monitoring IAM Roles Anywhere with Amazon CloudWatch

You can monitor AWS Identity and Access Management Roles Anywhere using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical
information and gain a better perspective on how your web application or service is performing. You can also set
alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For
more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

For IAM Roles Anywhere, you might want to watch for trust anchor and end-entity certificates expiration dates and renew your certificates when your certificates
are nearing expiration.

The IAM Roles Anywhere service reports the following metrics
in the `AWS/RolesAnywhere` namespace.

| Metric         | Description                                                                                                                                                                                                                                                                                                                           |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Success`      | Gets published every time `CreateSession`<br>succeeds in returning credentials to the user.<br>Valid Dimensions: Operation, TrustAnchorArn<br>Valid Statistic: Sum<br>Units: Count                                                                                                                                                    |
| `Failure`      | Gets published every time `CreateSession`<br>fails to return credentials to the user.<br>Valid Dimensions: Operation, ErrorType<br>Valid Statistic: Sum<br>Units: Count                                                                                                                                                               |
| `DaysToExpiry` | Gets published every time trust anchor certificates satisfies [notification evaluation criteria](customize-notification-settings.md#notification-evaluation "customize-notification-settings.md#notification-evaluation"). This metric will be published at<br>most once a day.<br>Valid Dimensions: TrustAnchorArn<br>Units: Integer |

The following dimensions are supported for the IAM Roles Anywhere metrics.

| Dimension        | Description                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------- |
| `Operation`      | The operation for which the metric applies to. This can only<br>take on the value, CreateSession. |
| `TrustAnchorArn` | The ARN of the trust anchor that is relevant for<br>this metric.                                  |
| `ErrorType`      | The type of error that `CreateSession` errors out with.                                           |
