# AWS CloudHSM endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name               | Region         | Endpoint                                                                                                            | Protocol                |
| ------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| US East (Ohio)            | us-east-2      | cloudhsmv2.us-east-2.amazonaws.com<br>cloudhsmv2.us-east-2.api.aws<br>cloudhsmv2-fips.us-east-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)     | us-east-1      | cloudhsmv2.us-east-1.amazonaws.com<br>cloudhsmv2.us-east-1.api.aws<br>cloudhsmv2-fips.us-east-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)   | us-west-1      | cloudhsmv2.us-west-1.amazonaws.com<br>cloudhsmv2.us-west-1.api.aws<br>cloudhsmv2-fips.us-west-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)          | us-west-2      | cloudhsmv2.us-west-2.amazonaws.com<br>cloudhsmv2.us-west-2.api.aws<br>cloudhsmv2-fips.us-west-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)        | af-south-1     | cloudhsmv2.af-south-1.amazonaws.com<br>cloudhsmv2.af-south-1.api.aws                                                | HTTPS<br>HTTPS          |
| Asia Pacific (Hong Kong)  | ap-east-1      | cloudhsmv2.ap-east-1.amazonaws.com<br>cloudhsmv2.ap-east-1.api.aws                                                  | HTTPS<br>HTTPS          |
| Asia Pacific (Hyderabad)  | ap-south-2     | cloudhsmv2.ap-south-2.amazonaws.com<br>cloudhsmv2.ap-south-2.api.aws                                                | HTTPS<br>HTTPS          |
| Asia Pacific (Jakarta)    | ap-southeast-3 | cloudhsmv2.ap-southeast-3.amazonaws.com<br>cloudhsmv2.ap-southeast-3.api.aws                                        | HTTPS<br>HTTPS          |
| Asia Pacific (Mumbai)     | ap-south-1     | cloudhsmv2.ap-south-1.amazonaws.com<br>cloudhsmv2.ap-south-1.api.aws                                                | HTTPS<br>HTTPS          |
| Asia Pacific (Osaka)      | ap-northeast-3 | cloudhsmv2.ap-northeast-3.amazonaws.com<br>cloudhsmv2.ap-northeast-3.api.aws                                        | HTTPS<br>HTTPS          |
| Asia Pacific (Seoul)      | ap-northeast-2 | cloudhsmv2.ap-northeast-2.amazonaws.com<br>cloudhsmv2.ap-northeast-2.api.aws                                        | HTTPS<br>HTTPS          |
| Asia Pacific (Singapore)  | ap-southeast-1 | cloudhsmv2.ap-southeast-1.amazonaws.com<br>cloudhsmv2.ap-southeast-1.api.aws                                        | HTTPS<br>HTTPS          |
| Asia Pacific (Sydney)     | ap-southeast-2 | cloudhsmv2.ap-southeast-2.amazonaws.com<br>cloudhsmv2.ap-southeast-2.api.aws                                        | HTTPS<br>HTTPS          |
| Asia Pacific (Tokyo)      | ap-northeast-1 | cloudhsmv2.ap-northeast-1.amazonaws.com<br>cloudhsmv2.ap-northeast-1.api.aws                                        | HTTPS<br>HTTPS          |
| Canada (Central)          | ca-central-1   | cloudhsmv2.ca-central-1.amazonaws.com<br>cloudhsmv2.ca-central-1.api.aws<br>cloudhsmv2-fips.ca-central-1.api.aws    | HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)        | eu-central-1   | cloudhsmv2.eu-central-1.amazonaws.com<br>cloudhsmv2.eu-central-1.api.aws                                            | HTTPS<br>HTTPS          |
| Europe (Ireland)          | eu-west-1      | cloudhsmv2.eu-west-1.amazonaws.com<br>cloudhsmv2.eu-west-1.api.aws                                                  | HTTPS<br>HTTPS          |
| Europe (London)           | eu-west-2      | cloudhsmv2.eu-west-2.amazonaws.com<br>cloudhsmv2.eu-west-2.api.aws                                                  | HTTPS<br>HTTPS          |
| Europe (Milan)            | eu-south-1     | cloudhsmv2.eu-south-1.amazonaws.com<br>cloudhsmv2.eu-south-1.api.aws                                                | HTTPS<br>HTTPS          |
| Europe (Paris)            | eu-west-3      | cloudhsmv2.eu-west-3.amazonaws.com<br>cloudhsmv2.eu-west-3.api.aws                                                  | HTTPS<br>HTTPS          |
| Europe (Spain)            | eu-south-2     | cloudhsmv2.eu-south-2.amazonaws.com<br>cloudhsmv2.eu-south-2.api.aws                                                | HTTPS<br>HTTPS          |
| Europe (Stockholm)        | eu-north-1     | cloudhsmv2.eu-north-1.amazonaws.com<br>cloudhsmv2.eu-north-1.api.aws                                                | HTTPS<br>HTTPS          |
| Europe (Zurich)           | eu-central-2   | cloudhsmv2.eu-central-2.amazonaws.com<br>cloudhsmv2.eu-central-2.api.aws                                            | HTTPS<br>HTTPS          |
| Israel (Tel Aviv)         | il-central-1   | cloudhsmv2.il-central-1.amazonaws.com<br>cloudhsmv2.il-central-1.api.aws                                            | HTTPS<br>HTTPS          |
| Middle East (Bahrain)     | me-south-1     | cloudhsmv2.me-south-1.amazonaws.com<br>cloudhsmv2.me-south-1.api.aws                                                | HTTPS<br>HTTPS          |
| Middle East (UAE)         | me-central-1   | cloudhsmv2.me-central-1.amazonaws.com<br>cloudhsmv2.me-central-1.api.aws                                            | HTTPS<br>HTTPS          |
| South America (São Paulo) | sa-east-1      | cloudhsmv2.sa-east-1.amazonaws.com<br>cloudhsmv2.sa-east-1.api.aws                                                  | HTTPS<br>HTTPS          |
| AWS GovCloud (US-East)    | us-gov-east-1  | cloudhsmv2.us-gov-east-1.amazonaws.com<br>cloudhsmv2.us-gov-east-1.api.aws<br>cloudhsmv2-fips.us-gov-east-1.api.aws | HTTPS<br>HTTPS<br>HTTPS |
| AWS GovCloud (US-West)    | us-gov-west-1  | cloudhsmv2.us-gov-west-1.amazonaws.com<br>cloudhsmv2-fips.us-gov-west-1.api.aws<br>cloudhsmv2.us-gov-west-1.api.aws | HTTPS<br>HTTPS<br>HTTPS |

## Service quotas

| Name                                    | Default                      | Adjustable                                                                                                                                                                           | Description                                                                               |
| --------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Clusters per AWS Region and AWS account | Each supported Region: 4     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/cloudhsm/quotas/L-4B16B391 "https://console.aws.amazon.com/servicequotas/home/services/cloudhsm/quotas/L-4B16B391") | The maximum number of clusters that you can create in this account in the current Region. |
| HSMs per AWS Region and AWS account     | Each supported Region: 6     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/cloudhsm/quotas/L-95BA35D1 "https://console.aws.amazon.com/servicequotas/home/services/cloudhsm/quotas/L-95BA35D1") | The maximum number of HSMs that you can create in this account in the current Region.     |
| HSMs per CloudHSM cluster               | Each supported Region: 28    | No                                                                                                                                                                                   | The maximum number of HSMs that you can create in a CloudHSM cluster.                     |
| Keys per CloudHSM cluster               | Each supported Region: 3,300 | No                                                                                                                                                                                   | The maximum number of keys that you can create in a CloudHSM cluster.                     |
| Length of a Username                    | Each supported Region: 31    | No                                                                                                                                                                                   | The maximum number of characters for a username.                                          |
| Length of a password                    | Each supported Region: 32    | No                                                                                                                                                                                   | The maximum number of characters for a password.                                          |
| Minimum length of a password            | Each supported Region: 7     | No                                                                                                                                                                                   | The minimum number of characters for a password.                                          |
| Number of concurrent clients            | Each supported Region: 900   | No                                                                                                                                                                                   | The maximum number of concurrent clients that can exist in a Region.                      |
| Users per CloudHSM cluster              | Each supported Region: 1,024 | No                                                                                                                                                                                   | The maximum number of users who can be created on a cluster in an account.                |

For more information, see [Quotas](../../../cloudhsm/latest/userguide/limits.md "../../../cloudhsm/latest/userguide/limits.md") in the
_AWS CloudHSM User Guide_.
