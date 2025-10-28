# AWS Compute Optimizer endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                                    | Region                   | Endpoint                                           | Protocol                                        |
| ---------------------------------------------- | ------------------------ | -------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (Ohio)                                 | us-east-2                | compute-optimizer.us-east-2.amazonaws.com          | HTTPS                                           |
| US East (N. Virginia)                          | us-east-1                | compute-optimizer.us-east-1.amazonaws.com          | HTTPS                                           |
| US West (N. California)                        | us-west-1                | compute-optimizer.us-west-1.amazonaws.com          | HTTPS                                           |
| US West (Oregon)                               | us-west-2                | compute-optimizer.us-west-2.amazonaws.com          | HTTPS                                           |
| Africa (Cape Town)                             | af-south-1               | compute-optimizer.af-south-1.amazonaws.com         | HTTPS                                           |
| Asia Pacific (Hong Kong)                       | ap-east-1                | compute-optimizer.ap-east-1.amazonaws.com          | HTTPS                                           |
| Asia Pacific (Hyderabad)                       | ap-south-2               | compute-optimizer.ap-south-2.amazonaws.com         | HTTPS                                           |
| Asia Pacific (Jakarta)                         | ap-southeast-3           | compute-optimizer.ap-southeast-3.amazonaws.com     | HTTPS                                           |
| Asia Pacific (Melbourne)                       | ap-southeast-4           | compute-optimizer.ap-southeast-4.amazonaws.com     | HTTPS                                           |
| Asia Pacific (Mumbai)                          | ap-south-1               | compute-optimizer.ap-south-1.amazonaws.com         | HTTPS                                           |
| Asia Pacific (Osaka)                           | ap-northeast-3           | compute-optimizer.ap-northeast-3.amazonaws.com     | HTTPS                                           |
| Asia Pacific (Seoul)                           | ap-northeast-2           | compute-optimizer.ap-northeast-2.amazonaws.com     | HTTPS                                           |
| Asia Pacific (Singapore)                       | ap-southeast-1           | compute-optimizer.ap-southeast-1.amazonaws.com     | HTTPS                                           |
| Asia Pacific (Sydney)                          | ap-southeast-2           | compute-optimizer.ap-southeast-2.amazonaws.com     | HTTPS                                           |
| Asia Pacific (Tokyo)                           | ap-northeast-1           | compute-optimizer.ap-northeast-1.amazonaws.com     | HTTPS                                           |
| Canada (Central)                               | ca-central-1             | compute-optimizer.ca-central-1.amazonaws.com       | HTTPS                                           |
| Europe (Frankfurt)                             | eu-central-1             | compute-optimizer.eu-central-1.amazonaws.com       | HTTPS                                           |
| Europe (Ireland)                               | eu-west-1                | compute-optimizer.eu-west-1.amazonaws.com          | HTTPS                                           |
| Europe (London)                                | eu-west-2                | compute-optimizer.eu-west-2.amazonaws.com          | HTTPS                                           |
| Europe (Milan)                                 | eu-south-1               | compute-optimizer.eu-south-1.amazonaws.com         | HTTPS                                           |
| Europe (Paris)                                 | eu-west-3                | compute-optimizer.eu-west-3.amazonaws.com          | HTTPS                                           |
| Europe (Spain)                                 | eu-south-2               | compute-optimizer.eu-south-2.amazonaws.com         | HTTPS                                           |
| Europe (Stockholm)                             | eu-north-1               | compute-optimizer.eu-north-1.amazonaws.com         | HTTPS                                           |
| Europe (Zurich)                                | eu-central-2             | compute-optimizer.eu-central-2.amazonaws.com       | HTTPS                                           |
| Israel (Tel Aviv)                              | il-central-1             | compute-optimizer.il-central-1.amazonaws.com       | HTTPS                                           |
| Middle East (Bahrain)                          | me-south-1               | compute-optimizer.me-south-1.amazonaws.com         | HTTPS                                           |
| Middle East (UAE)                              | me-central-1             | compute-optimizer.me-central-1.amazonaws.com       | HTTPS                                           |
| South America (São Paulo)                      | sa-east-1                | compute-optimizer.sa-east-1.amazonaws.com          | HTTPS                                           |
| AWS GovCloud (US-East)                         | us-gov-east-1            | compute-optimizer-fips.us-gov-east-1.amazonaws.com | HTTPS                                           |
| AWS GovCloud (US-West)                         | us-gov-west-1            | compute-optimizer-fips.us-gov-west-1.amazonaws.com | HTTPS                                           | ###### Note AWS Compute Optimizer offers dual stack endpoints so that you can access the service using IPv4 and IPv6 requests. For more information, see [Dual stack endpoints](rande.md#dual-stack-endpoints "rande.md#dual-stack-endpoints"). ## Service quotas |
| Name                                           | Default                  | Adjustable                                         | Description                                     |
| ---                                            | ---                      | ---                                                | ---                                             |
| The number of API calls per second per account | Each supported Region: 5 | No                                                 | The number of API calls per second per account. |
