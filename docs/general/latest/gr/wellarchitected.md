# AWS Well-Architected Tool endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                             | Region                               | Endpoint                                     | Protocol                                                                            |
| --------------------------------------- | ------------------------------------ | -------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------- |
| US East (Ohio)                          | us-east-2                            | wellarchitected.us-east-2.amazonaws.com      | HTTPS                                                                               |
| US East (N. Virginia)                   | us-east-1                            | wellarchitected.us-east-1.amazonaws.com      | HTTPS                                                                               |
| US West (N. California)                 | us-west-1                            | wellarchitected.us-west-1.amazonaws.com      | HTTPS                                                                               |
| US West (Oregon)                        | us-west-2                            | wellarchitected.us-west-2.amazonaws.com      | HTTPS                                                                               |
| Asia Pacific (Hong Kong)                | ap-east-1                            | wellarchitected.ap-east-1.amazonaws.com      | HTTPS                                                                               |
| Asia Pacific (Mumbai)                   | ap-south-1                           | wellarchitected.ap-south-1.amazonaws.com     | HTTPS                                                                               |
| Asia Pacific (Seoul)                    | ap-northeast-2                       | wellarchitected.ap-northeast-2.amazonaws.com | HTTPS                                                                               |
| Asia Pacific (Singapore)                | ap-southeast-1                       | wellarchitected.ap-southeast-1.amazonaws.com | HTTPS                                                                               |
| Asia Pacific (Sydney)                   | ap-southeast-2                       | wellarchitected.ap-southeast-2.amazonaws.com | HTTPS                                                                               |
| Asia Pacific (Tokyo)                    | ap-northeast-1                       | wellarchitected.ap-northeast-1.amazonaws.com | HTTPS                                                                               |
| Canada (Central)                        | ca-central-1                         | wellarchitected.ca-central-1.amazonaws.com   | HTTPS                                                                               |
| Europe (Frankfurt)                      | eu-central-1                         | wellarchitected.eu-central-1.amazonaws.com   | HTTPS                                                                               |
| Europe (Ireland)                        | eu-west-1                            | wellarchitected.eu-west-1.amazonaws.com      | HTTPS                                                                               |
| Europe (London)                         | eu-west-2                            | wellarchitected.eu-west-2.amazonaws.com      | HTTPS                                                                               |
| Europe (Paris)                          | eu-west-3                            | wellarchitected.eu-west-3.amazonaws.com      | HTTPS                                                                               |
| Europe (Stockholm)                      | eu-north-1                           | wellarchitected.eu-north-1.amazonaws.com     | HTTPS                                                                               |
| Middle East (Bahrain)                   | me-south-1                           | wellarchitected.me-south-1.amazonaws.com     | HTTPS                                                                               |
| South America (São Paulo)               | sa-east-1                            | wellarchitected.sa-east-1.amazonaws.com      | HTTPS                                                                               |
| AWS GovCloud (US-East)                  | us-gov-east-1                        | wellarchitected.us-gov-east-1.amazonaws.com  | HTTPS                                                                               |
| AWS GovCloud (US-West)                  | us-gov-west-1                        | wellarchitected.us-gov-west-1.amazonaws.com  | HTTPS                                                                               | ## Service quotas |
| Name                                    | Default                              | Adjustable                                   | Description                                                                         |
| ---                                     | ---                                  | ---                                          | ---                                                                                 |
| Choices per question                    | Each supported Region: 15            | No                                           | The maximum number of choices that can be created for a question.                   |
| Lens size                               | Each supported Region: 500 Kilobytes | No                                           | The maximum lens size, in KB.                                                       |
| Lenses per account per Region           | Each supported Region: 15            | No                                           | The maximum number of lenses that can be created per account in a Region.           |
| Lenses per review template              | Each supported Region: 20            | No                                           | The maximum number of lenses that can be associated with a review template.         |
| Lenses per workload                     | Each supported Region: 20            | No                                           | The maximum number of lenses that can be associated with a workload.                |
| Milestones per workload                 | Each supported Region: 100           | No                                           | The maximum number of milestones that can be created for a workload.                |
| Pillars per lens                        | Each supported Region: 10            | No                                           | The maximum number of pillars that can be created for a lens.                       |
| Questions per pillar                    | Each supported Region: 20            | No                                           | The maximum number of questions that can be created for a pillar.                   |
| Review templates per account per Region | Each supported Region: 500           | No                                           | The maximum number of review templates that can be created per account in a Region. |
| Shares per lens                         | Each supported Region: 300           | No                                           | The maximum number of shares that can be created for a lens.                        |
| Shares per review template              | Each supported Region: 20            | No                                           | The maximum number of shares that can be created for a review template.             |
| Shares per workload                     | Each supported Region: 20            | No                                           | The maximum number of shares that can be created for a workload.                    |
| Versions per lens                       | Each supported Region: 100           | No                                           | The maximum number of versions that can be created for a lens.                      |
| Workloads per account per Region        | Each supported Region: 1,000         | No                                           | The maximum number of workloads that can be created per account in a Region.        |
