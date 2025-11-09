# CloudWatch Observability Access Manager endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                | Region         | Endpoint                                                                                                                               | Protocol                         |
| -------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| US East (Ohio)             | us-east-2      | oam.us-east-2.amazonaws.com<br>oam-fips.us-east-2.api.aws<br>oam-fips.us-east-2.amazonaws.com<br>oam.us-east-2.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | oam.us-east-1.amazonaws.com<br>oam-fips.us-east-1.api.aws<br>oam-fips.us-east-1.amazonaws.com<br>oam.us-east-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | oam.us-west-1.amazonaws.com<br>oam-fips.us-west-1.api.aws<br>oam-fips.us-west-1.amazonaws.com<br>oam.us-west-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | oam.us-west-2.amazonaws.com<br>oam-fips.us-west-2.api.aws<br>oam-fips.us-west-2.amazonaws.com<br>oam.us-west-2.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | oam.af-south-1.amazonaws.com<br>oam.af-south-1.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Hong Kong)   | ap-east-1      | oam.ap-east-1.amazonaws.com<br>oam.ap-east-1.api.aws                                                                                   | HTTPS<br>HTTPS                   |
| Asia Pacific (Hyderabad)   | ap-south-2     | oam.ap-south-2.amazonaws.com<br>oam.ap-south-2.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Jakarta)     | ap-southeast-3 | oam.ap-southeast-3.amazonaws.com<br>oam.ap-southeast-3.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Malaysia)    | ap-southeast-5 | oam.ap-southeast-5.amazonaws.com<br>oam.ap-southeast-5.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Melbourne)   | ap-southeast-4 | oam.ap-southeast-4.amazonaws.com<br>oam.ap-southeast-4.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Mumbai)      | ap-south-1     | oam.ap-south-1.amazonaws.com<br>oam.ap-south-1.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (New Zealand) | ap-southeast-6 | oam.ap-southeast-6.amazonaws.com                                                                                                       | HTTPS                            |
| Asia Pacific (Osaka)       | ap-northeast-3 | oam.ap-northeast-3.amazonaws.com<br>oam.ap-northeast-3.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)       | ap-northeast-2 | oam.ap-northeast-2.amazonaws.com<br>oam.ap-northeast-2.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore)   | ap-southeast-1 | oam.ap-southeast-1.amazonaws.com<br>oam.ap-southeast-1.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)      | ap-southeast-2 | oam.ap-southeast-2.amazonaws.com<br>oam.ap-southeast-2.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Taipei)      | ap-east-2      | oam.ap-east-2.amazonaws.com<br>oam.ap-east-2.api.aws                                                                                   | HTTPS<br>HTTPS                   |
| Asia Pacific (Thailand)    | ap-southeast-7 | oam.ap-southeast-7.amazonaws.com<br>oam.ap-southeast-7.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Tokyo)       | ap-northeast-1 | oam.ap-northeast-1.amazonaws.com<br>oam.ap-northeast-1.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Canada (Central)           | ca-central-1   | oam.ca-central-1.amazonaws.com<br>oam-fips.ca-central-1.api.aws<br>oam-fips.ca-central-1.amazonaws.com<br>oam.ca-central-1.api.aws     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | oam.ca-west-1.amazonaws.com<br>oam-fips.ca-west-1.api.aws<br>oam-fips.ca-west-1.amazonaws.com<br>oam.ca-west-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)         | eu-central-1   | oam.eu-central-1.amazonaws.com<br>oam.eu-central-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Europe (Ireland)           | eu-west-1      | oam.eu-west-1.amazonaws.com<br>oam.eu-west-1.api.aws                                                                                   | HTTPS<br>HTTPS                   |
| Europe (London)            | eu-west-2      | oam.eu-west-2.amazonaws.com<br>oam.eu-west-2.api.aws                                                                                   | HTTPS<br>HTTPS                   |
| Europe (Milan)             | eu-south-1     | oam.eu-south-1.amazonaws.com<br>oam.eu-south-1.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Paris)             | eu-west-3      | oam.eu-west-3.amazonaws.com<br>oam.eu-west-3.api.aws                                                                                   | HTTPS<br>HTTPS                   |
| Europe (Spain)             | eu-south-2     | oam.eu-south-2.amazonaws.com<br>oam.eu-south-2.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Stockholm)         | eu-north-1     | oam.eu-north-1.amazonaws.com<br>oam.eu-north-1.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Zurich)            | eu-central-2   | oam.eu-central-2.amazonaws.com<br>oam.eu-central-2.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Israel (Tel Aviv)          | il-central-1   | oam.il-central-1.amazonaws.com<br>oam.il-central-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Mexico (Central)           | mx-central-1   | oam.mx-central-1.amazonaws.com<br>oam.mx-central-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Middle East (Bahrain)      | me-south-1     | oam.me-south-1.amazonaws.com<br>oam.me-south-1.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| Middle East (UAE)          | me-central-1   | oam.me-central-1.amazonaws.com<br>oam.me-central-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| South America (São Paulo)  | sa-east-1      | oam.sa-east-1.amazonaws.com<br>oam.sa-east-1.api.aws                                                                                   | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-East)     | us-gov-east-1  | oam.us-gov-east-1.amazonaws.com<br>oam-fips.us-gov-east-1.api.aws<br>oam-fips.us-gov-east-1.amazonaws.com<br>oam.us-gov-east-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| AWS GovCloud (US-West)     | us-gov-west-1  | oam.us-gov-west-1.amazonaws.com<br>oam-fips.us-gov-west-1.api.aws<br>oam-fips.us-gov-west-1.amazonaws.com<br>oam.us-gov-west-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |

## Service quotas

| Name                                 | Default                              | Adjustable | Description                                                                                                   |
| ------------------------------------ | ------------------------------------ | ---------- | ------------------------------------------------------------------------------------------------------------- |
| Links per sink                       | Each supported Region: 100,000       | No         | Maximum number of links that can be attached to a sink                                                        |
| Number of links                      | Each supported Region: 5             | No         | Maximum number of links in your account                                                                       |
| Number of sinks                      | Each supported Region: 1             | No         | Maximum number of sinks in your account                                                                       |
| Rate of CreateLink requests          | Each supported Region: 10 per second | No         | Maximum number of CreateLink requests you can make per second, in this account in the current region          |
| Rate of CreateSink requests          | Each supported Region: 10 per second | No         | Maximum number of CreateSink requests you can make per second, in this account in the current region          |
| Rate of DeleteLink requests          | Each supported Region: 10 per second | No         | Maximum number of DeleteLink requests you can make per second, in this account in the current region          |
| Rate of DeleteSink requests          | Each supported Region: 10 per second | No         | Maximum number of DeleteSink requests you can make per second, in this account in the current region          |
| Rate of GetLink requests             | Each supported Region: 10 per second | No         | Maximum number of GetLink requests you can make per second, in this account in the current region             |
| Rate of GetSink requests             | Each supported Region: 10 per second | No         | Maximum number of GetSink requests you can make per second, in this account in the current region             |
| Rate of GetSinkPolicy requests       | Each supported Region: 10 per second | No         | Maximum number of GetSinkPolicy requests you can make per second, in this account in the current region       |
| Rate of ListAttachedLinks requests   | Each supported Region: 10 per second | No         | Maximum number of ListAttachedLinks requests you can make per second, in this account in the current region   |
| Rate of ListLinks requests           | Each supported Region: 10 per second | No         | Maximum number of ListLinks requests you can make per second, in this account in the current region           |
| Rate of ListSinks requests           | Each supported Region: 10 per second | No         | Maximum number of ListSinks requests you can make per second, in this account in the current region           |
| Rate of ListTagsForResource requests | Each supported Region: 10 per second | No         | Maximum number of ListTagsForResource requests you can make per second, in this account in the current region |
| Rate of PutSinkPolicy requests       | Each supported Region: 1 per second  | No         | Maximum number of PutSinkPolicy requests you can make per second, in this account in the current region       |
| Rate of TagResource requests         | Each supported Region: 10 per second | No         | Maximum number of TagResource requests you can make per second, in this account in the current region         |
| Rate of UntagResource requests       | Each supported Region: 10 per second | No         | Maximum number of UntagResource requests you can make per second, in this account in the current region       |
| Rate of UpdateLink requests          | Each supported Region: 10 per second | No         | Maximum number of UpdateLink requests you can make per second, in this account in the current region          |
