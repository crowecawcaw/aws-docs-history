# AWS Snow Family endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

Snow Family devices are available in the following AWS Regions.

| Region Name               | Region         | Endpoint                                                                                                                                                       | Protocol                         |
| ------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| US East (Ohio)            | us-east-2      | snowball.us-east-2.amazonaws.com<br>snowball.us-east-2.api.aws<br>snowball-fips.us-east-2.amazonaws.com<br>snowball-fips.us-east-2.api.aws                     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)     | us-east-1      | snowball.us-east-1.amazonaws.com<br>snowball-fips.us-east-1.amazonaws.com<br>snowball.us-east-1.api.aws<br>snowball-fips.us-east-1.api.aws                     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)   | us-west-1      | snowball.us-west-1.amazonaws.com<br>snowball.us-west-1.api.aws<br>snowball-fips.us-west-1.api.aws<br>snowball-fips.us-west-1.amazonaws.com                     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)          | us-west-2      | snowball.us-west-2.amazonaws.com<br>snowball-fips.us-west-2.amazonaws.com<br>snowball.us-west-2.api.aws<br>snowball-fips.us-west-2.api.aws                     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)        | af-south-1     | snowball.af-south-1.amazonaws.com<br>snowball.af-south-1.api.aws<br>snowball-fips.af-south-1.amazonaws.com<br>snowball-fips.af-south-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Hong Kong)  | ap-east-1      | snowball.ap-east-1.amazonaws.com<br>snowball.ap-east-1.api.aws<br>snowball-fips.ap-east-1.api.aws<br>snowball-fips.ap-east-1.amazonaws.com                     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Jakarta)    | ap-southeast-3 | snowball.ap-southeast-3.amazonaws.com<br>snowball.ap-southeast-3.api.aws<br>snowball-fips.ap-southeast-3.amazonaws.com<br>snowball-fips.ap-southeast-3.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Mumbai)     | ap-south-1     | snowball.ap-south-1.amazonaws.com<br>snowball.ap-south-1.api.aws<br>snowball-fips.ap-south-1.amazonaws.com<br>snowball-fips.ap-south-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Osaka)      | ap-northeast-3 | snowball.ap-northeast-3.amazonaws.com<br>snowball-fips.ap-northeast-3.api.aws<br>snowball-fips.ap-northeast-3.amazonaws.com<br>snowball.ap-northeast-3.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Seoul)      | ap-northeast-2 | snowball.ap-northeast-2.amazonaws.com<br>snowball-fips.ap-northeast-2.amazonaws.com<br>snowball.ap-northeast-2.api.aws<br>snowball-fips.ap-northeast-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Singapore)  | ap-southeast-1 | snowball.ap-southeast-1.amazonaws.com<br>snowball.ap-southeast-1.api.aws<br>snowball-fips.ap-southeast-1.api.aws<br>snowball-fips.ap-southeast-1.amazonaws.com | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Sydney)     | ap-southeast-2 | snowball.ap-southeast-2.amazonaws.com<br>snowball-fips.ap-southeast-2.api.aws<br>snowball-fips.ap-southeast-2.amazonaws.com<br>snowball.ap-southeast-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Tokyo)      | ap-northeast-1 | snowball.ap-northeast-1.amazonaws.com<br>snowball-fips.ap-northeast-1.amazonaws.com<br>snowball.ap-northeast-1.api.aws<br>snowball-fips.ap-northeast-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Canada (Central)          | ca-central-1   | snowball.ca-central-1.amazonaws.com<br>snowball.ca-central-1.api.aws<br>snowball-fips.ca-central-1.amazonaws.com<br>snowball-fips.ca-central-1.api.aws         | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)        | eu-central-1   | snowball.eu-central-1.amazonaws.com<br>snowball.eu-central-1.api.aws<br>snowball-fips.eu-central-1.api.aws<br>snowball-fips.eu-central-1.amazonaws.com         | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Ireland)          | eu-west-1      | snowball.eu-west-1.amazonaws.com<br>snowball-fips.eu-west-1.amazonaws.com<br>snowball.eu-west-1.api.aws<br>snowball-fips.eu-west-1.api.aws                     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (London)           | eu-west-2      | snowball.eu-west-2.amazonaws.com<br>snowball.eu-west-2.api.aws<br>snowball-fips.eu-west-2.amazonaws.com<br>snowball-fips.eu-west-2.api.aws                     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Milan)            | eu-south-1     | snowball.eu-south-1.amazonaws.com<br>snowball-fips.eu-south-1.api.aws<br>snowball-fips.eu-south-1.amazonaws.com<br>snowball.eu-south-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Paris)            | eu-west-3      | snowball.eu-west-3.amazonaws.com<br>snowball-fips.eu-west-3.api.aws<br>snowball-fips.eu-west-3.amazonaws.com<br>snowball.eu-west-3.api.aws                     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Stockholm)        | eu-north-1     | snowball.eu-north-1.amazonaws.com<br>snowball.eu-north-1.api.aws<br>snowball-fips.eu-north-1.amazonaws.com<br>snowball-fips.eu-north-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Israel (Tel Aviv)         | il-central-1   | snowball.il-central-1.amazonaws.com<br>snowball-fips.il-central-1.api.aws<br>snowball-fips.il-central-1.amazonaws.com<br>snowball.il-central-1.api.aws         | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Middle East (UAE)         | me-central-1   | snowball.me-central-1.amazonaws.com<br>snowball-fips.me-central-1.api.aws<br>snowball-fips.me-central-1.amazonaws.com<br>snowball.me-central-1.api.aws         | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| South America (São Paulo) | sa-east-1      | snowball.sa-east-1.amazonaws.com<br>snowball.sa-east-1.api.aws<br>snowball-fips.sa-east-1.amazonaws.com<br>snowball-fips.sa-east-1.api.aws                     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| AWS GovCloud (US-East)    | us-gov-east-1  | snowball.us-gov-east-1.amazonaws.com<br>snowball.us-gov-east-1.api.aws<br>snowball-fips.us-gov-east-1.amazonaws.com<br>snowball-fips.us-gov-east-1.api.aws     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| AWS GovCloud (US-West)    | us-gov-west-1  | snowball.us-gov-west-1.amazonaws.com<br>snowball-fips.us-gov-west-1.api.aws<br>snowball-fips.us-gov-west-1.amazonaws.com<br>snowball.us-gov-west-1.api.aws     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |

###### AWS Snowball Edge is available only in the following AWS Regions:

- US East (N. Virginia)
- US East (Ohio)
- US West (N. California)
- US West (Oregon)
- Canada (Central)
- South America (São Paulo)
- Europe (Ireland)
- Europe (Frankfurt)
- Europe (London)
- Europe (Paris)
- Asia Pacific (Mumbai)
- Asia Pacific (Sydney)
- Asia Pacific (Singapore)
- Asia Pacific (Tokyo)
- Israel (Tel Aviv)

## Service quotas

| Name                  | Default                  | Adjustable                                                                                                                                                                           | Description                                  |
| --------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| Snowball Edge devices | Each supported Region: 1 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/snowball/quotas/L-B6883B9F "https://console.aws.amazon.com/servicequotas/home/services/snowball/quotas/L-B6883B9F") | The maximum number of Snowball Edge devices. |
| Snowcone devices      | Each supported Region: 1 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/snowball/quotas/L-9F53AA61 "https://console.aws.amazon.com/servicequotas/home/services/snowball/quotas/L-9F53AA61") | The maximum number of Snowcone devices.      |
