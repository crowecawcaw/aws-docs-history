# RecoveryPointByBackupVault

Contains detailed information about the recovery points stored in a backup vault.

## Contents

**BackupSizeInBytes**

The size, in bytes, of a backup.

Type: Long

Required: No

**BackupVaultArn**

An ARN that uniquely identifies a backup vault; for example,
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

**CalculatedLifecycle**

A `CalculatedLifecycle` object containing `DeleteAt` and
`MoveToColdStorageAt` timestamps.

Type: [CalculatedLifecycle](API_CalculatedLifecycle.md "API_CalculatedLifecycle.md") object

Required: No

**CompletionDate**

The date and time a job to restore a recovery point is completed, in Unix format and
Coordinated Universal Time (UTC). The value of `CompletionDate` is accurate to
milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
12:11:30.087 AM.

Type: Timestamp

Required: No

**CompositeMemberIdentifier**

The identifier of a resource within a composite group, such as
nested (child) recovery point belonging to a composite (parent) stack. The
ID is transferred from
the [logical ID](../../../AWSCloudFormation/latest/UserGuide/resources-section-structure.md#resources-section-structure-syntax "../../../AWSCloudFormation/latest/UserGuide/resources-section-structure.md#resources-section-structure-syntax") within a stack.

Type: String

Required: No

**CreatedBy**

Contains identifying information about the creation of a recovery point, including the
`BackupPlanArn`, `BackupPlanId`, `BackupPlanVersion`,
and `BackupRuleId` of the backup plan that is used to create it.

Type: [RecoveryPointCreator](API_RecoveryPointCreator.md "API_RecoveryPointCreator.md") object

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

**IamRoleArn**

Specifies the IAM role ARN used to create the target recovery point; for example,
`arn:aws:iam::123456789012:role/S3Access`.

Type: String

Required: No

**IndexStatus**

This is the current status for the backup index associated
with the specified recovery point.

Statuses are: `PENDING` | `ACTIVE` | `FAILED` |
`DELETING`

A recovery point with an index that has the status of `ACTIVE`
can be included in a search.

Type: String

Valid Values: `PENDING | ACTIVE | FAILED | DELETING`

Required: No

**IndexStatusMessage**

A string in the form of a detailed message explaining the status of a backup index associated
with the recovery point.

Type: String

Required: No

**InitiationDate**

The date and time when the backup job that created this recovery point was initiated, in
Unix format and Coordinated Universal Time (UTC).

Type: Timestamp

Required: No

**IsEncrypted**

A Boolean value that is returned as `TRUE` if the specified recovery point is
encrypted, or `FALSE` if the recovery point is not encrypted.

Type: Boolean

Required: No

**IsParent**

This is a boolean value indicating this is
a parent (composite) recovery point.

Type: Boolean

Required: No

**LastRestoreTime**

The date and time a recovery point was last restored, in Unix format and Coordinated
Universal Time (UTC). The value of `LastRestoreTime` is accurate to
milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
12:11:30.087 AM.

Type: Timestamp

Required: No

**Lifecycle**

The lifecycle defines when a protected resource is transitioned to cold storage and when
it expires. AWS Backup transitions and expires backups automatically according to
the lifecycle that you define.

Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
days. Therefore, the “retention” setting must be 90 days greater than the “transition to
cold after days” setting. The “transition to cold after days” setting cannot be changed
after a backup has been transitioned to cold.

Resource types that can transition to cold storage are listed in the [Feature
availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") table. AWS Backup ignores this expression for
other resource types.

Type: [Lifecycle](API_Lifecycle.md "API_Lifecycle.md") object

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

**ResourceArn**

An ARN that uniquely identifies a resource. The format of the ARN depends on the
resource type.

Type: String

Required: No

**ResourceName**

The non-unique name of the resource that
belongs to the specified backup.

Type: String

Required: No

**ResourceType**

The type of AWS resource saved as a recovery point; for example, an
Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database. For Windows Volume Shadow Copy Service (VSS) backups, the only
supported resource type is Amazon EC2.

Type: String

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

Required: No

**SourceBackupVaultArn**

The backup vault where the recovery point was originally copied from. If the recovery
point is restored to the same account this value will be `null`.

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

The type of vault in which the described recovery point is stored.

Type: String

Valid Values: `BACKUP_VAULT | LOGICALLY_AIR_GAPPED_BACKUP_VAULT | RESTORE_ACCESS_BACKUP_VAULT`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/RecoveryPointByBackupVault.md "../../../goto/SdkForCpp/backup-2018-11-15/RecoveryPointByBackupVault.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/RecoveryPointByBackupVault.md "../../../goto/SdkForJavaV2/backup-2018-11-15/RecoveryPointByBackupVault.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/RecoveryPointByBackupVault.md "../../../goto/SdkForRubyV3/backup-2018-11-15/RecoveryPointByBackupVault.md")
