# AWS Application Migration Service endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name               | Region         | Endpoint                                                                | Protocol       |
| ------------------------- | -------------- | ----------------------------------------------------------------------- | -------------- |
| US East (Ohio)            | us-east-2      | mgn.us-east-2.amazonaws.com<br>mgn-fips.us-east-2.amazonaws.com         | HTTPS<br>HTTPS |
| US East (N. Virginia)     | us-east-1      | mgn.us-east-1.amazonaws.com<br>mgn-fips.us-east-1.amazonaws.com         | HTTPS<br>HTTPS |
| US West (N. California)   | us-west-1      | mgn.us-west-1.amazonaws.com<br>mgn-fips.us-west-1.amazonaws.com         | HTTPS<br>HTTPS |
| US West (Oregon)          | us-west-2      | mgn.us-west-2.amazonaws.com<br>mgn-fips.us-west-2.amazonaws.com         | HTTPS<br>HTTPS |
| Africa (Cape Town)        | af-south-1     | mgn.af-south-1.amazonaws.com                                            | HTTPS          |
| Asia Pacific (Hong Kong)  | ap-east-1      | mgn.ap-east-1.amazonaws.com                                             | HTTPS          |
| Asia Pacific (Hyderabad)  | ap-south-2     | mgn.ap-south-2.amazonaws.com                                            | HTTPS          |
| Asia Pacific (Jakarta)    | ap-southeast-3 | mgn.ap-southeast-3.amazonaws.com                                        | HTTPS          |
| Asia Pacific (Malaysia)   | ap-southeast-5 | mgn.ap-southeast-5.amazonaws.com                                        | HTTPS          |
| Asia Pacific (Melbourne)  | ap-southeast-4 | mgn.ap-southeast-4.amazonaws.com                                        | HTTPS          |
| Asia Pacific (Mumbai)     | ap-south-1     | mgn.ap-south-1.amazonaws.com                                            | HTTPS          |
| Asia Pacific (Osaka)      | ap-northeast-3 | mgn.ap-northeast-3.amazonaws.com                                        | HTTPS          |
| Asia Pacific (Seoul)      | ap-northeast-2 | mgn.ap-northeast-2.amazonaws.com                                        | HTTPS          |
| Asia Pacific (Singapore)  | ap-southeast-1 | mgn.ap-southeast-1.amazonaws.com                                        | HTTPS          |
| Asia Pacific (Sydney)     | ap-southeast-2 | mgn.ap-southeast-2.amazonaws.com                                        | HTTPS          |
| Asia Pacific (Thailand)   | ap-southeast-7 | mgn.ap-southeast-7.amazonaws.com                                        | HTTPS          |
| Asia Pacific (Tokyo)      | ap-northeast-1 | mgn.ap-northeast-1.amazonaws.com                                        | HTTPS          |
| Canada (Central)          | ca-central-1   | mgn.ca-central-1.amazonaws.com                                          | HTTPS          |
| Europe (Frankfurt)        | eu-central-1   | mgn.eu-central-1.amazonaws.com                                          | HTTPS          |
| Europe (Ireland)          | eu-west-1      | mgn.eu-west-1.amazonaws.com                                             | HTTPS          |
| Europe (London)           | eu-west-2      | mgn.eu-west-2.amazonaws.com                                             | HTTPS          |
| Europe (Milan)            | eu-south-1     | mgn.eu-south-1.amazonaws.com                                            | HTTPS          |
| Europe (Paris)            | eu-west-3      | mgn.eu-west-3.amazonaws.com                                             | HTTPS          |
| Europe (Spain)            | eu-south-2     | mgn.eu-south-2.amazonaws.com                                            | HTTPS          |
| Europe (Stockholm)        | eu-north-1     | mgn.eu-north-1.amazonaws.com                                            | HTTPS          |
| Europe (Zurich)           | eu-central-2   | mgn.eu-central-2.amazonaws.com                                          | HTTPS          |
| Israel (Tel Aviv)         | il-central-1   | mgn.il-central-1.amazonaws.com                                          | HTTPS          |
| Middle East (Bahrain)     | me-south-1     | mgn.me-south-1.amazonaws.com                                            | HTTPS          |
| Middle East (UAE)         | me-central-1   | mgn.me-central-1.amazonaws.com                                          | HTTPS          |
| South America (São Paulo) | sa-east-1      | mgn.sa-east-1.amazonaws.com                                             | HTTPS          |
| AWS GovCloud (US-East)    | us-gov-east-1  | mgn.us-gov-east-1.amazonaws.com<br>mgn-fips.us-gov-east-1.amazonaws.com | HTTPS<br>HTTPS |
| AWS GovCloud (US-West)    | us-gov-west-1  | mgn.us-gov-west-1.amazonaws.com<br>mgn-fips.us-gov-west-1.amazonaws.com | HTTPS<br>HTTPS |

## Service quotas

| Name                                                           | Default                       | Adjustable                                                                                                                                                                 | Description                                                    |
| -------------------------------------------------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Concurrent jobs in progress                                    | Each supported Region: 20     | No                                                                                                                                                                         | Concurrent jobs in progress                                    |
| Max Active Source Servers                                      | Each supported Region: 150    | [Yes](https://console.aws.amazon.com/servicequotas/home/services/mgn/quotas/L-9A599620 "https://console.aws.amazon.com/servicequotas/home/services/mgn/quotas/L-9A599620") | Max Active Source Servers                                      |
| Max NSX gateway policy rules per network migration definition  | Each supported Region: 2,500  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/mgn/quotas/L-13A5D930 "https://console.aws.amazon.com/servicequotas/home/services/mgn/quotas/L-13A5D930") | Max NSX gateway policy rules per network migration definition  |
| Max NSX security policy rules per network migration definition | Each supported Region: 2,500  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/mgn/quotas/L-866BF8B4 "https://console.aws.amazon.com/servicequotas/home/services/mgn/quotas/L-866BF8B4") | Max NSX security policy rules per network migration definition |
| Max Non-Archived Source Servers                                | Each supported Region: 4,000  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/mgn/quotas/L-50980698 "https://console.aws.amazon.com/servicequotas/home/services/mgn/quotas/L-50980698") | Max Non-Archived Source Servers                                |
| Max Source Servers in a single Job                             | Each supported Region: 200    | No                                                                                                                                                                         | Max Source Servers in a single Job                             |
| Max Source Servers in all Jobs                                 | Each supported Region: 200    | No                                                                                                                                                                         | Max Source Servers in all Jobs                                 |
| Max Total Source Servers Per AWS Account                       | Each supported Region: 50,000 | No                                                                                                                                                                         | Max Total Source Servers Per AWS Account                       |
| Max actions per source server                                  | Each supported Region: 100    | No                                                                                                                                                                         | Max actions per source server                                  |
| Max actions per template                                       | Each supported Region: 100    | No                                                                                                                                                                         | Max actions per template                                       |
| Max active applications                                        | Each supported Region: 200    | No                                                                                                                                                                         | Max active applications                                        |
| Max active waves                                               | Each supported Region: 200    | No                                                                                                                                                                         | Max active waves                                               |
| Max applications per wave                                      | Each supported Region: 1,000  | No                                                                                                                                                                         | Max applications per wave                                      |
| Max archived applications                                      | Each supported Region: 10,000 | No                                                                                                                                                                         | Max archived applications                                      |
| Max archived waves                                             | Each supported Region: 10,000 | No                                                                                                                                                                         | Max archived waves                                             |
| Max concurrent Jobs per Source Server                          | Each supported Region: 1      | No                                                                                                                                                                         | Max concurrent Jobs per Source Server                          |
| Max network migration definitions per account per Region       | Each supported Region: 5      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/mgn/quotas/L-D617A7E7 "https://console.aws.amazon.com/servicequotas/home/services/mgn/quotas/L-D617A7E7") | Max network migration definitions per account per Region       |
| Max source servers per application                             | Each supported Region: 200    | No                                                                                                                                                                         | Max source servers per application                             |

The following table lists additional information.

| Resource           | Retention          |
| ------------------ | ------------------ |
| Launch history     | Saved for 10 years |
| Individual Job log | Saved for 185 days |
