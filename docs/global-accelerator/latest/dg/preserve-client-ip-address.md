# AWS Region availability for AWS Global Accelerator

For detailed information about Regional support and service endpoints for AWS Global Accelerator,
see [AWS Global Accelerator
endpoints and quotas](../../../general/latest/gr/global_accelerator.md "../../../general/latest/gr/global_accelerator.md") in the _Amazon Web Services General Reference_.

###### Note

AWS Global Accelerator is a global service. However, you must specify the US West (Oregon)
Region (that is, specify the parameter `--region us-west-2`) in Regional Global Accelerator AWS CLI commands. That is, when
you create resources, such as accelerators.

Global Accelerator is currently available in the following AWS Regions. Availability Zone (AZ) exceptions are noted.
Adding endpoints in AWS Local Zones is not supported.

| Region Name               | Region                                 |
| ------------------------- | -------------------------------------- |
| US East (Ohio)            | `us-east-2`                            |
| US East (N. Virginia)     | `us-east-1`                            |
| US West (N. California)   | `us-west-1 (except AZ usw1-az2)`       |
| US West (Oregon)          | `us-west-2`                            |
| Africa (Cape Town)        | `af-south-1`                           |
| Asia Pacific (Hong Kong)  | `ap-east-1`                            |
| Asia Pacific (Taipei)     | `ap-east-2`                            |
| Asia Pacific (Mumbai)     | `ap-south-1`                           |
| Asia Pacific (Hyderabad)  | `ap-south-2`                           |
| Asia Pacific (Jakarta)    | `ap-southeast-3`                       |
| Asia Pacific (Melbourne)  | `ap-southeast-4`                       |
| Asia Pacific (Osaka)      | `ap-northeast-3`                       |
| Asia Pacific (Singapore)  | `ap-southeast-1`                       |
| Asia Pacific (Sydney)     | `ap-southeast-2`                       |
| Asia Pacific (Malaysia)   | `ap-southeast-5`                       |
| Asia Pacific (Thailand)   | `ap-southeast-7`                       |
| Asia Pacific (Tokyo)      | `ap-northeast-1 (except AZ apne1-az3)` |
| Asia Pacific (Seoul)      | `ap-northeast-2`                       |
| Canada (Central)          | `ca-central-1 (except AZ cac1-az3)`    |
| Canada West (Calgary)     | `ca-west-1`                            |
| Canada West (Calgary)     | `ca-west-1`                            |
| Europe (Frankfurt)        | `eu-central-1`                         |
| Europe (Ireland)          | `eu-west-1`                            |
| Europe (London)           | `eu-west-2`                            |
| Europe (Milan)            | `eu-south-1`                           |
| Europe (Paris)            | `eu-west-3`                            |
| Europe (Spain)            | `eu-south-2`                           |
| Europe (Stockholm)        | `eu-north-1`                           |
| Europe (Zurich)           | `eu-central-2`                         |
| Israel (Tel Aviv)         | `il-central-1`                         |
| Mexico (Central)          | `mx-central-1`                         |
| Middle East (Bahrain)     | `me-south-1`                           |
| Middle East (UAE)         | `me-central-1`                         |
| South America (São Paulo) | `sa-east-1`                            |
