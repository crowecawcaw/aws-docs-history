# Amazon Inspector Classic endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name             | Region         | Endpoint                                                                            | Protocol       |
| ----------------------- | -------------- | ----------------------------------------------------------------------------------- | -------------- |
| US East (Ohio)          | us-east-2      | inspector.us-east-2.amazonaws.com<br>inspector-fips.us-east-2.amazonaws.com         | HTTPS<br>HTTPS |
| US East (N. Virginia)   | us-east-1      | inspector.us-east-1.amazonaws.com<br>inspector-fips.us-east-1.amazonaws.com         | HTTPS<br>HTTPS |
| US West (N. California) | us-west-1      | inspector.us-west-1.amazonaws.com<br>inspector-fips.us-west-1.amazonaws.com         | HTTPS<br>HTTPS |
| US West (Oregon)        | us-west-2      | inspector.us-west-2.amazonaws.com<br>inspector-fips.us-west-2.amazonaws.com         | HTTPS<br>HTTPS |
| Asia Pacific (Mumbai)   | ap-south-1     | inspector.ap-south-1.amazonaws.com                                                  | HTTPS          |
| Asia Pacific (Seoul)    | ap-northeast-2 | inspector.ap-northeast-2.amazonaws.com                                              | HTTPS          |
| Asia Pacific (Sydney)   | ap-southeast-2 | inspector.ap-southeast-2.amazonaws.com                                              | HTTPS          |
| Asia Pacific (Tokyo)    | ap-northeast-1 | inspector.ap-northeast-1.amazonaws.com                                              | HTTPS          |
| Europe (Frankfurt)      | eu-central-1   | inspector.eu-central-1.amazonaws.com                                                | HTTPS          |
| Europe (Ireland)        | eu-west-1      | inspector.eu-west-1.amazonaws.com                                                   | HTTPS          |
| Europe (London)         | eu-west-2      | inspector.eu-west-2.amazonaws.com                                                   | HTTPS          |
| Europe (Stockholm)      | eu-north-1     | inspector.eu-north-1.amazonaws.com                                                  | HTTPS          |
| AWS GovCloud (US-East)  | us-gov-east-1  | inspector.us-gov-east-1.amazonaws.com<br>inspector-fips.us-gov-east-1.amazonaws.com | HTTPS<br>HTTPS |
| AWS GovCloud (US-West)  | us-gov-west-1  | inspector.us-gov-west-1.amazonaws.com<br>inspector-fips.us-gov-west-1.amazonaws.com | HTTPS<br>HTTPS |

## Service quotas

| Name                             | Default                       | Adjustable                                                                                                                                                                             | Description                                                                                                                                                                                                                                        |
| -------------------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Assessment Targets               | Each supported Region: 50     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/inspector/quotas/L-E1AFB5F4 "https://console.aws.amazon.com/servicequotas/home/services/inspector/quotas/L-E1AFB5F4") | The maximum number of assessment targets that you can have at any given time per account per region.                                                                                                                                               |
| Assessment Templates             | Each supported Region: 500    | [Yes](https://console.aws.amazon.com/servicequotas/home/services/inspector/quotas/L-7A3AEC10 "https://console.aws.amazon.com/servicequotas/home/services/inspector/quotas/L-7A3AEC10") | The maximum number of assessment templates that you can have at any given time per account per region.                                                                                                                                             |
| Assessment runs                  | Each supported Region: 50,000 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/inspector/quotas/L-12943E2F "https://console.aws.amazon.com/servicequotas/home/services/inspector/quotas/L-12943E2F") | The maximum number of assessment runs that you can create per account per region. You can have multiple assessment runs happening at the same time as long as the assessment targets used for these runs do not contain overlapping EC2 instances. |
| Instances in running assessments | Each supported Region: 500    | [Yes](https://console.aws.amazon.com/servicequotas/home/services/inspector/quotas/L-6750F872 "https://console.aws.amazon.com/servicequotas/home/services/inspector/quotas/L-6750F872") | The maximum number of EC2 instances that can be included across all running assessments per account per region.                                                                                                                                    |

For more information, see the [Amazon Inspector Classic quotas](../../../inspector/latest/userguide/inspector_limits.md "../../../inspector/latest/userguide/inspector_limits.md")
in the _Amazon Inspector User Guide_.
