

# AWS managed policy: AWSElasticDisasterRecoveryServiceRolePolicy
<a name="security-iam-awsmanpol-AWSElasticDisasterRecoveryServiceRolePolicy"></a>

This policy allows AWS Elastic Disaster Recovery to manage AWS resources on your behalf. 

This policy is attached to the [AWSServiceRoleForElasticDisasterRecovery](using-service-linked-roles.md) role.

 **Permissions details** 

This policy includes permissions to do the following:
+ ec2 – Retrieve and modify resources needed to support failover and failback of source servers and source networks.
+ cloudwatch – Retrieve disk usage to allow cost optimization
+  iam – Acquire the permissions required for recovery
+  kms – Allow using encrypted volumes
+ drs – Retrieve tags and set tags for DRS resources, create DRS resources on failover

 **Permissions details** 

To view the policy permission details see [AWSElasticDisasterRecoveryServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticDisasterRecoveryServiceRolePolicy.html) in the AWS Managed Policy Reference Guide.