NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# AWS managed policy:

AWSApplicationMigrationNetworkMigrationCustomResource

Allows modification of Transit Gateway resources created by Application Migration Service. You can attach the `AWSApplicationMigrationNetworkMigrationCustomResource` policy to your IAM identities.

This identity-based policy allows modification of Transit Gateway resources that were specifically created by Application Migration Service. The policy grants permission to modify Transit Gateways and their route tables,
but only if they are tagged with `[CreatedBy: AWSApplicationMigrationService]`. This restriction ensures that only resources created by the migration service can be modified, providing targeted control over
Transit Gateway infrastructure during migration processes. The policy grants the permissions necessary to complete these actions programmatically from the AWS API or AWS CLI.

The policy is particularly useful for:

- Managing Transit Gateway configurations during application migration
- Ensuring only migration service-created resources can be modified
- Maintaining control over network infrastructure changes during migration processes

**Permissions details**

To view the policy permission details see [AWSApplicationMigrationNetworkMigrationCustomResource](../../../aws-managed-policy/latest/reference/AWSApplicationMigrationNetworkMigrationCustomResource.md "../../../aws-managed-policy/latest/reference/AWSApplicationMigrationNetworkMigrationCustomResource.md") in the AWS Managed Policy Reference Guide.
