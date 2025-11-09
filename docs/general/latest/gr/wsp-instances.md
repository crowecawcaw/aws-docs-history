# Amazon WorkSpaces Instances endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

###### Note

The AWS Regions in the following table apply to WorkSpaces Instances.

| Region Name               | Region         | Endpoint                                                                              | Protocol |
| ------------------------- | -------------- | ------------------------------------------------------------------------------------- | -------- |
| US East (N. Virginia)     | us-east-1      | workspaces-instances.us-east-1.api.aws<br>workspaces-instances-fips.us-east-1.api.aws | HTTPS    |
| US East (Ohio)            | us-east-2      | workspaces-instances.us-east-2.api.aws<br>workspaces-instances-fips.us-east-2.api.aws | HTTPS    |
| US West (Oregon)          | us-west-2      | workspaces-instances.us-west-2.api.aws<br>workspaces-instances-fips.us-west-2.api.aws | HTTPS    |
| Africa (Cape Town)        | af-south-1     | workspaces-instances.af-south-1.api.aws                                               | HTTPS    |
| Asia Pacific (Hong Kong)  | ap-east-1      | workspaces-instances.ap-east-1.api.aws                                                | HTTPS    |
| Asia Pacific (Malaysia)   | ap-southeast-5 | workspaces-instances.ap-southeast-5.api.aws                                           | HTTPS    |
| Asia Pacific (Mumbai)     | ap-south-1     | workspaces-instances.ap-south-1.api.aws                                               | HTTPS    |
| Asia Pacific (Seoul)      | ap-northeast-2 | workspaces-instances.ap-northeast-2.api.aws                                           | HTTPS    |
| Asia Pacific (Singapore)  | ap-southeast-1 | workspaces-instances.ap-southeast-1.api.aws                                           | HTTPS    |
| Asia Pacific (Sydney)     | ap-southeast-2 | workspaces-instances.ap-southeast-2.api.aws                                           | HTTPS    |
| Asia Pacific (Tokyo)      | ap-northeast-1 | workspaces-instances.ap-northeast-1.api.aws                                           | HTTPS    |
| Canada (Central)          | ca-central-1   | workspaces-instances.ca-central-1.api.aws                                             | HTTPS    |
| Europe (Frankfurt)        | eu-central-1   | workspaces-instances.eu-central-1.api.aws                                             | HTTPS    |
| Europe (Ireland)          | eu-west-1      | workspaces-instances.eu-west-1.api.aws                                                | HTTPS    |
| Europe (London)           | eu-west-2      | workspaces-instances.eu-west-2.api.aws                                                | HTTPS    |
| Europe (Paris)            | eu-west-3      | workspaces-instances.eu-west-3.api.aws                                                | HTTPS    |
| Europe (Spain)            | eu-south-2     | workspaces-instances.eu-south-2.api.aws                                               | HTTPS    |
| Middle East (UAE)         | me-central-1   | workspaces-instances.me-central-1.api.aws                                             | HTTPS    |
| Israel (Tel Aviv)         | il-central-1   | workspaces-instances.il-central-1.api.aws                                             | HTTPS    |
| South America (São Paulo) | sa-east-1      | workspaces-instances.sa-east-1.api.aws                                                | HTTPS    |

## Service quotas

| Resource                                                    | Default | Description                                                                                                                 | Adjustable |
| ----------------------------------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------- | ---------- |
| WorkSpaces Core Managed Instances                           | 1000    | The maximum number of WorkSpaces Managed Instances in this account in<br>the current Region.                                | Yes        |
| Concurrent WorkSpaces Managed Instances in allocating state | 700     | The maximum number of concurrent WorkSpaces Managed Instances in<br>allocating state in this account in the current Region. | No         |
