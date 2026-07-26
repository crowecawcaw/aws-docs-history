# AWS managed policies for Oracle Database@AWS

To add permissions to permission sets and roles, it's easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To
get started quickly, you can use our AWS managed policies. These policies cover common use
cases and are available in your AWS account. For more information about AWS managed
policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to
an AWS managed policy to support new features. This type of update affects all identities
(permission sets and roles) where the policy is attached. Services are most likely to update
an AWS managed policy when a new feature is launched or when new operations become
available. Services don't remove permissions from an AWS managed policy, so policy updates
don't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the `ReadOnlyAccess` AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

###### Topics

- [AWS managed policy: AmazonODBFullAccess](#odb-security-iam-awsmanpol-AmazonODBFullAccess "#odb-security-iam-awsmanpol-AmazonODBFullAccess")
- [AWS managed policy: AmazonODBServiceRolePolicy](#odb-security-iam-awsmanpol-AmazonODBServiceRolePolicy "#odb-security-iam-awsmanpol-AmazonODBServiceRolePolicy")
- [Additional permissions to add manually](#odb-security-iam-awsmanpol-additional-permissions "#odb-security-iam-awsmanpol-additional-permissions")

## AWS managed policy: AmazonODBFullAccess

You can attach the `AmazonODBFullAccess` policy to your IAM identities.
With this policy attached, you can create and manage all Oracle Database@AWS resources and related
service resources.

The policy includes permissions to:

- Create, view, update, delete, and list all Oracle Database@AWS resources, including
  Exadata infrastructure, Cloud VM clusters, Autonomous VM clusters, Autonomous
  Databases and their backups, DB nodes, DB servers, ODB networks, and ODB peering
  connections
- Manage the Autonomous Database lifecycle, including start, stop, reboot,
  shrink, switchover, failover, and restore
- Create and retrieve Autonomous Database wallet details
- List DB system shapes, Grid Infrastructure versions, system versions,
  Autonomous Database versions, and Autonomous Database character sets
- Manage resource policies and create outbound integrations
- Tag, untag, and list tags for Oracle Database@AWS resources
- View Amazon VPCs and Availability Zones
- Create, modify, and delete ODB network peering in Amazon EC2 (requires
  `aws:CalledVia` equal to `odb.amazonaws.com`)
- Create the service-linked role for Oracle Database@AWS and for VPC Lattice

This policy lacks the following permissions. Add each through your own customer managed
policy:

- Permissions for Amazon VPC Lattice and Amazon EC2 VPC endpoints that Oracle Database@AWS
  needs to provision or delete an ODB network. This set also includes the
  `ec2:DescribeVpcEndpoints` and
  `ec2:DescribeVpcEndpointAssociations` read permissions. For the
  specific actions and an example policy, see
  [VPC Lattice and VPC endpoints for service integrations](#odb-security-iam-awsmanpol-additional-vpclattice "#odb-security-iam-awsmanpol-additional-vpclattice").
- Permissions for managing the Oracle Database@AWS managed placement group
  in Amazon EC2 (create, attach, delete, and detach), which Oracle Database@AWS requires in Availability
  Zones that support managed cluster placement groups. For the specific actions and
  an example policy, see
  [Placement group management](#odb-security-iam-awsmanpol-additional-placementgroup "#odb-security-iam-awsmanpol-additional-placementgroup").
- Permissions for Amazon EC2 networking setup for ODB peering
  and DNS resolution. For the specific actions and an example policy, see
  [Amazon EC2 networking setup for ODB peering and DNS resolution](#odb-security-iam-awsmanpol-additional-ec2networking "#odb-security-iam-awsmanpol-additional-ec2networking").

To view the permissions for this policy, see
[AmazonODBFullAccess](../../../aws-managed-policy/latest/reference/AmazonODBFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonODBFullAccess.md") in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AmazonODBServiceRolePolicy

You can't attach the `AmazonODBServiceRolePolicy` policy to your IAM entities.
This policy is attached to a service-linked role that allows Oracle Database@AWS to perform actions on your behalf.
For more information, see [Using service-linked roles for Oracle Database@AWS](odb-SLR.md "odb-SLR.md").

To view more details about the policy, including the latest version of the JSON policy document, see
[AmazonODBServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonODBServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonODBServiceRolePolicy.md") in the _AWS Managed Policy Reference Guide_.

## Additional permissions to add manually

The managed policies on this page deliberately omit several permissions. These
permissions depend on services that do not yet support tight scoping or resource-tag
scoping at create time. Others apply only to specific use cases. Add them
through your own customer managed policies when your use case requires them. The examples
that follow use scoping consistent with the design of the managed policies. Replace account
IDs, AWS Regions, and resource names with your own values.

### Resource sharing with AWS Resource Access Manager (AWS RAM)

You need the following permissions when you share Oracle Exadata infrastructure or
ODB networks across AWS accounts using AWS Resource Access Manager (AWS RAM).
The Oracle Database@AWS managed policies do not include these permissions.

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

The Oracle Database@AWS managed policies do not grant access to the AWS RAM console. To view
resource shares in the AWS RAM console, attach the
`AWSResourceAccessManagerReadOnlyAccess` managed policy. To accept resource
shares in a trusted account, attach the
`AWSResourceAccessManagerResourceShareParticipantAccess` managed
policy.

### VPC Lattice and VPC endpoints for service integrations

With Oracle Database@AWS, you can connect your ODB network to AWS service integrations, such
as Amazon S3 backups, through VPC Lattice.

###### Permissions required for create and delete operations

Creating an ODB network provisions a default Oracle-managed backup integration to
Amazon S3. Deleting the ODB network removes that integration. You need these permissions when
you create and delete an ODB network, not only when you explicitly enable an
integration.

The managed policies do not grant these actions. Add them through your own customer
managed policy. The full-access policy trusts the
`vpc-lattice.amazonaws.com` service principal in its service-linked role
creation condition. With this trust in place, VPC Lattice can create its own
service-linked role.

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

In Availability Zones that support managed cluster placement groups, Oracle Database@AWS
creates a managed placement group when it provisions a resource. Resources include
ODB networks, Cloud VM clusters, and Autonomous VM clusters. Oracle Database@AWS attaches the
cluster resources to the placement group, then detaches and deletes it when you
remove the resource.

No managed policy grants the placement group actions. Add them through your own
customer managed policy. Without them, Oracle Database@AWS cannot create resources in any
Availability Zone that supports managed cluster placement groups.

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

You need the following caller permissions when you use a customer managed KMS
key to encrypt an Autonomous Database Serverless resource. You also need them when
you update the encryption key on an existing resource.

You must pass the encryption role to Oracle Database@AWS and describe the KMS key. Scope
`iam:PassRole` to the specific encryption role, and constrain it with the
`iam:PassedToService` condition. Scope `kms:DescribeKey` to the
specific key.

When you update the encryption key, Oracle Database@AWS resolves the VPC Lattice service
network association for your ODB network on your behalf. This operation requires
`vpc-lattice:GetServiceNetworkResourceAssociation`. Add these permissions
through your own customer managed policy.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowPassOdbEncryptionRole",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::`111122223333`:role/`odb-adbs-encryption-role`",
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
            "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`"
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

### Amazon EC2 networking setup for ODB peering and DNS resolution

You need the following permissions when you set up Amazon EC2 networking for ODB peering
and DNS resolution. The Oracle Database@AWS managed policies do not include these
permissions.

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
