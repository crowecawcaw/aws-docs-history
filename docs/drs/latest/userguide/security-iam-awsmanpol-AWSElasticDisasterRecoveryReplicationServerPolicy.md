# AWS managed policy:

AWSElasticDisasterRecoveryReplicationServerPolicy

This policy is attached to the AWS Elastic Disaster Recovery replication server’s instance role.

This policy allows the AWS Elastic Disaster Recovery (AWS DRS) replication servers, which are
Amazon EC2 instances launched by Elastic Disaster Recovery, to communicate with the
DRS service, and to create EBS snapshots in your AWS account. An IAM role with
this policy is attached (as an EC2 instance profile) by AWS DRS to the AWS DRS
replication servers which are automatically launched and terminated by AWS DRS,
as needed. AWS DRS replication servers are used to facilitate data replication
from your external servers to AWS, as part of the recovery process managed by
AWS DRS. We do not recommend that you attach this policy to your users or
roles.

**Permissions details**

To view the policy permission details see [AWSElasticDisasterRecoveryReplicationServerPolicy](../../../aws-managed-policy/latest/reference/AWSElasticDisasterRecoveryReplicationServerPolicy.md "../../../aws-managed-policy/latest/reference/AWSElasticDisasterRecoveryReplicationServerPolicy.md") in the AWS Managed Policy Reference Guide.
