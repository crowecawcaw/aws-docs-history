# Migration Hub Orchestrator endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name           | Region         | Endpoint                                               | Protocol |
| --------------------- | -------------- | ------------------------------------------------------ | -------- |
| US East (N. Virginia) | us-east-1      | migrationhub-orchestrator.us-east-1.amazonaws.com      | HTTPS    |
| US West (Oregon)      | us-west-2      | migrationhub-orchestrator.us-west-2.amazonaws.com      | HTTPS    |
| Asia Pacific (Sydney) | ap-southeast-2 | migrationhub-orchestrator.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)  | ap-northeast-1 | migrationhub-orchestrator.ap-northeast-1.amazonaws.com | HTTPS    |
| Europe (Frankfurt)    | eu-central-1   | migrationhub-orchestrator.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)      | eu-west-1      | migrationhub-orchestrator.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)       | eu-west-2      | migrationhub-orchestrator.eu-west-2.amazonaws.com      | HTTPS    |

## Service quotas

| Name                        | Default | Adjustable | Description                                                |
| --------------------------- | ------- | ---------- | ---------------------------------------------------------- |
| Maximum steps               | 15      | No         | The maximum number of steps in a step group.               |
| Maximum step groups         | 15      | No         | The maximum number of step groups in a migration workflow. |
| Maximum migration workflows | 50      | No         | The maximum number of migration workflows in progress.     |
