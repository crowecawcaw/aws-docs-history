# BackupJob

Contains detailed information about a backup job.

## Contents

**AccountId**

The account ID that owns the backup job.

Type: String

Pattern: `^[0-9]{12}$`

Required: No

**BackupJobId**

Uniquely identifies a request to AWS Backup to back up a resource.

Type: String

Required: No

**BackupOptions**

Specifies the backup option for a selected resource. This option is only available for
Windows Volume Shadow Copy Service (VSS) backup jobs.

Valid values: Set to `"WindowsVSS":"enabled"` to enable the
`WindowsVSS` backup option and create a Windows VSS backup. Set to
`"WindowsVSS":"disabled"` to create a regular backup. If you specify an
invalid option, you get an `InvalidParameterValueException` exception.

Type: String to string map

Key Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

Value Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

Required: No

**BackupSizeInBytes**

The size, in bytes, of a backup (recovery point).

This value can render differently depending on the resource type as AWS Backup pulls in data information from other AWS services. For example, the
value returned may show a value of `0`, which may differ from the
anticipated value.

The expected behavior for values by resource type are described as follows:

- Amazon Aurora, Amazon DocumentDB, and Amazon Neptune do
  not have this value populate from the operation
  `GetBackupJobStatus`.
- For Amazon DynamoDB with advanced features, this value refers to the size
  of the recovery point (backup).
- Amazon EC2 and Amazon EBS show volume size (provisioned storage)
  returned as part of this value. Amazon EBS does not return backup size
  information; snapshot size will have the same value as the original resource that was
  backed up.
- For Amazon EFS, this value refers to the delta bytes transferred during a
  backup.
- Amazon FSx does not populate this value from the operation
  `GetBackupJobStatus` for FSx file systems.
- An Amazon RDS instance will show as `0`.
- For virtual machines running VMware, this value is passed to AWS Backup
  through an asynchronous workflow, which can mean this displayed value can
  under-represent the actual backup size.

Type: Long

Required: No

**BackupType**

Represents the type of backup for a backup job.

Type: String

Required: No

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

**BytesTransferred**

The size in bytes transferred to a backup vault at the time that the job status was
queried.

Type: Long

Required: No

**CompletionDate**

The date and time a job to create a backup job is completed, in Unix format and
Coordinated Universal Time (UTC). The value of `CompletionDate` is accurate to
milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
12:11:30.087 AM.

Type: Timestamp

Required: No

**CreatedBy**

Contains identifying information about the creation of a backup job, including the
`BackupPlanArn`, `BackupPlanId`, `BackupPlanVersion`,
and `BackupRuleId` of the backup plan used to create it.

Type: [RecoveryPointCreator](API_RecoveryPointCreator.md "API_RecoveryPointCreator.md") object

Required: No

**CreationDate**

The date and time a backup job is created, in Unix format and Coordinated Universal Time
(UTC). The value of `CreationDate` is accurate to milliseconds. For example, the
value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

Type: Timestamp

Required: No

**EncryptionKeyArn**

The Amazon Resource Name (ARN) of the KMS key used to encrypt the backup. This can be a customer-managed key or an AWS managed key, depending on the vault configuration.

Type: String

Required: No

**ExpectedCompletionDate**

The date and time a job to back up resources is expected to be completed, in Unix format
and Coordinated Universal Time (UTC). The value of `ExpectedCompletionDate` is
accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January
26, 2018 12:11:30.087 AM.

Type: Timestamp

Required: No

**IamRoleArn**

Specifies the IAM role ARN used to create the target recovery point. IAM roles other
than the default role must include either `AWSBackup` or `AwsBackup`
in the role name. For example,
`arn:aws:iam::123456789012:role/AWSBackupRDSAccess`. Role names without those
strings lack permissions to perform backup jobs.

Type: String

Required: No

**InitiationDate**

The date on which the backup
job was initiated.

Type: Timestamp

Required: No

**IsEncrypted**

A boolean value indicating whether the backup is encrypted. All backups in AWS Backup are encrypted, but this field indicates the encryption status for transparency.

Type: Boolean

Required: No

**IsParent**

This is a boolean value indicating this is
a parent (composite) backup job.

Type: Boolean

Required: No

**MessageCategory**

This parameter is the job count for the specified
message category.

Example strings may include `AccessDenied`,
`SUCCESS`, `AGGREGATE_ALL`, and
`INVALIDPARAMETERS`. See
[Monitoring](monitoring.md "monitoring.md")
for a list of MessageCategory strings.

The the value ANY returns count of all message categories.

`AGGREGATE_ALL` aggregates job counts
for all message categories and returns the sum.

Type: String

Required: No

**ParentJobId**

This uniquely identifies a request to AWS Backup
to back up a resource. The return will be the
parent (composite) job ID.

Type: String

Required: No

**PercentDone**

Contains an estimated percentage complete of a job at the time the job status was
queried.

Type: String

Required: No

**RecoveryPointArn**

An ARN that uniquely identifies a recovery point; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.

Type: String

Required: No

**RecoveryPointLifecycle**

Specifies the time period, in days, before a recovery point transitions to cold storage
or is deleted.

Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
days. Therefore, on the console, the retention setting must be 90 days greater than the
transition to cold after days setting. The transition to cold after days setting can't
be changed after a backup has been transitioned to cold.

Resource types that can transition to cold storage are listed in the [Feature
availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") table. AWS Backup ignores this expression for
other resource types.

To remove the existing lifecycle and retention periods and keep your recovery points indefinitely,
specify -1 for `MoveToColdStorageAfterDays` and `DeleteAfterDays`.

Type: [Lifecycle](API_Lifecycle.md "API_Lifecycle.md") object

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

The type of AWS resource to be backed up; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database. For Windows Volume Shadow Copy Service (VSS) backups, the only
supported resource type is Amazon EC2.

Type: String

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

Required: No

**StartBy**

Specifies the time in Unix format and Coordinated Universal Time (UTC) when a backup job
must be started before it is canceled. The value is calculated by adding the start window
to the scheduled time. So if the scheduled time were 6:00 PM and the start window is 2
hours, the `StartBy` time would be 8:00 PM on the date specified. The value of
`StartBy` is accurate to milliseconds. For example, the value 1516925490.087
represents Friday, January 26, 2018 12:11:30.087 AM.

Type: Timestamp

Required: No

**State**

The current state of a backup job.

Type: String

Valid Values: `CREATED | PENDING | RUNNING | ABORTING | ABORTED | COMPLETED | FAILED | EXPIRED | PARTIAL`

Required: No

**StatusMessage**

A detailed message explaining the status of the job to back up a resource.

Type: String

Required: No

**VaultLockState**

The lock state of the backup vault. For logically air-gapped vaults, this indicates whether the vault is locked in compliance mode. Valid values include `LOCKED` and `UNLOCKED`.

Type: String

Required: No

**VaultType**

The type of backup vault where the recovery point is stored. Valid values are `BACKUP_VAULT` for standard backup vaults and `LOGICALLY_AIR_GAPPED_BACKUP_VAULT` for logically air-gapped vaults.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/BackupJob.md "../../../goto/SdkForCpp/backup-2018-11-15/BackupJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/BackupJob.md "../../../goto/SdkForJavaV2/backup-2018-11-15/BackupJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/BackupJob.md "../../../goto/SdkForRubyV3/backup-2018-11-15/BackupJob.md")
