# AWS CloudShell endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name               | Region         | Endpoint                                | Protocol |
| ------------------------- | -------------- | --------------------------------------- | -------- |
| US East (Ohio)            | us-east-2      | cloudshell.us-east-2.amazonaws.com      | HTTPS    |
| US East (N. Virginia)     | us-east-1      | cloudshell.us-east-1.amazonaws.com      | HTTPS    |
| US West (N. California)   | us-west-1      | cloudshell.us-west-1.amazonaws.com      | HTTPS    |
| US West (Oregon)          | us-west-2      | cloudshell.us-west-2.amazonaws.com      | HTTPS    |
| Africa (Cape Town)        | af-south-1     | cloudshell.af-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Hong Kong)  | ap-east-1      | cloudshell.ap-east-1.amazonaws.com      | HTTPS    |
| Asia Pacific (Hyderabad)  | ap-south-2     | cloudshell.ap-south-2.amazonaws.com     | HTTPS    |
| Asia Pacific (Jakarta)    | ap-southeast-3 | cloudshell.ap-southeast-3.amazonaws.com | HTTPS    |
| Asia Pacific (Melbourne)  | ap-southeast-4 | cloudshell.ap-southeast-4.amazonaws.com | HTTPS    |
| Asia Pacific (Mumbai)     | ap-south-1     | cloudshell.ap-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Osaka)      | ap-northeast-3 | cloudshell.ap-northeast-3.amazonaws.com | HTTPS    |
| Asia Pacific (Seoul)      | ap-northeast-2 | cloudshell.ap-northeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Singapore)  | ap-southeast-1 | cloudshell.ap-southeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)     | ap-southeast-2 | cloudshell.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)      | ap-northeast-1 | cloudshell.ap-northeast-1.amazonaws.com | HTTPS    |
| Canada (Central)          | ca-central-1   | cloudshell.ca-central-1.amazonaws.com   | HTTPS    |
| Canada West (Calgary)     | ca-west-1      | cloudshell.ca-west-1.amazonaws.com      | HTTPS    |
| Europe (Frankfurt)        | eu-central-1   | cloudshell.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)          | eu-west-1      | cloudshell.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)           | eu-west-2      | cloudshell.eu-west-2.amazonaws.com      | HTTPS    |
| Europe (Milan)            | eu-south-1     | cloudshell.eu-south-1.amazonaws.com     | HTTPS    |
| Europe (Paris)            | eu-west-3      | cloudshell.eu-west-3.amazonaws.com      | HTTPS    |
| Europe (Spain)            | eu-south-2     | cloudshell.eu-south-2.amazonaws.com     | HTTPS    |
| Europe (Stockholm)        | eu-north-1     | cloudshell.eu-north-1.amazonaws.com     | HTTPS    |
| Israel (Tel Aviv)         | il-central-1   | cloudshell.il-central-1.amazonaws.com   | HTTPS    |
| Middle East (Bahrain)     | me-south-1     | cloudshell.me-south-1.amazonaws.com     | HTTPS    |
| Middle East (UAE)         | me-central-1   | cloudshell.me-central-1.amazonaws.com   | HTTPS    |
| South America (São Paulo) | sa-east-1      | cloudshell.sa-east-1.amazonaws.com      | HTTPS    |
| AWS GovCloud (US-East)    | us-gov-east-1  | cloudshell.us-gov-east-1.amazonaws.com  | HTTPS    |
| AWS GovCloud (US-West)    | us-gov-west-1  | cloudshell.us-gov-west-1.amazonaws.com  | HTTPS    |

## Service quotas

| Name                | Default                            | Adjustable                                                                                                                                                                               | Description                                                                                                      |
| ------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Concurrent shells   | Each supported Region: 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/cloudshell/quotas/L-C2A56602 "https://console.aws.amazon.com/servicequotas/home/services/cloudshell/quotas/L-C2A56602") | The maximum number of concurrent shells that you can run at the same time in this account in the current Region. |
| Data retention      | Each supported Region: 120         | No                                                                                                                                                                                       | The number of days that the data in the home directory will be retained after a shell was last accessed.         |
| Home directory size | Each supported Region: 1 Gigabytes | No                                                                                                                                                                                       | The maximum size of your shells home directory.                                                                  |
| Monthly usage       | Each supported Region: 200         | [Yes](https://console.aws.amazon.com/servicequotas/home/services/cloudshell/quotas/L-937D704D "https://console.aws.amazon.com/servicequotas/home/services/cloudshell/quotas/L-937D704D") | The maximum number of hours that you can use AWS CloudShell per month in this account in the current Region.     |
