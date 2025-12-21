# AWS Security Hub CSPM endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                | Region         | Endpoint                                                                                                                     | Protocol                |
| -------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| US East (Ohio)             | us-east-2      | securityhub.us-east-2.amazonaws.com<br>securityhub-fips.us-east-2.amazonaws.com<br>securityhub.us-east-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | securityhub.us-east-1.amazonaws.com<br>securityhub-fips.us-east-1.amazonaws.com<br>securityhub.us-east-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | securityhub.us-west-1.amazonaws.com<br>securityhub-fips.us-west-1.amazonaws.com<br>securityhub.us-west-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | securityhub.us-west-2.amazonaws.com<br>securityhub-fips.us-west-2.amazonaws.com<br>securityhub.us-west-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | securityhub.af-south-1.amazonaws.com<br>securityhub.af-south-1.api.aws                                                       | HTTPS<br>HTTPS          |
| Asia Pacific (Hong Kong)   | ap-east-1      | securityhub.ap-east-1.amazonaws.com<br>securityhub.ap-east-1.api.aws                                                         | HTTPS<br>HTTPS          |
| Asia Pacific (Hyderabad)   | ap-south-2     | securityhub.ap-south-2.amazonaws.com<br>securityhub.ap-south-2.api.aws                                                       | HTTPS<br>HTTPS          |
| Asia Pacific (Jakarta)     | ap-southeast-3 | securityhub.ap-southeast-3.amazonaws.com<br>securityhub.ap-southeast-3.api.aws                                               | HTTPS<br>HTTPS          |
| Asia Pacific (Malaysia)    | ap-southeast-5 | securityhub.ap-southeast-5.amazonaws.com<br>securityhub.ap-southeast-5.api.aws                                               | HTTPS<br>HTTPS          |
| Asia Pacific (Melbourne)   | ap-southeast-4 | securityhub.ap-southeast-4.amazonaws.com<br>securityhub.ap-southeast-4.api.aws                                               | HTTPS<br>HTTPS          |
| Asia Pacific (Mumbai)      | ap-south-1     | securityhub.ap-south-1.amazonaws.com<br>securityhub.ap-south-1.api.aws                                                       | HTTPS<br>HTTPS          |
| Asia Pacific (New Zealand) | ap-southeast-6 | securityhub.ap-southeast-6.amazonaws.com<br>securityhub.ap-southeast-6.api.aws                                               | HTTPS<br>HTTPS          |
| Asia Pacific (Osaka)       | ap-northeast-3 | securityhub.ap-northeast-3.amazonaws.com<br>securityhub.ap-northeast-3.api.aws                                               | HTTPS<br>HTTPS          |
| Asia Pacific (Seoul)       | ap-northeast-2 | securityhub.ap-northeast-2.amazonaws.com<br>securityhub.ap-northeast-2.api.aws                                               | HTTPS<br>HTTPS          |
| Asia Pacific (Singapore)   | ap-southeast-1 | securityhub.ap-southeast-1.amazonaws.com<br>securityhub.ap-southeast-1.api.aws                                               | HTTPS<br>HTTPS          |
| Asia Pacific (Sydney)      | ap-southeast-2 | securityhub.ap-southeast-2.amazonaws.com<br>securityhub.ap-southeast-2.api.aws                                               | HTTPS<br>HTTPS          |
| Asia Pacific (Taipei)      | ap-east-2      | securityhub.ap-east-2.amazonaws.com<br>securityhub.ap-east-2.api.aws                                                         | HTTPS<br>HTTPS          |
| Asia Pacific (Thailand)    | ap-southeast-7 | securityhub.ap-southeast-7.amazonaws.com<br>securityhub.ap-southeast-7.api.aws                                               | HTTPS<br>HTTPS          |
| Asia Pacific (Tokyo)       | ap-northeast-1 | securityhub.ap-northeast-1.amazonaws.com<br>securityhub.ap-northeast-1.api.aws                                               | HTTPS<br>HTTPS          |
| Canada (Central)           | ca-central-1   | securityhub.ca-central-1.amazonaws.com<br>securityhub.ca-central-1.api.aws                                                   | HTTPS<br>HTTPS          |
| Canada West (Calgary)      | ca-west-1      | securityhub.ca-west-1.amazonaws.com<br>securityhub.ca-west-1.api.aws                                                         | HTTPS<br>HTTPS          |
| Europe (Frankfurt)         | eu-central-1   | securityhub.eu-central-1.amazonaws.com<br>securityhub.eu-central-1.api.aws                                                   | HTTPS<br>HTTPS          |
| Europe (Ireland)           | eu-west-1      | securityhub.eu-west-1.amazonaws.com<br>securityhub.eu-west-1.api.aws                                                         | HTTPS<br>HTTPS          |
| Europe (London)            | eu-west-2      | securityhub.eu-west-2.amazonaws.com<br>securityhub.eu-west-2.api.aws                                                         | HTTPS<br>HTTPS          |
| Europe (Milan)             | eu-south-1     | securityhub.eu-south-1.amazonaws.com<br>securityhub.eu-south-1.api.aws                                                       | HTTPS<br>HTTPS          |
| Europe (Paris)             | eu-west-3      | securityhub.eu-west-3.amazonaws.com<br>securityhub.eu-west-3.api.aws                                                         | HTTPS<br>HTTPS          |
| Europe (Spain)             | eu-south-2     | securityhub.eu-south-2.amazonaws.com<br>securityhub.eu-south-2.api.aws                                                       | HTTPS<br>HTTPS          |
| Europe (Stockholm)         | eu-north-1     | securityhub.eu-north-1.amazonaws.com<br>securityhub.eu-north-1.api.aws                                                       | HTTPS<br>HTTPS          |
| Europe (Zurich)            | eu-central-2   | securityhub.eu-central-2.amazonaws.com<br>securityhub.eu-central-2.api.aws                                                   | HTTPS<br>HTTPS          |
| Israel (Tel Aviv)          | il-central-1   | securityhub.il-central-1.amazonaws.com<br>securityhub.il-central-1.api.aws                                                   | HTTPS<br>HTTPS          |
| Mexico (Central)           | mx-central-1   | securityhub.mx-central-1.amazonaws.com<br>securityhub.mx-central-1.api.aws                                                   | HTTPS<br>HTTPS          |
| Middle East (Bahrain)      | me-south-1     | securityhub.me-south-1.amazonaws.com<br>securityhub.me-south-1.api.aws                                                       | HTTPS<br>HTTPS          |
| Middle East (UAE)          | me-central-1   | securityhub.me-central-1.amazonaws.com<br>securityhub.me-central-1.api.aws                                                   | HTTPS<br>HTTPS          |
| South America (São Paulo)  | sa-east-1      | securityhub.sa-east-1.amazonaws.com<br>securityhub.sa-east-1.api.aws                                                         | HTTPS<br>HTTPS          |
| AWS GovCloud (US-East)     | us-gov-east-1  | securityhub.us-gov-east-1.amazonaws.com<br>securityhub-fips.us-gov-east-1.amazonaws.com<br>securityhub.us-gov-east-1.api.aws | HTTPS<br>HTTPS<br>HTTPS |
| AWS GovCloud (US-West)     | us-gov-west-1  | securityhub.us-gov-west-1.amazonaws.com<br>securityhub-fips.us-gov-west-1.amazonaws.com<br>securityhub.us-gov-west-1.api.aws | HTTPS<br>HTTPS<br>HTTPS |

## Service quotas

| Name                                           | Default                       | Adjustable | Description                                                                                                                                                      |
| ---------------------------------------------- | ----------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Number of Security Hub member accounts         | Each supported Region: 10,000 | No         | The maximum number of Security Hub member accounts that can be added for each Security Hub administrator account in each Region.                                 |
| Number of Security Hub outstanding invitations | Each supported Region: 1,000  | No         | The maximum number of outstanding Security Hub member account invitations that can be sent per AWS account (Security Hub administrator account) per Region.      |
| Number of automation rules                     | Each supported Region: 100    | No         | The maximum number of automation rules that can be created by a Security Hub administrator account.                                                              |
| Number of custom actions                       | Each supported Region: 50     | No         | The maximum number of custom actions that can be created per account per Region.                                                                                 |
| Number of custom insights                      | Each supported Region: 100    | No         | The maximum number of user-defined custom insights that can be created per AWS account per Region.                                                               |
| Number of insight results                      | Each supported Region: 100    | No         | The maximum number of aggregated results returned for the GetInsightsResults API operation.                                                                      |
| Security Hub finding retention time            | Each supported Region: 90     | No         | The maximum number of days a Security Hub finding is saved. This is 90 days after the most recent update or 90 days after the creation date if no update occurs. |

For more information about Security Hub CSPM quotas, see [Quotas](../../../securityhub/latest/userguide/securityhub_limits.md "../../../securityhub/latest/userguide/securityhub_limits.md") in the
_AWS Security Hub User Guide_.
