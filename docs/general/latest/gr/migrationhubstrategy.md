# Migration Hub Strategy Recommendations endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name           | Region         | Endpoint                                           | Protocol |
| --------------------- | -------------- | -------------------------------------------------- | -------- |
| US East (N. Virginia) | us-east-1      | migrationhub-strategy.us-east-1.amazonaws.com      | HTTPS    |
| US West (Oregon)      | us-west-2      | migrationhub-strategy.us-west-2.amazonaws.com      | HTTPS    |
| Asia Pacific (Sydney) | ap-southeast-2 | migrationhub-strategy.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)  | ap-northeast-1 | migrationhub-strategy.ap-northeast-1.amazonaws.com | HTTPS    |
| Europe (Frankfurt)    | eu-central-1   | migrationhub-strategy.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)      | eu-west-1      | migrationhub-strategy.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)       | eu-west-2      | migrationhub-strategy.eu-west-2.amazonaws.com      | HTTPS    |

## Service quotas

| Name                          | Default                    | Adjustable                                                                                                                                                                                                   | Description                                          |
| ----------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| Active Assessment Maximum     | Each supported Region: 1   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/migrationhubstrategy/quotas/L-A80C6746 "https://console.aws.amazon.com/servicequotas/home/services/migrationhubstrategy/quotas/L-A80C6746") | The maximum number of concurrent active assessments  |
| Active Import Maximum         | Each supported Region: 5   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/migrationhubstrategy/quotas/L-33C4B34A "https://console.aws.amazon.com/servicequotas/home/services/migrationhubstrategy/quotas/L-33C4B34A") | The maximum number of concurrent active import tasks |
| Assessment Maximum            | Each supported Region: 50  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/migrationhubstrategy/quotas/L-7571197D "https://console.aws.amazon.com/servicequotas/home/services/migrationhubstrategy/quotas/L-7571197D") | The maximum number of assessments per AWS account    |
| Maximum Server per Assessment | Each supported Region: 300 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/migrationhubstrategy/quotas/L-649F667C "https://console.aws.amazon.com/servicequotas/home/services/migrationhubstrategy/quotas/L-649F667C") | The maximum number of servers per assessment         |
