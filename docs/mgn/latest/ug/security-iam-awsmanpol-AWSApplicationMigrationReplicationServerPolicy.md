NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# AWS managed policy:

AWSApplicationMigrationReplicationServerPolicy

This policy is attached to the AWS Application Migration Service replication server’s
instance role.

This policy allows the AWS Application Migration Service (AWS MGN) Replication
Servers, which are EC2 instances launched by AWS Application Migration Service - to
communicate with the AWS MGN service, and to create EBS snapshots in your AWS
account. An IAM role with this policy is attached (as an EC2 Instance Profile)
by AWS Application Migration Service to the AWS MGN replication servers which are
automatically launched and terminated by AWS MGN, as needed. AWS MGN Replication Servers
are used to facilitate data replication from your external servers to AWS, as
part of the migration process managed using AWS MGN. We do not recommend that you
attach this policy to your users or roles.

**Permissions details**

To view the policy permission details see [AWSApplicationMigrationReplicationServerPolicy](../../../aws-managed-policy/latest/reference/AWSApplicationMigrationReplicationServerPolicy.md "../../../aws-managed-policy/latest/reference/AWSApplicationMigrationReplicationServerPolicy.md") in the AWS Managed Policy Reference Guide.
