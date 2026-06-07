# BackupVaultListMember

Contains metadata about a backup vault.

## Contents

**BackupVaultArn**

An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example,
`arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.

Type: String

Required: No

**BackupVaultName**

The name of a logical container where backups are stored. Backup vaults are identified
by names that are unique to the account used to create them and the AWS
Region where they are created.

Type: String

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: No

**CreationDate**

The date and time a resource backup is created, in Unix format and Coordinated Universal
Time (UTC). The value of `CreationDate` is accurate to milliseconds. For
example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

Required: No

**CreatorRequestId**

A unique string that identifies the request and allows failed requests to be retried
without the risk of running the operation twice. This parameter is optional.

If used, this parameter must contain 1 to 50 alphanumeric or '-\_.' characters.

Type: String

Required: No

**EncryptionKeyArn**

A server-side encryption key you can specify to encrypt your backups from services
that support full AWS Backup management; for example,
`arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`.
If you specify a key, you must specify its ARN, not its alias. If you do not specify a key,
AWS Backup creates a KMS key for you by default.

To learn which AWS Backup services support full AWS Backup management
and how AWS Backup handles encryption for backups from services that do not yet support
full AWS Backup, see [Encryption for backups in AWS Backup](encryption.md "encryption.md")

Type: String

Required: No

**EncryptionKeyType**

The type of encryption key used for the backup vault. Valid values are CUSTOMER_MANAGED_KMS_KEY for customer-managed keys or AWS_OWNED_KMS_KEY for AWS-owned keys.

Type: String

Valid Values: `AWS_OWNED_KMS_KEY | CUSTOMER_MANAGED_KMS_KEY`

Required: No

**LockDate**

The date and time when AWS Backup Vault Lock configuration becomes immutable,
meaning it cannot be changed or deleted.

If you applied Vault Lock to your vault without specifying a lock date, you can change
your Vault Lock settings, or delete Vault Lock from the vault entirely, at any time.

This value is in Unix format, Coordinated Universal Time (UTC), and accurate to
milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
12:11:30.087 AM.

Type: Timestamp

Required: No

**Locked**

A Boolean value that indicates whether AWS Backup Vault Lock applies to the
selected backup vault. If `true`, Vault Lock prevents delete and update
operations on the recovery points in the selected vault.

Type: Boolean

Required: No

**MaxRetentionDays**

The AWS Backup Vault Lock setting that specifies the maximum retention period
that the vault retains its recovery points. If this parameter is not specified, Vault Lock
does not enforce a maximum retention period on the recovery points in the vault (allowing
indefinite storage).

If specified, any backup or copy job to the vault must have a lifecycle policy with a
retention period equal to or shorter than the maximum retention period. If the job's
retention period is longer than that maximum retention period, then the vault fails the
backup or copy job, and you should either modify your lifecycle settings or use a different
vault. Recovery points already stored in the vault prior to Vault Lock are not
affected.

Type: Long

Required: No

**MinRetentionDays**

The AWS Backup Vault Lock setting that specifies the minimum retention period
that the vault retains its recovery points. If this parameter is not specified, Vault Lock
does not enforce a minimum retention period.

If specified, any backup or copy job to the vault must have a lifecycle policy with a
retention period equal to or longer than the minimum retention period. If the job's
retention period is shorter than that minimum retention period, then the vault fails the
backup or copy job, and you should either modify your lifecycle settings or use a different
vault. Recovery points already stored in the vault prior to Vault Lock are not
affected.

Type: Long

Required: No

**NumberOfRecoveryPoints**

The number of recovery points that are stored in a backup vault.

Type: Long

Required: No

**VaultState**

The current state of the vault.

Type: String

Valid Values: `CREATING | AVAILABLE | FAILED`

Required: No

**VaultType**

The type of vault in which the described recovery point is stored.

Type: String

Valid Values: `BACKUP_VAULT | LOGICALLY_AIR_GAPPED_BACKUP_VAULT | RESTORE_ACCESS_BACKUP_VAULT`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/BackupVaultListMember.md "../../../goto/SdkForCpp/backup-2018-11-15/BackupVaultListMember.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/BackupVaultListMember.md "../../../goto/SdkForJavaV2/backup-2018-11-15/BackupVaultListMember.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/BackupVaultListMember.md "../../../goto/SdkForRubyV3/backup-2018-11-15/BackupVaultListMember.md")
