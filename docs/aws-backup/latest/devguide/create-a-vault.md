# Backup vault creation and deletion

You must create at least one vault before creating a backup plan or starting a backup
job.

When you first use the **Backup Vaults** page of the AWS Backup console in an
AWS Region, the console automatically creates a default vault for the Region.

However, if you use AWS Backup through the AWS CLI, AWS SDK, or CloudFormation, a default vault is not
created. You must create your own vault.

## Required permissions

You must have the following permissions to create a backup vault using AWS Backup.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowKMSOperations",
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant",
 "kms:DescribeKey",
 "kms:RetireGrant",
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`444455556666`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`"
 },
 {
 "Sid": "AllowCreateBackupVault",
 "Effect": "Allow",
 "Action": [
 "backup:CreateBackupVault"
 ],
 "Resource": "arn:aws:backup:`us-east-1`:`444455556666`:backup-vault:*"
 },
 {
 "Sid": "AllowMountCapsule",
 "Effect": "Allow",
 "Action": [
 "backup-storage:MountCapsule"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Creating a backup vault (console)

Instead of using the default backup vault that is automatically created for you on the
AWS Backup console, you can create specific backup vaults to save and organize groups of backups
in the same vault.

###### To create a backup vault

1. On the AWS Backup console, in the navigation pane, choose **Backup
   vaults**.

###### Note

If the navigation pane is not visible on the left side, you can open it by
choosing the menu icon in the upper-left corner of the AWS Backup console. 2. Choose **Create backup vault**. 3. Enter a name for your backup vault. You can name your vault to reflect what you will
store in it, or to make it easier to search for the backups you need. For example, you
could name it `FinancialBackups`. 4. Select an AWS Key Management Service (AWS KMS) key. You can use either a key that you already created,
or select the default AWS Backup KMS key.

###### Note

The AWS KMS key that is specified here applies only to backups of services that
support AWS Backup independent encryption. To see the list of resources types that support
AWS Backup independent encryption, see the "Full AWS Backup management" section of the [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") table. 5. Optionally, add tags that will help you search for and identify your backup vault.
For example, you could add a `BackupType:Financial` tag. 6. Choose **Create Backup vault**. 7. In the navigation pane, choose **Backup vaults**, and verify that
your backup vault has been added.

###### Note

You can now edit a backup rule in one of your backup plans to store backups created by
that rule in the backup vault you just created.

## Creating a backup vault (programmatically)

The following AWS Command Line Interface command creates a backup vault:

```
aws backup create-backup-vault --backup-vault-name `test-vault`
```

You can also specify the following configurations for a backup vault.

## Backup vault name

Backup vault names are case sensitive. They must contain from 2 to 50 alphanumeric
characters, hyphens, or underscores.

## AWS KMS encryption key

The AWS KMS encryption key protects your backups in this backup vault. By default, AWS Backup
creates a KMS key with the alias `aws/backup` for you. You can choose that key or
choose any other key in your account (cross-account KMS keys can be used via CLI).

You can create a new encryption key by following the [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") procedure in the
_AWS Key Management Service Developer Guide_.

After you create a backup vault and set the AWS KMS encryption key, you can no longer edit
the key for that backup vault.

The encryption key that is specified in an AWS Backup vault applies to the backups of certain
resource types. For more information about backup encryption, see [Encryption for backups in AWS Backup](encryption.md "encryption.md") in the Security section. Backups of all
other resource types are backed up using the key that is used to encrypt the source
resource.

## Backup vault tags

These tags are associated with the backup vault to help you organize and track your
backup vaults.

## Delete a vault

To guard against accidental or malicious mass deletion, you can delete a backup vault in
AWS Backup only after you delete (or your backup plan lifecycles) all the recovery points in your
backup vault. To delete your recovery points manually, see [Clean up
resources](gs-cleanup-resources.md#cleanup-backups "gs-cleanup-resources.md#cleanup-backups").

When you delete a backup vault, update your backup plans to point to new backup vaults.
A backup plan that points to a deleted backup vault will cause the backup creation to
fail.

You can't delete the default backup vault or the Amazon EFS automatic backup vault using the
AWS Management Console. You can delete a default backup vault using the AWS CLI if it is empty. However,
if you open the AWS Backup console and select that Region, the console recreates the default
backup vault. You can delete unused snapshots in the Amazon EFS automatic backup vault.

###### To delete a backup vault using the AWS Backup console

1. Sign in to the AWS Management Console, and open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Backup vaults**.
3. Choose the name of the backup vault to open its details page.
4. Choose and delete any backups that are associated with the backup vault.
5. Choose **Delete vault**. When prompted for confirmation, enter the
   vault name and then choose **Delete Backup vault**.
