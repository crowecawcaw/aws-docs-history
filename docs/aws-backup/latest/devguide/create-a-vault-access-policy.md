# Vault access policies

With AWS Backup, you can assign policies to backup vaults and the resources they contain.
Assigning policies allows you to do things like grant access to users to create backup plans
and on-demand backups, but limit their ability to delete recovery points after they're
created.

For information about using policies to grant or restrict access to resources, see [Identity-Based Policies and
Resource-Based Policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") in the _IAM User Guide_. You can also
control access using tags.

You can use the following example policies as a guide to limit access to resources when
you are working with AWS Backup vaults. Unlike other IAM-based policies, AWS Backup access policies
don't support a wildcard in the `Action` key.

For a list of Amazon Resource Names (ARNs) that you can use to identify recovery points
for different resource types, see [AWS Backup resource ARNs](access-control.md#resource-arns-table "access-control.md#resource-arns-table") for resource-specific recovery point ARNs.

Vault access policies only control user access to AWS Backup APIs. Some backup types, such as
Amazon Elastic Block Store (Amazon EBS) and Amazon Relational Database Service (Amazon RDS) snapshots, can also be accessed using the APIs of
those services. You can create separate access policies in IAM that control access to
those APIs to fully control the access to those backup types.

Regardless of the AWS Backup vault's access policy, cross-account access for any action other
than `backup:CopyIntoBackupVault` will be rejected; that is, AWS Backup will reject any
other request from an account that is different from the account of the resource that is being
referenced.

###### Topics

- [Deny access to a resource type in a backup
  vault](#deny-access-to-ebs-snapshots "#deny-access-to-ebs-snapshots")
- [Deny access to a backup vault](#deny-access-to-a-backup-vault "#deny-access-to-a-backup-vault")
- [Deny access to delete recovery
  points in a backup vault](#deny-access-to-delete-recovery-points "#deny-access-to-delete-recovery-points")

## Deny access to a resource type in a backup

vault

This policy denies access to the specified API operations for all Amazon EBS snapshots in a
backup vault.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyRecoveryPointOperations",
 "Effect": "Deny",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`MyRole`"
 },
 "Action": [
 "backup:UpdateRecoveryPointLifecycle",
 "backup:DescribeRecoveryPoint",
 "backup:DeleteRecoveryPoint",
 "backup:GetRecoveryPointRestoreMetadata",
 "backup:StartRestoreJob"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:snapshot/*"
 ]
 }
 ]
}`

```

## Deny access to a backup vault

This policy denies access to the specified API operations targeting a backup
vault.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyBackupVaultOperations",
 "Effect": "Deny",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:role/`MyRole`"
 },
 "Action": [
 "backup:DescribeBackupVault",
 "backup:DeleteBackupVault",
 "backup:PutBackupVaultAccessPolicy",
 "backup:DeleteBackupVaultAccessPolicy",
 "backup:GetBackupVaultAccessPolicy",
 "backup:StartBackupJob",
 "backup:GetBackupVaultNotifications",
 "backup:PutBackupVaultNotifications",
 "backup:DeleteBackupVaultNotifications",
 "backup:ListRecoveryPointsByBackupVault"
 ],
 "Resource": "arn:aws:backup:`us-east-1`:`123456789012`:backup-vault:`backup vault name`"
 }
 ]
}`

```

## Deny access to delete recovery

points in a backup vault

Access to vaults and the ability to delete recovery points stored in them is determined
by the access that you grant your users.

Follow these steps to create a resource-based access policy on a backup vault that
prevents the deletion of any backups in the backup vault.

###### To create a resource-based access policy on a backup vault

1. Sign in to the AWS Management Console, and open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane on the left, choose **Backup
   vaults**.
3. Choose a backup vault in the list.
4. In the **Access policy** section, paste the following JSON example.
   This policy prevents anyone who is not the principal from deleting a recovery point in
   the target backup vault.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Principal": "*",
 "Action": "backup:DeleteRecoveryPoint",
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "aws:userId": [
 "`AIDA1234567890EXAMPLE`",
 "`AROA1234567890EXAMPLE:my-role-session`",
 "`AROA1234567890EXAMPLE:*`",
 "`112233445566`"
 ]
 }
 }
 }
 ]
}`

```

To allow list IAM identities using their ARN, use the `aws:PrincipalArn`
global condition key in the following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyDeleteRecoveryPoint",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "backup:DeleteRecoveryPoint",
 "Resource": "*",
 "Condition": {
 "ArnNotEquals": {
 "aws:PrincipalArn": [
 "arn:aws:iam::`112233445566`:role/`mys3role`",
 "arn:aws:iam::`112233445566`:user/`shaheer`",
 "arn:aws:iam::`112233445566`:root"
 ]
 }
 }
 }
 ]
}`

```

For information about getting a unique ID for an IAM entity, see [Getting the
unique identifier](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-get-unique-id "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-get-unique-id") in the _IAM User Guide_.

If you want to limit this to specific resource types, instead of `"Resource":
 "*"`, you can explicitly include the recovery point types to deny. For example,
for Amazon EBS snapshots, change the resource type to the following.

```
"Resource": ["arn:aws:ec2::`Region`::snapshot/*"]
```

5. Choose **Attach policy**.
