# Amazon Managed Service for Apache Flink endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                | Region         | Endpoint                                                                                          | Protocol       |
| -------------------------- | -------------- | ------------------------------------------------------------------------------------------------- | -------------- |
| US East (Ohio)             | us-east-2      | kinesisanalytics.us-east-2.amazonaws.com<br>kinesisanalytics-fips.us-east-2.amazonaws.com         | HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | kinesisanalytics.us-east-1.amazonaws.com<br>kinesisanalytics-fips.us-east-1.amazonaws.com         | HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | kinesisanalytics.us-west-1.amazonaws.com<br>kinesisanalytics-fips.us-west-1.amazonaws.com         | HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | kinesisanalytics.us-west-2.amazonaws.com<br>kinesisanalytics-fips.us-west-2.amazonaws.com         | HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | kinesisanalytics.af-south-1.amazonaws.com                                                         | HTTPS          |
| Asia Pacific (Hong Kong)   | ap-east-1      | kinesisanalytics.ap-east-1.amazonaws.com                                                          | HTTPS          |
| Asia Pacific (Hyderabad)   | ap-south-2     | kinesisanalytics.ap-south-2.amazonaws.com                                                         | HTTPS          |
| Asia Pacific (Jakarta)     | ap-southeast-3 | kinesisanalytics.ap-southeast-3.amazonaws.com                                                     | HTTPS          |
| Asia Pacific (Malaysia)    | ap-southeast-5 | kinesisanalytics.ap-southeast-5.amazonaws.com                                                     | HTTPS          |
| Asia Pacific (Melbourne)   | ap-southeast-4 | kinesisanalytics.ap-southeast-4.amazonaws.com                                                     | HTTPS          |
| Asia Pacific (Mumbai)      | ap-south-1     | kinesisanalytics.ap-south-1.amazonaws.com                                                         | HTTPS          |
| Asia Pacific (New Zealand) | ap-southeast-6 | kinesisanalytics.ap-southeast-6.amazonaws.com                                                     | HTTPS          |
| Asia Pacific (Osaka)       | ap-northeast-3 | kinesisanalytics.ap-northeast-3.amazonaws.com                                                     | HTTPS          |
| Asia Pacific (Seoul)       | ap-northeast-2 | kinesisanalytics.ap-northeast-2.amazonaws.com                                                     | HTTPS          |
| Asia Pacific (Singapore)   | ap-southeast-1 | kinesisanalytics.ap-southeast-1.amazonaws.com                                                     | HTTPS          |
| Asia Pacific (Sydney)      | ap-southeast-2 | kinesisanalytics.ap-southeast-2.amazonaws.com                                                     | HTTPS          |
| Asia Pacific (Taipei)      | ap-east-2      | kinesisanalytics.ap-east-2.amazonaws.com                                                          | HTTPS          |
| Asia Pacific (Thailand)    | ap-southeast-7 | kinesisanalytics.ap-southeast-7.amazonaws.com                                                     | HTTPS          |
| Asia Pacific (Tokyo)       | ap-northeast-1 | kinesisanalytics.ap-northeast-1.amazonaws.com                                                     | HTTPS          |
| Canada (Central)           | ca-central-1   | kinesisanalytics.ca-central-1.amazonaws.com<br>kinesisanalytics-fips.ca-central-1.amazonaws.com   | HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | kinesisanalytics.ca-west-1.amazonaws.com<br>kinesisanalytics-fips.ca-west-1.amazonaws.com         | HTTPS<br>HTTPS |
| Europe (Frankfurt)         | eu-central-1   | kinesisanalytics.eu-central-1.amazonaws.com                                                       | HTTPS          |
| Europe (Ireland)           | eu-west-1      | kinesisanalytics.eu-west-1.amazonaws.com                                                          | HTTPS          |
| Europe (London)            | eu-west-2      | kinesisanalytics.eu-west-2.amazonaws.com                                                          | HTTPS          |
| Europe (Milan)             | eu-south-1     | kinesisanalytics.eu-south-1.amazonaws.com                                                         | HTTPS          |
| Europe (Paris)             | eu-west-3      | kinesisanalytics.eu-west-3.amazonaws.com                                                          | HTTPS          |
| Europe (Spain)             | eu-south-2     | kinesisanalytics.eu-south-2.amazonaws.com                                                         | HTTPS          |
| Europe (Stockholm)         | eu-north-1     | kinesisanalytics.eu-north-1.amazonaws.com                                                         | HTTPS          |
| Europe (Zurich)            | eu-central-2   | kinesisanalytics.eu-central-2.amazonaws.com                                                       | HTTPS          |
| Israel (Tel Aviv)          | il-central-1   | kinesisanalytics.il-central-1.amazonaws.com                                                       | HTTPS          |
| Mexico (Central)           | mx-central-1   | kinesisanalytics.mx-central-1.amazonaws.com                                                       | HTTPS          |
| Middle East (Bahrain)      | me-south-1     | kinesisanalytics.me-south-1.amazonaws.com                                                         | HTTPS          |
| Middle East (UAE)          | me-central-1   | kinesisanalytics.me-central-1.amazonaws.com                                                       | HTTPS          |
| South America (São Paulo)  | sa-east-1      | kinesisanalytics.sa-east-1.amazonaws.com                                                          | HTTPS          |
| AWS GovCloud (US-East)     | us-gov-east-1  | kinesisanalytics.us-gov-east-1.amazonaws.com<br>kinesisanalytics-fips.us-gov-east-1.amazonaws.com | HTTPS<br>HTTPS |
| AWS GovCloud (US-West)     | us-gov-west-1  | kinesisanalytics.us-gov-west-1.amazonaws.com<br>kinesisanalytics-fips.us-gov-west-1.amazonaws.com | HTTPS<br>HTTPS |

## Service quotas

| Name                                                    | Default                    | Adjustable                                                                                                                                                                                           | Description                                                                                       |
| ------------------------------------------------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Apache Flink Kinesis Processing Units (KPUs)            | Each supported Region: 64  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/kinesisanalytics/quotas/L-3A88E041 "https://console.aws.amazon.com/servicequotas/home/services/kinesisanalytics/quotas/L-3A88E041") | The maximum number of Kinesis Processing Units (KPUs) that your Apache Flink application can use. |
| Application count                                       | Each supported Region: 100 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/kinesisanalytics/quotas/L-3729A2EF "https://console.aws.amazon.com/servicequotas/home/services/kinesisanalytics/quotas/L-3729A2EF") | The maximum number of applications per account per Region.                                        |
| Input Parallelism in input streams for SQL applications | Each supported Region: 64  | No                                                                                                                                                                                                   | The maximum number of in-application input streams for SQL applications.                          |
| SQL Kinesis Processing Units (KPUs)                     | Each supported Region: 8   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/kinesisanalytics/quotas/L-90BEDB9D "https://console.aws.amazon.com/servicequotas/home/services/kinesisanalytics/quotas/L-90BEDB9D") | The maximum number of Kinesis Processing Units (KPUs) that your SQL application can use.          |

For more information, see [Quotas](../../../kinesisanalytics/latest/java/limits.md "../../../kinesisanalytics/latest/java/limits.md") in the
_Amazon Managed Service for Apache Flink for Apache Flink Developer Guide_.
