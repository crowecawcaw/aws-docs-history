

# Supported CloudWatch metrics
<a name="cloudwatch-metrics"></a>

Amazon CloudWatch is a monitoring service for AWS resources. You can use CloudWatch to collect and track metrics, set alarms, and automatically react to changes in your AWS resources.

The `AWS/CertificateManager` namespace includes the following metrics. 



| Metric | Description | Unit | Dimensions | 
| --- | --- | --- | --- | 
| DaysToExpiry | Number of days until a certificate expires. ACM publishes this metric twice per day for every certificate until expiration, and stops publishing it after a certificate expires. | Integer | CertificateArn+  Value: ARN of the certificate  | 
| CertificateIssuanceSuccess | The number of certificates successfully issued through an ACME endpoint. ACM publishes a value of 1 for each successful issuance and 0 otherwise. | Count | AcmeEndpointArn+  Value: ARN of the ACME endpoint  | 
| CertificateIssuanceFailed | The number of certificate issuance attempts that failed for an ACME endpoint. ACM publishes a value of 1 for each failed issuance and 0 otherwise. | Count | AcmeEndpointArn+  Value: ARN of the ACME endpoint  | 

For more information about CloudWatch metrics, see the following topics:
+ [Using Amazon CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
+ [Creating Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)