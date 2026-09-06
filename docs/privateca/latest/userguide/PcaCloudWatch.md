

# AWS Private CA CloudWatch metrics
<a name="PcaCloudWatch"></a>

Amazon CloudWatch is a monitoring service for AWS resources. You can use CloudWatch to collect and track metrics, set alarms, and automatically react to changes in your AWS resources. CloudWatch metrics are published at least once.

AWS Private CA supports the following CloudWatch metrics. 





| Metric | Namespace | Description | 
| --- | --- | --- | 
| CRLGenerated | AWS/ACMPrivateCA | A certificate revocation list (CRL) was generated. This metric applies only to a private CA. | 
| MisconfiguredCRLBucket | AWS/ACMPrivateCA | The S3 bucket specified for the CRL is not correctly configured. Check the bucket policy. This metric applies only to a private CA. | 
| Time | AWS/ACMPrivateCA | The time in milliseconds between an issuance request and the completion (or failure) of issuance. This metric applies only to the IssueCertificate operation.  | 
| Success | AWS/ACMPrivateCA | A certificate was successfully issued. This metric applies only to the IssueCertificate operation. | 
| Failure | AWS/ACMPrivateCA | An operation failed. This metric applies only to the IssueCertificate operation. | 
| CertificateAuthority | AWS/Usage | The total number of private certificate authorities in your account in the current Region. This metric includes CAs in all states (ACTIVE, DISABLED, CREATING, etc.) and can be used to monitor CA inventory and track usage against account quotas. | 
| CertificatesPerCA | AWS/Usage | The total number of certificates issued by a specific private certificate authority since its creation. This metric increments with each successful certificate issuance and is not decremented when certificates expire or are revoked. This metric applies to individual private CAs and can be used to track certificate issuance volume and capacity planning. This metric is only published in the owner account and is not available in accounts that the CA is shared to. | 

**Note**  
For any private CAs created prior to March 26, 2026, the `CertificateAuthority` and `CertificatesPerCA` metrics might take until April 30, 2026 to be available in CloudWatch.

For more information about CloudWatch metrics, see the following topics:
+ [Using Amazon CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
+ [Creating Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)