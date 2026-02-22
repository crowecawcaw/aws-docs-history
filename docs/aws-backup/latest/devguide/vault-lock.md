# AWS Backup Vault Lock

###### Note

AWS Backup Vault Lock has been assessed by Cohasset Associates for use in environments
that are subject to SEC 17a-4, CFTC, and FINRA regulations. For more information about
how AWS Backup Vault Lock relates to these regulations, see the
[Cohasset Associates
Compliance Assessment.](samples/cohassetreport.md "samples/cohassetreport.md")

AWS Backup Vault Lock is an optional feature of a backup vault, which can be helpful in giving you
additional security and control over your backup vaults. When a lock is active in Compliance
mode and the grace time is over, the vault
configuration cannot be altered or deleted by a customer, account/data owner, or AWS
as long as it contains recovery points.
Each vault can have one vault lock in place.

AWS Backup ensures that your backups are available for you until they reach the expiration of their
retention periods. If any user (including the root user) attempts to delete a backup or change
the lifecycle properties in a locked vault, AWS Backup will deny the operation.

- Vaults locked in
  **governance mode** can have the lock removed by users with sufficient IAM permissions.
- Vaults locked in **compliance mode** _cannot be deleted_ once the cooling-off
  period ("**grace time**") expires if any recovery points are in the
  vault. During grace time, you can still remove
  the vault lock and change the lock configuration.

###### Warning

Once the grace time is expired, the vault and its lock are immutable. It cannot be changed or deleted by any user or by AWS. Backups within a locked vault cannot be deleted until their lifecycle completes, resulting in persistent costs if you are not careful.

## Vault lock modes

When you create a vault lock, you have a choice of two modes:
**Governance mode** or **Compliance mode**. Governance mode
is intended to allow a vault to be managed only by users with sufficient IAM privileges.
Governance mode helps an organization meet governance requirements, ensuring
only designated personnel can make changes to a backup vault. Compliance mode is intended for
backup vaults in which the vault (and by extension, its contents) is expected to never be deleted
or altered until the data retention period is complete. Once a vault in compliance mode is
locked, it is **immutable**, meaning the lock _cannot be removed_
(the vault itself can be deleted if it is empty and does not contain any recovery
points).

A vault locked in Governance mode can be managed or deleted by users who have the appropriate
IAM permissions.

A vault lock in Compliance mode cannot be altered or deleted by any user or by AWS. A
vault lock in compliance mode has a grace time period you set before it locks and the
contents and vault lock become immutable.

## Vault lock benefits

AWS Backup Vault Lock provides several benefits, including:

- WORM (_write-once, read-many_) configuration for
  all the backups you store and create in a backup vault.
- An additional layer of defense that protects backups
  (recovery points) in your backup vaults from inadvertent or malicious deletions.
- Enforcement of retention periods, which prevent early deletions by
  privileged users (including the AWS account root user), and meet your organization’s data
  protection policies and procedures.

## Lock a backup vault using the console

You can add a vault lock to your AWS Backup Vault using the Backup console.

To add a vault lock to your backup vault:

1. Sign in to the AWS Management Console, and open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, find **Backup vaults**. Click the link
   nested under Backup vaults called **Vault locks**.
3. Under **How vault locks work** or **Vault locks**,
   click **+ Create vault lock**.
4. In the pane **Vault lock details**, choose which vault to which
   you want your lock applied.
5. Under **Vault lock mode** choose in which mode you want your
   vault locked. For more information on choosing your modes, see
   [Vault lock modes](vault-lock.md#backup-vault-lock-modes "vault-lock.md#backup-vault-lock-modes") earlier on this page.
6. For the **Retention period**, choose the minimum and maximum retention
   periods (retention periods are _optional_). New backup
   and copy jobs created in the vault will fail if they do not conform to the retention periods you
   set; these periods will not apply to recovery points that are already
   in the vault. Recovery points that were present in the vault prior to the vault lock being enabled will follow their previous lifecycle settings.
7. If you chose compliance mode, a section called **Vault lock start date**
   is shown. If you chose Governance mode, this will not be displayed, and this step
   can be skipped.

In compliance mode, a vault lock has a cooling-off period from the creation of the vault lock
until the vault and its lock becomes immutable and unchangeable. You choose the duration of this
period (called **grace time**), though it must be _at least_
3 days (72 hours).

###### Important

Once the grace time is expired, the vault and its lock are immutable. It cannot be
changed or deleted by any user or by AWS. 8. When you are satisfied with the configuration choices, click **Create vault lock**. 9. To confirm you wish to create this lock in the chosen mode, type `confirm`
in the text box, then check the box acknowledging the configuration is as intended.

If the steps have been completed successfully, a "Success" banner will appear at
the top of the console.

## Lock a backup vault programmatically

To configure AWS Backup Vault Lock, use the API `PutBackupVaultLockConfiguration`. The parameters to include will depend on
which vault lock mode you intend. If you wish to create a vault lock in governance mode, **do not
include** `ChangeableForDays`. If this parameter is included, the vault lock will be
created in compliance mode.

Here is a CLI example of a compliance mode vault lock creation:

```
aws backup put-backup-vault-lock-configuration \
        --backup-vault-name `my_vault_to_lock` \
        --changeable-for-days `3` \
        --min-retention-days `7` \
        --max-retention-days `30`
```

Here is a CLI example of a governance mode vault lock creation:

```
aws backup put-backup-vault-lock-configuration \
        --backup-vault-name `my_vault_to_lock` \
        --min-retention-days `7` \
        --max-retention-days `30`
```

You can configure four options.

1. `**BackupVaultName**`

The name of the vault to lock. 2. `**ChangeableForDays**` (include _only_ for compliance mode)

This parameter instructs AWS Backup to create the vault lock in **compliance mode**.
Omit this parameter if you intend to create the lock in **governance mode**.

This value is expressed in days. It must be a number no less than 3 and no greater
than 36,500; otherwise, an error will return.

From the creation of this vault lock until the expiration of the date specified, the vault
lock can be removed from the vault using `DeleteBackupVaultLockConfiguration`.
Alternatively, during this time, you can change the configuration using
`PutBackupVaultLockConfiguration`.

On and after the specified date determined by this parameter, the backup vault will be
immutable and cannot be changed or deleted. 3. `**MaxRetentionDays**` _(optional)_

This is a numerical value expressed in days. This is the maximum retention period that
the vault retains its recovery points.

The maximum retention time frame you choose should be in alignment with your organization's
policies for retaining data. If your organization instructs data to be retained for a period,
this value can be set to that period (in days). For example, financial or banking data may be
required to be kept for 7 years (approximately 2,557 days, depending on leap years).

If not specified, AWS Backup Vault Lock will not enforce a maximum retention
period. If specified, backup and copy jobs to this vault with lifecycle retention periods
longer than the maximum retention period will fail. Recovery points already saved in the
vault prior to the vault lock's creation are not affected. The longest maximum retention period
you can specify is 36500 days (approximately 100 years). 4. `**MinRetentionDays**` (_optional_; required for CloudFormation)

This is a numerical value expressed in days. This is the minimum retention period that the
vault retains its recovery points. This setting should be set to the amount of time your
organization is _required_ to maintain data. For example, if regulations or
law requires data to be retained for at least seven years, the value in days would be
approximately 2,557, depending on leap years.

If not specified, AWS Backup Vault Lock will not enforce a minimum retention
period. If specified, backup and copy jobs to this vault with lifecycle retention periods
shorter than the minimum retention period will fail. Recovery points already saved in
the vault prior to AWS Backup Vault Lock are not affected. The shortest minimum retention period
you can specify is 1 day.

## Review a backup vault for its AWS Backup Vault

Lock configuration

You can review AWS Backup Vault Lock details on a vault anytime by calling `DescribeBackupVault` or `ListBackupVaults` APIs.

To determine whether you applied a vault lock to a backup vault, call
`DescribeBackupVault` and check the `Locked` property. If
`"Locked": true`, like the following example, you have applied AWS Backup Vault Lock
to your backup vault.

```
{
    "BackupVaultName": "my_vault_to_lock",
    "BackupVaultArn": "arn:aws:backup:us-east-1:555500000000:backup-vault:my_vault_to_lock",
    "EncryptionKeyArn": "arn:aws:kms:us-east-1:555500000000:key/00000000-1111-2222-3333-000000000000",
    "CreationDate": "2021-09-24T12:25:43.030000-07:00",
    "CreatorRequestId": "ac6ce255-0456-4f84-bbc4-eec919f50709",
    "NumberOfRecoveryPoints": 1,
    "Locked": true,
    "MinRetentionDays": 7,
    "MaxRetentionDays": 30,
    "LockDate": "2021-09-30T10:12:38.089000-07:00"
}
```

The preceding output confirms the following options:

1. `Locked` is a Boolean that indicates whether you have applied AWS Backup Vault
   Lock to this backup vault. `True` means that AWS Backup Vault Lock causes delete
   or update operations to the recovery points stored in the vault to fail (regardless of
   whether you are still in the cooling-off grace time period).
2. `LockDate` is the UTC date and time when your cooling-off grace time period ends.
   After this time, you cannot delete or change your lock on this vault. Use
   any publicly-available time converters to convert this string to your local time.

If `"Locked":false`, like the following example, you have not applied a vault
lock (or a previous one has been deleted).

```
{
    "BackupVaultName": "my_vault_to_lock",
    "BackupVaultArn": "arn:aws:backup:us-east-1:555500000000:backup-vault:my_vault_to_lock",
    "EncryptionKeyArn": "arn:aws:kms:us-east-1:555500000000:key/00000000-1111-2222-3333-000000000000",
    "CreationDate": "2021-09-24T12:25:43.030000-07:00",
    "CreatorRequestId": "ac6ce255-0456-4f84-bbc4-eec919f50709",
    "NumberOfRecoveryPoints": 3,
    "Locked": false
}
```

## Vault lock removal during grace time (Compliance mode)

To delete your vault lock during grace time (the time after locking the vault but
before your `LockDate`) using the AWS Backup console,

1. Sign in to the AWS Management Console, and open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the left navigation under **My account**, click
   Backup vaults, then click Backup Vault Lock.
3. Click the vault lock you wish to remove, then click
   **Manage vault lock**.
4. Click **Delete vault lock**.
5. A warning box will appear, asking you to confirm your intent
   to delete the vault lock. Type `confirm` into the text box,
   then click **confirm**.

After the steps have all been completed successfully, a Success banner will appear
at the top of the console screen.

To delete your vault lock during grace time using a CLI command,
use `DeleteBackupVaultLockConfiguration` like this CLI example:

```
aws backup delete-backup-vault-lock-configuration \
          --backup-vault-name `my_vault_to_lock`
```

## AWS account closure with a locked

vault

When you close an AWS account that contains a backup vault, AWS and AWS Backup suspend
your account for 90 days with your backups intact. If you do not reopen your account during
those 90 days, AWS deletes the contents of your backup vault, even if AWS Backup
Vault Lock was in place.

## Additional security considerations

AWS Backup Vault Lock adds an additional layer of security to your data protection defense in
depth. Vault lock can be combined with these other security features:

- [Encryption for your recovery points](encryption.md "encryption.md")
- [AWS Backup vault and
  recovery point access policies](create-a-vault-access-policy.md "create-a-vault-access-policy.md"), which allow you to grant or deny permissions
  at the vault level,
- [AWS Backup security best
  practices](security-considerations.md "security-considerations.md"), including its library of [customer managed policies](security-iam-awsmanpol.md#customer-managed-policies "security-iam-awsmanpol.md#customer-managed-policies") that allow you to grant or deny backup and restore
  permissions by AWS supported service, and
- [AWS Backup Audit
  Manager](aws-backup-audit-manager.md "aws-backup-audit-manager.md"), which allows you to automate compliance checks for your backups
  against [a list of
  controls](controls-and-remediation.md "controls-and-remediation.md") you define.

You can work through [Creating frameworks using the AWS Backup API](creating-frameworks-api.md "creating-frameworks-api.md") for the control [Resources are in a backup plan with an AWS Backup Vault Lock](controls-and-remediation.md#backup-vault-lock-control "controls-and-remediation.md#backup-vault-lock-control") with
AWS Backup Audit Manager to help ensure that your intended resources are protected with a
vault lock.

- Mechanisms that render resources inactive can impact the ability to restore them.
  While they still cannot be deleted in a locked vault, they can be in a state other than
  active. For instance, the Amazon Elastic Compute Cloud setting that allows you to [disable an
  AMI](../../../AWSEC2/latest/UserGuide/disable-an-ami.md "../../../AWSEC2/latest/UserGuide/disable-an-ami.md") can temporarily block the ability to restore backups of EC2 instances.
  This affects all EC2 recovery points, even backups affected by a vault lock or a legal
  hold.

If an EC2 backup is disabled, you can [re-enable a
disabled AMI](../../../AWSEC2/latest/UserGuide/disable-an-ami.md#re-enable-a-disabled-ami "../../../AWSEC2/latest/UserGuide/disable-an-ami.md#re-enable-a-disabled-ami"). Once it is re-enabled, it is eligible to be restored. To block
the AMI disable feature, you can use IAM policies to not allow
`ec2:DisableImage`.

###### Note

AWS Backup Vault Lock is not the same feature as [Amazon Glacier Vault
Lock](../../../amazonglacier/latest/dev/vault-lock.md "../../../amazonglacier/latest/dev/vault-lock.md"), which is compatible only with Amazon Glacier.
