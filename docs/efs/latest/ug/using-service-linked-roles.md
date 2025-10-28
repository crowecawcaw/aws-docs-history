# Using service-linked roles for Amazon EFS

Amazon EFS uses an AWS Identity and Access Management (IAM)[service-linked role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). The Amazon EFS service-linked role is a unique type of IAM
role that is linked directly to Amazon EFS. The predefined Amazon EFS service-linked role
includes permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up Amazon EFS easier because you don't have to
manually add the necessary permissions. Amazon EFS defines the permissions of its
service-linked role, and only Amazon EFS can assume its role. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy can't be attached to any other IAM entity.

You can delete the Amazon EFS service-linked role only after first deleting your Amazon EFS file systems. This
protects your Amazon EFS resources because you can't inadvertently remove permission to
access the resources.

The service-linked role enables all API calls to be visible through AWS CloudTrail. This helps
with monitoring and auditing requirements because you can track all actions that Amazon EFS performs
on your behalf. For more information, see [Log entries for EFS service-linked roles](logging-using-cloudtrail.md#efs-service-linked-role-ct "logging-using-cloudtrail.md#efs-service-linked-role-ct").

For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Service-linked role permissions for Amazon EFS

Amazon EFS uses the service-linked role named **AWSServiceRoleForAmazonElasticFileSystem**
to allow Amazon EFS to call and manage AWS resources on behalf of your EFS file systems.

The AWSServiceRoleForAmazonElasticFileSystem service-linked role trusts the `elasticfilesystem.amazonaws.com` to assume
the role.

The role permissions policy allows Amazon EFS to complete the actions included in the policy definition JSON:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "backup-storage:MountCapsule",
 "ec2:CreateNetworkInterface",
 "ec2:DeleteNetworkInterface",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeNetworkInterfaceAttribute",
 "ec2:ModifyNetworkInterfaceAttribute",
 "tag:GetResources"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey"
 ],
 "Resource": "arn:aws:kms:*:*:key/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "backup:CreateBackupVault",
 "backup:PutBackupVaultAccessPolicy"
 ],
 "Resource": [
 "arn:aws:backup:*:*:backup-vault:aws/efs/automatic-backup-vault"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "backup:CreateBackupPlan",
 "backup:CreateBackupSelection"
 ],
 "Resource": [
 "arn:aws:backup:*:*:backup-plan:*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": [
 "backup.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/backup.amazonaws.com/AWSServiceRoleForBackup"
 ],
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "backup.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "elasticfilesystem:DescribeFileSystems",
 "elasticfilesystem:CreateReplicationConfiguration",
 "elasticfilesystem:DescribeReplicationConfigurations",
 "elasticfilesystem:DeleteReplicationConfiguration",
 "elasticfilesystem:ReplicationRead",
 "elasticfilesystem:ReplicationWrite"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

You must manually configure IAM permissions for AWS KMS when creating a new
EFS file system that is encrypted at rest. To learn more, see [Encrypting data at rest](encryption-at-rest.md "encryption-at-rest.md").

You must configure permissions to allow an IAM entity (such as a user, group, or role) to
create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Creating a service-linked role for Amazon EFS

In most cases, you don't need to manually create a service-linked role. When you
create mount targets or a replication configuration for your EFS file system in the AWS Management Console, the AWS CLI, or the AWS API, Amazon EFS creates
the service-linked role for you.

Additionally, if you manually delete this service-linked-role, and then need to create it
again, you can use the same process to recreate the role in your account. When you
create mount targets or a replication configuration for your EFS file system, Amazon EFS creates the service-linked role for you.

If, however, Amazon EFS does not create the service-linked-role or if you started using Amazon EFS
before it supported service-linked roles, then you can manually create the service-linked role.
For instructions, see [Creating a service-linked role](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md") in the _IAM User Guide_.

## Editing a service-linked role for Amazon EFS

Amazon EFS doesn't allow you to edit the `AWSServiceRoleForAmazonElasticFileSystem` service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Update
a service-linked role](../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md") in the _IAM User Guide_.

## Deleting a service-linked role for Amazon EFS

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don't have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it. For more information, see [Clean up resources and protect your AWS
account](getting-started.md#gs-step-five-cleanup "getting-started.md#gs-step-five-cleanup").

###### Note

If the Amazon EFS service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAmazonElasticFileSystem
service-linked role. For more information, see [Deleting a
service-linked role](../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr "../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr") in the _IAM User Guide_.

## Supported Regions for Amazon EFS service-linked roles

Amazon EFS supports using service-linked roles in all of the AWS Regions where the service is
available. For more information, see [AWS service endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the _AWS General Reference User
Guide_.
