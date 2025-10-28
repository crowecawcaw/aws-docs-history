# Amazon Glacier endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                        | Region                                  | Endpoint                                                                   | Protocol                                                                            |
| ---------------------------------- | --------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------- |
| US East (Ohio)                     | us-east-2                               | glacier.us-east-2.amazonaws.com glacier-fips.us-east-2.amazonaws.com       | HTTP and HTTPS HTTPS                                                                |
| US East (N. Virginia)              | us-east-1                               | glacier.us-east-1.amazonaws.com glacier-fips.us-east-1.amazonaws.com       | HTTP and HTTPS HTTPS                                                                |
| US West (N. California)            | us-west-1                               | glacier.us-west-1.amazonaws.com glacier-fips.us-west-1.amazonaws.com       | HTTP and HTTPS HTTPS                                                                |
| US West (Oregon)                   | us-west-2                               | glacier.us-west-2.amazonaws.com glacier-fips.us-west-2.amazonaws.com       | HTTP and HTTPS HTTPS                                                                |
| Africa (Cape Town)                 | af-south-1                              | glacier.af-south-1.amazonaws.com                                           | HTTP and HTTPS                                                                      |
| Asia Pacific (Hong Kong)           | ap-east-1                               | glacier.ap-east-1.amazonaws.com                                            | HTTP and HTTPS                                                                      |
| Asia Pacific (Jakarta)             | ap-southeast-3                          | glacier.ap-southeast-3.amazonaws.com                                       | HTTP and HTTPS                                                                      |
| Asia Pacific (Mumbai)              | ap-south-1                              | glacier.ap-south-1.amazonaws.com                                           | HTTP and HTTPS                                                                      |
| Asia Pacific (Osaka)               | ap-northeast-3                          | glacier.ap-northeast-3.amazonaws.com                                       | HTTP and HTTPS                                                                      |
| Asia Pacific (Seoul)               | ap-northeast-2                          | glacier.ap-northeast-2.amazonaws.com                                       | HTTP and HTTPS                                                                      |
| Asia Pacific (Singapore)           | ap-southeast-1                          | glacier.ap-southeast-1.amazonaws.com                                       | HTTP and HTTPS                                                                      |
| Asia Pacific (Sydney)              | ap-southeast-2                          | glacier.ap-southeast-2.amazonaws.com                                       | HTTP and HTTPS                                                                      |
| Asia Pacific (Tokyo)               | ap-northeast-1                          | glacier.ap-northeast-1.amazonaws.com                                       | HTTP and HTTPS                                                                      |
| Canada (Central)                   | ca-central-1                            | glacier.ca-central-1.amazonaws.com glacier-fips.ca-central-1.amazonaws.com | HTTP and HTTPS HTTPS                                                                |
| Europe (Frankfurt)                 | eu-central-1                            | glacier.eu-central-1.amazonaws.com                                         | HTTP and HTTPS                                                                      |
| Europe (Ireland)                   | eu-west-1                               | glacier.eu-west-1.amazonaws.com                                            | HTTP and HTTPS                                                                      |
| Europe (London)                    | eu-west-2                               | glacier.eu-west-2.amazonaws.com                                            | HTTP and HTTPS                                                                      |
| Europe (Milan)                     | eu-south-1                              | glacier.eu-south-1.amazonaws.com                                           | HTTP and HTTPS                                                                      |
| Europe (Paris)                     | eu-west-3                               | glacier.eu-west-3.amazonaws.com                                            | HTTP and HTTPS                                                                      |
| Europe (Stockholm)                 | eu-north-1                              | glacier.eu-north-1.amazonaws.com                                           | HTTP and HTTPS                                                                      |
| Middle East (Bahrain)              | me-south-1                              | glacier.me-south-1.amazonaws.com                                           | HTTP and HTTPS                                                                      |
| South America (São Paulo)          | sa-east-1                               | glacier.sa-east-1.amazonaws.com                                            | HTTP and HTTPS                                                                      |
| AWS GovCloud (US-East)             | us-gov-east-1                           | glacier.us-gov-east-1.amazonaws.com                                        | HTTP and HTTPS                                                                      |
| AWS GovCloud (US-West)             | us-gov-west-1                           | glacier.us-gov-west-1.amazonaws.com                                        | HTTP and HTTPS                                                                      | ## Service quotas |
| Name                               | Default                                 | Adjustable                                                                 | Description                                                                         |
| ---                                | ---                                     | ---                                                                        | ---                                                                                 |
| Archive size in GB.                | Each supported Region: 40,000 Gigabytes | No                                                                         | The maximum size of an archive.                                                     |
| Archive size.                      | Each supported Region: 4 Megabytes      | No                                                                         | The minimum size (in MB) of an archive (or part).                                   |
| Multipart parts size.              | Each supported Region: 4 Gigabytes      | No                                                                         | The maximum size (in GB) of parts allowed in a multipart upload.                    |
| Number of multipart parts.         | Each supported Region: 10,000           | No                                                                         | The maximum number of parts allowed in a multipart upload.                          |
| Number of random restore requests. | Each supported Region: 35               | No                                                                         | The number of random restore requests per PiB stored per day.                       |
| Number of vault tags.              | Each supported Region: 50               | No                                                                         | The maximum number of tags that can be applied to a vault.                          |
| Provisioned capacity units         | Each supported Region: 2                | No                                                                         | The maximum number of provisioned capacity units available to purchase per account. |
| Vaults per account                 | Each supported Region: 1,000            | No                                                                         | The maximum number of vaults an account can have.                                   |
