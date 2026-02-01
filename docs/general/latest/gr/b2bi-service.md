# AWS B2B Data Interchange endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name              | Region         | Endpoint                                                                                                                               | Protocol                         |
| ------------------------ | -------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| US East (Ohio)           | us-east-2      | b2bi.us-east-2.amazonaws.com<br>b2bi-fips.us-east-2.api.aws<br>b2bi-fips.us-east-2.amazonaws.com<br>b2bi.us-east-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)    | us-east-1      | b2bi.us-east-1.amazonaws.com<br>b2bi-fips.us-east-1.api.aws<br>b2bi-fips.us-east-1.amazonaws.com<br>b2bi.us-east-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)         | us-west-2      | b2bi.us-west-2.amazonaws.com<br>b2bi-fips.us-west-2.api.aws<br>b2bi-fips.us-west-2.amazonaws.com<br>b2bi.us-west-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Hyderabad) | ap-south-2     | b2bi.ap-south-2.amazonaws.com<br>b2bi.ap-south-2.api.aws                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)    | ap-southeast-2 | b2bi.ap-southeast-2.amazonaws.com<br>b2bi.ap-southeast-2.api.aws                                                                       | HTTPS<br>HTTPS                   |
| Canada (Central)         | ca-central-1   | b2bi.ca-central-1.amazonaws.com<br>b2bi-fips.ca-central-1.api.aws<br>b2bi-fips.ca-central-1.amazonaws.com<br>b2bi.ca-central-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)       | eu-central-1   | b2bi.eu-central-1.amazonaws.com<br>b2bi.eu-central-1.api.aws                                                                           | HTTPS<br>HTTPS                   |
| Europe (Ireland)         | eu-west-1      | b2bi.eu-west-1.amazonaws.com<br>b2bi.eu-west-1.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Paris)           | eu-west-3      | b2bi.eu-west-3.amazonaws.com<br>b2bi.eu-west-3.api.aws                                                                                 | HTTPS<br>HTTPS                   |

## Service quotas

| Name         | Default                    | Adjustable                                                                                                                                                                   | Description                     |
| ------------ | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| Capabilities | Each supported Region: 100 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/b2bi/quotas/L-19B5E505 "https://console.aws.amazon.com/servicequotas/home/services/b2bi/quotas/L-19B5E505") | Maximum number of Capabilities. |
| Partnerships | Each supported Region: 700 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/b2bi/quotas/L-CD5D2786 "https://console.aws.amazon.com/servicequotas/home/services/b2bi/quotas/L-CD5D2786") | Maximum number of Partnerships. |
| Profiles     | Each supported Region: 5   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/b2bi/quotas/L-05F6A9EF "https://console.aws.amazon.com/servicequotas/home/services/b2bi/quotas/L-05F6A9EF") | Maximum number of Profiles.     |
| Transformers | Each supported Region: 500 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/b2bi/quotas/L-E15C983E "https://console.aws.amazon.com/servicequotas/home/services/b2bi/quotas/L-E15C983E") | Maximum number of Transformers. |
