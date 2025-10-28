# AWS Health endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name            | Region        | Endpoint                                                                                                                                  | Protocol                |
| ---------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (Ohio)         | us-east-2     | health.us-east-2.amazonaws.com global.health.amazonaws.com health-fips.us-east-2.amazonaws.com health.us-east-2.api.aws                   | HTTPS HTTPS HTTPS HTTPS |
| US East (N. Virginia)  | us-east-1     | health.us-east-1.amazonaws.com global.health.amazonaws.com health.us-east-1.api.aws                                                       | HTTPS HTTPS HTTPS       |
| AWS GovCloud (US-East) | us-gov-east-1 | health.us-gov-east-1.amazonaws.com health-fips.us-gov-east-1.api.aws health-fips.us-gov-east-1.amazonaws.com health.us-gov-east-1.api.aws | HTTPS HTTPS HTTPS HTTPS |
| AWS GovCloud (US-West) | us-gov-west-1 | health.us-gov-west-1.amazonaws.com health-fips.us-gov-west-1.api.aws health-fips.us-gov-west-1.amazonaws.com health.us-gov-west-1.api.aws | HTTPS HTTPS HTTPS HTTPS | For more information, see [Accessing the AWS Health API](../../../health/latest/ug/health-api.md "../../../health/latest/ug/health-api.md") in the _AWS Health User Guide_. ## Service quotas This service has no quotas. |
