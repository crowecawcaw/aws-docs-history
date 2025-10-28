# AWS

managed policy: AWSElasticDisasterRecoveryServiceRolePolicy

This policy allows AWS Elastic Disaster Recovery to manage AWS resources on your
behalf.

This policy is attached to the [AWSServiceRoleForElasticDisasterRecovery](using-service-linked-roles.md "using-service-linked-roles.md") role.

**Permissions details**

This policy includes permissions to do the following:

- ec2 – Retrieve and modify resources needed to support failover and failback of source servers
  and source networks.
- cloudwtach – Retrieve disk usage to allow cost optimization
- iam – Acquire the permissions required for recovery
- kms – Allow using encrypted volumes
- drs – Retrieve tags and set tags for DRS resources, create DRS
  resources on failover

**Permissions details**

To view the policy permission details see [AWSElasticDisasterRecoveryServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSElasticDisasterRecoveryServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSElasticDisasterRecoveryServiceRolePolicy.md") in the AWS Managed Policy Reference Guide.
