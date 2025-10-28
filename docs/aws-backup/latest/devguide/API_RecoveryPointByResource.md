# RecoveryPointByResource

Contains detailed information about a saved recovery point.

## Contents

**BackupSizeBytes**

The size, in bytes, of a backup.

Type: Long

Required: No

**BackupVaultName**

The name of a logical container where backups are stored. Backup vaults are identified
by names that are unique to the account used to create them and the AWS
Region where they are created.

Type: String

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: No

**CreationDate**

The date and time a recovery point is created, in Unix format and Coordinated Universal
Time (UTC). The value of `CreationDate` is accurate to milliseconds. For
example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

Required: No

**EncryptionKeyArn**

The server-side encryption key that is used to protect your backups; for example,
`arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`.

Type: String

Required: No

**IndexStatus**

This is the current status for the backup index associated
with the specified recovery point.

Statuses are: `PENDING` | `ACTIVE` | `FAILED` | `DELETING`

A recovery point with an index that has the status of `ACTIVE`
can be included in a search.

Type: String

Valid Values: `PENDING | ACTIVE | FAILED | DELETING`

Required: No

**IndexStatusMessage**

A string in the form of a detailed message explaining the status of a backup index
associated with the recovery point.

Type: String

Required: No

**IsParent**

This is a boolean value indicating this is
a parent (composite) recovery point.

Type: Boolean

Required: No

**ParentRecoveryPointArn**

The Amazon Resource Name (ARN) of the parent (composite)
recovery point.

Type: String

Required: No

**RecoveryPointArn**

An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.

Type: String

Required: No

**ResourceName**

The non-unique name of the resource that
belongs to the specified backup.

Type: String

Required: No

**Status**

A status code specifying the state of the recovery point.

Type: String

Valid Values: `COMPLETED | PARTIAL | DELETING | EXPIRED | AVAILABLE | STOPPED | CREATING`

Required: No

**StatusMessage**

A message explaining the current status of the recovery point.

Type: String

Required: No

**VaultType**

The type of vault in which the described recovery point is
stored.

Type: String

Valid Values: `BACKUP_VAULT | LOGICALLY_AIR_GAPPED_BACKUP_VAULT | RESTORE_ACCESS_BACKUP_VAULT`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/RecoveryPointByResource.md "../../../goto/SdkForCpp/backup-2018-11-15/RecoveryPointByResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/RecoveryPointByResource.md "../../../goto/SdkForJavaV2/backup-2018-11-15/RecoveryPointByResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/RecoveryPointByResource.md "../../../goto/SdkForRubyV3/backup-2018-11-15/RecoveryPointByResource.md")
