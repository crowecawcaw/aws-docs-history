# AWS Private CA CloudWatch metrics

Amazon CloudWatch is a monitoring service for AWS resources. You can use CloudWatch to collect and
track metrics, set alarms, and automatically react to changes in your AWS resources.
CloudWatch metrics are published at least once.

AWS Private CA supports the following CloudWatch metrics.

| Metric                   | Namespace          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------ | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CRLGenerated`           | `AWS/ACMPrivateCA` | A certificate revocation list (CRL) was generated. This metric applies<br>only to a private CA.                                                                                                                                                                                                                                                                                                                                                                                           |
| `MisconfiguredCRLBucket` | `AWS/ACMPrivateCA` | The S3 bucket specified for the CRL is not correctly configured. Check<br>the bucket policy. This metric applies only to a private CA.                                                                                                                                                                                                                                                                                                                                                    |
| `Time`                   | `AWS/ACMPrivateCA` | The time in milliseconds between an issuance request and the completion<br>(or failure) of issuance. This metric applies only to the<br>*_IssueCertificate_<br>• operation.                                                                                                                                                                                                                                                                                                               |
| `Success`                | `AWS/ACMPrivateCA` | A certificate was successfully issued. This metric applies only to the<br>*_IssueCertificate_<br>• operation.                                                                                                                                                                                                                                                                                                                                                                             |
| `Failure`                | `AWS/ACMPrivateCA` | An operation failed. This metric applies only to the<br>*_IssueCertificate_<br>• operation.                                                                                                                                                                                                                                                                                                                                                                                               |
| `CertificateAuthority`   | `AWS/Usage`        | The total number of private certificate authorities in your account in the current Region.<br>This metric includes CAs in all states (ACTIVE, DISABLED, CREATING, etc.)<br>and can be used to monitor CA inventory and track usage against account quotas.                                                                                                                                                                                                                                |
| `CertificatesPerCA`      | `AWS/Usage`        | The total number of certificates issued by a specific private certificate authority since its creation.<br>This metric increments with each successful certificate issuance and is not decremented when certificates expire or are revoked.<br>This metric applies to individual private CAs and can be used to track certificate issuance volume and capacity planning.<br>This metric is only published in the owner account and is not available in accounts that the CA is shared to. |

###### Note

For any private CAs created prior to March 26, 2026, the
`CertificateAuthority` and `CertificatesPerCA` metrics
might take until April 30, 2026 to be available in CloudWatch.

For more information about CloudWatch metrics, see the following topics:

- [Using Amazon CloudWatch
  Metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md")
- [Creating Amazon CloudWatch
  Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
