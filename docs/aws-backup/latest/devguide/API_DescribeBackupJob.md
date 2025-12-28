# DescribeBackupJob

Returns backup job details for the specified `BackupJobId`.

## Request Syntax

```
GET /backup-jobs/`backupJobId` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[backupJobId](#API_DescribeBackupJob_RequestSyntax "#API_DescribeBackupJob_RequestSyntax")**

Uniquely identifies a request to AWS Backup to back up a resource.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "AccountId": "***string***",
   "BackupJobId": "***string***",
   "BackupOptions": {
      "***string***" : "***string***"
   },
   "BackupSizeInBytes": ***number***,
   "BackupType": "***string***",
   "BackupVaultArn": "***string***",
   "BackupVaultName": "***string***",
   "BytesTransferred": ***number***,
   "ChildJobsInState": {
      "***string***" : ***number***
   },
   "CompletionDate": ***number***,
   "CreatedBy": {
      "BackupPlanArn": "***string***",
      "BackupPlanId": "***string***",
      "BackupPlanName": "***string***",
      "BackupPlanVersion": "***string***",
      "BackupRuleCron": "***string***",
      "BackupRuleId": "***string***",
      "BackupRuleName": "***string***",
      "BackupRuleTimezone": "***string***"
   },
   "CreationDate": ***number***,
   "EncryptionKeyArn": "***string***",
   "ExpectedCompletionDate": ***number***,
   "IamRoleArn": "***string***",
   "InitiationDate": ***number***,
   "IsEncrypted": ***boolean***,
   "IsParent": ***boolean***,
   "MessageCategory": "***string***",
   "NumberOfChildJobs": ***number***,
   "ParentJobId": "***string***",
   "PercentDone": "***string***",
   "RecoveryPointArn": "***string***",
   "RecoveryPointLifecycle": {
      "DeleteAfterDays": ***number***,
      "DeleteAfterEvent": "***string***",
      "MoveToColdStorageAfterDays": ***number***,
      "OptInToArchiveForSupportedResources": ***boolean***
   },
   "ResourceArn": "***string***",
   "ResourceName": "***string***",
   "ResourceType": "***string***",
   "StartBy": ***number***,
   "State": "***string***",
   "StatusMessage": "***string***",
   "VaultLockState": "***string***",
   "VaultType": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AccountId](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

Returns the account ID that owns the backup job.

Type: String

Pattern: `^[0-9]{12}$`

**[BackupJobId](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

Uniquely identifies a request to AWS Backup to back up a resource.

Type: String

**[BackupOptions](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

Represents the options specified as part of backup plan or on-demand backup job.

Type: String to string map

Key Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

Value Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

**[BackupSizeInBytes](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

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
- For Amazon EKS, this value refers to the size of your nested EKS recovery point.
- Amazon FSx does not populate this value from the operation
  `GetBackupJobStatus` for FSx file systems.
- An Amazon RDS instance will show as `0`.
- For virtual machines running VMware, this value is passed to AWS Backup
  through an asynchronous workflow, which can mean this displayed value can
  under-represent the actual backup size.

Type: Long

**[BackupType](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

Represents the actual backup type selected for a backup job. For example, if a
successful Windows Volume Shadow Copy Service (VSS) backup was taken,
`BackupType` returns `"WindowsVSS"`. If `BackupType` is
empty, then the backup type was a regular backup.

Type: String

**[BackupVaultArn](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example,
`arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.

Type: String

**[BackupVaultName](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

The name of a logical container where backups are stored. Backup vaults are identified
by names that are unique to the account used to create them and the AWS
Region where they are created.

Type: String

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

**[BytesTransferred](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

The size in bytes transferred to a backup vault at the time that the job status was
queried.

Type: Long

**[ChildJobsInState](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

This returns the statistics of the included child (nested) backup jobs.

Type: String to long map

Valid Keys: `CREATED | PENDING | RUNNING | ABORTING | ABORTED | COMPLETED | FAILED | EXPIRED | PARTIAL`

**[CompletionDate](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

The date and time that a job to create a backup job is completed, in Unix format and
Coordinated Universal Time (UTC). The value of `CompletionDate` is accurate to
milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
12:11:30.087 AM.

Type: Timestamp

**[CreatedBy](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

Contains identifying information about the creation of a backup job, including the
`BackupPlanArn`, `BackupPlanId`, `BackupPlanVersion`,
and `BackupRuleId` of the backup plan that is used to create it.

Type: [RecoveryPointCreator](API_RecoveryPointCreator.md "API_RecoveryPointCreator.md") object

**[CreationDate](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

The date and time that a backup job is created, in Unix format and Coordinated Universal
Time (UTC). The value of `CreationDate` is accurate to milliseconds. For
example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

**[EncryptionKeyArn](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

The Amazon Resource Name (ARN) of the KMS key used to encrypt the backup. This can be a customer-managed key or an AWS managed key, depending on the vault configuration.

Type: String

**[ExpectedCompletionDate](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

The date and time that a job to back up resources is expected to be completed, in Unix
format and Coordinated Universal Time (UTC). The value of
`ExpectedCompletionDate` is accurate to milliseconds. For example, the value
1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

Type: Timestamp

**[IamRoleArn](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

Specifies the IAM role ARN used to create the target recovery point; for example,
`arn:aws:iam::123456789012:role/S3Access`.

Type: String

**[InitiationDate](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

The date a backup job was initiated.

Type: Timestamp

**[IsEncrypted](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

A boolean value indicating whether the backup is encrypted. All backups in AWS Backup are encrypted, but this field indicates the encryption status for transparency.

Type: Boolean

**[IsParent](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

This returns the boolean value that a backup job is a parent (composite) job.

Type: Boolean

**[MessageCategory](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

The job count for the specified
message category.

Example strings may include `AccessDenied`, `SUCCESS`,
`AGGREGATE_ALL`, and `INVALIDPARAMETERS`. View [Monitoring](monitoring.md "monitoring.md")
for a list of accepted MessageCategory strings.

Type: String

**[NumberOfChildJobs](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

This returns the number of child (nested) backup jobs.

Type: Long

**[ParentJobId](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

This returns the parent (composite) resource backup job ID.

Type: String

**[PercentDone](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

Contains an estimated percentage that is complete of a job at the time the job status
was queried.

Type: String

**[RecoveryPointArn](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

An ARN that uniquely identifies a recovery point; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.

Type: String

**[RecoveryPointLifecycle](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

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

**[ResourceArn](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

An ARN that uniquely identifies a saved resource. The format of the ARN depends on the
resource type.

Type: String

**[ResourceName](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

The non-unique name of the resource that
belongs to the specified backup.

Type: String

**[ResourceType](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

The type of AWS resource to be backed up; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

Type: String

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

**[StartBy](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

Specifies the time in Unix format and Coordinated Universal Time (UTC) when a backup job
must be started before it is canceled. The value is calculated by adding the start window
to the scheduled time. So if the scheduled time were 6:00 PM and the start window is 2
hours, the `StartBy` time would be 8:00 PM on the date specified. The value of
`StartBy` is accurate to milliseconds. For example, the value 1516925490.087
represents Friday, January 26, 2018 12:11:30.087 AM.

Type: Timestamp

**[State](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

The current state of a backup job.

Type: String

Valid Values: `CREATED | PENDING | RUNNING | ABORTING | ABORTED | COMPLETED | FAILED | EXPIRED | PARTIAL`

**[StatusMessage](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

A detailed message explaining the status of the job to back up a resource.

Type: String

**[VaultLockState](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

The lock state of the backup vault. For logically air-gapped vaults, this indicates whether the vault is locked in compliance mode. Valid values include `LOCKED` and `UNLOCKED`.

Type: String

**[VaultType](#API_DescribeBackupJob_ResponseSyntax "#API_DescribeBackupJob_ResponseSyntax")**

The type of backup vault where the recovery point is stored. Valid values are `BACKUP_VAULT` for standard backup vaults and `LOGICALLY_AIR_GAPPED_BACKUP_VAULT` for logically air-gapped vaults.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**DependencyFailureException**

A dependent AWS service or resource returned an error to the AWS Backup service, and the action cannot be completed.

**Context**

**Type**

HTTP Status Code: 500

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

**MissingParameterValueException**

Indicates that a required parameter is missing.

**Context**

**Type**

HTTP Status Code: 400

**ResourceNotFoundException**

A resource that is required for the action doesn't exist.

**Context**

**Type**

HTTP Status Code: 400

**ServiceUnavailableException**

The request failed due to a temporary failure of the server.

**Context**

**Type**

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/DescribeBackupJob.md "../../../goto/cli2/backup-2018-11-15/DescribeBackupJob.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/DescribeBackupJob.md "../../../goto/DotNetSDKV3/backup-2018-11-15/DescribeBackupJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/DescribeBackupJob.md "../../../goto/SdkForCpp/backup-2018-11-15/DescribeBackupJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/DescribeBackupJob.md "../../../goto/SdkForGoV2/backup-2018-11-15/DescribeBackupJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/DescribeBackupJob.md "../../../goto/SdkForJavaV2/backup-2018-11-15/DescribeBackupJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeBackupJob.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeBackupJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/DescribeBackupJob.md "../../../goto/SdkForKotlin/backup-2018-11-15/DescribeBackupJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/DescribeBackupJob.md "../../../goto/SdkForPHPV3/backup-2018-11-15/DescribeBackupJob.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/DescribeBackupJob.md "../../../goto/boto3/backup-2018-11-15/DescribeBackupJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/DescribeBackupJob.md "../../../goto/SdkForRubyV3/backup-2018-11-15/DescribeBackupJob.md")
