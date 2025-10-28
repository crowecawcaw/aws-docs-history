# AWS AppFabric endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                | Region                    | Endpoint                               | Protocol                                                                                                                |
| -------------------------- | ------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------- |
| US East (N. Virginia)      | us-east-1                 | appfabric.us-east-1.amazonaws.com      | HTTPS                                                                                                                   |
| Asia Pacific (Tokyo)       | ap-northeast-1            | appfabric.ap-northeast-1.amazonaws.com | HTTPS                                                                                                                   |
| Europe (Ireland)           | eu-west-1                 | appfabric.eu-west-1.amazonaws.com      | HTTPS                                                                                                                   | ## Service quotas |
| Name                       | Default                   | Adjustable                             | Description                                                                                                             |
| ---                        | ---                       | ---                                    | ---                                                                                                                     |
| Application authorizations | Each supported Region: 50 | No                                     | The maximum number of application authorizations that you can create in an account in the current AWS Region.           |
| Application bundles        | Each supported Region: 1  | No                                     | The maximum number of application bundles that you can create in an account in the current AWS Region.                  |
| Ingestion destinations     | Each supported Region: 5  | No                                     | The maximum number of ingestion destinations that you can create per ingestion in an account in the current AWS Region. |
| Ingestions                 | Each supported Region: 50 | No                                     | The maximum number of ingestions that you can create in an account in the current AWS Region.                           |
