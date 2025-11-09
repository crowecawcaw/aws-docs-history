# Supported CloudWatch metrics

Amazon CloudWatch is a monitoring service for AWS resources. You can use CloudWatch to collect and
track metrics, set alarms, and automatically react to changes in your AWS resources.
ACM publishes metrics twice per day for every certificate in an account until
expiration.

The `AWS/CertificateManager` namespace includes the following metric.

| Metric         | Description                                                                                                  | Unit    | Dimensions                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------ | ------- | ------------------------------------------------- |
| `DaysToExpiry` | Number of days until a certificate expires. ACM stops publishing<br>this metric after a certificate expires. | Integer | CertificateArn<br>• Value: ARN of the certificate |

For more information about CloudWatch metrics, see the following topics:

- [Using Amazon CloudWatch
  Metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md")
- [Creating Amazon CloudWatch
  Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
