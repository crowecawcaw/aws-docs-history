

# AWS managed policies for Oracle Database@AWS
<a name="odb-security-iam-awsmanpol"></a>

To add permissions to permission sets and roles, it's easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (permission sets and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services don't remove permissions from an AWS managed policy, so policy updates don't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the `ReadOnlyAccess` AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

**Topics**
+ [AWS managed policy: AmazonODBReadOnlyAccess](#odb-security-iam-awsmanpol-AmazonODBReadOnlyAccess)
+ [AWS managed policy: AmazonODBFullAccess](#odb-security-iam-awsmanpol-AmazonODBFullAccess)
+ [AWS managed policy: AmazonODBExadataInfrastructureAdmin](#odb-security-iam-awsmanpol-AmazonODBExadataInfrastructureAdmin)
+ [AWS managed policy: AmazonODBNetworkAdmin](#odb-security-iam-awsmanpol-AmazonODBNetworkAdmin)
+ [AWS managed policy: AmazonODBAutonomousVmClusterAdmin](#odb-security-iam-awsmanpol-AmazonODBAutonomousVmClusterAdmin)
+ [AWS managed policy: AmazonODBAutonomousDatabaseAdmin](#odb-security-iam-awsmanpol-AmazonODBAutonomousDatabaseAdmin)
+ [AWS managed policy: AmazonODBExadataVmClusterAdmin](#odb-security-iam-awsmanpol-AmazonODBExadataVmClusterAdmin)
+ [AWS managed policy: AmazonODBExascaleStorageVaultAdmin](#odb-security-iam-awsmanpol-AmazonODBExascaleStorageVaultAdmin)
+ [AWS managed policy: AmazonODBExascaleVmClusterAdmin](#odb-security-iam-awsmanpol-AmazonODBExascaleVmClusterAdmin)
+ [AWS managed policy: AmazonODBServiceRolePolicy](#odb-security-iam-awsmanpol-AmazonODBServiceRolePolicy)
+ [Additional permissions to add manually](#odb-security-iam-awsmanpol-additional-permissions)

## AWS managed policy: AmazonODBReadOnlyAccess
<a name="odb-security-iam-awsmanpol-AmazonODBReadOnlyAccess"></a>

You can attach the `AmazonODBReadOnlyAccess` policy to your IAM identities. With this policy attached, you can view all Oracle Database@AWS resources and related service resources.

The policy includes permissions to:
+ View and list all Oracle Database@AWS resources, including Exadata infrastructure, Exadata VM cluster resources, Autonomous VM cluster resources, Exascale Storage Vault resources, Exascale VM cluster resources, Autonomous Databases and their backups, DB nodes, DB servers, ODB networks, and ODB peering connections
+ View unallocated resources for Exadata infrastructure
+ List DB system shapes, flex components, Grid Infrastructure versions, Grid Infrastructure minor versions, system versions, Autonomous Database versions, and Autonomous Database character sets
+ View resource policies and list tags for Oracle Database@AWS resources
+ View Amazon VPCs and Availability Zones

This policy includes only read-only actions. It does not create, update, or delete resources.

To view the permissions for this policy, see [AmazonODBReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonODBReadOnlyAccess.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AmazonODBFullAccess
<a name="odb-security-iam-awsmanpol-AmazonODBFullAccess"></a>

You can attach the `AmazonODBFullAccess` policy to your IAM identities. With this policy attached, you can create and manage all Oracle Database@AWS resources and related service resources.

The policy includes permissions to:
+ Create, view, update, delete, and list all Oracle Database@AWS resources, including Exadata infrastructure, Exadata VM cluster resources, Autonomous VM cluster resources, Exascale Storage Vault resources, Exascale VM cluster resources, Autonomous Databases and their backups, DB nodes, DB servers, ODB networks, and ODB peering connections
+ Attach and detach virtual machines for Exascale VM cluster resources
+ Associate and disassociate IAM roles for VM cluster resources
+ Manage the Autonomous Database lifecycle, including start, stop, reboot, shrink, switchover, failover, and restore
+ Create and retrieve Autonomous Database wallet details
+ List DB system shapes, flex components, Grid Infrastructure versions, Grid Infrastructure minor versions, system versions, Autonomous Database versions, and Autonomous Database character sets
+ Manage resource policies
+ Create and update outbound integrations
+ Create, update, and delete grant shares, which share Oracle Database@AWS entitlements with other AWS accounts through AWS License Manager
+ Tag, untag, and list tags for Oracle Database@AWS resources
+ View Amazon VPCs and Availability Zones
+ Create, modify, and delete ODB network peering in Amazon EC2
+ Create the service-linked role for Oracle Database@AWS and for VPC Lattice

This policy lacks the following permissions. Add each through your own customer managed policy:
+ Permissions for Amazon VPC Lattice and Amazon EC2 VPC endpoints that Oracle Database@AWS needs to provision or delete an ODB network. This set also includes the `ec2:DescribeVpcEndpoints` and `ec2:DescribeVpcEndpointAssociations` read permissions. For the specific actions and an example policy, see [VPC Lattice and VPC endpoints for service integrations](#odb-security-iam-awsmanpol-additional-vpclattice).
+ Permissions for managing the Oracle Database@AWS managed placement group in Amazon EC2 (create, attach, delete, and detach), which Oracle Database@AWS requires in Availability Zones that support managed cluster placement groups. For the specific actions and an example policy, see [Placement group management](#odb-security-iam-awsmanpol-additional-placementgroup).
+ Permissions for Amazon EC2 networking setup for ODB peering and DNS resolution. For the specific actions and an example policy, see [Amazon EC2 networking setup for ODB peering and DNS resolution](#odb-security-iam-awsmanpol-additional-ec2networking).
+ Permissions for the `iam:PassRole` action, which passes an IAM role to Oracle Database@AWS when you associate that role with a VM cluster. This use of `iam:PassRole` is separate from the one required for customer managed AWS Key Management Service encryption of an Autonomous Database Serverless resource. Scope it to the role ARNs that you choose, and constrain it with the `iam:PassedToService` condition set to `odb.amazonaws.com`. Without this action, requests to associate an IAM role fail. Disassociating an IAM role doesn't require this action. For the specific actions and an example policy, see [IAM role association for VM cluster resources](#odb-security-iam-awsmanpol-additional-iamrole).
+ Permissions for the `iam:PassRole` action and for describing the AWS Key Management Service key. You need these actions when you update the encryption key on an existing Autonomous Database Serverless resource to use a customer managed AWS Key Management Service key. For the specific actions and an example policy, see [Customer-managed KMS encryption for Autonomous Database Serverless](#odb-security-iam-awsmanpol-additional-kms).
+ Permissions for the `secretsmanager:DescribeSecret` action for the Autonomous Database Serverless AWS Secrets Manager integration. You need this action only when you supply a customer managed AWS Secrets Manager secret for an Autonomous Database Serverless admin password or wallet password. The integration also requires `iam:PassRole` for the role that you supply with the secret. For the specific actions and an example policy, see [AWS Secrets Manager integration for Autonomous Database Serverless](#odb-security-iam-awsmanpol-additional-secretsmanager).

To view the permissions for this policy, see [AmazonODBFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonODBFullAccess.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AmazonODBExadataInfrastructureAdmin
<a name="odb-security-iam-awsmanpol-AmazonODBExadataInfrastructureAdmin"></a>

You can attach the `AmazonODBExadataInfrastructureAdmin` policy to your IAM identities. With this policy attached, you can create and manage Oracle Exadata infrastructure resources. You can also list Exadata VM clusters and Autonomous VM clusters, which are visible in the Oracle Database@AWS console.

The policy includes permissions to:
+ Initialize the Oracle Database@AWS service
+ Create, view, update, delete, and list Exadata infrastructure resources
+ View unallocated resources for Exadata infrastructure
+ List Exadata VM clusters and Autonomous VM clusters
+ View and list DB servers
+ List flex components for Exadata infrastructure
+ Put, get, and delete resource policies
+ View Availability Zones
+ Tag, untag, and list tags for Exadata infrastructure resources
+ Create the service-linked role for Oracle Database@AWS

To view the permissions for this policy, see [AmazonODBExadataInfrastructureAdmin](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonODBExadataInfrastructureAdmin.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AmazonODBNetworkAdmin
<a name="odb-security-iam-awsmanpol-AmazonODBNetworkAdmin"></a>

You can attach the `AmazonODBNetworkAdmin` policy to your IAM identities. With this policy attached, you can set up and manage networking resources for Oracle Database@AWS.

The policy includes permissions to:
+ Initialize the Oracle Database@AWS service
+ Create, view, update, delete, and list ODB network resources
+ Create, view, update, delete, and list ODB peering connections
+ Put, get, and delete resource policies
+ Tag, untag, and list tags for ODB network and ODB peering connection resources
+ View Amazon VPCs and Availability Zones
+ Create, modify, and delete ODB network peering in Amazon EC2
+ Create the service-linked role for Oracle Database@AWS and for VPC Lattice

This policy lacks the following permissions. Add each through your own customer managed policy:
+ Permissions for Amazon VPC Lattice and Amazon EC2 VPC endpoints that Oracle Database@AWS needs to provision or delete an ODB network. This set also includes the `ec2:DescribeVpcEndpoints` and `ec2:DescribeVpcEndpointAssociations` read permissions. For the specific actions and an example policy, see [VPC Lattice and VPC endpoints for service integrations](#odb-security-iam-awsmanpol-additional-vpclattice).
+ Permissions for managing the Oracle Database@AWS managed placement group in Amazon EC2 (create, attach, delete, and detach), which Oracle Database@AWS requires in Availability Zones that support managed cluster placement groups. For the specific actions and an example policy, see [Placement group management](#odb-security-iam-awsmanpol-additional-placementgroup).
+ Permissions for Amazon EC2 networking setup for ODB peering and DNS resolution. For the specific actions and an example policy, see [Amazon EC2 networking setup for ODB peering and DNS resolution](#odb-security-iam-awsmanpol-additional-ec2networking).

To view the permissions for this policy, see [AmazonODBNetworkAdmin](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonODBNetworkAdmin.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AmazonODBAutonomousVmClusterAdmin
<a name="odb-security-iam-awsmanpol-AmazonODBAutonomousVmClusterAdmin"></a>

You can attach the `AmazonODBAutonomousVmClusterAdmin` policy to your IAM identities. With this policy attached, you can manage Autonomous VM cluster resources. You can also view Exadata infrastructure and ODB network resources, which are required dependencies for Autonomous VM clusters.

The policy includes permissions to:
+ Initialize the Oracle Database@AWS service
+ Create, view, delete, and list Autonomous VM clusters
+ Associate and disassociate IAM roles for Autonomous VM cluster resources
+ View Exadata infrastructure resources and their unallocated resources
+ List Autonomous virtual machines
+ View and list DB servers
+ View and list ODB network resources
+ List DB system shapes, Grid Infrastructure versions, and system versions
+ List tags for Oracle Database@AWS resources
+ View Availability Zones
+ Tag and untag Autonomous VM cluster resources
+ Create and update outbound integrations for Autonomous VM cluster resources

This policy lacks the following permissions. Add each through your own customer managed policy:
+ Permissions for the `iam:PassRole` action, which passes an IAM role to Oracle Database@AWS when you associate that role with an Autonomous VM cluster. Scope it to the role ARNs that you choose, and constrain it with the `iam:PassedToService` condition set to `odb.amazonaws.com`. Without this action, requests to associate an IAM role fail. Disassociating an IAM role doesn't require this action. For the specific actions and an example policy, see [IAM role association for VM cluster resources](#odb-security-iam-awsmanpol-additional-iamrole).

To view the permissions for this policy, see [AmazonODBAutonomousVmClusterAdmin](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonODBAutonomousVmClusterAdmin.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AmazonODBAutonomousDatabaseAdmin
<a name="odb-security-iam-awsmanpol-AmazonODBAutonomousDatabaseAdmin"></a>

You can attach the `AmazonODBAutonomousDatabaseAdmin` policy to your IAM identities. With this policy attached, you can manage Autonomous Database Serverless resources and their backups. You can also view the ODB network resources that an Autonomous Database Serverless resource attaches to.

The policy includes permissions to:
+ Initialize the Oracle Database@AWS service
+ Create, view, update, delete, and list Autonomous Databases, including their clones and peers
+ Manage the Autonomous Database lifecycle, including start, stop, reboot, shrink, switchover, failover, and restore
+ Create and retrieve Autonomous Database wallet details
+ Create, view, update, delete, and list Autonomous Database backups
+ View and list ODB network resources
+ List Autonomous Database versions and Autonomous Database character sets
+ List tags for Oracle Database@AWS resources
+ View Availability Zones
+ Create the service-linked role for Oracle Database@AWS
+ Tag and untag Autonomous Database and Autonomous Database backup resources
+ Create and update outbound integrations for Autonomous Database resources

This policy lacks the following permissions. Add each through your own customer managed policy:
+ Permissions for the `iam:PassRole` action and for describing the AWS Key Management Service key. You need these actions when you update the encryption key on an existing Autonomous Database Serverless resource to use a customer managed AWS Key Management Service key. For the specific actions and an example policy, see [Customer-managed KMS encryption for Autonomous Database Serverless](#odb-security-iam-awsmanpol-additional-kms).
+ Permissions for the `secretsmanager:DescribeSecret` action for the Autonomous Database Serverless AWS Secrets Manager integration. You need this action only when you supply a customer managed AWS Secrets Manager secret for an Autonomous Database Serverless admin password or wallet password. The integration also requires `iam:PassRole` for the role that you supply with the secret. For the specific actions and an example policy, see [AWS Secrets Manager integration for Autonomous Database Serverless](#odb-security-iam-awsmanpol-additional-secretsmanager).

To view the permissions for this policy, see [AmazonODBAutonomousDatabaseAdmin](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonODBAutonomousDatabaseAdmin.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AmazonODBExadataVmClusterAdmin
<a name="odb-security-iam-awsmanpol-AmazonODBExadataVmClusterAdmin"></a>

You can attach the `AmazonODBExadataVmClusterAdmin` policy to your IAM identities. With this policy attached, you can manage Exadata VM cluster resources and their DB nodes. You can also view Exadata infrastructure and ODB network resources, which are required dependencies for Exadata VM cluster resources.

The policy includes permissions to:
+ Initialize the Oracle Database@AWS service
+ View and list Exadata infrastructure resources and their unallocated resources
+ Create, view, delete, and list Exadata VM cluster resources
+ Associate and disassociate IAM roles for Exadata VM cluster resources
+ Create, view, reboot, start, stop, delete, and list DB nodes
+ View and list DB servers
+ View and list ODB network resources
+ List DB system shapes, flex components, Grid Infrastructure versions, and system versions
+ List tags for Oracle Database@AWS resources
+ View Availability Zones
+ Tag and untag Exadata VM cluster and DB node resources
+ Create and update outbound integrations for Exadata VM cluster resources

This policy lacks the following permissions. Add each through your own customer managed policy:
+ Permissions for the `iam:PassRole` action, which passes an IAM role to Oracle Database@AWS when you associate that role with an Exadata VM cluster. Scope it to the role ARNs that you choose, and constrain it with the `iam:PassedToService` condition set to `odb.amazonaws.com`. Without this action, requests to associate an IAM role fail. Disassociating an IAM role doesn't require this action. For the specific actions and an example policy, see [IAM role association for VM cluster resources](#odb-security-iam-awsmanpol-additional-iamrole).

To view the permissions for this policy, see [AmazonODBExadataVmClusterAdmin](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonODBExadataVmClusterAdmin.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AmazonODBExascaleStorageVaultAdmin
<a name="odb-security-iam-awsmanpol-AmazonODBExascaleStorageVaultAdmin"></a>

You can attach the `AmazonODBExascaleStorageVaultAdmin` policy to your IAM identities. With this policy attached, you can create and manage Exascale Storage Vault resources. You can also list Exascale VM cluster resources and view the DB servers that use an Exascale Storage Vault.

The policy includes permissions to:
+ Initialize the Oracle Database@AWS service
+ Create, view, update, delete, and list Exascale Storage Vault resources
+ List Exascale VM cluster resources
+ View and list DB servers
+ List DB system shapes and flex components
+ Put, get, and delete resource policies
+ List tags for Oracle Database@AWS resources
+ View Availability Zones
+ Create the service-linked role for Oracle Database@AWS
+ Tag and untag Exascale Storage Vault resources

To view the permissions for this policy, see [AmazonODBExascaleStorageVaultAdmin](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonODBExascaleStorageVaultAdmin.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AmazonODBExascaleVmClusterAdmin
<a name="odb-security-iam-awsmanpol-AmazonODBExascaleVmClusterAdmin"></a>

You can attach the `AmazonODBExascaleVmClusterAdmin` policy to your IAM identities. With this policy attached, you can manage Exascale VM cluster resources and their DB nodes. You can also view the Exascale Storage Vault and ODB network resources that an Exascale VM cluster attaches to.

The policy includes permissions to:
+ Initialize the Oracle Database@AWS service
+ View and list Exascale Storage Vault resources
+ Create, view, update, delete, and list Exascale VM cluster resources
+ Attach and detach virtual machines for Exascale VM cluster resources
+ Associate and disassociate IAM roles for Exascale VM cluster resources
+ Create, view, reboot, start, stop, delete, and list DB nodes
+ View and list DB servers
+ View and list ODB network resources
+ List DB system shapes, flex components, Grid Infrastructure versions, Grid Infrastructure minor versions, and system versions
+ List tags for Oracle Database@AWS resources
+ View Availability Zones
+ Tag and untag Exascale VM cluster and DB node resources
+ Create and update outbound integrations for Exascale VM cluster resources

This policy lacks the following permissions. Add each through your own customer managed policy:
+ Permissions for the `iam:PassRole` action, which passes an IAM role to Oracle Database@AWS when you associate that role with an Exascale VM cluster. Scope it to the role ARNs that you choose, and constrain it with the `iam:PassedToService` condition set to `odb.amazonaws.com`. Without this action, requests to associate an IAM role fail. Disassociating an IAM role doesn't require this action. For the specific actions and an example policy, see [IAM role association for VM cluster resources](#odb-security-iam-awsmanpol-additional-iamrole).

To view the permissions for this policy, see [AmazonODBExascaleVmClusterAdmin](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonODBExascaleVmClusterAdmin.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AmazonODBServiceRolePolicy
<a name="odb-security-iam-awsmanpol-AmazonODBServiceRolePolicy"></a>

You can't attach the `AmazonODBServiceRolePolicy` policy to your IAM entities. This policy is attached to a service-linked role that allows Oracle Database@AWS to perform actions on your behalf. For more information, see [Using service-linked roles for Oracle Database@AWS](odb-SLR.md).

To view more details about the policy, including the latest version of the JSON policy document, see [AmazonODBServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonODBServiceRolePolicy.html) in the *AWS Managed Policy Reference Guide*.

## Additional permissions to add manually
<a name="odb-security-iam-awsmanpol-additional-permissions"></a>

The managed policies on this page deliberately omit several permissions. These permissions depend on services that do not yet support tight scoping or resource-tag scoping at create time. Others apply only to specific use cases. Add them through your own customer managed policies when your use case requires them. The examples that follow use scoping consistent with the design of the managed policies. Replace account IDs, AWS Regions, and resource names with your own values.

### Resource sharing with AWS Resource Access Manager (AWS RAM)
<a name="odb-security-iam-awsmanpol-additional-ram"></a>

You need the following permissions when you share Oracle Exadata infrastructure or ODB networks across AWS accounts using AWS Resource Access Manager (AWS RAM). The Oracle Database@AWS managed policies do not include these permissions.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowOdbResourceSharing",
            "Effect": "Allow",
            "Action": [
                "ram:CreateResourceShare",
                "ram:AssociateResourceShare",
                "ram:DisassociateResourceShare"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "ram:RequestedResourceType": [
                        "odb:cloud-exadata-infrastructure",
                        "odb:odb-network"
                    ]
                }
            }
        }
    ]
}
```

The Oracle Database@AWS managed policies do not grant access to the AWS RAM console. To view resource shares in the AWS RAM console, attach the `AWSResourceAccessManagerReadOnlyAccess` managed policy. To accept resource shares in a trusted account, attach the `AWSResourceAccessManagerResourceShareParticipantAccess` managed policy.

### VPC Lattice and VPC endpoints for service integrations
<a name="odb-security-iam-awsmanpol-additional-vpclattice"></a>

With Oracle Database@AWS, you can connect your ODB network to AWS service integrations, such as Amazon S3 backups, through VPC Lattice.

**Permissions required for create and delete operations**  
Creating an ODB network provisions a default Oracle-managed backup integration to Amazon S3. Deleting the ODB network removes that integration. You need these permissions when you create and delete an ODB network, not only when you explicitly enable an integration.

The managed policies do not grant these actions. Add them through your own customer managed policy. The full-access policy trusts the `vpc-lattice.amazonaws.com` service principal in its service-linked role creation condition. With this trust in place, VPC Lattice can create its own service-linked role.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowOdbVpcLatticeActions",
            "Effect": "Allow",
            "Action": [
                "vpc-lattice:CreateServiceNetwork",
                "vpc-lattice:DeleteServiceNetwork",
                "vpc-lattice:GetServiceNetwork",
                "vpc-lattice:CreateServiceNetworkResourceAssociation",
                "vpc-lattice:DeleteServiceNetworkResourceAssociation",
                "vpc-lattice:GetServiceNetworkResourceAssociation",
                "vpc-lattice:CreateResourceGateway",
                "vpc-lattice:DeleteResourceGateway",
                "vpc-lattice:GetResourceGateway",
                "vpc-lattice:CreateServiceNetworkVpcEndpointAssociation"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowOdbVpcEndpointManagement",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateVpcEndpoint",
                "ec2:DeleteVpcEndpoints",
                "ec2:CreateTags",
                "ec2:DescribeVpcEndpoints",
                "ec2:DescribeVpcEndpointAssociations"
            ],
            "Resource": "*"
        }
    ]
}
```

### Placement group management
<a name="odb-security-iam-awsmanpol-additional-placementgroup"></a>

In Availability Zones that support managed cluster placement groups, Oracle Database@AWS creates a managed placement group when it provisions a resource. Resources include ODB networks, Exadata VM clusters, and Autonomous VM clusters. Oracle Database@AWS attaches the cluster resources to the placement group, then detaches and deletes it when you remove the resource.

No managed policy grants the placement group actions. Add them through your own customer managed policy. Without them, Oracle Database@AWS cannot create resources in any Availability Zone that supports managed cluster placement groups.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowOdbManagedPlacementGroup",
            "Effect": "Allow",
            "Action": [
                "ec2:CreatePlacementGroup",
                "ec2:AttachResourcesToPlacementGroup",
                "ec2:DeletePlacementGroup",
                "ec2:DetachResourcesFromPlacementGroup"
            ],
            "Resource": "*"
        }
    ]
}
```

### Customer-managed KMS encryption for Autonomous Database Serverless
<a name="odb-security-iam-awsmanpol-additional-kms"></a>

You need the following caller permissions when you update the encryption key on an existing Autonomous Database Serverless resource to use a customer managed KMS key. Using a customer managed KMS key to encrypt an Autonomous Database Serverless resource on creation is currently not supported.

You must pass the encryption role to Oracle Database@AWS and describe the KMS key. Scope `iam:PassRole` to the specific encryption role, and constrain it with the `iam:PassedToService` condition. Scope `kms:DescribeKey` to the specific key.

When you update the encryption key, Oracle Database@AWS resolves the VPC Lattice service network association for your ODB network on your behalf. This operation requires `vpc-lattice:GetServiceNetworkResourceAssociation`. Add these permissions through your own customer managed policy.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowPassOdbEncryptionRole",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{111122223333}}:role/{{odb-adbs-encryption-role}}",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "odb.amazonaws.com"
                }
            }
        },
        {
            "Sid": "AllowDescribeOdbEncryptionKey",
            "Effect": "Allow",
            "Action": "kms:DescribeKey",
            "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}}"
        },
        {
            "Sid": "AllowOdbEncryptionKeyVpcLatticeRead",
            "Effect": "Allow",
            "Action": "vpc-lattice:GetServiceNetworkResourceAssociation",
            "Resource": "*"
        }
    ]
}
```

### AWS Secrets Manager integration for Autonomous Database Serverless
<a name="odb-security-iam-awsmanpol-additional-secretsmanager"></a>

To use the Autonomous Database Serverless AWS Secrets Manager integration, grant the following caller permissions.

Oracle Database@AWS resolves the secret with your caller permissions, so you must grant `secretsmanager:DescribeSecret` on that secret. You need this action only for this integration. This requirement applies when you create or update an Autonomous Database Serverless resource with a customer managed secret for the admin password. It also applies when you create a wallet for an Autonomous Database Serverless resource with a customer managed secret for the wallet password.

You must also pass the IAM role that you supply with the secret. Scope `iam:PassRole` to that role, and constrain it with the `iam:PassedToService` condition set to `odb.amazonaws.com`. The `AmazonODBFullAccess` and `AmazonODBAutonomousDatabaseAdmin` policies don't grant either action. Add both actions through your own customer managed policy.

The following example policy grants only these two actions. For a broader identity-based policy that already includes the `AllowSecretsManagerAccess` statement, see [Allow users to provision Oracle Database@AWS resources](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-full-access).

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowSecretsManagerAccess",
            "Effect": "Allow",
            "Action": "secretsmanager:DescribeSecret",
            "Resource": "arn:aws:secretsmanager:{{us-east-1}}:{{111122223333}}:secret:{{odb-adbs-admin-password-a1b2c3}}"
        },
        {
            "Sid": "AllowPassAdbsSecretAccessRole",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{111122223333}}:role/{{odb-adbs-secret-access-role}}",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "odb.amazonaws.com"
                }
            }
        }
    ]
}
```

### IAM role association for VM cluster resources
<a name="odb-security-iam-awsmanpol-additional-iamrole"></a>

You need the following caller permission when you associate an IAM role with an Exadata VM cluster, an Exascale VM cluster, or an Autonomous VM cluster.

The VM cluster administrator policies and the `AmazonODBFullAccess` policy already grant the `odb:AssociateIamRoleToResource` actions. They don't grant `iam:PassRole`. You must pass the IAM role to Oracle Database@AWS for association, so add this action through your own customer managed policy. Scope it to the role ARNs that you choose, and constrain it with the `iam:PassedToService` condition set to `odb.amazonaws.com`. Without this action, requests to associate an IAM role fail. Disassociating an IAM role doesn't require this action.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowPassOdbResourceRole",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{111122223333}}:role/{{odb-resource-role}}",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "odb.amazonaws.com"
                }
            }
        }
    ]
}
```

### Amazon EC2 networking setup for ODB peering and DNS resolution
<a name="odb-security-iam-awsmanpol-additional-ec2networking"></a>

You need the following permissions when you set up Amazon EC2 networking for ODB peering and DNS resolution. The Oracle Database@AWS managed policies do not include these permissions.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowOdbNetworkingSetup",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeRouteTables",
                "ec2:CreateRoute",
                "route53resolver:CreateResolverEndpoint",
                "route53resolver:CreateResolverRule",
                "route53resolver:AssociateResolverRule"
            ],
            "Resource": "*"
        }
    ]
}
```