# AWS Control

Catalog endpoints
and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service Endpoints

AWS Control Catalog has the following endpoints:

| Region Name                | Region         | Endpoint                                                                                                                                                              | Protocol                |
| -------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | --------------------------------------------- |
| US East (Ohio)             | us-east-2      | controlcatalog.us-east-2.amazonaws.com controlcatalog-fips.us-east-2.api.aws controlcatalog-fips.us-east-2.amazonaws.com controlcatalog.us-east-2.api.aws             | HTTPS HTTPS HTTPS HTTPS |
| US East (N. Virginia)      | us-east-1      | controlcatalog.us-east-1.amazonaws.com controlcatalog-fips.us-east-1.api.aws controlcatalog-fips.us-east-1.amazonaws.com controlcatalog.us-east-1.api.aws             | HTTPS HTTPS HTTPS HTTPS |
| US West (N. California)    | us-west-1      | controlcatalog.us-west-1.amazonaws.com controlcatalog-fips.us-west-1.api.aws controlcatalog-fips.us-west-1.amazonaws.com controlcatalog.us-west-1.api.aws             | HTTPS HTTPS HTTPS HTTPS |
| US West (Oregon)           | us-west-2      | controlcatalog.us-west-2.amazonaws.com controlcatalog-fips.us-west-2.api.aws controlcatalog-fips.us-west-2.amazonaws.com controlcatalog.us-west-2.api.aws             | HTTPS HTTPS HTTPS HTTPS |
| Africa (Cape Town)         | af-south-1     | controlcatalog.af-south-1.amazonaws.com controlcatalog.af-south-1.api.aws                                                                                             | HTTPS HTTPS             |
| Asia Pacific (Hong Kong)   | ap-east-1      | controlcatalog.ap-east-1.amazonaws.com controlcatalog.ap-east-1.api.aws                                                                                               | HTTPS HTTPS             |
| Asia Pacific (Hyderabad)   | ap-south-2     | controlcatalog.ap-south-2.amazonaws.com controlcatalog.ap-south-2.api.aws                                                                                             | HTTPS HTTPS             |
| Asia Pacific (Jakarta)     | ap-southeast-3 | controlcatalog.ap-southeast-3.amazonaws.com controlcatalog.ap-southeast-3.api.aws                                                                                     | HTTPS HTTPS             |
| Asia Pacific (Malaysia)    | ap-southeast-5 | controlcatalog.ap-southeast-5.amazonaws.com controlcatalog.ap-southeast-5.api.aws                                                                                     | HTTPS HTTPS             |
| Asia Pacific (Melbourne)   | ap-southeast-4 | controlcatalog.ap-southeast-4.amazonaws.com controlcatalog.ap-southeast-4.api.aws                                                                                     | HTTPS HTTPS             |
| Asia Pacific (Mumbai)      | ap-south-1     | controlcatalog.ap-south-1.amazonaws.com controlcatalog.ap-south-1.api.aws                                                                                             | HTTPS HTTPS             |
| Asia Pacific (New Zealand) | ap-southeast-6 | controlcatalog.ap-southeast-6.amazonaws.com controlcatalog.ap-southeast-6.api.aws                                                                                     | HTTPS HTTPS             |
| Asia Pacific (Osaka)       | ap-northeast-3 | controlcatalog.ap-northeast-3.amazonaws.com controlcatalog.ap-northeast-3.api.aws                                                                                     | HTTPS HTTPS             |
| Asia Pacific (Seoul)       | ap-northeast-2 | controlcatalog.ap-northeast-2.amazonaws.com controlcatalog.ap-northeast-2.api.aws                                                                                     | HTTPS HTTPS             |
| Asia Pacific (Singapore)   | ap-southeast-1 | controlcatalog.ap-southeast-1.amazonaws.com controlcatalog.ap-southeast-1.api.aws                                                                                     | HTTPS HTTPS             |
| Asia Pacific (Sydney)      | ap-southeast-2 | controlcatalog.ap-southeast-2.amazonaws.com controlcatalog.ap-southeast-2.api.aws                                                                                     | HTTPS HTTPS             |
| Asia Pacific (Taipei)      | ap-east-2      | controlcatalog.ap-east-2.amazonaws.com controlcatalog.ap-east-2.api.aws                                                                                               | HTTPS HTTPS             |
| Asia Pacific (Thailand)    | ap-southeast-7 | controlcatalog.ap-southeast-7.amazonaws.com controlcatalog.ap-southeast-7.api.aws                                                                                     | HTTPS HTTPS             |
| Asia Pacific (Tokyo)       | ap-northeast-1 | controlcatalog.ap-northeast-1.amazonaws.com controlcatalog.ap-northeast-1.api.aws                                                                                     | HTTPS HTTPS             |
| Canada (Central)           | ca-central-1   | controlcatalog.ca-central-1.amazonaws.com controlcatalog-fips.ca-central-1.api.aws controlcatalog-fips.ca-central-1.amazonaws.com controlcatalog.ca-central-1.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Canada West (Calgary)      | ca-west-1      | controlcatalog.ca-west-1.amazonaws.com controlcatalog-fips.ca-west-1.api.aws controlcatalog-fips.ca-west-1.amazonaws.com controlcatalog.ca-west-1.api.aws             | HTTPS HTTPS HTTPS HTTPS |
| Europe (Frankfurt)         | eu-central-1   | controlcatalog.eu-central-1.amazonaws.com controlcatalog.eu-central-1.api.aws                                                                                         | HTTPS HTTPS             |
| Europe (Ireland)           | eu-west-1      | controlcatalog.eu-west-1.amazonaws.com controlcatalog.eu-west-1.api.aws                                                                                               | HTTPS HTTPS             |
| Europe (London)            | eu-west-2      | controlcatalog.eu-west-2.amazonaws.com controlcatalog.eu-west-2.api.aws                                                                                               | HTTPS HTTPS             |
| Europe (Milan)             | eu-south-1     | controlcatalog.eu-south-1.amazonaws.com controlcatalog.eu-south-1.api.aws                                                                                             | HTTPS HTTPS             |
| Europe (Paris)             | eu-west-3      | controlcatalog.eu-west-3.amazonaws.com controlcatalog.eu-west-3.api.aws                                                                                               | HTTPS HTTPS             |
| Europe (Spain)             | eu-south-2     | controlcatalog.eu-south-2.amazonaws.com controlcatalog.eu-south-2.api.aws                                                                                             | HTTPS HTTPS             |
| Europe (Stockholm)         | eu-north-1     | controlcatalog.eu-north-1.amazonaws.com controlcatalog.eu-north-1.api.aws                                                                                             | HTTPS HTTPS             |
| Europe (Zurich)            | eu-central-2   | controlcatalog.eu-central-2.amazonaws.com controlcatalog.eu-central-2.api.aws                                                                                         | HTTPS HTTPS             |
| Israel (Tel Aviv)          | il-central-1   | controlcatalog.il-central-1.amazonaws.com controlcatalog.il-central-1.api.aws                                                                                         | HTTPS HTTPS             |
| Mexico (Central)           | mx-central-1   | controlcatalog.mx-central-1.amazonaws.com controlcatalog.mx-central-1.api.aws                                                                                         | HTTPS HTTPS             |
| Middle East (Bahrain)      | me-south-1     | controlcatalog.me-south-1.amazonaws.com controlcatalog.me-south-1.api.aws                                                                                             | HTTPS HTTPS             |
| Middle East (UAE)          | me-central-1   | controlcatalog.me-central-1.amazonaws.com controlcatalog.me-central-1.api.aws                                                                                         | HTTPS HTTPS             |
| South America (São Paulo)  | sa-east-1      | controlcatalog.sa-east-1.amazonaws.com controlcatalog.sa-east-1.api.aws                                                                                               | HTTPS HTTPS             |
| AWS GovCloud (US-East)     | us-gov-east-1  | controlcatalog.us-gov-east-1.amazonaws.com controlcatalog.us-gov-east-1.api.aws                                                                                       | HTTPS HTTPS             |
| AWS GovCloud (US-West)     | us-gov-west-1  | controlcatalog.us-gov-west-1.amazonaws.com controlcatalog.us-gov-west-1.api.aws                                                                                       | HTTPS HTTPS             | ## Service Quotas This service has no quotas. |
