# Amazon CloudWatch Application Insights endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name               | Region         | Endpoint                                                                                                                                                                                               | Protocol                         |
| ------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------- |
| US East (Ohio)            | us-east-2      | applicationinsights.us-east-2.amazonaws.com<br>applicationinsights-fips.us-east-2.api.aws<br>applicationinsights-fips.us-east-2.amazonaws.com<br>applicationinsights.us-east-2.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)     | us-east-1      | applicationinsights.us-east-1.amazonaws.com<br>applicationinsights-fips.us-east-1.api.aws<br>applicationinsights-fips.us-east-1.amazonaws.com<br>applicationinsights.us-east-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)   | us-west-1      | applicationinsights.us-west-1.amazonaws.com<br>applicationinsights-fips.us-west-1.api.aws<br>applicationinsights-fips.us-west-1.amazonaws.com<br>applicationinsights.us-west-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)          | us-west-2      | applicationinsights.us-west-2.amazonaws.com<br>applicationinsights-fips.us-west-2.api.aws<br>applicationinsights-fips.us-west-2.amazonaws.com<br>applicationinsights.us-west-2.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)        | af-south-1     | applicationinsights.af-south-1.amazonaws.com<br>applicationinsights.af-south-1.api.aws                                                                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Hong Kong)  | ap-east-1      | applicationinsights.ap-east-1.amazonaws.com<br>applicationinsights.ap-east-1.api.aws                                                                                                                   | HTTPS<br>HTTPS                   |
| Asia Pacific (Hyderabad)  | ap-south-2     | applicationinsights.ap-south-2.amazonaws.com<br>applicationinsights.ap-south-2.api.aws                                                                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Jakarta)    | ap-southeast-3 | applicationinsights.ap-southeast-3.amazonaws.com<br>applicationinsights.ap-southeast-3.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Melbourne)  | ap-southeast-4 | applicationinsights.ap-southeast-4.amazonaws.com<br>applicationinsights.ap-southeast-4.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Mumbai)     | ap-south-1     | applicationinsights.ap-south-1.amazonaws.com<br>applicationinsights.ap-south-1.api.aws                                                                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Osaka)      | ap-northeast-3 | applicationinsights.ap-northeast-3.amazonaws.com<br>applicationinsights.ap-northeast-3.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)      | ap-northeast-2 | applicationinsights.ap-northeast-2.amazonaws.com<br>applicationinsights.ap-northeast-2.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore)  | ap-southeast-1 | applicationinsights.ap-southeast-1.amazonaws.com<br>applicationinsights.ap-southeast-1.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)     | ap-southeast-2 | applicationinsights.ap-southeast-2.amazonaws.com<br>applicationinsights.ap-southeast-2.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Tokyo)      | ap-northeast-1 | applicationinsights.ap-northeast-1.amazonaws.com<br>applicationinsights.ap-northeast-1.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Canada (Central)          | ca-central-1   | applicationinsights.ca-central-1.amazonaws.com<br>applicationinsights-fips.ca-central-1.api.aws<br>applicationinsights-fips.ca-central-1.amazonaws.com<br>applicationinsights.ca-central-1.api.aws     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Canada West (Calgary)     | ca-west-1      | applicationinsights.ca-west-1.amazonaws.com<br>applicationinsights-fips.ca-west-1.api.aws<br>applicationinsights-fips.ca-west-1.amazonaws.com<br>applicationinsights.ca-west-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)        | eu-central-1   | applicationinsights.eu-central-1.amazonaws.com<br>applicationinsights.eu-central-1.api.aws                                                                                                             | HTTPS<br>HTTPS                   |
| Europe (Ireland)          | eu-west-1      | applicationinsights.eu-west-1.amazonaws.com<br>applicationinsights.eu-west-1.api.aws                                                                                                                   | HTTPS<br>HTTPS                   |
| Europe (London)           | eu-west-2      | applicationinsights.eu-west-2.amazonaws.com<br>applicationinsights.eu-west-2.api.aws                                                                                                                   | HTTPS<br>HTTPS                   |
| Europe (Milan)            | eu-south-1     | applicationinsights.eu-south-1.amazonaws.com<br>applicationinsights.eu-south-1.api.aws                                                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Paris)            | eu-west-3      | applicationinsights.eu-west-3.amazonaws.com<br>applicationinsights.eu-west-3.api.aws                                                                                                                   | HTTPS<br>HTTPS                   |
| Europe (Spain)            | eu-south-2     | applicationinsights.eu-south-2.amazonaws.com<br>applicationinsights.eu-south-2.api.aws                                                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Stockholm)        | eu-north-1     | applicationinsights.eu-north-1.amazonaws.com<br>applicationinsights.eu-north-1.api.aws                                                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Zurich)           | eu-central-2   | applicationinsights.eu-central-2.amazonaws.com<br>applicationinsights.eu-central-2.api.aws                                                                                                             | HTTPS<br>HTTPS                   |
| Israel (Tel Aviv)         | il-central-1   | applicationinsights.il-central-1.amazonaws.com<br>applicationinsights.il-central-1.api.aws                                                                                                             | HTTPS<br>HTTPS                   |
| Middle East (Bahrain)     | me-south-1     | applicationinsights.me-south-1.amazonaws.com<br>applicationinsights.me-south-1.api.aws                                                                                                                 | HTTPS<br>HTTPS                   |
| Middle East (UAE)         | me-central-1   | applicationinsights.me-central-1.amazonaws.com<br>applicationinsights.me-central-1.api.aws                                                                                                             | HTTPS<br>HTTPS                   |
| South America (São Paulo) | sa-east-1      | applicationinsights.sa-east-1.amazonaws.com<br>applicationinsights.sa-east-1.api.aws                                                                                                                   | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-East)    | us-gov-east-1  | applicationinsights.us-gov-east-1.amazonaws.com<br>applicationinsights-fips.us-gov-east-1.api.aws<br>applicationinsights-fips.us-gov-east-1.amazonaws.com<br>applicationinsights.us-gov-east-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| AWS GovCloud (US-West)    | us-gov-west-1  | applicationinsights.us-gov-west-1.amazonaws.com<br>applicationinsights-fips.us-gov-west-1.api.aws<br>applicationinsights-fips.us-gov-west-1.amazonaws.com<br>applicationinsights.us-gov-west-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |

## Service quotas

| Resource                    | Default quota                                                 |
| --------------------------- | ------------------------------------------------------------- |
| API requests                | All API actions are throttled to 5 TPS                        |
| Resource Group applications | 100 per account                                               |
| Account applications        | 1 per account                                                 |
| Log Streams                 | 5 per resource                                                |
| Observations per problem    | 20 per dashboard<br>40 per DescribeProblemObservations action |
| Metrics                     | 60 per resource                                               |
