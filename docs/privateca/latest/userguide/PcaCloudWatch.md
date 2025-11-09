# AWS Private CA CloudWatch metrics

Amazon CloudWatch is a monitoring service for AWS resources. You can use CloudWatch to collect and
track metrics, set alarms, and automatically react to changes in your AWS resources.
CloudWatch metrics are published at least once.

AWS Private CA supports the following CloudWatch metrics.

| Metric                   | Description                                                                                                                                                                  |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CRLGenerated`           | A certificate revocation list (CRL) was generated. This metric applies<br>only to a private CA.                                                                              |
| `MisconfiguredCRLBucket` | The S3 bucket specified for the CRL is not correctly configured. Check<br>the bucket policy. This metric applies only to a private CA.                                       |
| `Time`                   | The time in milliseconds between an issuance request and the completion<br>(or failure) of issuance. This metric applies only to the<br>\*_IssueCertificate_<br>• operation. |
| `Success`                | A certificate was successfully issued. This metric applies only to the<br>\*_IssueCertificate_<br>• operation.                                                               |
| `Failure`                | An operation failed. This metric applies only to the<br>\*_IssueCertificate_<br>• operation.                                                                                 |

For more information about CloudWatch metrics, see the following topics:

- [Using Amazon CloudWatch
  Metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md")
- [Creating Amazon CloudWatch
  Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
