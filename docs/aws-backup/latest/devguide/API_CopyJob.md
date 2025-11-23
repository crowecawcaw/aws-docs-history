# CopyJob

Contains detailed information about a copy job.

## Contents

**AccountId**

The account ID that owns the copy job.

Type: String

Pattern: `^[0-9]{12}$`

Required: No

**BackupSizeInBytes**

The size, in bytes, of a copy job.

Type: Long

Required: No

**ChildJobsInState**

This returns the statistics of the included
child (nested) copy jobs.

Type: String to long map

Valid Keys: `CREATED | RUNNING | COMPLETED | FAILED | PARTIAL`

Required: No

**CompletionDate**

The date and time a copy job is completed, in Unix format and Coordinated Universal Time
(UTC). The value of `CompletionDate` is accurate to milliseconds. For example,
the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

Type: Timestamp

Required: No

**CompositeMemberIdentifier**

The identifier of a resource within a composite group, such as
nested (child) recovery point belonging to a composite (parent) stack. The
ID is transferred from
the [logical ID](../../../AWSCloudFormation/latest/UserGuide/resources-section-structure.md#resources-section-structure-syntax "../../../AWSCloudFormation/latest/UserGuide/resources-section-structure.md#resources-section-structure-syntax") within a stack.

Type: String

Required: No

**CopyJobId**

Uniquely identifies a copy job.

Type: String

Required: No

**CreatedBy**

Contains information about the backup plan and rule that AWS Backup used to
initiate the recovery point backup.

Type: [RecoveryPointCreator](API_RecoveryPointCreator.md "API_RecoveryPointCreator.md") object

Required: No

**CreatedByBackupJobId**

The backup job ID that initiated this copy job. Only applicable to scheduled copy
jobs and automatic copy jobs to logically air-gapped vault.

Type: String

Required: No

**CreationDate**

The date and time a copy job is created, in Unix format and Coordinated Universal Time
(UTC). The value of `CreationDate` is accurate to milliseconds. For example, the
value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

Type: Timestamp

Required: No

**DestinationBackupVaultArn**

An Amazon Resource Name (ARN) that uniquely identifies a destination copy vault; for
example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.

Type: String

Required: No

**DestinationEncryptionKeyArn**

The Amazon Resource Name (ARN) of the KMS key used to encrypt the copied backup in the destination vault. This can be a customer-managed key or an AWS managed key.

Type: String

Required: No

**DestinationRecoveryPointArn**

An ARN that uniquely identifies a destination recovery point; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.

Type: String

Required: No

**DestinationRecoveryPointLifecycle**

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

**DestinationVaultLockState**

The lock state of the destination backup vault. For logically air-gapped vaults, this indicates whether the vault is locked in compliance mode. Valid values include `LOCKED` and `UNLOCKED`.

Type: String

Required: No

**DestinationVaultType**

The type of destination backup vault where the copied recovery point is stored. Valid values are `BACKUP_VAULT` for standard backup vaults and `LOGICALLY_AIR_GAPPED_BACKUP_VAULT` for logically air-gapped vaults.

Type: String

Required: No

**IamRoleArn**

Specifies the IAM role ARN used to copy the target recovery point; for example,
`arn:aws:iam::123456789012:role/S3Access`.

Type: String

Required: No

**IsParent**

This is a boolean value indicating this is
a parent (composite) copy job.

Type: Boolean

Required: No

**MessageCategory**

This parameter is the job count for the specified
message category.

Example strings may include `AccessDenied`,
`SUCCESS`, `AGGREGATE_ALL`, and
`InvalidParameters`. See
[Monitoring](monitoring.md "monitoring.md")
for a list of MessageCategory strings.

The the value ANY returns count of all message categories.

`AGGREGATE_ALL` aggregates job counts
for all message categories and returns the sum

Type: String

Required: No

**NumberOfChildJobs**

The number of child (nested) copy jobs.

Type: Long

Required: No

**ParentJobId**

This uniquely identifies a request to AWS Backup
to copy a resource. The return will be the
parent (composite) job ID.

Type: String

Required: No

**ResourceArn**

The AWS resource to be copied; for example, an Amazon Elastic Block Store
(Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS)
database.

Type: String

Required: No

**ResourceName**

The non-unique name of the resource that
belongs to the specified backup.

Type: String

Required: No

**ResourceType**

The type of AWS resource to be copied; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

Type: String

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

Required: No

**SourceBackupVaultArn**

An Amazon Resource Name (ARN) that uniquely identifies a source copy vault; for example,
`arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.

Type: String

Required: No

**SourceRecoveryPointArn**

An ARN that uniquely identifies a source recovery point; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.

Type: String

Required: No

**State**

The current state of a copy job.

Type: String

Valid Values: `CREATED | RUNNING | COMPLETED | FAILED | PARTIAL`

Required: No

**StatusMessage**

A detailed message explaining the status of the job to copy a resource.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/CopyJob.md "../../../goto/SdkForCpp/backup-2018-11-15/CopyJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/CopyJob.md "../../../goto/SdkForJavaV2/backup-2018-11-15/CopyJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/CopyJob.md "../../../goto/SdkForRubyV3/backup-2018-11-15/CopyJob.md")
