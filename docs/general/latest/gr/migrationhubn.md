# AWS Migration Hub endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

The migration tools that integrate with AWS Migration Hub send migration status to the
Migration Hub in the home Region you choose. For information about choosing a home Region, see
[The AWS Migration Hub Home Region](../../../migrationhub/latest/ug/home-region.md "../../../migrationhub/latest/ug/home-region.md") in the _AWS Migration Hub User Guide_.

| Region Name           | Region         | Endpoint                         | Protocol |
| --------------------- | -------------- | -------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (N. Virginia) | us-east-1      | mgh.us-east-1.amazonaws.com      | HTTPS    |
| US West (Oregon)      | us-west-2      | mgh.us-west-2.amazonaws.com      | HTTPS    |
| Asia Pacific (Sydney) | ap-southeast-2 | mgh.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)  | ap-northeast-1 | mgh.ap-northeast-1.amazonaws.com | HTTPS    |
| Europe (Frankfurt)    | eu-central-1   | mgh.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)      | eu-west-1      | mgh.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)       | eu-west-2      | mgh.eu-west-2.amazonaws.com      | HTTPS    | ## Service quotas The quotas associated with AWS Migration Hub are the AWS Application Discovery Service quotas. For more information, see [AWS Application Discovery Service Quotas](appdiscserv.md#limits_appdiscserve "appdiscserv.md#limits_appdiscserve"). |
