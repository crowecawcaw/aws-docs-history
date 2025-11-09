# AWS Security Token Service endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

###### Note

AWS recommends using Regional STS endpoints within your applications and avoid using
the global (legacy) STS endpoint. Regional STS endpoints reduce latency, build in
redundancy, and increase session token validity. For more information about configuring
your applications to use the regional STS endpoint, see [AWS STS Regionalized
endpoints](../../../sdkref/latest/guide/feature-sts-regionalized-endpoints.md "../../../sdkref/latest/guide/feature-sts-regionalized-endpoints.md") in the _AWS SDKs and Tools Reference Guide_. For
more information about the global (legacy) AWS STS endpoint, including how to monitor for use
of this endpoint, see [How to use Regional
AWS STS endpoints](../../../sdkref/latest/guide/feature-sts-regionalized-endpoints.md "../../../sdkref/latest/guide/feature-sts-regionalized-endpoints.md") in the _AWS Security blog_.

## Service endpoints

Although the global (legacy) AWS STS endpoint `https://sts.amazonaws.com` is
highly available, it’s hosted in a single AWS Region, US East (N. Virginia), and like
other endpoints, it doesn’t provide automatic failover to endpoints in other Regions. Most
Regional endpoints are active by default, but you must manually enable endpoints for some
Regions, such as Asia Pacific (Hong Kong). You can deactivate STS endpoints for any Regions
that are enabled by default if you do not intend to use those Regions.

| Region Name                | Region         | Endpoint                                                        | Protocol       |
| -------------------------- | -------------- | --------------------------------------------------------------- | -------------- |
| US East (Ohio)             | us-east-2      | sts.us-east-2.amazonaws.com<br>sts-fips.us-east-2.amazonaws.com | HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | sts.us-east-1.amazonaws.com<br>sts-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | sts.us-west-1.amazonaws.com<br>sts-fips.us-west-1.amazonaws.com | HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | sts.us-west-2.amazonaws.com<br>sts-fips.us-west-2.amazonaws.com | HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | sts.af-south-1.amazonaws.com                                    | HTTPS          |
| Asia Pacific (Hong Kong)   | ap-east-1      | sts.ap-east-1.amazonaws.com                                     | HTTPS          |
| Asia Pacific (Hyderabad)   | ap-south-2     | sts.ap-south-2.amazonaws.com                                    | HTTPS          |
| Asia Pacific (Jakarta)     | ap-southeast-3 | sts.ap-southeast-3.amazonaws.com                                | HTTPS          |
| Asia Pacific (Malaysia)    | ap-southeast-5 | sts.ap-southeast-5.amazonaws.com                                | HTTPS          |
| Asia Pacific (Melbourne)   | ap-southeast-4 | sts.ap-southeast-4.amazonaws.com                                | HTTPS          |
| Asia Pacific (Mumbai)      | ap-south-1     | sts.ap-south-1.amazonaws.com                                    | HTTPS          |
| Asia Pacific (New Zealand) | ap-southeast-6 | sts.ap-southeast-6.amazonaws.com                                | HTTPS          |
| Asia Pacific (Osaka)       | ap-northeast-3 | sts.ap-northeast-3.amazonaws.com                                | HTTPS          |
| Asia Pacific (Seoul)       | ap-northeast-2 | sts.ap-northeast-2.amazonaws.com                                | HTTPS          |
| Asia Pacific (Singapore)   | ap-southeast-1 | sts.ap-southeast-1.amazonaws.com                                | HTTPS          |
| Asia Pacific (Sydney)      | ap-southeast-2 | sts.ap-southeast-2.amazonaws.com                                | HTTPS          |
| Asia Pacific (Taipei)      | ap-east-2      | sts.ap-east-2.amazonaws.com                                     | HTTPS          |
| Asia Pacific (Thailand)    | ap-southeast-7 | sts.ap-southeast-7.amazonaws.com                                | HTTPS          |
| Asia Pacific (Tokyo)       | ap-northeast-1 | sts.ap-northeast-1.amazonaws.com                                | HTTPS          |
| Canada (Central)           | ca-central-1   | sts.ca-central-1.amazonaws.com                                  | HTTPS          |
| Canada West (Calgary)      | ca-west-1      | sts.ca-west-1.amazonaws.com                                     | HTTPS          |
| Europe (Frankfurt)         | eu-central-1   | sts.eu-central-1.amazonaws.com                                  | HTTPS          |
| Europe (Ireland)           | eu-west-1      | sts.eu-west-1.amazonaws.com                                     | HTTPS          |
| Europe (London)            | eu-west-2      | sts.eu-west-2.amazonaws.com                                     | HTTPS          |
| Europe (Milan)             | eu-south-1     | sts.eu-south-1.amazonaws.com                                    | HTTPS          |
| Europe (Paris)             | eu-west-3      | sts.eu-west-3.amazonaws.com                                     | HTTPS          |
| Europe (Spain)             | eu-south-2     | sts.eu-south-2.amazonaws.com                                    | HTTPS          |
| Europe (Stockholm)         | eu-north-1     | sts.eu-north-1.amazonaws.com                                    | HTTPS          |
| Europe (Zurich)            | eu-central-2   | sts.eu-central-2.amazonaws.com                                  | HTTPS          |
| Israel (Tel Aviv)          | il-central-1   | sts.il-central-1.amazonaws.com                                  | HTTPS          |
| Mexico (Central)           | mx-central-1   | sts.mx-central-1.amazonaws.com                                  | HTTPS          |
| Middle East (Bahrain)      | me-south-1     | sts.me-south-1.amazonaws.com                                    | HTTPS          |
| Middle East (UAE)          | me-central-1   | sts.me-central-1.amazonaws.com                                  | HTTPS          |
| South America (São Paulo)  | sa-east-1      | sts.sa-east-1.amazonaws.com                                     | HTTPS          |
| AWS GovCloud (US-East)     | us-gov-east-1  | sts.us-gov-east-1.amazonaws.com                                 | HTTPS          |
| AWS GovCloud (US-West)     | us-gov-west-1  | sts.us-gov-west-1.amazonaws.com                                 | HTTPS          |

## Service quotas

For information about AWS STS quotas, see [IAM and AWS STS quotas](../../../IAM/latest/UserGuide/reference_iam-quotas.md "../../../IAM/latest/UserGuide/reference_iam-quotas.md") in the
_IAM User Guide_.
