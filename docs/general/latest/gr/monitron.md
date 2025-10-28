# Amazon Monitron endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

###### Important

Amazon Monitron currently does not support programmatic access to service
endpoints.

Amazon Monitron is currently supported in the following Regions:

- US East (N. Virginia): us-east-1
- Europe (Ireland): eu-west-1
- Asia Pacific (Sydney): ap-south-east-2

## Service quotas

| Name                       | Default                    | Adjustable                                                                                                                                                                           | Description                                                        |
| -------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| Asset classes per project  | Each supported Region: 25  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/monitron/quotas/L-7771F483 "https://console.aws.amazon.com/servicequotas/home/services/monitron/quotas/L-7771F483") | The maximum number of asset classes per project.                   |
| Assets per site            | Each supported Region: 100 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/monitron/quotas/L-25B02F46 "https://console.aws.amazon.com/servicequotas/home/services/monitron/quotas/L-25B02F46") | The maximum number of assets per site.                             |
| Gateways per site          | Each supported Region: 200 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/monitron/quotas/L-6B3EE8A2 "https://console.aws.amazon.com/servicequotas/home/services/monitron/quotas/L-6B3EE8A2") | The maximum number of gateways per site.                           |
| Positions per asset        | Each supported Region: 20  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/monitron/quotas/L-E7428CE9 "https://console.aws.amazon.com/servicequotas/home/services/monitron/quotas/L-E7428CE9") | The maximum number of positions per asset.                         |
| Positions per custom class | Each supported Region: 500 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/monitron/quotas/L-D3D5A0EF "https://console.aws.amazon.com/servicequotas/home/services/monitron/quotas/L-D3D5A0EF") | The maximum number of positions per custom class.                  |
| Projects per account       | Each supported Region: 10  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/monitron/quotas/L-2C0BD955 "https://console.aws.amazon.com/servicequotas/home/services/monitron/quotas/L-2C0BD955") | The maximum number of projects that can be created for an account. |
| Sites per project          | Each supported Region: 50  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/monitron/quotas/L-7FA56BB1 "https://console.aws.amazon.com/servicequotas/home/services/monitron/quotas/L-7FA56BB1") | The maximum number of sites per project.                           |
| Users per site             | Each supported Region: 20  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/monitron/quotas/L-42582A4B "https://console.aws.amazon.com/servicequotas/home/services/monitron/quotas/L-42582A4B") | The maximum number of users per site.                              |
