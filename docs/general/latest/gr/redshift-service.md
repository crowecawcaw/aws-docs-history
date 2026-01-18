# Amazon Redshift endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

**Redshift API**

| Region Name                | Region         | Endpoint                                                                        | Protocol       |
| -------------------------- | -------------- | ------------------------------------------------------------------------------- | -------------- |
| US East (Ohio)             | us-east-2      | redshift.us-east-2.amazonaws.com<br>redshift-fips.us-east-2.amazonaws.com       | HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | redshift.us-east-1.amazonaws.com<br>redshift-fips.us-east-1.amazonaws.com       | HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | redshift.us-west-1.amazonaws.com<br>redshift-fips.us-west-1.amazonaws.com       | HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | redshift.us-west-2.amazonaws.com<br>redshift-fips.us-west-2.amazonaws.com       | HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | redshift.af-south-1.amazonaws.com                                               | HTTPS          |
| Asia Pacific (Hong Kong)   | ap-east-1      | redshift.ap-east-1.amazonaws.com                                                | HTTPS          |
| Asia Pacific (Hyderabad)   | ap-south-2     | redshift.ap-south-2.amazonaws.com                                               | HTTPS          |
| Asia Pacific (Jakarta)     | ap-southeast-3 | redshift.ap-southeast-3.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Malaysia)    | ap-southeast-5 | redshift.ap-southeast-5.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Melbourne)   | ap-southeast-4 | redshift.ap-southeast-4.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Mumbai)      | ap-south-1     | redshift.ap-south-1.amazonaws.com                                               | HTTPS          |
| Asia Pacific (New Zealand) | ap-southeast-6 | redshift.ap-southeast-6.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Osaka)       | ap-northeast-3 | redshift.ap-northeast-3.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Seoul)       | ap-northeast-2 | redshift.ap-northeast-2.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Singapore)   | ap-southeast-1 | redshift.ap-southeast-1.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Sydney)      | ap-southeast-2 | redshift.ap-southeast-2.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Taipei)      | ap-east-2      | redshift.ap-east-2.amazonaws.com                                                | HTTPS          |
| Asia Pacific (Thailand)    | ap-southeast-7 | redshift.ap-southeast-7.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Tokyo)       | ap-northeast-1 | redshift.ap-northeast-1.amazonaws.com                                           | HTTPS          |
| Canada (Central)           | ca-central-1   | redshift.ca-central-1.amazonaws.com<br>redshift-fips.ca-central-1.amazonaws.com | HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | redshift.ca-west-1.amazonaws.com<br>redshift-fips.ca-west-1.amazonaws.com       | HTTPS<br>HTTPS |
| Europe (Frankfurt)         | eu-central-1   | redshift.eu-central-1.amazonaws.com                                             | HTTPS          |
| Europe (Ireland)           | eu-west-1      | redshift.eu-west-1.amazonaws.com                                                | HTTPS          |
| Europe (London)            | eu-west-2      | redshift.eu-west-2.amazonaws.com                                                | HTTPS          |
| Europe (Milan)             | eu-south-1     | redshift.eu-south-1.amazonaws.com                                               | HTTPS          |
| Europe (Paris)             | eu-west-3      | redshift.eu-west-3.amazonaws.com                                                | HTTPS          |
| Europe (Spain)             | eu-south-2     | redshift.eu-south-2.amazonaws.com                                               | HTTPS          |
| Europe (Stockholm)         | eu-north-1     | redshift.eu-north-1.amazonaws.com                                               | HTTPS          |
| Europe (Zurich)            | eu-central-2   | redshift.eu-central-2.amazonaws.com                                             | HTTPS          |
| Israel (Tel Aviv)          | il-central-1   | redshift.il-central-1.amazonaws.com                                             | HTTPS          |
| Mexico (Central)           | mx-central-1   | redshift.mx-central-1.amazonaws.com                                             | HTTPS          |
| Middle East (Bahrain)      | me-south-1     | redshift.me-south-1.amazonaws.com                                               | HTTPS          |
| Middle East (UAE)          | me-central-1   | redshift.me-central-1.amazonaws.com                                             | HTTPS          |
| South America (São Paulo)  | sa-east-1      | redshift.sa-east-1.amazonaws.com                                                | HTTPS          |
| AWS GovCloud (US-East)     | us-gov-east-1  | redshift.us-gov-east-1.amazonaws.com<br>redshift-fips.us-gov-east-1.api.aws     | HTTPS<br>HTTPS |
| AWS GovCloud (US-West)     | us-gov-west-1  | redshift.us-gov-west-1.amazonaws.com<br>redshift-fips.us-gov-west-1.api.aws     | HTTPS<br>HTTPS |

**Redshift Serverless API**

| Region Name                | Region         | Endpoint                                                                                                                                                                                               | Protocol                         |
| -------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------- |
| US East (Ohio)             | us-east-2      | redshift-serverless.us-east-2.amazonaws.com<br>redshift-serverless-fips.us-east-2.api.aws<br>redshift-serverless-fips.us-east-2.amazonaws.com<br>redshift-serverless.us-east-2.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | redshift-serverless.us-east-1.amazonaws.com<br>redshift-serverless-fips.us-east-1.api.aws<br>redshift-serverless-fips.us-east-1.amazonaws.com<br>redshift-serverless.us-east-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | redshift-serverless.us-west-1.amazonaws.com<br>redshift-serverless-fips.us-west-1.api.aws<br>redshift-serverless-fips.us-west-1.amazonaws.com<br>redshift-serverless.us-west-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | redshift-serverless.us-west-2.amazonaws.com<br>redshift-serverless-fips.us-west-2.api.aws<br>redshift-serverless-fips.us-west-2.amazonaws.com<br>redshift-serverless.us-west-2.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | redshift-serverless.af-south-1.amazonaws.com<br>redshift-serverless.af-south-1.api.aws                                                                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Hong Kong)   | ap-east-1      | redshift-serverless.ap-east-1.amazonaws.com<br>redshift-serverless.ap-east-1.api.aws                                                                                                                   | HTTPS<br>HTTPS                   |
| Asia Pacific (Hyderabad)   | ap-south-2     | redshift-serverless.ap-south-2.amazonaws.com<br>redshift-serverless.ap-south-2.api.aws                                                                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Jakarta)     | ap-southeast-3 | redshift-serverless.ap-southeast-3.amazonaws.com<br>redshift-serverless.ap-southeast-3.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Malaysia)    | ap-southeast-5 | redshift-serverless.ap-southeast-5.amazonaws.com<br>redshift-serverless.ap-southeast-5.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Mumbai)      | ap-south-1     | redshift-serverless.ap-south-1.amazonaws.com<br>redshift-serverless.ap-south-1.api.aws                                                                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (New Zealand) | ap-southeast-6 | redshift-serverless.ap-southeast-6.amazonaws.com<br>redshift-serverless.ap-southeast-6.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Osaka)       | ap-northeast-3 | redshift-serverless.ap-northeast-3.amazonaws.com<br>redshift-serverless.ap-northeast-3.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)       | ap-northeast-2 | redshift-serverless.ap-northeast-2.amazonaws.com<br>redshift-serverless.ap-northeast-2.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore)   | ap-southeast-1 | redshift-serverless.ap-southeast-1.amazonaws.com<br>redshift-serverless.ap-southeast-1.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)      | ap-southeast-2 | redshift-serverless.ap-southeast-2.amazonaws.com<br>redshift-serverless.ap-southeast-2.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Taipei)      | ap-east-2      | redshift-serverless.ap-east-2.amazonaws.com<br>redshift-serverless.ap-east-2.api.aws                                                                                                                   | HTTPS<br>HTTPS                   |
| Asia Pacific (Thailand)    | ap-southeast-7 | redshift-serverless.ap-southeast-7.amazonaws.com<br>redshift-serverless.ap-southeast-7.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Tokyo)       | ap-northeast-1 | redshift-serverless.ap-northeast-1.amazonaws.com<br>redshift-serverless.ap-northeast-1.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Canada (Central)           | ca-central-1   | redshift-serverless.ca-central-1.amazonaws.com<br>redshift-serverless-fips.ca-central-1.api.aws<br>redshift-serverless-fips.ca-central-1.amazonaws.com<br>redshift-serverless.ca-central-1.api.aws     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)         | eu-central-1   | redshift-serverless.eu-central-1.amazonaws.com<br>redshift-serverless.eu-central-1.api.aws                                                                                                             | HTTPS<br>HTTPS                   |
| Europe (Ireland)           | eu-west-1      | redshift-serverless.eu-west-1.amazonaws.com<br>redshift-serverless.eu-west-1.api.aws                                                                                                                   | HTTPS<br>HTTPS                   |
| Europe (London)            | eu-west-2      | redshift-serverless.eu-west-2.amazonaws.com<br>redshift-serverless.eu-west-2.api.aws                                                                                                                   | HTTPS<br>HTTPS                   |
| Europe (Milan)             | eu-south-1     | redshift-serverless.eu-south-1.amazonaws.com<br>redshift-serverless.eu-south-1.api.aws                                                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Paris)             | eu-west-3      | redshift-serverless.eu-west-3.amazonaws.com<br>redshift-serverless.eu-west-3.api.aws                                                                                                                   | HTTPS<br>HTTPS                   |
| Europe (Spain)             | eu-south-2     | redshift-serverless.eu-south-2.amazonaws.com<br>redshift-serverless.eu-south-2.api.aws                                                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Stockholm)         | eu-north-1     | redshift-serverless.eu-north-1.amazonaws.com<br>redshift-serverless.eu-north-1.api.aws                                                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Zurich)            | eu-central-2   | redshift-serverless.eu-central-2.amazonaws.com<br>redshift-serverless.eu-central-2.api.aws                                                                                                             | HTTPS<br>HTTPS                   |
| Israel (Tel Aviv)          | il-central-1   | redshift-serverless.il-central-1.amazonaws.com<br>redshift-serverless.il-central-1.api.aws                                                                                                             | HTTPS<br>HTTPS                   |
| Mexico (Central)           | mx-central-1   | redshift-serverless.mx-central-1.amazonaws.com<br>redshift-serverless.mx-central-1.api.aws                                                                                                             | HTTPS<br>HTTPS                   |
| Middle East (UAE)          | me-central-1   | redshift-serverless.me-central-1.amazonaws.com<br>redshift-serverless.me-central-1.api.aws                                                                                                             | HTTPS<br>HTTPS                   |
| South America (São Paulo)  | sa-east-1      | redshift-serverless.sa-east-1.amazonaws.com<br>redshift-serverless.sa-east-1.api.aws                                                                                                                   | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-East)     | us-gov-east-1  | redshift-serverless.us-gov-east-1.amazonaws.com<br>redshift-serverless-fips.us-gov-east-1.api.aws<br>redshift-serverless-fips.us-gov-east-1.amazonaws.com<br>redshift-serverless.us-gov-east-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| AWS GovCloud (US-West)     | us-gov-west-1  | redshift-serverless.us-gov-west-1.amazonaws.com<br>redshift-serverless-fips.us-gov-west-1.api.aws<br>redshift-serverless-fips.us-gov-west-1.amazonaws.com<br>redshift-serverless.us-gov-west-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |

**Redshift Data API**

| Region Name                | Region         | Endpoint                                                                                                                                                                       | Protocol                         |
| -------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------- |
| US East (Ohio)             | us-east-2      | redshift-data.us-east-2.amazonaws.com<br>redshift-data-fips.us-east-2.api.aws<br>redshift-data.us-east-2.api.aws<br>redshift-data-fips.us-east-2.amazonaws.com                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | redshift-data.us-east-1.amazonaws.com<br>redshift-data-fips.us-east-1.api.aws<br>redshift-data.us-east-1.api.aws<br>redshift-data-fips.us-east-1.amazonaws.com                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | redshift-data.us-west-1.amazonaws.com<br>redshift-data-fips.us-west-1.api.aws<br>redshift-data.us-west-1.api.aws<br>redshift-data-fips.us-west-1.amazonaws.com                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | redshift-data.us-west-2.amazonaws.com<br>redshift-data-fips.us-west-2.api.aws<br>redshift-data.us-west-2.api.aws<br>redshift-data-fips.us-west-2.amazonaws.com                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | redshift-data.af-south-1.amazonaws.com<br>redshift-data.af-south-1.api.aws                                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Hong Kong)   | ap-east-1      | redshift-data.ap-east-1.amazonaws.com<br>redshift-data.ap-east-1.api.aws                                                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (Hyderabad)   | ap-south-2     | redshift-data.ap-south-2.amazonaws.com<br>redshift-data.ap-south-2.api.aws                                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Jakarta)     | ap-southeast-3 | redshift-data.ap-southeast-3.amazonaws.com<br>redshift-data.ap-southeast-3.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Malaysia)    | ap-southeast-5 | redshift-data.ap-southeast-5.amazonaws.com<br>redshift-data.ap-southeast-5.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Melbourne)   | ap-southeast-4 | redshift-data.ap-southeast-4.amazonaws.com<br>redshift-data.ap-southeast-4.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Mumbai)      | ap-south-1     | redshift-data.ap-south-1.amazonaws.com<br>redshift-data.ap-south-1.api.aws                                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (New Zealand) | ap-southeast-6 | redshift-data.ap-southeast-6.amazonaws.com<br>redshift-data.ap-southeast-6.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Osaka)       | ap-northeast-3 | redshift-data.ap-northeast-3.amazonaws.com<br>redshift-data.ap-northeast-3.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)       | ap-northeast-2 | redshift-data.ap-northeast-2.amazonaws.com<br>redshift-data.ap-northeast-2.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore)   | ap-southeast-1 | redshift-data.ap-southeast-1.amazonaws.com<br>redshift-data.ap-southeast-1.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)      | ap-southeast-2 | redshift-data.ap-southeast-2.amazonaws.com<br>redshift-data.ap-southeast-2.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Taipei)      | ap-east-2      | redshift-data.ap-east-2.amazonaws.com<br>redshift-data.ap-east-2.api.aws                                                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (Thailand)    | ap-southeast-7 | redshift-data.ap-southeast-7.amazonaws.com<br>redshift-data.ap-southeast-7.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Tokyo)       | ap-northeast-1 | redshift-data.ap-northeast-1.amazonaws.com<br>redshift-data.ap-northeast-1.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Canada (Central)           | ca-central-1   | redshift-data.ca-central-1.amazonaws.com<br>redshift-data-fips.ca-central-1.api.aws<br>redshift-data.ca-central-1.api.aws<br>redshift-data-fips.ca-central-1.amazonaws.com     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | redshift-data.ca-west-1.amazonaws.com<br>redshift-data-fips.ca-west-1.api.aws<br>redshift-data.ca-west-1.api.aws<br>redshift-data-fips.ca-west-1.amazonaws.com                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)         | eu-central-1   | redshift-data.eu-central-1.amazonaws.com<br>redshift-data.eu-central-1.api.aws                                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Ireland)           | eu-west-1      | redshift-data.eu-west-1.amazonaws.com<br>redshift-data.eu-west-1.api.aws                                                                                                       | HTTPS<br>HTTPS                   |
| Europe (London)            | eu-west-2      | redshift-data.eu-west-2.amazonaws.com<br>redshift-data.eu-west-2.api.aws                                                                                                       | HTTPS<br>HTTPS                   |
| Europe (Milan)             | eu-south-1     | redshift-data.eu-south-1.amazonaws.com<br>redshift-data.eu-south-1.api.aws                                                                                                     | HTTPS<br>HTTPS                   |
| Europe (Paris)             | eu-west-3      | redshift-data.eu-west-3.amazonaws.com<br>redshift-data.eu-west-3.api.aws                                                                                                       | HTTPS<br>HTTPS                   |
| Europe (Spain)             | eu-south-2     | redshift-data.eu-south-2.amazonaws.com<br>redshift-data.eu-south-2.api.aws                                                                                                     | HTTPS<br>HTTPS                   |
| Europe (Stockholm)         | eu-north-1     | redshift-data.eu-north-1.amazonaws.com<br>redshift-data.eu-north-1.api.aws                                                                                                     | HTTPS<br>HTTPS                   |
| Europe (Zurich)            | eu-central-2   | redshift-data.eu-central-2.amazonaws.com<br>redshift-data.eu-central-2.api.aws                                                                                                 | HTTPS<br>HTTPS                   |
| Israel (Tel Aviv)          | il-central-1   | redshift-data.il-central-1.amazonaws.com<br>redshift-data.il-central-1.api.aws                                                                                                 | HTTPS<br>HTTPS                   |
| Mexico (Central)           | mx-central-1   | redshift-data.mx-central-1.amazonaws.com<br>redshift-data.mx-central-1.api.aws                                                                                                 | HTTPS<br>HTTPS                   |
| Middle East (Bahrain)      | me-south-1     | redshift-data.me-south-1.amazonaws.com<br>redshift-data.me-south-1.api.aws                                                                                                     | HTTPS<br>HTTPS                   |
| Middle East (UAE)          | me-central-1   | redshift-data.me-central-1.amazonaws.com<br>redshift-data.me-central-1.api.aws                                                                                                 | HTTPS<br>HTTPS                   |
| South America (São Paulo)  | sa-east-1      | redshift-data.sa-east-1.amazonaws.com<br>redshift-data.sa-east-1.api.aws                                                                                                       | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-East)     | us-gov-east-1  | redshift-data.us-gov-east-1.amazonaws.com<br>redshift-data-fips.us-gov-east-1.api.aws<br>redshift-data.us-gov-east-1.api.aws<br>redshift-data-fips.us-gov-east-1.amazonaws.com | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| AWS GovCloud (US-West)     | us-gov-west-1  | redshift-data.us-gov-west-1.amazonaws.com<br>redshift-data-fips.us-gov-west-1.api.aws<br>redshift-data.us-gov-west-1.api.aws<br>redshift-data-fips.us-gov-west-1.amazonaws.com | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |

**Redshift query editor v2**

| Region Name                | Region         | Endpoint                                      | Protocol |
| -------------------------- | -------------- | --------------------------------------------- | -------- |
| US East (Ohio)             | us-east-2      | api.sqlworkbench.us-east-2.amazonaws.com      | HTTPS    |
| US East (N. Virginia)      | us-east-1      | api.sqlworkbench.us-east-1.amazonaws.com      | HTTPS    |
| US West (N. California)    | us-west-1      | api.sqlworkbench.us-west-1.amazonaws.com      | HTTPS    |
| US West (Oregon)           | us-west-2      | api.sqlworkbench.us-west-2.amazonaws.com      | HTTPS    |
| Africa (Cape Town)         | af-south-1     | api.sqlworkbench.af-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Hong Kong)   | ap-east-1      | api.sqlworkbench.ap-east-1.amazonaws.com      | HTTPS    |
| Asia Pacific (Hyderabad)   | ap-south-2     | api.sqlworkbench.ap-south-2.amazonaws.com     | HTTPS    |
| Asia Pacific (Jakarta)     | ap-southeast-3 | api.sqlworkbench.ap-southeast-3.amazonaws.com | HTTPS    |
| Asia Pacific (Malaysia)    | ap-southeast-5 | api.sqlworkbench.ap-southeast-5.amazonaws.com | HTTPS    |
| Asia Pacific (Melbourne)   | ap-southeast-4 | api.sqlworkbench.ap-southeast-4.amazonaws.com | HTTPS    |
| Asia Pacific (Mumbai)      | ap-south-1     | api.sqlworkbench.ap-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (New Zealand) | ap-southeast-6 | api.sqlworkbench.ap-southeast-6.amazonaws.com | HTTPS    |
| Asia Pacific (Osaka)       | ap-northeast-3 | api.sqlworkbench.ap-northeast-3.amazonaws.com | HTTPS    |
| Asia Pacific (Seoul)       | ap-northeast-2 | api.sqlworkbench.ap-northeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Singapore)   | ap-southeast-1 | api.sqlworkbench.ap-southeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)      | ap-southeast-2 | api.sqlworkbench.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Thailand)    | ap-southeast-7 | api.sqlworkbench.ap-southeast-7.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)       | ap-northeast-1 | api.sqlworkbench.ap-northeast-1.amazonaws.com | HTTPS    |
| Canada (Central)           | ca-central-1   | api.sqlworkbench.ca-central-1.amazonaws.com   | HTTPS    |
| Canada West (Calgary)      | ca-west-1      | api.sqlworkbench.ca-west-1.amazonaws.com      | HTTPS    |
| Europe (Frankfurt)         | eu-central-1   | api.sqlworkbench.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)           | eu-west-1      | api.sqlworkbench.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)            | eu-west-2      | api.sqlworkbench.eu-west-2.amazonaws.com      | HTTPS    |
| Europe (Milan)             | eu-south-1     | api.sqlworkbench.eu-south-1.amazonaws.com     | HTTPS    |
| Europe (Paris)             | eu-west-3      | api.sqlworkbench.eu-west-3.amazonaws.com      | HTTPS    |
| Europe (Spain)             | eu-south-2     | api.sqlworkbench.eu-south-2.amazonaws.com     | HTTPS    |
| Europe (Stockholm)         | eu-north-1     | api.sqlworkbench.eu-north-1.amazonaws.com     | HTTPS    |
| Europe (Zurich)            | eu-central-2   | api.sqlworkbench.eu-central-2.amazonaws.com   | HTTPS    |
| Israel (Tel Aviv)          | il-central-1   | api.sqlworkbench.il-central-1.amazonaws.com   | HTTPS    |
| Mexico (Central)           | mx-central-1   | api.sqlworkbench.mx-central-1.amazonaws.com   | HTTPS    |
| Middle East (Bahrain)      | me-south-1     | api.sqlworkbench.me-south-1.amazonaws.com     | HTTPS    |
| Middle East (UAE)          | me-central-1   | api.sqlworkbench.me-central-1.amazonaws.com   | HTTPS    |
| South America (São Paulo)  | sa-east-1      | api.sqlworkbench.sa-east-1.amazonaws.com      | HTTPS    |
| AWS GovCloud (US-East)     | us-gov-east-1  | api.sqlworkbench.us-gov-east-1.amazonaws.com  | HTTPS    |
| AWS GovCloud (US-West)     | us-gov-west-1  | api.sqlworkbench.us-gov-west-1.amazonaws.com  | HTTPS    |

## Service quotas

For information, see [Quotas and limits
in Amazon Redshift](../../../redshift/latest/mgmt/amazon-redshift-limits.md "../../../redshift/latest/mgmt/amazon-redshift-limits.md") in the _Amazon Redshift Management Guide_.
