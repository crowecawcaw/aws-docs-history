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

| Region Name              | Region         | Endpoint                                                                                                                                                  | Protocol                |
| ------------------------ | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| US East (Ohio)           | us-east-2      | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| US East (N. Virginia)    | us-east-1      | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| US West (N. California)  | us-west-1      | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| US West (Oregon)         | us-west-2      | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Africa (Cape Town)       | af-south-1     | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Asia Pacific (Hyderabad) | ap-south-2     | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Asia Pacific (Jakarta)   | ap-southeast-3 | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Asia Pacific (Malaysia)  | ap-southeast-5 | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Asia Pacific (Melbourne) | ap-southeast-4 | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Asia Pacific (Mumbai)    | ap-south-1     | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Asia Pacific (Osaka)     | ap-northeast-3 | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Asia Pacific (Seoul)     | ap-northeast-2 | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Asia Pacific (Singapore) | ap-southeast-1 | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Asia Pacific (Sydney)    | ap-southeast-2 | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Asia Pacific (Tokyo)     | ap-northeast-1 | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Canada (Central)         | ca-central-1   | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Canada West (Calgary)    | ca-west-1      | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Europe (Frankfurt)       | eu-central-1   | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Europe (Ireland)         | eu-west-1      | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Europe (London)          | eu-west-2      | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Europe (Milan)           | eu-south-1     | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Europe (Paris)           | eu-west-3      | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Europe (Spain)           | eu-south-2     | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Europe (Stockholm)       | eu-north-1     | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Europe (Zurich)          | eu-central-2   | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Israel (Tel Aviv)        | il-central-1   | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Middle East (Bahrain)    | me-south-1     | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| Middle East (UAE)        | me-central-1   | networkmanager.us-west-2.amazonaws.com networkmanager-fips.us-west-2.api.aws networkmanager-fips.us-west-2.amazonaws.com networkmanager.us-west-2.api.aws | HTTPS HTTPS HTTPS HTTPS |
| AWS GovCloud (US-East)   | us-gov-east-1  | networkmanager.us-gov-west-1.amazonaws.com networkmanager.us-gov-west-1.api.aws                                                                           | HTTPS HTTPS             |
| AWS GovCloud (US-West)   | us-gov-west-1  | networkmanager.us-gov-west-1.amazonaws.com networkmanager.us-gov-west-1.api.aws                                                                           | HTTPS HTTPS             | ## Service quotas For a list of quotas, see [Quotas](../../../network-manager/latest/cloudwan/cloudwan-quotas.md "../../../network-manager/latest/cloudwan/cloudwan-quotas.md") in the _AWS Cloud WAN User Guide_. |
