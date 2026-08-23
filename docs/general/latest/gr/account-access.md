# Account access management endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name               | Region         | Endpoint                              | Protocol |
| ------------------------- | -------------- | ------------------------------------- | -------- |
| US East (Ohio)            | us-east-2      | account-access.us-east-2.api.aws      |          |
| US East (N. Virginia)     | us-east-1      | account-access.us-east-1.api.aws      |          |
| US West (Oregon)          | us-west-2      | account-access.us-west-2.api.aws      |          |
| Asia Pacific (Mumbai)     | ap-south-1     | account-access.ap-south-1.api.aws     |          |
| Asia Pacific (Osaka)      | ap-northeast-3 | account-access.ap-northeast-3.api.aws |          |
| Asia Pacific (Seoul)      | ap-northeast-2 | account-access.ap-northeast-2.api.aws |          |
| Asia Pacific (Sydney)     | ap-southeast-2 | account-access.ap-southeast-2.api.aws |          |
| Asia Pacific (Tokyo)      | ap-northeast-1 | account-access.ap-northeast-1.api.aws |          |
| Canada (Central)          | ca-central-1   | account-access.ca-central-1.api.aws   |          |
| Europe (Frankfurt)        | eu-central-1   | account-access.eu-central-1.api.aws   |          |
| Europe (Ireland)          | eu-west-1      | account-access.eu-west-1.api.aws      |          |
| Europe (London)           | eu-west-2      | account-access.eu-west-2.api.aws      |          |
| Europe (Paris)            | eu-west-3      | account-access.eu-west-3.api.aws      |          |
| Europe (Stockholm)        | eu-north-1     | account-access.eu-north-1.api.aws     |          |
| South America (São Paulo) | sa-east-1      | account-access.sa-east-1.api.aws      |          |

## Service quotas

| Name                        | Default                   | Adjustable                                                                                                                                                                                       | Description                                                                                       |
| --------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| Group entitlements per role | Each supported Region: 20 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/account-access/quotas/L-42A1D874 "https://console.aws.amazon.com/servicequotas/home/services/account-access/quotas/L-42A1D874") | The maximum number of group entitlements that can be assigned to a single role in an application. |
