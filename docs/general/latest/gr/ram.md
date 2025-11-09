# AWS Resource Access Manager endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                | Region         | Endpoint                                                                                                                           | Protocol                         |
| -------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| US East (Ohio)             | us-east-2      | ram.us-east-2.amazonaws.com<br>ram-fips.us-east-2.api.aws<br>ram.us-east-2.api.aws<br>ram-fips.us-east-2.amazonaws.com             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | ram.us-east-1.amazonaws.com<br>ram-fips.us-east-1.api.aws<br>ram-fips.us-east-1.amazonaws.com<br>ram.us-east-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | ram.us-west-1.amazonaws.com<br>ram.us-west-1.api.aws<br>ram-fips.us-west-1.api.aws<br>ram-fips.us-west-1.amazonaws.com             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | ram.us-west-2.amazonaws.com<br>ram-fips.us-west-2.api.aws<br>ram.us-west-2.api.aws<br>ram-fips.us-west-2.amazonaws.com             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | ram.af-south-1.amazonaws.com<br>ram.af-south-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Hong Kong)   | ap-east-1      | ram.ap-east-1.amazonaws.com<br>ram.ap-east-1.api.aws                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Hyderabad)   | ap-south-2     | ram.ap-south-2.amazonaws.com<br>ram.ap-south-2.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Jakarta)     | ap-southeast-3 | ram.ap-southeast-3.amazonaws.com<br>ram.ap-southeast-3.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Malaysia)    | ap-southeast-5 | ram.ap-southeast-5.amazonaws.com<br>ram.ap-southeast-5.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Melbourne)   | ap-southeast-4 | ram.ap-southeast-4.amazonaws.com<br>ram.ap-southeast-4.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Mumbai)      | ap-south-1     | ram.ap-south-1.amazonaws.com<br>ram.ap-south-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (New Zealand) | ap-southeast-6 | ram.ap-southeast-6.amazonaws.com<br>ram.ap-southeast-6.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Osaka)       | ap-northeast-3 | ram.ap-northeast-3.amazonaws.com<br>ram.ap-northeast-3.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)       | ap-northeast-2 | ram.ap-northeast-2.amazonaws.com<br>ram.ap-northeast-2.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore)   | ap-southeast-1 | ram.ap-southeast-1.amazonaws.com<br>ram.ap-southeast-1.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)      | ap-southeast-2 | ram.ap-southeast-2.amazonaws.com<br>ram.ap-southeast-2.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Taipei)      | ap-east-2      | ram.ap-east-2.amazonaws.com<br>ram.ap-east-2.api.aws                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Thailand)    | ap-southeast-7 | ram.ap-southeast-7.amazonaws.com<br>ram.ap-southeast-7.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Tokyo)       | ap-northeast-1 | ram.ap-northeast-1.amazonaws.com<br>ram.ap-northeast-1.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Canada (Central)           | ca-central-1   | ram.ca-central-1.amazonaws.com<br>ram.ca-central-1.api.aws<br>ram-fips.ca-central-1.api.aws<br>ram-fips.ca-central-1.amazonaws.com | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | ram.ca-west-1.amazonaws.com<br>ram.ca-west-1.api.aws<br>ram-fips.ca-west-1.api.aws<br>ram-fips.ca-west-1.amazonaws.com             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)         | eu-central-1   | ram.eu-central-1.amazonaws.com<br>ram.eu-central-1.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Europe (Ireland)           | eu-west-1      | ram.eu-west-1.amazonaws.com<br>ram.eu-west-1.api.aws                                                                               | HTTPS<br>HTTPS                   |
| Europe (London)            | eu-west-2      | ram.eu-west-2.amazonaws.com<br>ram.eu-west-2.api.aws                                                                               | HTTPS<br>HTTPS                   |
| Europe (Milan)             | eu-south-1     | ram.eu-south-1.amazonaws.com<br>ram.eu-south-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Europe (Paris)             | eu-west-3      | ram.eu-west-3.amazonaws.com<br>ram.eu-west-3.api.aws                                                                               | HTTPS<br>HTTPS                   |
| Europe (Spain)             | eu-south-2     | ram.eu-south-2.amazonaws.com<br>ram.eu-south-2.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Europe (Stockholm)         | eu-north-1     | ram.eu-north-1.amazonaws.com<br>ram.eu-north-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Europe (Zurich)            | eu-central-2   | ram.eu-central-2.amazonaws.com<br>ram.eu-central-2.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Israel (Tel Aviv)          | il-central-1   | ram.il-central-1.amazonaws.com<br>ram.il-central-1.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Mexico (Central)           | mx-central-1   | ram.mx-central-1.amazonaws.com<br>ram.mx-central-1.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Middle East (Bahrain)      | me-south-1     | ram.me-south-1.amazonaws.com<br>ram.me-south-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Middle East (UAE)          | me-central-1   | ram.me-central-1.amazonaws.com<br>ram.me-central-1.api.aws                                                                         | HTTPS<br>HTTPS                   |
| South America (São Paulo)  | sa-east-1      | ram.sa-east-1.amazonaws.com<br>ram.sa-east-1.api.aws                                                                               | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-East)     | us-gov-east-1  | ram.us-gov-east-1.amazonaws.com<br>ram.us-gov-east-1.api.aws                                                                       | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-West)     | us-gov-west-1  | ram.us-gov-west-1.amazonaws.com<br>ram.us-gov-west-1.api.aws                                                                       | HTTPS<br>HTTPS                   |

## Service quotas

| Name                                                | Default                       | Adjustable                                                                                                                                                                 | Description                                                                     |
| --------------------------------------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Number of custom permissions                        | Each supported Region: 1,500  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ram/quotas/L-9EBA15DD "https://console.aws.amazon.com/servicequotas/home/services/ram/quotas/L-9EBA15DD") | The maximum number of custom permissions.                                       |
| Number of custom permissions per resource type      | Each supported Region: 10     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ram/quotas/L-2870BE9D "https://console.aws.amazon.com/servicequotas/home/services/ram/quotas/L-2870BE9D") | The maximum number of custom permissions that you can create per resource type. |
| Number of pending invitations                       | Each supported Region: 250    | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ram/quotas/L-238C96EE "https://console.aws.amazon.com/servicequotas/home/services/ram/quotas/L-238C96EE") | The maximum number of pending invitations.                                      |
| Number of principal associations                    | Each supported Region: 25,000 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ram/quotas/L-8491BF81 "https://console.aws.amazon.com/servicequotas/home/services/ram/quotas/L-8491BF81") | The maximum number of principal associations.                                   |
| Number of principal associations per resource share | Each supported Region: 5,000  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ram/quotas/L-275DAC00 "https://console.aws.amazon.com/servicequotas/home/services/ram/quotas/L-275DAC00") | The maximum number of principals that you can specify in a resource share.      |
| Number of resource associations                     | Each supported Region: 25,000 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ram/quotas/L-4A6CEE66 "https://console.aws.amazon.com/servicequotas/home/services/ram/quotas/L-4A6CEE66") | The maximum number of resources associations.                                   |
| Number of resource associations per resource share  | Each supported Region: 5,000  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ram/quotas/L-1F7F8A25 "https://console.aws.amazon.com/servicequotas/home/services/ram/quotas/L-1F7F8A25") | The maximum number of resources that you can include in a resource share.       |
| Number of resource shares                           | Each supported Region: 25,000 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ram/quotas/L-595828F9 "https://console.aws.amazon.com/servicequotas/home/services/ram/quotas/L-595828F9") | The maximum number of resource shares.                                          |

###### Notes

- The quota for **Number of pending invitations** applies
  to only _sending_ accounts who share with
  accounts that are **_not_** part of sender's AWS
  Organization.
- There is no quota for how many pending invitations a receiving account can
  have.
- Invitations are not used when sharing between accounts that are part of
  the same AWS Organization and [resource sharing within that AWS Organization is turned
  on](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs").
