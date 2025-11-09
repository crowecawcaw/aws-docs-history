# Amazon CloudWatch Synthetics endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                | Region         | Endpoint                                                                                                                                                           | Protocol                         |
| -------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------- |
| US East (Ohio)             | us-east-2      | synthetics.us-east-2.amazonaws.com<br>synthetics-fips.us-east-2.api.aws<br>synthetics-fips.us-east-2.amazonaws.com<br>synthetics.us-east-2.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | synthetics.us-east-1.amazonaws.com<br>synthetics-fips.us-east-1.api.aws<br>synthetics-fips.us-east-1.amazonaws.com<br>synthetics.us-east-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | synthetics.us-west-1.amazonaws.com<br>synthetics-fips.us-west-1.api.aws<br>synthetics-fips.us-west-1.amazonaws.com<br>synthetics.us-west-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | synthetics.us-west-2.amazonaws.com<br>synthetics-fips.us-west-2.api.aws<br>synthetics-fips.us-west-2.amazonaws.com<br>synthetics.us-west-2.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | synthetics.af-south-1.amazonaws.com<br>synthetics.af-south-1.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Hong Kong)   | ap-east-1      | synthetics.ap-east-1.amazonaws.com<br>synthetics.ap-east-1.api.aws                                                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Hyderabad)   | ap-south-2     | synthetics.ap-south-2.amazonaws.com<br>synthetics.ap-south-2.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Jakarta)     | ap-southeast-3 | synthetics.ap-southeast-3.amazonaws.com<br>synthetics.ap-southeast-3.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (Malaysia)    | ap-southeast-5 | synthetics.ap-southeast-5.amazonaws.com<br>synthetics.ap-southeast-5.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (Melbourne)   | ap-southeast-4 | synthetics.ap-southeast-4.amazonaws.com<br>synthetics.ap-southeast-4.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (Mumbai)      | ap-south-1     | synthetics.ap-south-1.amazonaws.com<br>synthetics.ap-south-1.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (New Zealand) | ap-southeast-6 | synthetics.ap-southeast-6.amazonaws.com<br>synthetics.ap-southeast-6.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (Osaka)       | ap-northeast-3 | synthetics.ap-northeast-3.amazonaws.com<br>synthetics.ap-northeast-3.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)       | ap-northeast-2 | synthetics.ap-northeast-2.amazonaws.com<br>synthetics.ap-northeast-2.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore)   | ap-southeast-1 | synthetics.ap-southeast-1.amazonaws.com<br>synthetics.ap-southeast-1.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)      | ap-southeast-2 | synthetics.ap-southeast-2.amazonaws.com<br>synthetics.ap-southeast-2.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (Taipei)      | ap-east-2      | synthetics.ap-east-2.amazonaws.com<br>synthetics.ap-east-2.api.aws                                                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Thailand)    | ap-southeast-7 | synthetics.ap-southeast-7.amazonaws.com<br>synthetics.ap-southeast-7.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (Tokyo)       | ap-northeast-1 | synthetics.ap-northeast-1.amazonaws.com<br>synthetics.ap-northeast-1.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Canada (Central)           | ca-central-1   | synthetics.ca-central-1.amazonaws.com<br>synthetics-fips.ca-central-1.api.aws<br>synthetics-fips.ca-central-1.amazonaws.com<br>synthetics.ca-central-1.api.aws     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | synthetics.ca-west-1.amazonaws.com<br>synthetics-fips.ca-west-1.api.aws<br>synthetics-fips.ca-west-1.amazonaws.com<br>synthetics.ca-west-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)         | eu-central-1   | synthetics.eu-central-1.amazonaws.com<br>synthetics.eu-central-1.api.aws                                                                                           | HTTPS<br>HTTPS                   |
| Europe (Ireland)           | eu-west-1      | synthetics.eu-west-1.amazonaws.com<br>synthetics.eu-west-1.api.aws                                                                                                 | HTTPS<br>HTTPS                   |
| Europe (London)            | eu-west-2      | synthetics.eu-west-2.amazonaws.com<br>synthetics.eu-west-2.api.aws                                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Milan)             | eu-south-1     | synthetics.eu-south-1.amazonaws.com<br>synthetics.eu-south-1.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Europe (Paris)             | eu-west-3      | synthetics.eu-west-3.amazonaws.com<br>synthetics.eu-west-3.api.aws                                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Spain)             | eu-south-2     | synthetics.eu-south-2.amazonaws.com<br>synthetics.eu-south-2.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Europe (Stockholm)         | eu-north-1     | synthetics.eu-north-1.amazonaws.com<br>synthetics.eu-north-1.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Europe (Zurich)            | eu-central-2   | synthetics.eu-central-2.amazonaws.com<br>synthetics.eu-central-2.api.aws                                                                                           | HTTPS<br>HTTPS                   |
| Israel (Tel Aviv)          | il-central-1   | synthetics.il-central-1.amazonaws.com<br>synthetics.il-central-1.api.aws                                                                                           | HTTPS<br>HTTPS                   |
| Mexico (Central)           | mx-central-1   | synthetics.mx-central-1.amazonaws.com<br>synthetics.mx-central-1.api.aws                                                                                           | HTTPS<br>HTTPS                   |
| Middle East (Bahrain)      | me-south-1     | synthetics.me-south-1.amazonaws.com<br>synthetics.me-south-1.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Middle East (UAE)          | me-central-1   | synthetics.me-central-1.amazonaws.com<br>synthetics.me-central-1.api.aws                                                                                           | HTTPS<br>HTTPS                   |
| South America (São Paulo)  | sa-east-1      | synthetics.sa-east-1.amazonaws.com<br>synthetics.sa-east-1.api.aws                                                                                                 | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-East)     | us-gov-east-1  | synthetics.us-gov-east-1.amazonaws.com<br>synthetics-fips.us-gov-east-1.api.aws<br>synthetics-fips.us-gov-east-1.amazonaws.com<br>synthetics.us-gov-east-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| AWS GovCloud (US-West)     | us-gov-west-1  | synthetics.us-gov-west-1.amazonaws.com<br>synthetics-fips.us-gov-west-1.api.aws<br>synthetics-fips.us-gov-west-1.amazonaws.com<br>synthetics.us-gov-west-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |

## Service quotas

| Name               | Default                     | Adjustable                                                                                                                                                                                                   |
| ------------------ | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Number of canaries | 200 per Region per account. | [Yes](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/monitoring/quotas/L-C1FE0F5C "https://us-east-1.console.aws.amazon.com/servicequotas/home/services/monitoring/quotas/L-C1FE0F5C") |

For more information, see [CloudWatch
service quotas](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_limits.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_limits.md") in the _Amazon CloudWatch User Guide_.
