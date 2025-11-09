# Amazon VPC Lattice endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name               | Region         | Endpoint                                 | Protocol |
| ------------------------- | -------------- | ---------------------------------------- | -------- |
| US East (Ohio)            | us-east-2      | vpc-lattice.us-east-2.amazonaws.com      | HTTPS    |
| US East (N. Virginia)     | us-east-1      | vpc-lattice.us-east-1.amazonaws.com      | HTTPS    |
| US West (N. California)   | us-west-1      | vpc-lattice.us-west-1.amazonaws.com      | HTTPS    |
| US West (Oregon)          | us-west-2      | vpc-lattice.us-west-2.amazonaws.com      | HTTPS    |
| Africa (Cape Town)        | af-south-1     | vpc-lattice.af-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Hong Kong)  | ap-east-1      | vpc-lattice.ap-east-1.amazonaws.com      | HTTPS    |
| Asia Pacific (Hyderabad)  | ap-south-2     | vpc-lattice.ap-south-2.amazonaws.com     | HTTPS    |
| Asia Pacific (Jakarta)    | ap-southeast-3 | vpc-lattice.ap-southeast-3.amazonaws.com | HTTPS    |
| Asia Pacific (Melbourne)  | ap-southeast-4 | vpc-lattice.ap-southeast-4.amazonaws.com | HTTPS    |
| Asia Pacific (Mumbai)     | ap-south-1     | vpc-lattice.ap-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Osaka)      | ap-northeast-3 | vpc-lattice.ap-northeast-3.amazonaws.com | HTTPS    |
| Asia Pacific (Seoul)      | ap-northeast-2 | vpc-lattice.ap-northeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Singapore)  | ap-southeast-1 | vpc-lattice.ap-southeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)     | ap-southeast-2 | vpc-lattice.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)      | ap-northeast-1 | vpc-lattice.ap-northeast-1.amazonaws.com | HTTPS    |
| Canada (Central)          | ca-central-1   | vpc-lattice.ca-central-1.amazonaws.com   | HTTPS    |
| Canada West (Calgary)     | ca-west-1      | vpc-lattice.ca-west-1.amazonaws.com      | HTTPS    |
| Europe (Frankfurt)        | eu-central-1   | vpc-lattice.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)          | eu-west-1      | vpc-lattice.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)           | eu-west-2      | vpc-lattice.eu-west-2.amazonaws.com      | HTTPS    |
| Europe (Milan)            | eu-south-1     | vpc-lattice.eu-south-1.amazonaws.com     | HTTPS    |
| Europe (Paris)            | eu-west-3      | vpc-lattice.eu-west-3.amazonaws.com      | HTTPS    |
| Europe (Spain)            | eu-south-2     | vpc-lattice.eu-south-2.amazonaws.com     | HTTPS    |
| Europe (Stockholm)        | eu-north-1     | vpc-lattice.eu-north-1.amazonaws.com     | HTTPS    |
| Europe (Zurich)           | eu-central-2   | vpc-lattice.eu-central-2.amazonaws.com   | HTTPS    |
| Middle East (Bahrain)     | me-south-1     | vpc-lattice.me-south-1.amazonaws.com     | HTTPS    |
| Middle East (UAE)         | me-central-1   | vpc-lattice.me-central-1.amazonaws.com   | HTTPS    |
| South America (São Paulo) | sa-east-1      | vpc-lattice.sa-east-1.amazonaws.com      | HTTPS    |

## Service quotas

| Name                                                           | Default                             | Adjustable                                                                                                                                                                                 | Description                                                                                                                                              |
| -------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Auth policy size                                               | Each supported Region: 10 Kilobytes | No                                                                                                                                                                                         | The maximum size of a JSON file in an Auth policy.                                                                                                       |
| Child Resource Configurations per Group Resource Configuration | Each supported Region: 60           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-9BC96FEF "https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-9BC96FEF") | The maximum number of child resource configurations in a group resource configuration. For additional capacity and limit increases, contact AWS Support. |
| Domain Verifications per AWS Region                            | Each supported Region: 5            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-73D0F278 "https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-73D0F278") | The maximum number of domain verifications that can be created per account. For additional capacity and limit increases, contact AWS Support.            |
| Listeners per service                                          | Each supported Region: 2            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-D64E952E "https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-D64E952E") | The maximum number of listeners that you can create for a service. For additional capacity and limit increases, contact AWS Support.                     |
| Resource Configurations per service network                    | Each supported Region: 500          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-6095700C "https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-6095700C") | The maximum number of resource configurations associated with a service network. For additional capacity and limit increases, contact AWS Support.       |
| Resource configurations per AWS Region                         | Each supported Region: 2,000        | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-5FF8F9B9 "https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-5FF8F9B9") | The maximum number of resource configurations an AWS account can have per AWS Region. For additional capacity and limit increases, contact AWS Support.  |
| Resource gateways per VPC                                      | Each supported Region: 500          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-0DCA4434 "https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-0DCA4434") | The maximum number of resource gateways in a VPC. For additional capacity and limit increases, contact AWS Support.                                      |
| Rules per listener                                             | Each supported Region: 10           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-CF78395E "https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-CF78395E") | The maximum number of rules that you can define for your service listener. For additional capacity and limit increases, contact AWS Support.             |
| Security groups per association                                | Each supported Region: 5            | No                                                                                                                                                                                         | The maximum number of security groups that you can add to an association between a VPC and a service network.                                            |
| Service associations per service network                       | Each supported Region: 500          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-75D4A19E "https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-75D4A19E") | The maximum number of services that you can associate with a single service network. For additional capacity and limit increases, contact AWS Support.   |
| Service networks per region                                    | Each supported Region: 50           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-9CAD07FB "https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-9CAD07FB") | The maximum number of service networks per region. For additional capacity and limit increases, contact AWS Support.                                     |
| Services per region                                            | Each supported Region: 2,000        | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-620C821E "https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-620C821E") | The maximum number of services per region. For additional capacity and limit increases, contact AWS Support.                                             |
| Target groups per region                                       | Each supported Region: 500          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-BB11C6B9 "https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-BB11C6B9") | The maximum number of target groups per region. For additional capacity and limit increases, contact AWS Support.                                        |
| Target groups per service                                      | Each supported Region: 10           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-3DEC3B9F "https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-3DEC3B9F") | The maximum number of target groups that you can associate with a service. For additional capacity and limit increases, contact AWS Support.             |
| Targets per target group                                       | Each supported Region: 1,000        | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-D71303F3 "https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-D71303F3") | The maximum number of targets that you can associate with a single target group. For additional capacity and limit increases, contact AWS Support.       |
| VPC associations per service network                           | Each supported Region: 500          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-EF6E2D62 "https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-EF6E2D62") | The maximum number of VPCs that you can associate with a single service network. For additional capacity and limit increases, contact AWS Support.       |
| VPC endpoints of type service network per service network      | Each supported Region: 200          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-89DEA27F "https://console.aws.amazon.com/servicequotas/home/services/vpc-lattice/quotas/L-89DEA27F") | The maximum number of service network endpoints associated with a service network. For additional capacity and limit increases, contact AWS Support.     |
