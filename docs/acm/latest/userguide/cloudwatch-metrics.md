# Supported CloudWatch metrics

Amazon CloudWatch is a monitoring service for AWS resources. You can use CloudWatch to collect and
track metrics, set alarms, and automatically react to changes in your AWS resources.

The `AWS/CertificateManager` namespace includes the following metrics.

| Metric                       | Description                                                                                                                                                                            | Unit    | Dimensions                                           |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------------------------------------------- |
| `DaysToExpiry`               | Number of days until a certificate expires. ACM publishes this<br>metric twice per day for every certificate until expiration, and stops<br>publishing it after a certificate expires. | Integer | CertificateArn<br>• Value: ARN of the certificate    |
| `CertificateIssuanceSuccess` | The number of certificates successfully issued through an<br>ACME endpoint. ACM publishes a value of 1 for each successful<br>issuance and 0 otherwise.                                | Count   | AcmeEndpointArn<br>• Value: ARN of the ACME endpoint |
| `CertificateIssuanceFailed`  | The number of certificate issuance attempts that failed for an<br>ACME endpoint. ACM publishes a value of 1 for each failed<br>issuance and 0 otherwise.                               | Count   | AcmeEndpointArn<br>• Value: ARN of the ACME endpoint |

For more information about CloudWatch metrics, see the following topics:

- [Using Amazon CloudWatch
  Metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md")
- [Creating Amazon CloudWatch
  Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
