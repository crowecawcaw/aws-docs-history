# Amazon DevOps Guru endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name               | Region         | Endpoint                                                                              | Protocol       |
| ------------------------- | -------------- | ------------------------------------------------------------------------------------- | -------------- |
| US East (Ohio)            | us-east-2      | devops-guru.us-east-2.amazonaws.com<br>devops-guru-fips.us-east-2.amazonaws.com       | HTTPS<br>HTTPS |
| US East (N. Virginia)     | us-east-1      | devops-guru.us-east-1.amazonaws.com<br>devops-guru-fips.us-east-1.amazonaws.com       | HTTPS<br>HTTPS |
| US West (N. California)   | us-west-1      | devops-guru.us-west-1.amazonaws.com<br>devops-guru-fips.us-west-1.amazonaws.com       | HTTPS<br>HTTPS |
| US West (Oregon)          | us-west-2      | devops-guru.us-west-2.amazonaws.com<br>devops-guru-fips.us-west-2.amazonaws.com       | HTTPS<br>HTTPS |
| Asia Pacific (Mumbai)     | ap-south-1     | devops-guru.ap-south-1.amazonaws.com                                                  | HTTPS          |
| Asia Pacific (Seoul)      | ap-northeast-2 | devops-guru.ap-northeast-2.amazonaws.com                                              | HTTPS          |
| Asia Pacific (Singapore)  | ap-southeast-1 | devops-guru.ap-southeast-1.amazonaws.com                                              | HTTPS          |
| Asia Pacific (Sydney)     | ap-southeast-2 | devops-guru.ap-southeast-2.amazonaws.com                                              | HTTPS          |
| Asia Pacific (Tokyo)      | ap-northeast-1 | devops-guru.ap-northeast-1.amazonaws.com                                              | HTTPS          |
| Canada (Central)          | ca-central-1   | devops-guru.ca-central-1.amazonaws.com<br>devops-guru-fips.ca-central-1.amazonaws.com | HTTPS<br>HTTPS |
| Europe (Frankfurt)        | eu-central-1   | devops-guru.eu-central-1.amazonaws.com                                                | HTTPS          |
| Europe (Ireland)          | eu-west-1      | devops-guru.eu-west-1.amazonaws.com                                                   | HTTPS          |
| Europe (London)           | eu-west-2      | devops-guru.eu-west-2.amazonaws.com                                                   | HTTPS          |
| Europe (Paris)            | eu-west-3      | devops-guru.eu-west-3.amazonaws.com                                                   | HTTPS          |
| Europe (Stockholm)        | eu-north-1     | devops-guru.eu-north-1.amazonaws.com                                                  | HTTPS          |
| South America (São Paulo) | sa-east-1      | devops-guru.sa-east-1.amazonaws.com                                                   | HTTPS          |

## Service quotas

| Name                                                             | Default | Adjustable |
| ---------------------------------------------------------------- | ------- | ---------- |
| Maximum number of Amazon SNS topics that you can specify at once | 2       | No         |
| Maximum number of AWS CloudFormation stacks that you can specify | 1,000   | No         |
| Maximum number of Amazon SQS queues for monitoring               | 100     | Yes        |

For more information, see [Quotas and limits](../../../devops-guru/latest/userguide/quotas.md "../../../devops-guru/latest/userguide/quotas.md") in the
_Amazon DevOps Guru User Guide_.
