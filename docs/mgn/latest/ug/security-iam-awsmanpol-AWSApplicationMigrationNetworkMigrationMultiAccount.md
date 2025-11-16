NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# AWS managed policy:

AWSApplicationMigrationNetworkMigrationMultiAccount

You can attach the `AWSApplicationMigrationNetworkMigrationMultiAccount` policy to your IAM identities.

This identity-based policy enables AWS Application Migration Service (MGN) to create, modify, and manage network infrastructure components through CloudFormation. The policy grants permissions necessary for:

1. **Network Resource Management:** Creating and managing VPCs, subnets, route tables, and network ACLs; configuring Transit Gateways and their attachments; managing security groups and their rules; setting up NAT Gateways and Internet Gateways; handling network interfaces and elastic IPs
2. **CloudFormation Operations:** Creating and managing stacks with prefix [Nmd\*]; describing stack resources and events; updating and deleting stacks
3. **Resource Sharing:** Managing RAM (Resource Access Manager) resource shares; sharing Transit Gateways across accounts within the same organization
4. **Custom Resources:** Creating and managing Lambda functions with prefix [network-migration\*]; managing IAM roles with prefix [Nmd\*modifyTransitGateway\*]; creating and managing CloudWatch log groups
   The policy enforces security through resource tagging requirements (CreatedBy: AWSApplicationMigrationService), conditional checks ensuring operations are called via CloudFormation, organization-level controls for cross-account resource sharing, and specific resource-level permissions for critical network components.

This policy grants both programmatic and console access required for AWS Application Migration Service to orchestrate network infrastructure deployment and management through CloudFormation.

**Permissions details**

To view the policy permission details see [AWSApplicationMigrationNetworkMigrationMultiAccount](../../../aws-managed-policy/latest/reference/AWSApplicationMigrationNetworkMigrationMultiAccount.md "../../../aws-managed-policy/latest/reference/AWSApplicationMigrationNetworkMigrationMultiAccount.md") in the AWS Managed Policy Reference Guide.
