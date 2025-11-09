# AWS Cloud WAN endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

AWS Cloud WAN is available in the following Regions. Cloud WAN aggregates and stores
information in its [home Region](../../../network-manager/latest/cloudwan/what-is-cloudwan.md#cloudwan-home-region "../../../network-manager/latest/cloudwan/what-is-cloudwan.md#cloudwan-home-region").
Cloud WAN supports the following home Region:
`us-west-2` — US West (Oregon).

| Region Name                | Region         | Endpoint                                                                                                                                                           | Protocol                         |
| -------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------- |
| US East (Ohio)             | us-east-2      | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Hyderabad)   | ap-south-2     | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Jakarta)     | ap-southeast-3 | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Malaysia)    | ap-southeast-5 | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Melbourne)   | ap-southeast-4 | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Mumbai)      | ap-south-1     | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (New Zealand) | ap-southeast-6 | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Osaka)       | ap-northeast-3 | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Seoul)       | ap-northeast-2 | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Singapore)   | ap-southeast-1 | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Sydney)      | ap-southeast-2 | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Taipei)      | ap-east-2      | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Thailand)    | ap-southeast-7 | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Tokyo)       | ap-northeast-1 | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Canada (Central)           | ca-central-1   | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)         | eu-central-1   | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Ireland)           | eu-west-1      | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (London)            | eu-west-2      | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Milan)             | eu-south-1     | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Paris)             | eu-west-3      | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Spain)             | eu-south-2     | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Stockholm)         | eu-north-1     | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Zurich)            | eu-central-2   | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Israel (Tel Aviv)          | il-central-1   | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Middle East (Bahrain)      | me-south-1     | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Middle East (UAE)          | me-central-1   | networkmanager.us-west-2.amazonaws.com<br>networkmanager-fips.us-west-2.api.aws<br>networkmanager-fips.us-west-2.amazonaws.com<br>networkmanager.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| AWS GovCloud (US-East)     | us-gov-east-1  | networkmanager.us-gov-west-1.amazonaws.com<br>networkmanager.us-gov-west-1.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-West)     | us-gov-west-1  | networkmanager.us-gov-west-1.amazonaws.com<br>networkmanager.us-gov-west-1.api.aws                                                                                 | HTTPS<br>HTTPS                   |

## Service quotas

For a list of quotas, see [Quotas](../../../network-manager/latest/cloudwan/cloudwan-quotas.md "../../../network-manager/latest/cloudwan/cloudwan-quotas.md") in the
_AWS Cloud WAN User Guide_.
