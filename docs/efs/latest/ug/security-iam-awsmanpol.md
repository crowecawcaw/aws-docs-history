# AWS managed policies for Amazon EFS

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed policy: AWSServiceRoleForAmazonElasticFileSystem

Amazon EFS uses the service-linked role named `AWSServiceRoleForAmazonElasticFileSystem` to allow
Amazon EFS to manage AWS resources on your behalf. This role trusts the
`elasticfilesystem.amazonaws.com` service to assume the role. For more
information, see [Using service-linked roles for Amazon EFS](using-service-linked-roles.md "using-service-linked-roles.md").

## AWS managed policy: AmazonElasticFileSystemFullAccess

You can attach the `AmazonElasticFileSystemFullAccess` policy to your IAM identities.

This policy grants administrative permissions that allow full access to Amazon EFS and
access to related AWS services via the AWS Management Console.

**Permissions details**

This policy includes the following permissions.

- `elasticfilesystem` – Allows principals to perform all actions
  in the Amazon EFS console. It also allows principals to create
  (`elasticfilesystem:Backup`) and restore
  (`elasticfilesystem:Restore`) backups using AWS Backup.
- `cloudwatch` – Allows principals to describe Amazon CloudWatch file
  system metrics and alarms for a metric in the Amazon EFS console.
- `ec2` – Allows principals to create, delete, and describe
  network interfaces, describe and modify network interface attributes, describe
  Availability Zones, security groups, subnets, virtual private clouds (VPCs) and VPC
  attributes associated with an EFS file system in the Amazon EFS
  console.
- `kms` – Allows principals to list aliases for AWS Key Management Service (AWS KMS)
  keys and to describe KMS keys in the Amazon EFS console.
- `iam` – Grants permission to create a service linked role that
  allows Amazon EFS to manage AWS resources on the user's behalf.
- `iam:PassRole` – Grants permission to pass an IAM role to
  Amazon EFS.

To view the permissions for this policy, see [AmazonElasticFileSystemFullAccess](../../../aws-managed-policy/latest/reference/AmazonElasticFileSystemFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonElasticFileSystemFullAccess.md") in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AmazonElasticFileSystemReadOnlyAccess

You can attach the `AmazonElasticFileSystemReadOnlyAccess` policy to your IAM identities.

This policy grants read only access to Amazon EFS via the AWS Management Console.

**Permissions details**

This policy includes the following permissions.

- `elasticfilesystem` – Allows principals to describe attributes
  of Amazon EFS file systems, including account preferences, backup and file system
  policies, lifecycle configuration, mount targets and their security groups,
  tags, and access points in the Amazon EFS console.
- `cloudwatch` – Allows principals to retrieve CloudWatch metrics and
  describe alarms for metrics in the Amazon EFS console.
- `ec2` – Allows principals to view Availability Zones, network
  interfaces and their attributes, security groups, subnets, VPCs and their
  attributes in the Amazon EFS console.
- `kms` – Allows principals to list aliases for AWS KMS keys in the
  Amazon EFS console.

To view the permissions for this policy, see [AmazonElasticFileSystemReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonElasticFileSystemReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonElasticFileSystemReadOnlyAccess.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed policy: AmazonElasticFileSystemClientFullAccess

You can attach the `AmazonElasticFileSystemClientFullAccess` policy to an IAM entity.

This policy grants read and write client access to EFS file systems. This
policy allows NFS clients to mount, read and write to EFS file
systems.

To view the permissions for this policy, see [AmazonElasticFileSystemClientFullAccess](../../../aws-managed-policy/latest/reference/AmazonElasticFileSystemClientFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonElasticFileSystemClientFullAccess.md") in the
_AWS Managed Policy Reference Guide_.

## AWS managed policy: AmazonElasticFileSystemClientReadWriteAccess

You can attach the `AmazonElasticFileSystemClientReadWriteAccess` policy to
an IAM entity.

This policy grants read and write client access to EFS file systems. This
policy allows NFS clients to mount, read and write to EFS file
systems.

To view the permissions for this policy, see [AmazonElasticFileSystemClientReadWriteAccess](../../../aws-managed-policy/latest/reference/AmazonElasticFileSystemClientReadWriteAccess.md "../../../aws-managed-policy/latest/reference/AmazonElasticFileSystemClientReadWriteAccess.md") in the _AWS Managed
Policy Reference Guide_.

## Amazon EFS updates to AWS managed

policies

View details about updates to AWS managed policies for Amazon EFS since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the Amazon EFS [Document history](document-history.md "document-history.md") page.

| Change                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                    | Date              |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Update to an existing policy           | Policy: [AmazonElasticFileSystemFullAccess](#security-iam-awsmanpol-AmazonElasticFileSystemFullAccess "#security-iam-awsmanpol-AmazonElasticFileSystemFullAccess")<br>Amazon EFS added the following:<br>• `ReplicationRead` and `ReplicationWrite` to give permission to read<br>and write file system data for replication.<br>• `iam:PassRole` to give permission for Amazon EFS to create<br>replication configurations.                   | November 7, 2024  |
| Update to an existing policy           | Policy: [AmazonElasticFileSystemServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions")<br>Amazon EFS added `ReplicationRead` and `ReplicationWrite` to give<br>permission to read and write file system data for replication.                                                                                                                                                       | November 7, 2024  |
| Update to an existing policy           | Policy: [AmazonElasticFileSystemReadOnlyAccess](#security-iam-awsmanpol-AmazonElasticFileSystemReadOnlyAccess "#security-iam-awsmanpol-AmazonElasticFileSystemReadOnlyAccess")<br>Amazon EFS added the `ReplicationRead` action to give permission to<br>read file system data for replication.                                                                                                                                                | November 7, 2024  |
| Update to an existing policy           | Policy: [AmazonElasticFileSystemReadOnlyAccess](#security-iam-awsmanpol-AmazonElasticFileSystemReadOnlyAccess "#security-iam-awsmanpol-AmazonElasticFileSystemReadOnlyAccess")<br>Amazon EFS added new permissions that give source and destination<br>accounts access to file systems for cross-account replications.                                                                                                                         | August 7, 2024    |
| Update to an existing policy           | Policy: [AmazonElasticFileSystemFullAccess](#security-iam-awsmanpol-AmazonElasticFileSystemFullAccess "#security-iam-awsmanpol-AmazonElasticFileSystemFullAccess")Amazon EFS added a new<br>permission to allow principals to disable and enable protection on a<br>file system. The permissions are required to allow Amazon EFS to<br>replicate to an existing file system.                                                                  | November 27, 2023 |
| Update to an existing policy           | Policy: [AmazonElasticFileSystemServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions")<br>Amazon EFS added new permissions to allow principals to create,<br>describe, and delete Amazon EFS replications, and to create Amazon EFS<br>file systems. The permissions are required to allow Amazon EFS to<br>manage files system replication configurations on the user's<br>behalf. | January 25, 2022  |
| Update to an existing policy           | Policy: [AmazonElasticFileSystemReadOnlyAccess](#security-iam-awsmanpol-AmazonElasticFileSystemReadOnlyAccess "#security-iam-awsmanpol-AmazonElasticFileSystemReadOnlyAccess")<br>Amazon EFS added a new permission to allow principals to describe<br>Amazon EFS replications. The permissions are required to allow users<br>to view files system replication configurations.                                                                | January 25, 2022  |
| Update to an existing policy           | Policy: [AmazonElasticFileSystemFullAccess](#security-iam-awsmanpol-AmazonElasticFileSystemFullAccess "#security-iam-awsmanpol-AmazonElasticFileSystemFullAccess")<br>Amazon EFS added new permissions to allow principals to create,<br>describe, and delete Amazon EFS replications. The permissions are<br>required to allow users to manage files system replication<br>configurations.                                                    | January 25, 2022  |
| Started tracking policy                | Policy: [AmazonElasticFileSystemClientReadWriteAccess](#security-iam-awsmanpol-AmazonElasticFileSystemClientReadWriteAccess "#security-iam-awsmanpol-AmazonElasticFileSystemClientReadWriteAccess")<br>Grants read and write privileges on Amazon EFS file systems to NFS<br>clients.                                                                                                                                                          | January 3, 2022   |
| Started tracking policy                | Policy: [AmazonElasticFileSystemServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions")The<br>service-linked role permissions for Amazon EFS.                                                                                                                                                                                                                                        | October 8, 2021   |
| Update to an existing policy           | Policy: [AmazonElasticFileSystemFullAccess](#security-iam-awsmanpol-AmazonElasticFileSystemFullAccess "#security-iam-awsmanpol-AmazonElasticFileSystemFullAccess")<br>Amazon EFS added new permissions to allow principals to modify and<br>describe Amazon EFS account preferences. The permissions are required<br>to allow users to view and set account preferences settings in the<br>Amazon EFS console.                                 | May 7, 2021       |
| Update to an existing policy           | Policy: [AmazonElasticFileSystemReadOnlyAccess](#security-iam-awsmanpol-AmazonElasticFileSystemReadOnlyAccess "#security-iam-awsmanpol-AmazonElasticFileSystemReadOnlyAccess")<br>Amazon EFS added new permissions to allow principals to describe<br>Amazon EFS account preferences. The permissions are required to allow<br>users to view account preferences settings in the Amazon EFS<br>console.                                        | May 7, 2021       |
| Amazon EFS started tracking<br>changes | Amazon EFS started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                                                                                                                                                                                                           | May 7, 2021       |
