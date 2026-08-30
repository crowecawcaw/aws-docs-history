NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# AWS managed policy: AWSApplicationMigrationConversionServerPolicy

This policy is attached to the AWS Transform MGN conversion server’s
instance role.

This policy allows the AWS Transform MGN conversion servers,
which are EC2 instances launched by AWS Transform MGN, to
communicate with the MGN service. An IAM role with this policy is attached (as
an EC2 Instance Profile) by MGN to the MGN Conversion Servers, which are
automatically launched and terminated by MGN, when needed. We do not recommend
that you attach this policy to your users or roles. MGN conversion servers are
used by AWS Transform MGN when users choose to launch test or
cutover instances using the MGN console, CLI, or API.

**Permissions details**

To view the policy permission details see [AWSApplicationMigrationConversionServerPolicy](../../../aws-managed-policy/latest/reference/AWSApplicationMigrationConversionServerPolicy.md "../../../aws-managed-policy/latest/reference/AWSApplicationMigrationConversionServerPolicy.md") in the AWS Managed Policy Reference Guide.
