NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# AWS managed policy: AWSApplicationMigrationMGHAccess

This policy allows AWS Application Migration Service (AWS MGN) to send metadata about the
progress of servers being migrated using AWS MGN to AWS Migration Hub (MGH). AWS MGN automatically
creates an IAM role with this policy attached and assumes this role. We do not recommend
that you attach this policy to your users or roles. Migration-progress data is only
sent after the AWS "home region” is set in AWS MGH. If the Home AWS Region is different than
the AWS Region into which a server is being migrated, this data will be sent cross-region.
To stop AWS MGN from sending this metadata to AWS MGH, detach it from your users or
roles.

**Permissions details**

To view the policy permission details see [AWSApplicationMigrationMGHAccess](../../../aws-managed-policy/latest/reference/AWSApplicationMigrationMGHAccess.md "../../../aws-managed-policy/latest/reference/AWSApplicationMigrationMGHAccess.md") in the AWS Managed Policy Reference Guide.
