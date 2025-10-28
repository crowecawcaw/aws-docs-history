# Amazon AI Operations endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                      | Region         | Endpoint                           | Protocol                                                                                          |
| -------------------------------- | -------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (Ohio)                   | us-east-2      | aiops.us-east-2.amazonaws.com      | HTTPS                                                                                             |
| US East (N. Virginia)            | us-east-1      | aiops.us-east-1.amazonaws.com      | HTTPS                                                                                             |
| US West (Oregon)                 | us-west-2      | aiops.us-west-2.amazonaws.com      | HTTPS                                                                                             |
| Europe (Ireland)                 | eu-west-1      | aiops.eu-west-1.amazonaws.com      | HTTPS                                                                                             |
| Europe (Frankfurt)               | eu-central-1   | aiops.eu-central-1.amazonaws.com   | HTTPS                                                                                             |
| Europe (Spain)                   | eu-south-2     | aiops.eu-south-2.amazonaws.com     | HTTPS                                                                                             |
| Europe (Stockholm)               | eu-north-1     | aiops.eu-north-1.amazonaws.com     | HTTPS                                                                                             |
| Asia Pacific (Mumbai)            | ap-south-1     | aiops.ap-south-1.amazonaws.com     | HTTPS                                                                                             |
| Asia Pacific (Singapore)         | ap-southeast-1 | aiops.ap-southeast-1.amazonaws.com | HTTPS                                                                                             |
| Asia Pacific (Sydney)            | ap-southeast-2 | aiops.ap-southeast-2.amazonaws.com | HTTPS                                                                                             |
| Asia Pacific (Tokyo)             | ap-northeast-1 | aiops.ap-northeast-1.amazonaws.com | HTTPS                                                                                             |
| Asia Pacific (Hong Kong)         | ap-east-1      | aiops.ap-east-1.amazonaws.com      | HTTPS                                                                                             |
| Asia Pacific (Malaysia)          | ap-southeast-5 | aiops.ap-southeast-5.amazonaws.com | HTTPS                                                                                             |
| Asia Pacific (Thailand)          | ap-southeast-7 | aiops.ap-southeast-7.amazonaws.com | HTTPS                                                                                             | ## Service quotas                                                                                                                                                                                                         |
| Name                             | Default        | Adjustable                         | Description                                                                                       |
| ---                              | ---            | ---                                | ---                                                                                               |
| Concurrent active investigations | 2              | No                                 | The maximum number of concurrent investigations with active AI analysis per account per Region.   |
| Investigation groups             | 1              | No                                 | The maximum number of investigation groups that can be created per account in a Region.           |
| Monthly investigations           | 150            | No                                 | The maximum number of AI-assisted investigations per month in this account in the current Region. | For more information, see [CloudWatch Quotas](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_limits.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_limits.md") in the _Amazon CloudWatch User Guide_. |
