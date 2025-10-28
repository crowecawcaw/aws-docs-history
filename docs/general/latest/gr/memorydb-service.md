# Amazon MemoryDB endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name               | Region         | Endpoint                                                                 | Protocol                            |
| ------------------------- | -------------- | ------------------------------------------------------------------------ | ----------------------------------- | ----------------- |
| US East (Ohio)            | us-east-2      | memory-db.us-east-2.amazonaws.com memory-db-fips.us-east-2.amazonaws.com | HTTPS HTTPS                         |
| US East (N. Virginia)     | us-east-1      | memory-db.us-east-1.amazonaws.com memory-db-fips.us-east-1.amazonaws.com | HTTPS HTTPS                         |
| US West (N. California)   | us-west-1      | memory-db.us-west-1.amazonaws.com memory-db-fips.us-west-1.amazonaws.com | HTTPS HTTPS                         |
| US West (Oregon)          | us-west-2      | memory-db.us-west-2.amazonaws.com memory-db-fips.us-west-2.amazonaws.com | HTTPS HTTPS                         |
| Asia Pacific (Hong Kong)  | ap-east-1      | memory-db.ap-east-1.amazonaws.com                                        | HTTPS                               |
| Asia Pacific (Mumbai)     | ap-south-1     | memory-db.ap-south-1.amazonaws.com                                       | HTTPS                               |
| Asia Pacific (Seoul)      | ap-northeast-2 | memory-db.ap-northeast-2.amazonaws.com                                   | HTTPS                               |
| Asia Pacific (Singapore)  | ap-southeast-1 | memory-db.ap-southeast-1.amazonaws.com                                   | HTTPS                               |
| Asia Pacific (Sydney)     | ap-southeast-2 | memory-db.ap-southeast-2.amazonaws.com                                   | HTTPS                               |
| Asia Pacific (Tokyo)      | ap-northeast-1 | memory-db.ap-northeast-1.amazonaws.com                                   | HTTPS                               |
| Canada (Central)          | ca-central-1   | memory-db.ca-central-1.amazonaws.com                                     | HTTPS                               |
| Europe (Frankfurt)        | eu-central-1   | memory-db.eu-central-1.amazonaws.com                                     | HTTPS                               |
| Europe (Ireland)          | eu-west-1      | memory-db.eu-west-1.amazonaws.com                                        | HTTPS                               |
| Europe (London)           | eu-west-2      | memory-db.eu-west-2.amazonaws.com                                        | HTTPS                               |
| Europe (Milan)            | eu-south-1     | memory-db.eu-south-1.amazonaws.com                                       | HTTPS                               |
| Europe (Paris)            | eu-west-3      | memory-db.eu-west-3.amazonaws.com                                        | HTTPS                               |
| Europe (Spain)            | eu-south-2     | memory-db.eu-south-2.amazonaws.com                                       | HTTPS                               |
| Europe (Stockholm)        | eu-north-1     | memory-db.eu-north-1.amazonaws.com                                       | HTTPS                               |
| South America (São Paulo) | sa-east-1      | memory-db.sa-east-1.amazonaws.com                                        | HTTPS                               |
| AWS GovCloud (US-East)    | us-gov-east-1  | memory-db.us-gov-east-1.amazonaws.com                                    | HTTPS                               |
| AWS GovCloud (US-West)    | us-gov-west-1  | memory-db.us-gov-west-1.amazonaws.com                                    | HTTPS                               | ## Service quotas |
| Resource                  | Default        |                                                                          | ---                                 | ---               |
| Nodes per Region          | 300            |                                                                          | Nodes per cluster per instance type | 90                |
| Nodes per shard           | 6              |                                                                          | Parameter groups per Region         | 150               |
| Subnet groups per Region  | 150            |                                                                          | Subnets per subnet group            | 20                |
