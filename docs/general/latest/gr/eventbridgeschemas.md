# Amazon EventBridge Schemas endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name               | Region         | Endpoint                             | Protocol |
| ------------------------- | -------------- | ------------------------------------ | -------- |
| US East (Ohio)            | us-east-2      | schemas.us-east-2.amazonaws.com      | HTTPS    |
| US East (N. Virginia)     | us-east-1      | schemas.us-east-1.amazonaws.com      | HTTPS    |
| US West (N. California)   | us-west-1      | schemas.us-west-1.amazonaws.com      | HTTPS    |
| US West (Oregon)          | us-west-2      | schemas.us-west-2.amazonaws.com      | HTTPS    |
| Africa (Cape Town)        | af-south-1     | schemas.af-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Hong Kong)  | ap-east-1      | schemas.ap-east-1.amazonaws.com      | HTTPS    |
| Asia Pacific (Jakarta)    | ap-southeast-3 | schemas.ap-southeast-3.amazonaws.com | HTTPS    |
| Asia Pacific (Mumbai)     | ap-south-1     | schemas.ap-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Osaka)      | ap-northeast-3 | schemas.ap-northeast-3.amazonaws.com | HTTPS    |
| Asia Pacific (Seoul)      | ap-northeast-2 | schemas.ap-northeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Singapore)  | ap-southeast-1 | schemas.ap-southeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)     | ap-southeast-2 | schemas.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)      | ap-northeast-1 | schemas.ap-northeast-1.amazonaws.com | HTTPS    |
| Canada (Central)          | ca-central-1   | schemas.ca-central-1.amazonaws.com   | HTTPS    |
| Europe (Frankfurt)        | eu-central-1   | schemas.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)          | eu-west-1      | schemas.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)           | eu-west-2      | schemas.eu-west-2.amazonaws.com      | HTTPS    |
| Europe (Milan)            | eu-south-1     | schemas.eu-south-1.amazonaws.com     | HTTPS    |
| Europe (Paris)            | eu-west-3      | schemas.eu-west-3.amazonaws.com      | HTTPS    |
| Europe (Spain)            | eu-south-2     | schemas.eu-south-2.amazonaws.com     | HTTPS    |
| Europe (Stockholm)        | eu-north-1     | schemas.eu-north-1.amazonaws.com     | HTTPS    |
| Europe (Zurich)           | eu-central-2   | schemas.eu-central-2.amazonaws.com   | HTTPS    |
| Middle East (Bahrain)     | me-south-1     | schemas.me-south-1.amazonaws.com     | HTTPS    |
| Middle East (UAE)         | me-central-1   | schemas.me-central-1.amazonaws.com   | HTTPS    |
| South America (São Paulo) | sa-east-1      | schemas.sa-east-1.amazonaws.com      | HTTPS    |
| AWS GovCloud (US-East)    | us-gov-east-1  | schemas.us-gov-east-1.amazonaws.com  | HTTPS    |
| AWS GovCloud (US-West)    | us-gov-west-1  | schemas.us-gov-west-1.amazonaws.com  | HTTPS    |

## Service quotas

| Name              | Default                    | Adjustable                                                                                                                                                                         | Description                                                                                                               |
| ----------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| DiscoveredSchemas | Each supported Region: 200 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/schemas/quotas/L-1738102F "https://console.aws.amazon.com/servicequotas/home/services/schemas/quotas/L-1738102F") | The maximum number of schemas for a discovered schema registry that you can create in the current region                  |
| Discoverers       | Each supported Region: 10  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/schemas/quotas/L-037FC7C4 "https://console.aws.amazon.com/servicequotas/home/services/schemas/quotas/L-037FC7C4") | The maximum number of discoverers that you can create in the current region.                                              |
| Registries        | Each supported Region: 10  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/schemas/quotas/L-85663EFB "https://console.aws.amazon.com/servicequotas/home/services/schemas/quotas/L-85663EFB") | The maximum number of registries that you can create in the current region.                                               |
| SchemaVersions    | Each supported Region: 100 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/schemas/quotas/L-3C443A2A "https://console.aws.amazon.com/servicequotas/home/services/schemas/quotas/L-3C443A2A") | The maximum number of versions per schema that you can create in the current region.                                      |
| Schemas           | Each supported Region: 100 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/schemas/quotas/L-EE9E5FA9 "https://console.aws.amazon.com/servicequotas/home/services/schemas/quotas/L-EE9E5FA9") | The maximum number of schemas per registry that you can create in the current region. (Except Discovered Schema Registry) |
