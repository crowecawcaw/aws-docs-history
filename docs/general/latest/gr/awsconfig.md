# AWS Config endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                | Region         | Endpoint                                                              | Protocol       |
| -------------------------- | -------------- | --------------------------------------------------------------------- | -------------- |
| US East (Ohio)             | us-east-2      | config.us-east-2.amazonaws.com<br>config-fips.us-east-2.amazonaws.com | HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | config.us-east-1.amazonaws.com<br>config-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | config.us-west-1.amazonaws.com<br>config-fips.us-west-1.amazonaws.com | HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | config.us-west-2.amazonaws.com<br>config-fips.us-west-2.amazonaws.com | HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | config.af-south-1.amazonaws.com                                       | HTTPS          |
| Asia Pacific (Hong Kong)   | ap-east-1      | config.ap-east-1.amazonaws.com                                        | HTTPS          |
| Asia Pacific (Hyderabad)   | ap-south-2     | config.ap-south-2.amazonaws.com                                       | HTTPS          |
| Asia Pacific (Jakarta)     | ap-southeast-3 | config.ap-southeast-3.amazonaws.com                                   | HTTPS          |
| Asia Pacific (Malaysia)    | ap-southeast-5 | config.ap-southeast-5.amazonaws.com                                   | HTTPS          |
| Asia Pacific (Melbourne)   | ap-southeast-4 | config.ap-southeast-4.amazonaws.com                                   | HTTPS          |
| Asia Pacific (Mumbai)      | ap-south-1     | config.ap-south-1.amazonaws.com                                       | HTTPS          |
| Asia Pacific (New Zealand) | ap-southeast-6 | config.ap-southeast-6.amazonaws.com                                   | HTTPS          |
| Asia Pacific (Osaka)       | ap-northeast-3 | config.ap-northeast-3.amazonaws.com                                   | HTTPS          |
| Asia Pacific (Seoul)       | ap-northeast-2 | config.ap-northeast-2.amazonaws.com                                   | HTTPS          |
| Asia Pacific (Singapore)   | ap-southeast-1 | config.ap-southeast-1.amazonaws.com                                   | HTTPS          |
| Asia Pacific (Sydney)      | ap-southeast-2 | config.ap-southeast-2.amazonaws.com                                   | HTTPS          |
| Asia Pacific (Taipei)      | ap-east-2      | config.ap-east-2.amazonaws.com                                        | HTTPS          |
| Asia Pacific (Thailand)    | ap-southeast-7 | config.ap-southeast-7.amazonaws.com                                   | HTTPS          |
| Asia Pacific (Tokyo)       | ap-northeast-1 | config.ap-northeast-1.amazonaws.com                                   | HTTPS          |
| Canada (Central)           | ca-central-1   | config.ca-central-1.amazonaws.com                                     | HTTPS          |
| Canada West (Calgary)      | ca-west-1      | config.ca-west-1.amazonaws.com                                        | HTTPS          |
| Europe (Frankfurt)         | eu-central-1   | config.eu-central-1.amazonaws.com                                     | HTTPS          |
| Europe (Ireland)           | eu-west-1      | config.eu-west-1.amazonaws.com                                        | HTTPS          |
| Europe (London)            | eu-west-2      | config.eu-west-2.amazonaws.com                                        | HTTPS          |
| Europe (Milan)             | eu-south-1     | config.eu-south-1.amazonaws.com                                       | HTTPS          |
| Europe (Paris)             | eu-west-3      | config.eu-west-3.amazonaws.com                                        | HTTPS          |
| Europe (Spain)             | eu-south-2     | config.eu-south-2.amazonaws.com                                       | HTTPS          |
| Europe (Stockholm)         | eu-north-1     | config.eu-north-1.amazonaws.com                                       | HTTPS          |
| Europe (Zurich)            | eu-central-2   | config.eu-central-2.amazonaws.com                                     | HTTPS          |
| Israel (Tel Aviv)          | il-central-1   | config.il-central-1.amazonaws.com                                     | HTTPS          |
| Mexico (Central)           | mx-central-1   | config.mx-central-1.amazonaws.com                                     | HTTPS          |
| Middle East (Bahrain)      | me-south-1     | config.me-south-1.amazonaws.com                                       | HTTPS          |
| Middle East (UAE)          | me-central-1   | config.me-central-1.amazonaws.com                                     | HTTPS          |
| South America (São Paulo)  | sa-east-1      | config.sa-east-1.amazonaws.com                                        | HTTPS          |
| AWS GovCloud (US-East)     | us-gov-east-1  | config.us-gov-east-1.amazonaws.com                                    | HTTPS          |
| AWS GovCloud (US-West)     | us-gov-west-1  | config.us-gov-west-1.amazonaws.com                                    | HTTPS          |

## Service quotas

| Resource tags                       | Name | Default | Adjustable |
| ----------------------------------- | ---- | ------- | ---------- |
| Maximum number of tags per resource | 50   | No      |

| AWS Config rules                                          | Name | Default | Adjustable |
| --------------------------------------------------------- | ---- | ------- | ---------- |
| Maximum number of AWS Config Rules per Region per account | 1000 | No      |

| Single Account Conformance Packs                        | Name | Default | Adjustable |
| ------------------------------------------------------- | ---- | ------- | ---------- |
| Maximum number of conformance packs per account         | 50   | No      |
| Maximum number of AWS Config Rules per conformance pack | 130  | No      |

###### Note

AWS Config rules in conformance packs count in the quota for the Maximum number of AWS Config Rules per Region per account.

| Organization Conformance Packs                                       | Name | Default | Adjustable |
| -------------------------------------------------------------------- | ---- | ------- | ---------- |
| Maximum number of conformance packs per organization                 | 50   | No      |
| Maximum number of AWS Config Rules per organization conformance pack | 130  | No      |

###### Note

Deploying at the organization level counts in quota for child accounts. AWS Config rules in conformance packs count in the quota for the Maximum number of AWS Config Rules per Region per account.

| Aggregators                                                                 | Name  | Default                                                                                                      | Adjustable |
| --------------------------------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------ | ---------- |
| Maximum number of configuration aggregators                                 | 50    | [Yes](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home") |
| Maximum number of accounts in an aggregator                                 | 10000 | No                                                                                                           |
| Maximum number of accounts added or deleted per week for all<br>aggregators | 1000  | [Yes](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home") |

###### Note

Organization level aggregators and individual account aggregators both count in the quota for the Maximum number of configuration aggregators.

| Advanced queries                                                 | Name | Default                                                                                                      | Adjustable |
| ---------------------------------------------------------------- | ---- | ------------------------------------------------------------------------------------------------------------ | ---------- |
| Maximum number of saved queries in a single account and a Region | 300  | [Yes](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home") |
