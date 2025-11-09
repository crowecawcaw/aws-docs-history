# AWS Identity and Access Management Roles Anywhere endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                | Region         | Endpoint                                                                                                                           | Protocol                |
| -------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| US East (Ohio)             | us-east-2      | rolesanywhere.us-east-2.amazonaws.com<br>rolesanywhere.us-east-2.api.aws<br>rolesanywhere-fips.us-east-2.amazonaws.com             | HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | rolesanywhere.us-east-1.amazonaws.com<br>rolesanywhere-fips.us-east-1.amazonaws.com<br>rolesanywhere.us-east-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | rolesanywhere.us-west-1.amazonaws.com<br>rolesanywhere.us-west-1.api.aws<br>rolesanywhere-fips.us-west-1.amazonaws.com             | HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | rolesanywhere.us-west-2.amazonaws.com<br>rolesanywhere.us-west-2.api.aws<br>rolesanywhere-fips.us-west-2.amazonaws.com             | HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | rolesanywhere.af-south-1.amazonaws.com<br>rolesanywhere.af-south-1.api.aws                                                         | HTTPS<br>HTTPS          |
| Asia Pacific (Hong Kong)   | ap-east-1      | rolesanywhere.ap-east-1.amazonaws.com<br>rolesanywhere.ap-east-1.api.aws                                                           | HTTPS<br>HTTPS          |
| Asia Pacific (Hyderabad)   | ap-south-2     | rolesanywhere.ap-south-2.amazonaws.com<br>rolesanywhere.ap-south-2.api.aws                                                         | HTTPS<br>HTTPS          |
| Asia Pacific (Jakarta)     | ap-southeast-3 | rolesanywhere.ap-southeast-3.amazonaws.com<br>rolesanywhere.ap-southeast-3.api.aws                                                 | HTTPS<br>HTTPS          |
| Asia Pacific (Malaysia)    | ap-southeast-5 | rolesanywhere.ap-southeast-5.amazonaws.com<br>rolesanywhere.ap-southeast-5.api.aws                                                 | HTTPS<br>HTTPS          |
| Asia Pacific (Melbourne)   | ap-southeast-4 | rolesanywhere.ap-southeast-4.amazonaws.com<br>rolesanywhere.ap-southeast-4.api.aws                                                 | HTTPS<br>HTTPS          |
| Asia Pacific (Mumbai)      | ap-south-1     | rolesanywhere.ap-south-1.amazonaws.com<br>rolesanywhere.ap-south-1.api.aws                                                         | HTTPS<br>HTTPS          |
| Asia Pacific (New Zealand) | ap-southeast-6 | rolesanywhere.ap-southeast-6.amazonaws.com<br>rolesanywhere.ap-southeast-6.api.aws                                                 | HTTPS<br>HTTPS          |
| Asia Pacific (Osaka)       | ap-northeast-3 | rolesanywhere.ap-northeast-3.amazonaws.com<br>rolesanywhere.ap-northeast-3.api.aws                                                 | HTTPS<br>HTTPS          |
| Asia Pacific (Seoul)       | ap-northeast-2 | rolesanywhere.ap-northeast-2.amazonaws.com<br>rolesanywhere.ap-northeast-2.api.aws                                                 | HTTPS<br>HTTPS          |
| Asia Pacific (Singapore)   | ap-southeast-1 | rolesanywhere.ap-southeast-1.amazonaws.com<br>rolesanywhere.ap-southeast-1.api.aws                                                 | HTTPS<br>HTTPS          |
| Asia Pacific (Sydney)      | ap-southeast-2 | rolesanywhere.ap-southeast-2.amazonaws.com<br>rolesanywhere.ap-southeast-2.api.aws                                                 | HTTPS<br>HTTPS          |
| Asia Pacific (Taipei)      | ap-east-2      | rolesanywhere.ap-east-2.amazonaws.com<br>rolesanywhere.ap-east-2.api.aws                                                           | HTTPS<br>HTTPS          |
| Asia Pacific (Thailand)    | ap-southeast-7 | rolesanywhere.ap-southeast-7.amazonaws.com<br>rolesanywhere.ap-southeast-7.api.aws                                                 | HTTPS<br>HTTPS          |
| Asia Pacific (Tokyo)       | ap-northeast-1 | rolesanywhere.ap-northeast-1.amazonaws.com<br>rolesanywhere.ap-northeast-1.api.aws                                                 | HTTPS<br>HTTPS          |
| Canada (Central)           | ca-central-1   | rolesanywhere.ca-central-1.amazonaws.com<br>rolesanywhere.ca-central-1.api.aws                                                     | HTTPS<br>HTTPS          |
| Canada West (Calgary)      | ca-west-1      | rolesanywhere.ca-west-1.amazonaws.com<br>rolesanywhere.ca-west-1.api.aws                                                           | HTTPS<br>HTTPS          |
| Europe (Frankfurt)         | eu-central-1   | rolesanywhere.eu-central-1.amazonaws.com<br>rolesanywhere.eu-central-1.api.aws                                                     | HTTPS<br>HTTPS          |
| Europe (Ireland)           | eu-west-1      | rolesanywhere.eu-west-1.amazonaws.com<br>rolesanywhere.eu-west-1.api.aws                                                           | HTTPS<br>HTTPS          |
| Europe (London)            | eu-west-2      | rolesanywhere.eu-west-2.amazonaws.com<br>rolesanywhere.eu-west-2.api.aws                                                           | HTTPS<br>HTTPS          |
| Europe (Milan)             | eu-south-1     | rolesanywhere.eu-south-1.amazonaws.com<br>rolesanywhere.eu-south-1.api.aws                                                         | HTTPS<br>HTTPS          |
| Europe (Paris)             | eu-west-3      | rolesanywhere.eu-west-3.amazonaws.com<br>rolesanywhere.eu-west-3.api.aws                                                           | HTTPS<br>HTTPS          |
| Europe (Spain)             | eu-south-2     | rolesanywhere.eu-south-2.amazonaws.com<br>rolesanywhere.eu-south-2.api.aws                                                         | HTTPS<br>HTTPS          |
| Europe (Stockholm)         | eu-north-1     | rolesanywhere.eu-north-1.amazonaws.com<br>rolesanywhere.eu-north-1.api.aws                                                         | HTTPS<br>HTTPS          |
| Europe (Zurich)            | eu-central-2   | rolesanywhere.eu-central-2.amazonaws.com<br>rolesanywhere.eu-central-2.api.aws                                                     | HTTPS<br>HTTPS          |
| Israel (Tel Aviv)          | il-central-1   | rolesanywhere.il-central-1.amazonaws.com<br>rolesanywhere.il-central-1.api.aws                                                     | HTTPS<br>HTTPS          |
| Mexico (Central)           | mx-central-1   | rolesanywhere.mx-central-1.amazonaws.com<br>rolesanywhere.mx-central-1.api.aws                                                     | HTTPS<br>HTTPS          |
| Middle East (Bahrain)      | me-south-1     | rolesanywhere.me-south-1.amazonaws.com<br>rolesanywhere.me-south-1.api.aws                                                         | HTTPS<br>HTTPS          |
| Middle East (UAE)          | me-central-1   | rolesanywhere.me-central-1.amazonaws.com<br>rolesanywhere.me-central-1.api.aws                                                     | HTTPS<br>HTTPS          |
| South America (São Paulo)  | sa-east-1      | rolesanywhere.sa-east-1.amazonaws.com<br>rolesanywhere.sa-east-1.api.aws                                                           | HTTPS<br>HTTPS          |
| AWS GovCloud (US-East)     | us-gov-east-1  | rolesanywhere.us-gov-east-1.amazonaws.com<br>rolesanywhere.us-gov-east-1.api.aws<br>rolesanywhere-fips.us-gov-east-1.amazonaws.com | HTTPS<br>HTTPS<br>HTTPS |
| AWS GovCloud (US-West)     | us-gov-west-1  | rolesanywhere.us-gov-west-1.amazonaws.com<br>rolesanywhere-fips.us-gov-west-1.amazonaws.com<br>rolesanywhere.us-gov-west-1.api.aws | HTTPS<br>HTTPS<br>HTTPS |

## Service quotas

| Resource                               | Description                                                                                                                                                                                     | Default value | Adjustable |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ---------- |
| Combined rate of trust anchor requests | The maximum transactions per second for ListTrustAnchors, CreateTrustAnchor, GetTrustAnchor, UpdateTrustAnchor, DeleteTrustAnchor, EnableTrustAnchor, and DisableTrustAnchor requests combined. | 1 per second  | Yes        |
| Combined rate of profile requests      | The maximum transactions per second for ListProfiles, CreateProfile, GetProfile, UpdateProfile, DeleteProfile, EnableProfile, and DisableProfile requests combined.                             | 1 per second  | Yes        |
| Combined rate of subject requests      | The maximum transactions per second for ListSubjects and GetSubject requests combined.                                                                                                          | 1 per second  | Yes        |
| Combined rate of tagging requests      | The maximum transactions per second for TagResource, UntagResource, and ListTagsForResource requests combined.                                                                                  | 1 per second  | Yes        |
| Combined rate of CRL requests          | The maximum transactions per second for ListCrls, GetCrl, ImportCrl, UpdateCrl, DeleteCrl, EnableCrl, and DisableCrl requests combined.                                                         | 1 per second  | Yes        |
| Rate of CreateSession requests         | The maximum transactions per second for CreateSession requests.                                                                                                                                 | 10 per second | Yes        |
| Trust anchors                          | The maximum number of trust anchors that you can create within an account.                                                                                                                      | 50            | Yes        |
| Profiles                               | The maximum number of profiles that you can create within an account.                                                                                                                           | 250           | Yes        |
| CRLs per trust anchor                  | The maximum number of Certificate Revocation Lists (CRLs) that you can create per trust anchor within an account.                                                                               | 2             | No         |
| Certificates per trust anchor          | The maximum number of certificates that you can create per trust anchor within an account.                                                                                                      | 2             | No         |

For more information, see [IAM Roles Anywhere quotas](../../../rolesanywhere/latest/userguide/load-balancer-limits.md "../../../rolesanywhere/latest/userguide/load-balancer-limits.md")
in the _IAM Roles Anywhere User Guide_.
