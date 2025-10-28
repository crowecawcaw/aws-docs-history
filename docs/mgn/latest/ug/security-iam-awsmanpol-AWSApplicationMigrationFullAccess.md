NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# AWS managed policy: AWSApplicationMigrationFullAccess

You can attach the `AWSApplicationMigrationFullAccess` policy to your IAM identities.

This policy provides permissions to all public APIs of AWS Application Migration Service (AWS MGN), as well as permissions to read KMS key, License Manager, Resource Groups, Elastic Load Balancing, IAM, and EC2 information.
This policy should only be granted to an administrator or a power-user.

###### Important

You must attach the [AWSApplicationMigrationFullAccess](../../../en_us/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationFullAccess.md "../../../en_us/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationFullAccess.md") and the
[AWSApplicationMigrationEC2Access](../../../en_us/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationEC2Access.md "../../../en_us/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationEC2Access.md") policies to your users and roles to enable them to
launch test and cutover instances and to complete a full migration cycle with AWS MGN.

**Permissions details**

To view the policy permission details see [AWSApplicationMigrationFullAccess](../../../aws-managed-policy/latest/reference/AWSApplicationMigrationFullAccess.md "../../../aws-managed-policy/latest/reference/AWSApplicationMigrationFullAccess.md") in the AWS Managed Policy Reference Guide.
