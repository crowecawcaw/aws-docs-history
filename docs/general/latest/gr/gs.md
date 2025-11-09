# AWS Ground Station endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name               | Region         | Endpoint                                                                                                                                                       | Protocol                         |
| ------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| US East (Ohio)            | us-east-2      | groundstation.us-east-2.amazonaws.com<br>groundstation-fips.us-east-2.api.aws<br>groundstation-fips.us-east-2.amazonaws.com<br>groundstation.us-east-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)     | us-east-1      | groundstation.us-east-1.amazonaws.com<br>groundstation-fips.us-east-1.api.aws<br>groundstation-fips.us-east-1.amazonaws.com<br>groundstation.us-east-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)          | us-west-2      | groundstation.us-west-2.amazonaws.com<br>groundstation-fips.us-west-2.api.aws<br>groundstation-fips.us-west-2.amazonaws.com<br>groundstation.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)        | af-south-1     | groundstation.af-south-1.amazonaws.com<br>groundstation.af-south-1.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)      | ap-northeast-2 | groundstation.ap-northeast-2.amazonaws.com<br>groundstation.ap-northeast-2.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore)  | ap-southeast-1 | groundstation.ap-southeast-1.amazonaws.com<br>groundstation.ap-southeast-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)     | ap-southeast-2 | groundstation.ap-southeast-2.amazonaws.com<br>groundstation.ap-southeast-2.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Europe (Frankfurt)        | eu-central-1   | groundstation.eu-central-1.amazonaws.com<br>groundstation.eu-central-1.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Ireland)          | eu-west-1      | groundstation.eu-west-1.amazonaws.com<br>groundstation.eu-west-1.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Europe (Stockholm)        | eu-north-1     | groundstation.eu-north-1.amazonaws.com<br>groundstation.eu-north-1.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Middle East (Bahrain)     | me-south-1     | groundstation.me-south-1.amazonaws.com<br>groundstation.me-south-1.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| South America (São Paulo) | sa-east-1      | groundstation.sa-east-1.amazonaws.com<br>groundstation.sa-east-1.api.aws                                                                                       | HTTPS<br>HTTPS                   |

## Service quotas

| Name                               | Default                      | Adjustable                                                                                                                                                                                     | Description                                                                       |
| ---------------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Config limit                       | Each supported Region: 100   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-5CCF0BC2 "https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-5CCF0BC2") | The maximum number of configs allowed.                                            |
| Contact Lead Time Maximum          | Each supported Region: 7     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-09DEC198 "https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-09DEC198") | Maximum lead time allowed for scheduling a contact in days                        |
| Dataflow endpoint group limit      | Each supported Region: 100   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-D6A1915B "https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-D6A1915B") | The maximum number of dataflow endpoint groups allowed.                           |
| Dataflow endpoints per group limit | Each supported Region: 20    | [Yes](https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-98A63A85 "https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-98A63A85") | The maximum number of dataflow endpoints per group allowed.                       |
| Enabled Ephemerides limit          | Each supported Region: 30    | [Yes](https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-BD84767C "https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-BD84767C") | Maximum number of enabled customer-provided ephemerides per satellite.            |
| Ephemeris Validation limit         | Each supported Region: 10    | [Yes](https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-DE376FC5 "https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-DE376FC5") | Maximum number of customer-provided ephemerides that be validated simultaneously. |
| Maximum Contact Duration           | Each supported Region: 20    | [Yes](https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-CCFDE387 "https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-CCFDE387") | The maximum contact duration permitted in minutes                                 |
| Mission profile limit              | Each supported Region: 100   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-5342B9BF "https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-5342B9BF") | The maximum number of mission profiles allowed.                                   |
| Scheduled Contacts Limit           | Each supported Region: 100   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-DF7B6DEC "https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-DF7B6DEC") | Maximum number of scheduled contacts allowed                                      |
| Scheduled Minutes Limit            | Each supported Region: 1,000 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-FED20749 "https://console.aws.amazon.com/servicequotas/home/services/groundstation/quotas/L-FED20749") | The maximum number of scheduled minutes allowed                                   |
