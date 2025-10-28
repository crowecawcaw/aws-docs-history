# AWS Launch Wizard workload availability

###### Note

End of support notice: On May 1, 2025, AWS Launch Wizard will discontinue support for Amazon Elastic Kubernetes Service, Microsoft Internet Information Services, and Microsoft Exchange Server.
After May 1, 2025, you can no longer use AWS Launch Wizard to access these workloads.

AWS Launch Wizard supports workloads based on the underlying resources it creates in an
AWS Region.

Some deployments don't support every configuration and setting for every Region. For
such deployments, the configurations and settings won't be listed in the Launch Wizard console
for the Region.

The following table describes which workloads are available in which Regions.

| Name                      | Code             | Active Directory | RD Gateway | SAP | SQL Server |
| ------------------------- | ---------------- | ---------------- | ---------- | --- | ---------- |
| US East (N. Virginia)     | `us-east-1`      | ✓                | ✓          | ✓   | ✓          |
| US East (Ohio)            | `us-east-2`      | ✓                | ✓          | ✓   | ✓          |
| US West (N. California)   | `us-west-1`      | ✓                | ✓          | ✓   | ✓          |
| US West (Oregon)          | `us-west-2`      | ✓                | ✓          | ✓   | ✓          |
| Africa (Cape Town)        | `af-south-1`     | ✓                | ✓          | ✓   | ✓          |
| Asia Pacific (Hong Kong)  | `ap-east-1`      | ✓                | ✓          | ✓   | ✓          |
| Asia Pacific (Hyderabad)  | `ap-south-2`     |                  |            | ✓   | ✓          |
| Asia Pacific (Jakarta)    | `ap-southeast-3` |                  |            | ✓   | ✓          |
| Asia Pacific (Malaysia)   | `ap-southeast-5` |                  | ✓          | ✓   | ✓          |
| Asia Pacific (Melbourne)  | `ap-southeast-4` |                  |            | ✓   | ✓          |
| Asia Pacific (Mumbai)     | `ap-south-1`     | ✓                | ✓          | ✓   | ✓          |
| Asia Pacific (Osaka)      | `ap-northeast-3` | ✓                | ✓          | ✓   | ✓          |
| Asia Pacific (Seoul)      | `ap-northeast-2` | ✓                | ✓          | ✓   | ✓          |
| Asia Pacific (Singapore)  | `ap-southeast-1` | ✓                | ✓          | ✓   | ✓          |
| Asia Pacific (Sydney)     | `ap-southeast-2` | ✓                | ✓          | ✓   | ✓          |
| Asia Pacific (Thailand)   | `ap-southeast-7` |                  |            |     |            |
| Asia Pacific (Tokyo)      | `ap-northeast-1` | ✓                | ✓          | ✓   | ✓          |
| Canada (Central)          | `ca-central-1`   | ✓                | ✓          | ✓   | ✓          |
| Canada West (Calgary)     | `ca-west-1`      |                  | ✓          | ✓   | ✓          |
| China (Beijing)           | `cn-north-1`     |                  |            | ✓   | ✓          |
| China (Ningxia)           | `cn-northwest-1` |                  |            | ✓   | ✓          |
| Europe (Frankfurt)        | `eu-central-1`   | ✓                | ✓          | ✓   | ✓          |
| Europe (Ireland)          | `eu-west-1`      | ✓                | ✓          | ✓   | ✓          |
| Europe (London)           | `eu-west-2`      | ✓                | ✓          | ✓   | ✓          |
| Europe (Milan)            | `eu-south-1`     | ✓                | ✓          | ✓   | ✓          |
| Europe (Paris)            | `eu-west-3`      | ✓                | ✓          | ✓   | ✓          |
| Europe (Spain)            | `eu-south-2`     |                  |            | ✓   | ✓          |
| Europe (Stockholm)        | `eu-north-1`     | ✓                | ✓          | ✓   | ✓          |
| Europe (Zurich)           | `eu-central-2`   |                  |            | ✓   | ✓          |
| Israel (Tel Aviv)         | `il-central-1`   |                  | ✓          | ✓   | ✓          |
| Mexico (Central)          | `mx-central-1`   |                  |            |     |            |
| Middle East (Bahrain)     | `me-south-1`     | ✓                | ✓          | ✓   | ✓          |
| Middle East (UAE)         | `me-central-1`   |                  |            | ✓   | ✓          |
| South America (São Paulo) | `sa-east-1`      | ✓                | ✓          | ✓   | ✓          |
| AWS GovCloud (US-East)    | `us-gov-east-1`  |                  |            | ✓   | ✓          |
| AWS GovCloud (US-West)    | `us-gov-west-1`  |                  |            | ✓   | ✓          |
