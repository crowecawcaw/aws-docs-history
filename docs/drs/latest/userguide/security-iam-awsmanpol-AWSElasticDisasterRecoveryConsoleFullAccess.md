# AWS managed

policy: AWSElasticDisasterRecoveryConsoleFullAccess

This policy provides full access to all public APIs of AWS Elastic Disaster Recovery (AWS DRS),
as well as permissions to read KMS key, License Manager,
Resource Groups, Elastic Load Balancing, IAM, and EC2 information. It also includes
EC2 actions that allow to launch, delete, or modify replication servers and recovery instances.
These EC2 actions are limited only to resources which the service creates with a specific
AWS-only tag.
policy to your users or roles.

AWSElasticDisasterRecoveryConsoleFullAccess includes access to your AWS
managed keys. However, it does not include access to your customer managed keys,
so if you use CMK you will need to add a policy statement to allow the usage of
your KMS keys.

**Permissions details**

To view the policy permission details see [AWSElasticDisasterRecoveryConsoleFullAccess](../../../aws-managed-policy/latest/reference/AWSElasticDisasterRecoveryConsoleFullAccess.md "../../../aws-managed-policy/latest/reference/AWSElasticDisasterRecoveryConsoleFullAccess.md") in the AWS Managed Policy Reference Guide.
