# Amazon Aurora endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

### Amazon Aurora MySQL-Compatible Edition

| Region Name                | Region         | Endpoint                         | Protocol |
| -------------------------- | -------------- | -------------------------------- | -------- |
| US East (Ohio)             | us-east-2      | rds.us-east-2.amazonaws.com      | HTTPS    |
| US East (N. Virginia)      | us-east-1      | rds.us-east-1.amazonaws.com      | HTTPS    |
| US West (N. California)    | us-west-1      | rds.us-west-1.amazonaws.com      | HTTPS    |
| US West (Oregon)           | us-west-2      | rds.us-west-2.amazonaws.com      | HTTPS    |
| Africa (Cape Town)         | af-south-1     | rds.af-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Hong Kong)   | ap-east-1      | rds.ap-east-1.amazonaws.com      | HTTPS    |
| Asia Pacific (Hyderabad)   | ap-south-2     | rds.ap-south-2.amazonaws.com     | HTTPS    |
| Asia Pacific (Jakarta)     | ap-southeast-3 | rds.ap-southeast-3.amazonaws.com | HTTPS    |
| Asia Pacific (Malaysia)    | ap-southeast-5 | rds.ap-southeast-5.amazonaws.com | HTTPS    |
| Asia Pacific (Melbourne)   | ap-southeast-4 | rds.ap-southeast-4.amazonaws.com | HTTPS    |
| Asia Pacific (Mumbai)      | ap-south-1     | rds.ap-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (New Zealand) | ap-southeast-6 | rds.ap-southeast-6.amazonaws.com | HTTPS    |
| Asia Pacific (Osaka)       | ap-northeast-3 | rds.ap-northeast-3.amazonaws.com | HTTPS    |
| Asia Pacific (Seoul)       | ap-northeast-2 | rds.ap-northeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Singapore)   | ap-southeast-1 | rds.ap-southeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)      | ap-southeast-2 | rds.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Taipei)      | ap-east-2      | rds.ap-east-2.amazonaws.com      | HTTPS    |
| Asia Pacific (Thailand)    | ap-southeast-7 | rds.ap-southeast-7.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)       | ap-northeast-1 | rds.ap-northeast-1.amazonaws.com | HTTPS    |
| Canada (Central)           | ca-central-1   | rds.ca-central-1.amazonaws.com   | HTTPS    |
| Canada West (Calgary)      | ca-west-1      | rds.ca-west-1.amazonaws.com      | HTTPS    |
| Europe (Frankfurt)         | eu-central-1   | rds.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)           | eu-west-1      | rds.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)            | eu-west-2      | rds.eu-west-2.amazonaws.com      | HTTPS    |
| Europe (Milan)             | eu-south-1     | rds.eu-south-1.amazonaws.com     | HTTPS    |
| Europe (Paris)             | eu-west-3      | rds.eu-west-3.amazonaws.com      | HTTPS    |
| Europe (Spain)             | eu-south-2     | rds.eu-south-2.amazonaws.com     | HTTPS    |
| Europe (Stockholm)         | eu-north-1     | rds.eu-north-1.amazonaws.com     | HTTPS    |
| Europe (Zurich)            | eu-central-2   | rds.eu-central-2.amazonaws.com   | HTTPS    |
| Israel (Tel Aviv)          | il-central-1   | rds.il-central-1.amazonaws.com   | HTTPS    |
| Mexico (Central)           | mx-central-1   | rds.mx-central-1.amazonaws.com   | HTTPS    |
| Middle East (Bahrain)      | me-south-1     | rds.me-south-1.amazonaws.com     | HTTPS    |
| Middle East (UAE)          | me-central-1   | rds.me-central-1.amazonaws.com   | HTTPS    |
| South America (São Paulo)  | sa-east-1      | rds.sa-east-1.amazonaws.com      | HTTPS    |
| AWS GovCloud (US-East)     | us-gov-east-1  | rds.us-gov-east-1.amazonaws.com  | HTTPS    |
| AWS GovCloud (US-West)     | us-gov-west-1  | rds.us-gov-west-1.amazonaws.com  | HTTPS    |

### Amazon Aurora PostgreSQL-Compatible Edition

| Region Name                | Region         | Endpoint                         | Protocol |
| -------------------------- | -------------- | -------------------------------- | -------- |
| US East (Ohio)             | us-east-2      | rds.us-east-2.amazonaws.com      | HTTPS    |
| US East (N. Virginia)      | us-east-1      | rds.us-east-1.amazonaws.com      | HTTPS    |
| US West (N. California)    | us-west-1      | rds.us-west-1.amazonaws.com      | HTTPS    |
| US West (Oregon)           | us-west-2      | rds.us-west-2.amazonaws.com      | HTTPS    |
| Africa (Cape Town)         | af-south-1     | rds.af-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Hong Kong)   | ap-east-1      | rds.ap-east-1.amazonaws.com      | HTTPS    |
| Asia Pacific (Hyderabad)   | ap-south-2     | rds.ap-south-2.amazonaws.com     | HTTPS    |
| Asia Pacific (Jakarta)     | ap-southeast-3 | rds.ap-southeast-3.amazonaws.com | HTTPS    |
| Asia Pacific (Malaysia)    | ap-southeast-5 | rds.ap-southeast-5.amazonaws.com | HTTPS    |
| Asia Pacific (Melbourne)   | ap-southeast-4 | rds.ap-southeast-4.amazonaws.com | HTTPS    |
| Asia Pacific (Mumbai)      | ap-south-1     | rds.ap-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (New Zealand) | ap-southeast-6 | rds.ap-southeast-6.amazonaws.com | HTTPS    |
| Asia Pacific (Osaka)       | ap-northeast-3 | rds.ap-northeast-3.amazonaws.com | HTTPS    |
| Asia Pacific (Seoul)       | ap-northeast-2 | rds.ap-northeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Singapore)   | ap-southeast-1 | rds.ap-southeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)      | ap-southeast-2 | rds.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Taipei)      | ap-east-2      | rds.ap-east-2.amazonaws.com      | HTTPS    |
| Asia Pacific (Thailand)    | ap-southeast-7 | rds.ap-southeast-7.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)       | ap-northeast-1 | rds.ap-northeast-1.amazonaws.com | HTTPS    |
| Canada (Central)           | ca-central-1   | rds.ca-central-1.amazonaws.com   | HTTPS    |
| Canada West (Calgary)      | ca-west-1      | rds.ca-west-1.amazonaws.com      | HTTPS    |
| Europe (Frankfurt)         | eu-central-1   | rds.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)           | eu-west-1      | rds.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)            | eu-west-2      | rds.eu-west-2.amazonaws.com      | HTTPS    |
| Europe (Milan)             | eu-south-1     | rds.eu-south-1.amazonaws.com     | HTTPS    |
| Europe (Paris)             | eu-west-3      | rds.eu-west-3.amazonaws.com      | HTTPS    |
| Europe (Spain)             | eu-south-2     | rds.eu-south-2.amazonaws.com     | HTTPS    |
| Europe (Stockholm)         | eu-north-1     | rds.eu-north-1.amazonaws.com     | HTTPS    |
| Europe (Zurich)            | eu-central-2   | rds.eu-central-2.amazonaws.com   | HTTPS    |
| Israel (Tel Aviv)          | il-central-1   | rds.il-central-1.amazonaws.com   | HTTPS    |
| Mexico (Central)           | mx-central-1   | rds.mx-central-1.amazonaws.com   | HTTPS    |
| Middle East (Bahrain)      | me-south-1     | rds.me-south-1.amazonaws.com     | HTTPS    |
| Middle East (UAE)          | me-central-1   | rds.me-central-1.amazonaws.com   | HTTPS    |
| South America (São Paulo)  | sa-east-1      | rds.sa-east-1.amazonaws.com      | HTTPS    |
| AWS GovCloud (US-East)     | us-gov-east-1  | rds.us-gov-east-1.amazonaws.com  | HTTPS    |
| AWS GovCloud (US-West)     | us-gov-west-1  | rds.us-gov-west-1.amazonaws.com  | HTTPS    |

## Service quotas

| Name                                             | Default                                                   | Adjustable                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------ | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authorizations per DB security group             | Each supported Region: 20                                 | No                                                                                                                                                                         | Number of security group authorizations per DB security group                                                                                                                                                                                                                                      |
| Custom endpoints per DB cluster                  | Each supported Region: 5                                  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-9372BAB3 "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-9372BAB3") | The maximum number of custom endpoints that you can create per Aurora DB cluster in this account in the current Region. This value reflects the highest number of custom endpoints in a DB cluster in the account. Other DB clusters in the account might have a lower number of custom endpoints. |
| Custom engine versions                           | Each supported Region: 40                                 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-A399AC0B "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-A399AC0B") | The maximum number of custom engine versions allowed in this account in the current Region                                                                                                                                                                                                         |
| DB cluster parameter groups                      | Each supported Region: 50                                 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-E4C808A8 "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-E4C808A8") | The maximum number of DB cluster parameter groups                                                                                                                                                                                                                                                  |
| DB clusters                                      | Each supported Region: 40                                 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-952B80B8 "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-952B80B8") | The maximum number of Aurora clusters allowed in this account in the current Region                                                                                                                                                                                                                |
| DB instances                                     | ap-south-1: 20<br>Each of the other supported Regions: 40 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-7B6409FD "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-7B6409FD") | The maximum number of DB instances allowed in this account in the current Region                                                                                                                                                                                                                   |
| DB shard groups                                  | Each supported Region: 5                                  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-75AC651F "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-75AC651F") | The maximum number of DB shard groups for Aurora Limitless Database in this account in the current Region                                                                                                                                                                                          |
| DB subnet groups                                 | ap-south-1: 20<br>Each of the other supported Regions: 50 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-48C6BF61 "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-48C6BF61") | The maximum number of DB subnet groups                                                                                                                                                                                                                                                             |
| Data API HTTP request body size                  | Each supported Region: 4 Megabytes                        | No                                                                                                                                                                         | The maximum size allowed for the HTTP request body.                                                                                                                                                                                                                                                |
| Data API maximum concurrent cluster-secret pairs | Each supported Region: 30                                 | No                                                                                                                                                                         | The maximum number of unique pairs of Aurora Serverless v1 DB clusters and secrets in concurrent Data API requests for this account in the current AWS Region.                                                                                                                                     |
| Data API maximum concurrent requests             | Each supported Region: 500                                | No                                                                                                                                                                         | The maximum number of Data API requests to an Aurora Serverless v1 DB cluster that use the same secret and can be processed at the same time. Additional requests are queued and processed as in-process requests complete.                                                                        |
| Data API maximum result set size                 | Each supported Region: 1 Megabytes                        | No                                                                                                                                                                         | The maximum size of the database result set that can be returned by the Data API.                                                                                                                                                                                                                  |
| Data API maximum size of JSON response string    | Each supported Region: 10 Megabytes                       | No                                                                                                                                                                         | The maximum size of the simplified JSON response string returned by the RDS Data API.                                                                                                                                                                                                              |
| Data API requests per second                     | Each supported Region: 1,000 per second                   | No                                                                                                                                                                         | The maximum number of requests to the Data API per second allowed for this account in the current AWS Region. This quota only applies to Amazon Aurora Serverless v1 clusters.                                                                                                                     |
| Event subscriptions                              | Each supported Region: 20                                 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-A59F4C87 "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-A59F4C87") | The maximum number of event subscriptions                                                                                                                                                                                                                                                          |
| IAM roles per DB cluster                         | Each supported Region: 5                                  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-E094F43D "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-E094F43D") | The maximum number of IAM roles associated with a DB cluster                                                                                                                                                                                                                                       |
| IAM roles per DB instance                        | Each supported Region: 5                                  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-DD2301CA "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-DD2301CA") | The maximum number of IAM roles associated with a DB instance                                                                                                                                                                                                                                      |
| Integrations                                     | Each supported Region: 100                                | No                                                                                                                                                                         | The maximum number of integrations allowed in this account in the current AWS Region                                                                                                                                                                                                               |
| Manual DB cluster snapshots                      | Each supported Region: 100                                | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-9B510759 "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-9B510759") | The maximum number of manual DB cluster snapshots                                                                                                                                                                                                                                                  |
| Manual DB instance snapshots                     | Each supported Region: 100                                | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-272F1212 "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-272F1212") | The maximum number of manual DB instance snapshots                                                                                                                                                                                                                                                 |
| Option groups                                    | Each supported Region: 20                                 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-9FA33840 "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-9FA33840") | The maximum number of option groups                                                                                                                                                                                                                                                                |
| Parameter groups                                 | ap-south-1: 20<br>Each of the other supported Regions: 50 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-DE55804A "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-DE55804A") | The maximum number of parameter groups                                                                                                                                                                                                                                                             |
| Proxies                                          | Each supported Region: 20                                 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-D94C7EA3 "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-D94C7EA3") | The maximum number of proxies allowed in this account in the current AWS Region                                                                                                                                                                                                                    |
| Read replicas per primary                        | Each supported Region: 15                                 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-5BC124EF "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-5BC124EF") | The maximum number of read replicas per primary DB instance. This quota cant be adjusted for Amazon Aurora.                                                                                                                                                                                        |
| Reserved DB instances                            | ap-south-1: 20<br>Each of the other supported Regions: 40 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-78E853F4 "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-78E853F4") | The maximum number of reserved DB instances allowed in this account in the current AWS Region                                                                                                                                                                                                      |
| Security groups                                  | ap-south-1: 20<br>Each of the other supported Regions: 25 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-732153D0 "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-732153D0") | The maximum number of DB security groups                                                                                                                                                                                                                                                           |
| Subnets per DB subnet group                      | Each supported Region: 20                                 | No                                                                                                                                                                         | The maximum number of subnets per DB subnet group                                                                                                                                                                                                                                                  |
| Total storage for all DB instances               | Each supported Region: 100,000                            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-7ADDB58A "https://console.aws.amazon.com/servicequotas/home/services/rds/quotas/L-7ADDB58A") | The maximum total storage (in GB) on EBS volumes for all Amazon RDS DB instances added together. This quota does not apply to Amazon Aurora, which has a maximum cluster volume of 128 TiB for each DB cluster.                                                                                    |
