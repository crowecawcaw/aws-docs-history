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

| Region Name                | Region         | Endpoint                                                                                                                                                                       | Protocol                         |
| -------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------- |
| US East (Ohio)             | us-east-2      | controlcatalog.us-east-2.amazonaws.com<br>controlcatalog-fips.us-east-2.api.aws<br>controlcatalog-fips.us-east-2.amazonaws.com<br>controlcatalog.us-east-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | controlcatalog.us-east-1.amazonaws.com<br>controlcatalog-fips.us-east-1.api.aws<br>controlcatalog-fips.us-east-1.amazonaws.com<br>controlcatalog.us-east-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | controlcatalog.us-west-1.amazonaws.com<br>controlcatalog-fips.us-west-1.api.aws<br>controlcatalog-fips.us-west-1.amazonaws.com<br>controlcatalog.us-west-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | controlcatalog.us-west-2.amazonaws.com<br>controlcatalog-fips.us-west-2.api.aws<br>controlcatalog-fips.us-west-2.amazonaws.com<br>controlcatalog.us-west-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | controlcatalog.af-south-1.amazonaws.com<br>controlcatalog.af-south-1.api.aws                                                                                                   | HTTPS<br>HTTPS                   |
| Asia Pacific (Hong Kong)   | ap-east-1      | controlcatalog.ap-east-1.amazonaws.com<br>controlcatalog.ap-east-1.api.aws                                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Hyderabad)   | ap-south-2     | controlcatalog.ap-south-2.amazonaws.com<br>controlcatalog.ap-south-2.api.aws                                                                                                   | HTTPS<br>HTTPS                   |
| Asia Pacific (Jakarta)     | ap-southeast-3 | controlcatalog.ap-southeast-3.amazonaws.com<br>controlcatalog.ap-southeast-3.api.aws                                                                                           | HTTPS<br>HTTPS                   |
| Asia Pacific (Malaysia)    | ap-southeast-5 | controlcatalog.ap-southeast-5.amazonaws.com<br>controlcatalog.ap-southeast-5.api.aws                                                                                           | HTTPS<br>HTTPS                   |
| Asia Pacific (Melbourne)   | ap-southeast-4 | controlcatalog.ap-southeast-4.amazonaws.com<br>controlcatalog.ap-southeast-4.api.aws                                                                                           | HTTPS<br>HTTPS                   |
| Asia Pacific (Mumbai)      | ap-south-1     | controlcatalog.ap-south-1.amazonaws.com<br>controlcatalog.ap-south-1.api.aws                                                                                                   | HTTPS<br>HTTPS                   |
| Asia Pacific (New Zealand) | ap-southeast-6 | controlcatalog.ap-southeast-6.amazonaws.com<br>controlcatalog.ap-southeast-6.api.aws                                                                                           | HTTPS<br>HTTPS                   |
| Asia Pacific (Osaka)       | ap-northeast-3 | controlcatalog.ap-northeast-3.amazonaws.com<br>controlcatalog.ap-northeast-3.api.aws                                                                                           | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)       | ap-northeast-2 | controlcatalog.ap-northeast-2.amazonaws.com<br>controlcatalog.ap-northeast-2.api.aws                                                                                           | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore)   | ap-southeast-1 | controlcatalog.ap-southeast-1.amazonaws.com<br>controlcatalog.ap-southeast-1.api.aws                                                                                           | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)      | ap-southeast-2 | controlcatalog.ap-southeast-2.amazonaws.com<br>controlcatalog.ap-southeast-2.api.aws                                                                                           | HTTPS<br>HTTPS                   |
| Asia Pacific (Taipei)      | ap-east-2      | controlcatalog.ap-east-2.amazonaws.com<br>controlcatalog.ap-east-2.api.aws                                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Thailand)    | ap-southeast-7 | controlcatalog.ap-southeast-7.amazonaws.com<br>controlcatalog.ap-southeast-7.api.aws                                                                                           | HTTPS<br>HTTPS                   |
| Asia Pacific (Tokyo)       | ap-northeast-1 | controlcatalog.ap-northeast-1.amazonaws.com<br>controlcatalog.ap-northeast-1.api.aws                                                                                           | HTTPS<br>HTTPS                   |
| Canada (Central)           | ca-central-1   | controlcatalog.ca-central-1.amazonaws.com<br>controlcatalog-fips.ca-central-1.api.aws<br>controlcatalog-fips.ca-central-1.amazonaws.com<br>controlcatalog.ca-central-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | controlcatalog.ca-west-1.amazonaws.com<br>controlcatalog-fips.ca-west-1.api.aws<br>controlcatalog-fips.ca-west-1.amazonaws.com<br>controlcatalog.ca-west-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)         | eu-central-1   | controlcatalog.eu-central-1.amazonaws.com<br>controlcatalog.eu-central-1.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Europe (Ireland)           | eu-west-1      | controlcatalog.eu-west-1.amazonaws.com<br>controlcatalog.eu-west-1.api.aws                                                                                                     | HTTPS<br>HTTPS                   |
| Europe (London)            | eu-west-2      | controlcatalog.eu-west-2.amazonaws.com<br>controlcatalog.eu-west-2.api.aws                                                                                                     | HTTPS<br>HTTPS                   |
| Europe (Milan)             | eu-south-1     | controlcatalog.eu-south-1.amazonaws.com<br>controlcatalog.eu-south-1.api.aws                                                                                                   | HTTPS<br>HTTPS                   |
| Europe (Paris)             | eu-west-3      | controlcatalog.eu-west-3.amazonaws.com<br>controlcatalog.eu-west-3.api.aws                                                                                                     | HTTPS<br>HTTPS                   |
| Europe (Spain)             | eu-south-2     | controlcatalog.eu-south-2.amazonaws.com<br>controlcatalog.eu-south-2.api.aws                                                                                                   | HTTPS<br>HTTPS                   |
| Europe (Stockholm)         | eu-north-1     | controlcatalog.eu-north-1.amazonaws.com<br>controlcatalog.eu-north-1.api.aws                                                                                                   | HTTPS<br>HTTPS                   |
| Europe (Zurich)            | eu-central-2   | controlcatalog.eu-central-2.amazonaws.com<br>controlcatalog.eu-central-2.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Israel (Tel Aviv)          | il-central-1   | controlcatalog.il-central-1.amazonaws.com<br>controlcatalog.il-central-1.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Mexico (Central)           | mx-central-1   | controlcatalog.mx-central-1.amazonaws.com<br>controlcatalog.mx-central-1.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Middle East (Bahrain)      | me-south-1     | controlcatalog.me-south-1.amazonaws.com<br>controlcatalog.me-south-1.api.aws                                                                                                   | HTTPS<br>HTTPS                   |
| Middle East (UAE)          | me-central-1   | controlcatalog.me-central-1.amazonaws.com<br>controlcatalog.me-central-1.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| South America (São Paulo)  | sa-east-1      | controlcatalog.sa-east-1.amazonaws.com<br>controlcatalog.sa-east-1.api.aws                                                                                                     | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-East)     | us-gov-east-1  | controlcatalog.us-gov-east-1.amazonaws.com<br>controlcatalog.us-gov-east-1.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-West)     | us-gov-west-1  | controlcatalog.us-gov-west-1.amazonaws.com<br>controlcatalog.us-gov-west-1.api.aws                                                                                             | HTTPS<br>HTTPS                   |

## Service Quotas

This service has no quotas.
