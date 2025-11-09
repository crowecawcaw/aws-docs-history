# Amazon Aurora DSQL endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name           | Region         | Endpoint                                              | Protocol       |
| --------------------- | -------------- | ----------------------------------------------------- | -------------- |
| US East (Ohio)        | us-east-2      | dsql.us-east-2.api.aws<br>dsql-fips.us-east-2.api.aws | HTTPS<br>HTTPS |
| US East (N. Virginia) | us-east-1      | dsql.us-east-1.api.aws<br>dsql-fips.us-east-1.api.aws | HTTPS<br>HTTPS |
| US West (Oregon)      | us-west-2      | dsql.us-west-2.api.aws<br>dsql-fips.us-west-2.api.aws | HTTPS<br>HTTPS |
| Asia Pacific (Osaka)  | ap-northeast-3 | dsql.ap-northeast-3.api.aws                           | HTTPS          |
| Asia Pacific (Seoul)  | ap-northeast-2 | dsql.ap-northeast-2.api.aws                           | HTTPS          |
| Asia Pacific (Tokyo)  | ap-northeast-1 | dsql.ap-northeast-1.api.aws                           | HTTPS          |
| Europe (Frankfurt)    | eu-central-1   | dsql.eu-central-1.api.aws                             | HTTPS          |
| Europe (Ireland)      | eu-west-1      | dsql.eu-west-1.api.aws                                | HTTPS          |
| Europe (London)       | eu-west-2      | dsql.eu-west-2.api.aws                                | HTTPS          |
| Europe (Paris)        | eu-west-3      | dsql.eu-west-3.api.aws                                | HTTPS          |

## Service quotas

| Name                    | Default                                 | Adjustable                                                                                                                                                                   | Description                                                                                                                  |
| ----------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Cluster size            | Each supported Region: 10,000 Gigabytes | [Yes](https://console.aws.amazon.com/servicequotas/home/services/dsql/quotas/L-9A50E9F1 "https://console.aws.amazon.com/servicequotas/home/services/dsql/quotas/L-9A50E9F1") | The maximum capacity (in GB) for an Aurora DSQL cluster. This quota applies to both single-Region and multi-Region clusters. |
| Connections per cluster | Each supported Region: 10,000           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/dsql/quotas/L-AA07A0EE "https://console.aws.amazon.com/servicequotas/home/services/dsql/quotas/L-AA07A0EE") | The maximum number of active connections per cluster that you can have in this account in the current Region.                |
| Multi-Region clusters   | Each supported Region: 5                | [Yes](https://console.aws.amazon.com/servicequotas/home/services/dsql/quotas/L-DCF93F11 "https://console.aws.amazon.com/servicequotas/home/services/dsql/quotas/L-DCF93F11") | The maximum number of multi region clusters allowed per account.                                                             |
| Single-Region clusters  | Each supported Region: 20               | [Yes](https://console.aws.amazon.com/servicequotas/home/services/dsql/quotas/L-B3A4E51E "https://console.aws.amazon.com/servicequotas/home/services/dsql/quotas/L-B3A4E51E") | The maximum number of active clusters allowed per account in a given region.                                                 |
