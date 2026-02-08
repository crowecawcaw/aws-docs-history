# Amazon Data Lifecycle Manager endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                | Region         | Endpoint                                                                                                                           | Protocol                         |
| -------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| US East (Ohio)             | us-east-2      | dlm.us-east-2.amazonaws.com<br>dlm.us-east-2.api.aws<br>dlm-fips.us-east-2.amazonaws.com<br>dlm-fips.us-east-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | dlm.us-east-1.amazonaws.com<br>dlm.us-east-1.api.aws<br>dlm-fips.us-east-1.api.aws<br>dlm-fips.us-east-1.amazonaws.com             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | dlm.us-west-1.amazonaws.com<br>dlm.us-west-1.api.aws<br>dlm-fips.us-west-1.api.aws<br>dlm-fips.us-west-1.amazonaws.com             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | dlm.us-west-2.amazonaws.com<br>dlm-fips.us-west-2.amazonaws.com<br>dlm.us-west-2.api.aws<br>dlm-fips.us-west-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | dlm.af-south-1.amazonaws.com<br>dlm.af-south-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Hong Kong)   | ap-east-1      | dlm.ap-east-1.amazonaws.com<br>dlm.ap-east-1.api.aws                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Hyderabad)   | ap-south-2     | dlm.ap-south-2.amazonaws.com<br>dlm.ap-south-2.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Jakarta)     | ap-southeast-3 | dlm.ap-southeast-3.amazonaws.com<br>dlm.ap-southeast-3.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Malaysia)    | ap-southeast-5 | dlm.ap-southeast-5.amazonaws.com<br>dlm.ap-southeast-5.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Melbourne)   | ap-southeast-4 | dlm.ap-southeast-4.amazonaws.com<br>dlm.ap-southeast-4.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Mumbai)      | ap-south-1     | dlm.ap-south-1.amazonaws.com<br>dlm.ap-south-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (New Zealand) | ap-southeast-6 | dlm.ap-southeast-6.amazonaws.com<br>dlm.ap-southeast-6.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Osaka)       | ap-northeast-3 | dlm.ap-northeast-3.amazonaws.com<br>dlm.ap-northeast-3.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)       | ap-northeast-2 | dlm.ap-northeast-2.amazonaws.com<br>dlm.ap-northeast-2.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore)   | ap-southeast-1 | dlm.ap-southeast-1.amazonaws.com<br>dlm.ap-southeast-1.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)      | ap-southeast-2 | dlm.ap-southeast-2.amazonaws.com<br>dlm.ap-southeast-2.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Taipei)      | ap-east-2      | dlm.ap-east-2.amazonaws.com<br>dlm.ap-east-2.api.aws                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Thailand)    | ap-southeast-7 | dlm.ap-southeast-7.amazonaws.com<br>dlm.ap-southeast-7.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Tokyo)       | ap-northeast-1 | dlm.ap-northeast-1.amazonaws.com<br>dlm.ap-northeast-1.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Canada (Central)           | ca-central-1   | dlm.ca-central-1.amazonaws.com<br>dlm.ca-central-1.api.aws<br>dlm-fips.ca-central-1.api.aws<br>dlm-fips.ca-central-1.amazonaws.com | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | dlm.ca-west-1.amazonaws.com<br>dlm.ca-west-1.api.aws<br>dlm-fips.ca-west-1.api.aws                                                 | HTTPS<br>HTTPS<br>HTTPS          |
| Europe (Frankfurt)         | eu-central-1   | dlm.eu-central-1.amazonaws.com<br>dlm.eu-central-1.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Europe (Ireland)           | eu-west-1      | dlm.eu-west-1.amazonaws.com<br>dlm.eu-west-1.api.aws                                                                               | HTTPS<br>HTTPS                   |
| Europe (London)            | eu-west-2      | dlm.eu-west-2.amazonaws.com<br>dlm.eu-west-2.api.aws                                                                               | HTTPS<br>HTTPS                   |
| Europe (Milan)             | eu-south-1     | dlm.eu-south-1.amazonaws.com<br>dlm.eu-south-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Europe (Paris)             | eu-west-3      | dlm.eu-west-3.amazonaws.com<br>dlm.eu-west-3.api.aws                                                                               | HTTPS<br>HTTPS                   |
| Europe (Spain)             | eu-south-2     | dlm.eu-south-2.amazonaws.com<br>dlm.eu-south-2.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Europe (Stockholm)         | eu-north-1     | dlm.eu-north-1.amazonaws.com<br>dlm.eu-north-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Europe (Zurich)            | eu-central-2   | dlm.eu-central-2.amazonaws.com<br>dlm.eu-central-2.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Israel (Tel Aviv)          | il-central-1   | dlm.il-central-1.amazonaws.com<br>dlm.il-central-1.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Mexico (Central)           | mx-central-1   | dlm.mx-central-1.amazonaws.com<br>dlm.mx-central-1.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Middle East (Bahrain)      | me-south-1     | dlm.me-south-1.amazonaws.com<br>dlm.me-south-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Middle East (UAE)          | me-central-1   | dlm.me-central-1.amazonaws.com<br>dlm.me-central-1.api.aws                                                                         | HTTPS<br>HTTPS                   |
| South America (São Paulo)  | sa-east-1      | dlm.sa-east-1.amazonaws.com<br>dlm.sa-east-1.api.aws                                                                               | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-East)     | us-gov-east-1  | dlm.us-gov-east-1.amazonaws.com<br>dlm.us-gov-east-1.api.aws<br>dlm-fips.us-gov-east-1.api.aws                                     | HTTPS<br>HTTPS<br>HTTPS          |
| AWS GovCloud (US-West)     | us-gov-west-1  | dlm.us-gov-west-1.amazonaws.com<br>dlm.us-gov-west-1.api.aws<br>dlm-fips.us-gov-west-1.api.aws                                     | HTTPS<br>HTTPS<br>HTTPS          |

## Service quotas

| Name                             | Default                    | Adjustable                                                                                                                                                                 | Description                                             |
| -------------------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Policies per Region              | Each supported Region: 100 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/dlm/quotas/L-5407D8DA "https://console.aws.amazon.com/servicequotas/home/services/dlm/quotas/L-5407D8DA") | The maximum number of policies per Region.              |
| Target accounts per sharing rule | Each supported Region: 50  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/dlm/quotas/L-DCA05F2F "https://console.aws.amazon.com/servicequotas/home/services/dlm/quotas/L-DCA05F2F") | The maximum number of target accounts per sharing rule. |
