# Amazon Kinesis Data Streams endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                | Region         | Endpoint                                                                                                                               | Protocol                         |
| -------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| US East (Ohio)             | us-east-2      | kinesis.us-east-2.amazonaws.com<br>kinesis-fips.us-east-2.api.aws<br>kinesis-fips.us-east-2.amazonaws.com<br>kinesis.us-east-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | kinesis.us-east-1.amazonaws.com<br>kinesis-fips.us-east-1.api.aws<br>kinesis-fips.us-east-1.amazonaws.com<br>kinesis.us-east-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | kinesis.us-west-1.amazonaws.com<br>kinesis-fips.us-west-1.api.aws<br>kinesis-fips.us-west-1.amazonaws.com<br>kinesis.us-west-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | kinesis.us-west-2.amazonaws.com<br>kinesis-fips.us-west-2.api.aws<br>kinesis-fips.us-west-2.amazonaws.com<br>kinesis.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | kinesis.af-south-1.amazonaws.com<br>kinesis.af-south-1.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Hong Kong)   | ap-east-1      | kinesis.ap-east-1.amazonaws.com<br>kinesis.ap-east-1.api.aws                                                                           | HTTPS<br>HTTPS                   |
| Asia Pacific (Hyderabad)   | ap-south-2     | kinesis.ap-south-2.amazonaws.com<br>kinesis.ap-south-2.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Jakarta)     | ap-southeast-3 | kinesis.ap-southeast-3.amazonaws.com<br>kinesis.ap-southeast-3.api.aws                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Malaysia)    | ap-southeast-5 | kinesis.ap-southeast-5.amazonaws.com<br>kinesis.ap-southeast-5.api.aws                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Melbourne)   | ap-southeast-4 | kinesis.ap-southeast-4.amazonaws.com<br>kinesis.ap-southeast-4.api.aws                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Mumbai)      | ap-south-1     | kinesis.ap-south-1.amazonaws.com<br>kinesis.ap-south-1.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (New Zealand) | ap-southeast-6 | kinesis.ap-southeast-6.amazonaws.com<br>kinesis.ap-southeast-6.api.aws                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Osaka)       | ap-northeast-3 | kinesis.ap-northeast-3.amazonaws.com<br>kinesis.ap-northeast-3.api.aws                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)       | ap-northeast-2 | kinesis.ap-northeast-2.amazonaws.com<br>kinesis.ap-northeast-2.api.aws                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore)   | ap-southeast-1 | kinesis.ap-southeast-1.amazonaws.com<br>kinesis.ap-southeast-1.api.aws                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)      | ap-southeast-2 | kinesis.ap-southeast-2.amazonaws.com<br>kinesis.ap-southeast-2.api.aws                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Taipei)      | ap-east-2      | kinesis.ap-east-2.amazonaws.com<br>kinesis.ap-east-2.api.aws                                                                           | HTTPS<br>HTTPS                   |
| Asia Pacific (Thailand)    | ap-southeast-7 | kinesis.ap-southeast-7.amazonaws.com<br>kinesis.ap-southeast-7.api.aws                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Tokyo)       | ap-northeast-1 | kinesis.ap-northeast-1.amazonaws.com<br>kinesis.ap-northeast-1.api.aws                                                                 | HTTPS<br>HTTPS                   |
| Canada (Central)           | ca-central-1   | kinesis.ca-central-1.amazonaws.com<br>kinesis.ca-central-1.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Canada West (Calgary)      | ca-west-1      | kinesis.ca-west-1.amazonaws.com<br>kinesis.ca-west-1.api.aws                                                                           | HTTPS<br>HTTPS                   |
| Europe (Frankfurt)         | eu-central-1   | kinesis.eu-central-1.amazonaws.com<br>kinesis.eu-central-1.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Europe (Ireland)           | eu-west-1      | kinesis.eu-west-1.amazonaws.com<br>kinesis.eu-west-1.api.aws                                                                           | HTTPS<br>HTTPS                   |
| Europe (London)            | eu-west-2      | kinesis.eu-west-2.amazonaws.com<br>kinesis.eu-west-2.api.aws                                                                           | HTTPS<br>HTTPS                   |
| Europe (Milan)             | eu-south-1     | kinesis.eu-south-1.amazonaws.com<br>kinesis.eu-south-1.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Europe (Paris)             | eu-west-3      | kinesis.eu-west-3.amazonaws.com<br>kinesis.eu-west-3.api.aws                                                                           | HTTPS<br>HTTPS                   |
| Europe (Spain)             | eu-south-2     | kinesis.eu-south-2.amazonaws.com<br>kinesis.eu-south-2.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Europe (Stockholm)         | eu-north-1     | kinesis.eu-north-1.amazonaws.com<br>kinesis.eu-north-1.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Europe (Zurich)            | eu-central-2   | kinesis.eu-central-2.amazonaws.com<br>kinesis.eu-central-2.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Israel (Tel Aviv)          | il-central-1   | kinesis.il-central-1.amazonaws.com<br>kinesis.il-central-1.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Mexico (Central)           | mx-central-1   | kinesis.mx-central-1.amazonaws.com<br>kinesis.mx-central-1.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Middle East (Bahrain)      | me-south-1     | kinesis.me-south-1.amazonaws.com<br>kinesis.me-south-1.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Middle East (UAE)          | me-central-1   | kinesis.me-central-1.amazonaws.com<br>kinesis.me-central-1.api.aws                                                                     | HTTPS<br>HTTPS                   |
| South America (São Paulo)  | sa-east-1      | kinesis.sa-east-1.amazonaws.com<br>kinesis.sa-east-1.api.aws                                                                           | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-East)     | us-gov-east-1  | kinesis.us-gov-east-1.amazonaws.com<br>kinesis.us-gov-east-1.api.aws                                                                   | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-West)     | us-gov-west-1  | kinesis.us-gov-west-1.amazonaws.com<br>kinesis.us-gov-west-1.api.aws                                                                   | HTTPS<br>HTTPS                   |

## Service quotas

| Name              | Default                                                                                                                                                                                                                                                                  | Adjustable                                                                                                                                                                         | Description                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Shards per Region | us-east-1: 20,000<br>us-east-2: 6,000<br>us-west-2: 20,000<br>ap-northeast-1: 6,000<br>ap-south-1: 6,000<br>ap-southeast-1: 6,000<br>ap-southeast-2: 6,000<br>eu-central-1: 6,000<br>eu-west-1: 20,000<br>eu-west-3: 6,000<br>Each of the other supported Regions: 1,000 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/kinesis/quotas/L-0918CF54 "https://console.aws.amazon.com/servicequotas/home/services/kinesis/quotas/L-0918CF54") | The maximum number of shards that you can create in this account in the current Region. |

If you’re using strict security policies that require explicit allowlisting of service endpoints, you must also allowlist the following account-level endpoints to ensure Kinesis Data Streams actions succeed.

- **Control-plane APIs**: `*.control-kinesis.<Region>.amazonaws.com and *.control-kinesis.<Region>.api.aws`
- **Data-plane APIs**: `*.data-kinesis.<Region>.amazonaws.com and *.data-kinesis.<Region>.api.aws`

The `.api.aws` endpoints are dual stack endpoints that accept IPv6 requests.

For more information, see [Amazon Kinesis Data Streams Quotas](../../../streams/latest/dev/service-sizes-and-limits.md "../../../streams/latest/dev/service-sizes-and-limits.md") in the _Amazon Kinesis Data Streams Developer Guide_.
