# CloudWatch Observability Access Manager endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                | Region         | Endpoint                                                                                                                      | Protocol                |
| -------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| US East (Ohio)             | us-east-2      | oam.us-east-2.amazonaws.com oam-fips.us-east-2.api.aws oam-fips.us-east-2.amazonaws.com oam.us-east-2.api.aws                 | HTTPS HTTPS HTTPS HTTPS |
| US East (N. Virginia)      | us-east-1      | oam.us-east-1.amazonaws.com oam-fips.us-east-1.api.aws oam-fips.us-east-1.amazonaws.com oam.us-east-1.api.aws                 | HTTPS HTTPS HTTPS HTTPS |
| US West (N. California)    | us-west-1      | oam.us-west-1.amazonaws.com oam-fips.us-west-1.api.aws oam-fips.us-west-1.amazonaws.com oam.us-west-1.api.aws                 | HTTPS HTTPS HTTPS HTTPS |
| US West (Oregon)           | us-west-2      | oam.us-west-2.amazonaws.com oam-fips.us-west-2.api.aws oam-fips.us-west-2.amazonaws.com oam.us-west-2.api.aws                 | HTTPS HTTPS HTTPS HTTPS |
| Africa (Cape Town)         | af-south-1     | oam.af-south-1.amazonaws.com oam.af-south-1.api.aws                                                                           | HTTPS HTTPS             |
| Asia Pacific (Hong Kong)   | ap-east-1      | oam.ap-east-1.amazonaws.com oam.ap-east-1.api.aws                                                                             | HTTPS HTTPS             |
| Asia Pacific (Hyderabad)   | ap-south-2     | oam.ap-south-2.amazonaws.com oam.ap-south-2.api.aws                                                                           | HTTPS HTTPS             |
| Asia Pacific (Jakarta)     | ap-southeast-3 | oam.ap-southeast-3.amazonaws.com oam.ap-southeast-3.api.aws                                                                   | HTTPS HTTPS             |
| Asia Pacific (Malaysia)    | ap-southeast-5 | oam.ap-southeast-5.amazonaws.com oam.ap-southeast-5.api.aws                                                                   | HTTPS HTTPS             |
| Asia Pacific (Melbourne)   | ap-southeast-4 | oam.ap-southeast-4.amazonaws.com oam.ap-southeast-4.api.aws                                                                   | HTTPS HTTPS             |
| Asia Pacific (Mumbai)      | ap-south-1     | oam.ap-south-1.amazonaws.com oam.ap-south-1.api.aws                                                                           | HTTPS HTTPS             |
| Asia Pacific (New Zealand) | ap-southeast-6 | oam.ap-southeast-6.amazonaws.com                                                                                              | HTTPS                   |
| Asia Pacific (Osaka)       | ap-northeast-3 | oam.ap-northeast-3.amazonaws.com oam.ap-northeast-3.api.aws                                                                   | HTTPS HTTPS             |
| Asia Pacific (Seoul)       | ap-northeast-2 | oam.ap-northeast-2.amazonaws.com oam.ap-northeast-2.api.aws                                                                   | HTTPS HTTPS             |
| Asia Pacific (Singapore)   | ap-southeast-1 | oam.ap-southeast-1.amazonaws.com oam.ap-southeast-1.api.aws                                                                   | HTTPS HTTPS             |
| Asia Pacific (Sydney)      | ap-southeast-2 | oam.ap-southeast-2.amazonaws.com oam.ap-southeast-2.api.aws                                                                   | HTTPS HTTPS             |
| Asia Pacific (Taipei)      | ap-east-2      | oam.ap-east-2.amazonaws.com oam.ap-east-2.api.aws                                                                             | HTTPS HTTPS             |
| Asia Pacific (Thailand)    | ap-southeast-7 | oam.ap-southeast-7.amazonaws.com oam.ap-southeast-7.api.aws                                                                   | HTTPS HTTPS             |
| Asia Pacific (Tokyo)       | ap-northeast-1 | oam.ap-northeast-1.amazonaws.com oam.ap-northeast-1.api.aws                                                                   | HTTPS HTTPS             |
| Canada (Central)           | ca-central-1   | oam.ca-central-1.amazonaws.com oam-fips.ca-central-1.api.aws oam-fips.ca-central-1.amazonaws.com oam.ca-central-1.api.aws     | HTTPS HTTPS HTTPS HTTPS |
| Canada West (Calgary)      | ca-west-1      | oam.ca-west-1.amazonaws.com oam-fips.ca-west-1.api.aws oam-fips.ca-west-1.amazonaws.com oam.ca-west-1.api.aws                 | HTTPS HTTPS HTTPS HTTPS |
| Europe (Frankfurt)         | eu-central-1   | oam.eu-central-1.amazonaws.com oam.eu-central-1.api.aws                                                                       | HTTPS HTTPS             |
| Europe (Ireland)           | eu-west-1      | oam.eu-west-1.amazonaws.com oam.eu-west-1.api.aws                                                                             | HTTPS HTTPS             |
| Europe (London)            | eu-west-2      | oam.eu-west-2.amazonaws.com oam.eu-west-2.api.aws                                                                             | HTTPS HTTPS             |
| Europe (Milan)             | eu-south-1     | oam.eu-south-1.amazonaws.com oam.eu-south-1.api.aws                                                                           | HTTPS HTTPS             |
| Europe (Paris)             | eu-west-3      | oam.eu-west-3.amazonaws.com oam.eu-west-3.api.aws                                                                             | HTTPS HTTPS             |
| Europe (Spain)             | eu-south-2     | oam.eu-south-2.amazonaws.com oam.eu-south-2.api.aws                                                                           | HTTPS HTTPS             |
| Europe (Stockholm)         | eu-north-1     | oam.eu-north-1.amazonaws.com oam.eu-north-1.api.aws                                                                           | HTTPS HTTPS             |
| Europe (Zurich)            | eu-central-2   | oam.eu-central-2.amazonaws.com oam.eu-central-2.api.aws                                                                       | HTTPS HTTPS             |
| Israel (Tel Aviv)          | il-central-1   | oam.il-central-1.amazonaws.com oam.il-central-1.api.aws                                                                       | HTTPS HTTPS             |
| Mexico (Central)           | mx-central-1   | oam.mx-central-1.amazonaws.com oam.mx-central-1.api.aws                                                                       | HTTPS HTTPS             |
| Middle East (Bahrain)      | me-south-1     | oam.me-south-1.amazonaws.com oam.me-south-1.api.aws                                                                           | HTTPS HTTPS             |
| Middle East (UAE)          | me-central-1   | oam.me-central-1.amazonaws.com oam.me-central-1.api.aws                                                                       | HTTPS HTTPS             |
| South America (São Paulo)  | sa-east-1      | oam.sa-east-1.amazonaws.com oam.sa-east-1.api.aws                                                                             | HTTPS HTTPS             |
| AWS GovCloud (US-East)     | us-gov-east-1  | oam.us-gov-east-1.amazonaws.com oam-fips.us-gov-east-1.api.aws oam-fips.us-gov-east-1.amazonaws.com oam.us-gov-east-1.api.aws | HTTPS HTTPS HTTPS HTTPS |
| AWS GovCloud (US-West)     | us-gov-west-1  | oam.us-gov-west-1.amazonaws.com oam-fips.us-gov-west-1.api.aws oam-fips.us-gov-west-1.amazonaws.com oam.us-gov-west-1.api.aws | HTTPS HTTPS HTTPS HTTPS | ## Service quotas For information about CloudWatch OAM quotas, see [CloudWatch service quotas](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_limits.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_limits.md"). |
