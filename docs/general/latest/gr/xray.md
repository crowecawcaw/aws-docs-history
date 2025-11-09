# AWS X-Ray endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                | Region         | Endpoint                                                                  | Protocol       |
| -------------------------- | -------------- | ------------------------------------------------------------------------- | -------------- |
| US East (Ohio)             | us-east-2      | xray.us-east-2.amazonaws.com<br>xray-fips.us-east-2.amazonaws.com         | HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | xray.us-east-1.amazonaws.com<br>xray-fips.us-east-1.amazonaws.com         | HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | xray.us-west-1.amazonaws.com<br>xray-fips.us-west-1.amazonaws.com         | HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | xray.us-west-2.amazonaws.com<br>xray-fips.us-west-2.amazonaws.com         | HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | xray.af-south-1.amazonaws.com                                             | HTTPS          |
| Asia Pacific (Hong Kong)   | ap-east-1      | xray.ap-east-1.amazonaws.com                                              | HTTPS          |
| Asia Pacific (Hyderabad)   | ap-south-2     | xray.ap-south-2.amazonaws.com                                             | HTTPS          |
| Asia Pacific (Jakarta)     | ap-southeast-3 | xray.ap-southeast-3.amazonaws.com                                         | HTTPS          |
| Asia Pacific (Malaysia)    | ap-southeast-5 | xray.ap-southeast-5.amazonaws.com                                         | HTTPS          |
| Asia Pacific (Melbourne)   | ap-southeast-4 | xray.ap-southeast-4.amazonaws.com                                         | HTTPS          |
| Asia Pacific (Mumbai)      | ap-south-1     | xray.ap-south-1.amazonaws.com                                             | HTTPS          |
| Asia Pacific (New Zealand) | ap-southeast-6 | xray.ap-southeast-6.amazonaws.com                                         | HTTPS          |
| Asia Pacific (Osaka)       | ap-northeast-3 | xray.ap-northeast-3.amazonaws.com                                         | HTTPS          |
| Asia Pacific (Seoul)       | ap-northeast-2 | xray.ap-northeast-2.amazonaws.com                                         | HTTPS          |
| Asia Pacific (Singapore)   | ap-southeast-1 | xray.ap-southeast-1.amazonaws.com                                         | HTTPS          |
| Asia Pacific (Sydney)      | ap-southeast-2 | xray.ap-southeast-2.amazonaws.com                                         | HTTPS          |
| Asia Pacific (Taipei)      | ap-east-2      | xray.ap-east-2.amazonaws.com                                              | HTTPS          |
| Asia Pacific (Thailand)    | ap-southeast-7 | xray.ap-southeast-7.amazonaws.com                                         | HTTPS          |
| Asia Pacific (Tokyo)       | ap-northeast-1 | xray.ap-northeast-1.amazonaws.com                                         | HTTPS          |
| Canada (Central)           | ca-central-1   | xray.ca-central-1.amazonaws.com                                           | HTTPS          |
| Canada West (Calgary)      | ca-west-1      | xray.ca-west-1.amazonaws.com                                              | HTTPS          |
| Europe (Frankfurt)         | eu-central-1   | xray.eu-central-1.amazonaws.com                                           | HTTPS          |
| Europe (Ireland)           | eu-west-1      | xray.eu-west-1.amazonaws.com                                              | HTTPS          |
| Europe (London)            | eu-west-2      | xray.eu-west-2.amazonaws.com                                              | HTTPS          |
| Europe (Milan)             | eu-south-1     | xray.eu-south-1.amazonaws.com                                             | HTTPS          |
| Europe (Paris)             | eu-west-3      | xray.eu-west-3.amazonaws.com                                              | HTTPS          |
| Europe (Spain)             | eu-south-2     | xray.eu-south-2.amazonaws.com                                             | HTTPS          |
| Europe (Stockholm)         | eu-north-1     | xray.eu-north-1.amazonaws.com                                             | HTTPS          |
| Europe (Zurich)            | eu-central-2   | xray.eu-central-2.amazonaws.com                                           | HTTPS          |
| Israel (Tel Aviv)          | il-central-1   | xray.il-central-1.amazonaws.com                                           | HTTPS          |
| Mexico (Central)           | mx-central-1   | xray.mx-central-1.amazonaws.com                                           | HTTPS          |
| Middle East (Bahrain)      | me-south-1     | xray.me-south-1.amazonaws.com                                             | HTTPS          |
| Middle East (UAE)          | me-central-1   | xray.me-central-1.amazonaws.com                                           | HTTPS          |
| South America (São Paulo)  | sa-east-1      | xray.sa-east-1.amazonaws.com                                              | HTTPS          |
| AWS GovCloud (US-East)     | us-gov-east-1  | xray.us-gov-east-1.amazonaws.com<br>xray-fips.us-gov-east-1.amazonaws.com | HTTPS<br>HTTPS |
| AWS GovCloud (US-West)     | us-gov-west-1  | xray.us-gov-west-1.amazonaws.com<br>xray-fips.us-gov-west-1.amazonaws.com | HTTPS<br>HTTPS |

## Service quotas

| Name                                      | Default                              | Adjustable                                                                                                                                                                   | Description                                                                  |
| ----------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Custom sampling rules per region          | Each supported Region: 25            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/xray/quotas/L-8C0C998A "https://console.aws.amazon.com/servicequotas/home/services/xray/quotas/L-8C0C998A") | The maximum number of custom sampling rules per region.                      |
| Groups in an account                      | Each supported Region: 25            | No                                                                                                                                                                           | The maximum number of groups per account.                                    |
| Indexed annotations per trace             | Each supported Region: 50            | No                                                                                                                                                                           | The maximum number of annotations that can be indexed within a single trace. |
| Segment document size                     | Each supported Region: 64 Kilobytes  | No                                                                                                                                                                           | The maximum size for segment documents.                                      |
| Segments per second                       | Each supported Region: 2,600         | No                                                                                                                                                                           | The maximum number of segments per second you can send to X-Ray.             |
| Tags per custom sampling rule             | Each supported Region: 50            | No                                                                                                                                                                           | The maximum number of tags per custom sampling rule.                         |
| Tags per group                            | Each supported Region: 50            | No                                                                                                                                                                           | The maximum number of tags per group.                                        |
| Trace and service graph retention in days | Each supported Region: 30            | No                                                                                                                                                                           | The number of days to retain trace and service map data.                     |
| Trace data modification period in days    | Each supported Region: 7             | No                                                                                                                                                                           | The number of days to update recorded data at no additional cost.            |
| Trace document size (dynamic upper limit) | Each supported Region: 500 Kilobytes | No                                                                                                                                                                           | The maximum size of a trace document.                                        |
| Trace document size (lower limit)         | Each supported Region: 100 Kilobytes | No                                                                                                                                                                           | The maximum size of a trace document.                                        |
