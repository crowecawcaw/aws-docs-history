# Amazon GuardDuty endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name               | Region         | Endpoint                                                                                                            | Protocol                |
| ------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| US East (Ohio)            | us-east-2      | guardduty.us-east-2.amazonaws.com<br>guardduty-fips.us-east-2.amazonaws.com<br>guardduty.us-east-2.api.aws          | HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)     | us-east-1      | guardduty.us-east-1.amazonaws.com<br>guardduty-fips.us-east-1.amazonaws.com<br>guardduty.us-east-1.api.aws          | HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)   | us-west-1      | guardduty.us-west-1.amazonaws.com<br>guardduty-fips.us-west-1.amazonaws.com<br>guardduty.us-west-1.api.aws          | HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)          | us-west-2      | guardduty.us-west-2.amazonaws.com<br>guardduty-fips.us-west-2.amazonaws.com<br>guardduty.us-west-2.api.aws          | HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)        | af-south-1     | guardduty.af-south-1.amazonaws.com<br>guardduty.af-south-1.api.aws                                                  | HTTPS<br>HTTPS          |
| Asia Pacific (Hong Kong)  | ap-east-1      | guardduty.ap-east-1.amazonaws.com<br>guardduty.ap-east-1.api.aws                                                    | HTTPS<br>HTTPS          |
| Asia Pacific (Hyderabad)  | ap-south-2     | guardduty.ap-south-2.amazonaws.com<br>guardduty.ap-south-2.api.aws                                                  | HTTPS<br>HTTPS          |
| Asia Pacific (Jakarta)    | ap-southeast-3 | guardduty.ap-southeast-3.amazonaws.com<br>guardduty.ap-southeast-3.api.aws                                          | HTTPS<br>HTTPS          |
| Asia Pacific (Malaysia)   | ap-southeast-5 | guardduty.ap-southeast-5.amazonaws.com<br>guardduty.ap-southeast-5.api.aws                                          | HTTPS<br>HTTPS          |
| Asia Pacific (Melbourne)  | ap-southeast-4 | guardduty.ap-southeast-4.amazonaws.com<br>guardduty.ap-southeast-4.api.aws                                          | HTTPS<br>HTTPS          |
| Asia Pacific (Mumbai)     | ap-south-1     | guardduty.ap-south-1.amazonaws.com<br>guardduty.ap-south-1.api.aws                                                  | HTTPS<br>HTTPS          |
| Asia Pacific (Osaka)      | ap-northeast-3 | guardduty.ap-northeast-3.amazonaws.com<br>guardduty.ap-northeast-3.api.aws                                          | HTTPS<br>HTTPS          |
| Asia Pacific (Seoul)      | ap-northeast-2 | guardduty.ap-northeast-2.amazonaws.com<br>guardduty.ap-northeast-2.api.aws                                          | HTTPS<br>HTTPS          |
| Asia Pacific (Singapore)  | ap-southeast-1 | guardduty.ap-southeast-1.amazonaws.com<br>guardduty.ap-southeast-1.api.aws                                          | HTTPS<br>HTTPS          |
| Asia Pacific (Sydney)     | ap-southeast-2 | guardduty.ap-southeast-2.amazonaws.com<br>guardduty.ap-southeast-2.api.aws                                          | HTTPS<br>HTTPS          |
| Asia Pacific (Taipei)     | ap-east-2      | guardduty.ap-east-2.amazonaws.com<br>guardduty.ap-east-2.api.aws                                                    | HTTPS<br>HTTPS          |
| Asia Pacific (Thailand)   | ap-southeast-7 | guardduty.ap-southeast-7.amazonaws.com<br>guardduty.ap-southeast-7.api.aws                                          | HTTPS<br>HTTPS          |
| Asia Pacific (Tokyo)      | ap-northeast-1 | guardduty.ap-northeast-1.amazonaws.com<br>guardduty.ap-northeast-1.api.aws                                          | HTTPS<br>HTTPS          |
| Canada (Central)          | ca-central-1   | guardduty.ca-central-1.amazonaws.com<br>guardduty-fips.ca-central-1.amazonaws.com<br>guardduty.ca-central-1.api.aws | HTTPS<br>HTTPS<br>HTTPS |
| Canada West (Calgary)     | ca-west-1      | guardduty.ca-west-1.amazonaws.com<br>guardduty-fips.ca-west-1.amazonaws.com<br>guardduty.ca-west-1.api.aws          | HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)        | eu-central-1   | guardduty.eu-central-1.amazonaws.com<br>guardduty.eu-central-1.api.aws                                              | HTTPS<br>HTTPS          |
| Europe (Ireland)          | eu-west-1      | guardduty.eu-west-1.amazonaws.com<br>guardduty.eu-west-1.api.aws                                                    | HTTPS<br>HTTPS          |
| Europe (London)           | eu-west-2      | guardduty.eu-west-2.amazonaws.com<br>guardduty.eu-west-2.api.aws                                                    | HTTPS<br>HTTPS          |
| Europe (Milan)            | eu-south-1     | guardduty.eu-south-1.amazonaws.com<br>guardduty.eu-south-1.api.aws                                                  | HTTPS<br>HTTPS          |
| Europe (Paris)            | eu-west-3      | guardduty.eu-west-3.amazonaws.com<br>guardduty.eu-west-3.api.aws                                                    | HTTPS<br>HTTPS          |
| Europe (Spain)            | eu-south-2     | guardduty.eu-south-2.amazonaws.com<br>guardduty.eu-south-2.api.aws                                                  | HTTPS<br>HTTPS          |
| Europe (Stockholm)        | eu-north-1     | guardduty.eu-north-1.amazonaws.com<br>guardduty.eu-north-1.api.aws                                                  | HTTPS<br>HTTPS          |
| Europe (Zurich)           | eu-central-2   | guardduty.eu-central-2.amazonaws.com<br>guardduty.eu-central-2.api.aws                                              | HTTPS<br>HTTPS          |
| Israel (Tel Aviv)         | il-central-1   | guardduty.il-central-1.amazonaws.com<br>guardduty.il-central-1.api.aws                                              | HTTPS<br>HTTPS          |
| Mexico (Central)          | mx-central-1   | guardduty.mx-central-1.amazonaws.com<br>guardduty.mx-central-1.api.aws                                              | HTTPS<br>HTTPS          |
| Middle East (Bahrain)     | me-south-1     | guardduty.me-south-1.amazonaws.com<br>guardduty.me-south-1.api.aws                                                  | HTTPS<br>HTTPS          |
| Middle East (UAE)         | me-central-1   | guardduty.me-central-1.amazonaws.com<br>guardduty.me-central-1.api.aws                                              | HTTPS<br>HTTPS          |
| South America (São Paulo) | sa-east-1      | guardduty.sa-east-1.amazonaws.com<br>guardduty.sa-east-1.api.aws                                                    | HTTPS<br>HTTPS          |
| AWS GovCloud (US-East)    | us-gov-east-1  | guardduty.us-gov-east-1.amazonaws.com<br>guardduty.us-gov-east-1.api.aws                                            | HTTPS<br>HTTPS          |
| AWS GovCloud (US-West)    | us-gov-west-1  | guardduty.us-gov-west-1.amazonaws.com<br>guardduty.us-gov-west-1.api.aws                                            | HTTPS<br>HTTPS          |

## Service quotas

| Name                                      | Default                       | Adjustable | Description                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------------------- | ----------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detectors                                 | Each supported Region: 1      | No         | The maximum number of detector resources that you can create per AWS account per region.                                                                                                                                                                                                                                                                   |
| Filters                                   | Each supported Region: 100    | No         | The maximum number of saved filters per AWS account per region.                                                                                                                                                                                                                                                                                            |
| Finding retention period                  | Each supported Region: 90     | No         | The maximum number of days a finding is retained. After 90 days findings are deleted.                                                                                                                                                                                                                                                                      |
| Member accounts by invitation             | Each supported Region: 5,000  | No         | The maximum number of member accounts that can be associated with a GuardDuty administrator account by invitation.                                                                                                                                                                                                                                         |
| Member accounts through AWS Organizations | Each supported Region: 50,000 | No         | Your current AWS Organizations member account quota shows the default maximum number of member accounts that you can associate with an administrator through AWS Organizations, including members added by invitation. The number of GuardDuty member accounts added through AWS Organizations cant exceed the total member accounts in your organization. |
| Threat intel sets                         | Each supported Region: 6      | No         | The maximum number of Threat intel sets that you can add per AWS account per region.                                                                                                                                                                                                                                                                       |
| Trusted IP sets                           | Each supported Region: 1      | No         | The maximum number of Trusted IP sets that you can add per AWS account per region.                                                                                                                                                                                                                                                                         |
