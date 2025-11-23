# DescribeRecoveryPoint

Returns metadata associated with a recovery point, including ID, status, encryption, and
lifecycle.

## Request Syntax

```
GET /backup-vaults/`backupVaultName`/recovery-points/`recoveryPointArn`?backupVaultAccountId=`BackupVaultAccountId` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[BackupVaultAccountId](#API_DescribeRecoveryPoint_RequestSyntax "#API_DescribeRecoveryPoint_RequestSyntax")**

The account ID of the specified backup vault.

Pattern: `^[0-9]{12}$`

**[backupVaultName](#API_DescribeRecoveryPoint_RequestSyntax "#API_DescribeRecoveryPoint_RequestSyntax")**

The name of a logical container where backups are stored. Backup vaults are identified
by names that are unique to the account used to create them and the AWS
Region where they are created.

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: Yes

**[recoveryPointArn](#API_DescribeRecoveryPoint_RequestSyntax "#API_DescribeRecoveryPoint_RequestSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupSizeInBytes": ***number***,
   "BackupVaultArn": "***string***",
   "BackupVaultName": "***string***",
   "CalculatedLifecycle": {
      "DeleteAt": ***number***,
      "MoveToColdStorageAt": ***number***
   },
   "CompletionDate": ***number***,
   "CompositeMemberIdentifier": "***string***",
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
   "EncryptionKeyType": "***string***",
   "IamRoleArn": "***string***",
   "IndexStatus": "***string***",
   "IndexStatusMessage": "***string***",
   "InitiationDate": ***number***,
   "IsEncrypted": ***boolean***,
   "IsParent": ***boolean***,
   "LastRestoreTime": ***number***,
   "Lifecycle": {
      "DeleteAfterDays": ***number***,
      "DeleteAfterEvent": "***string***",
      "MoveToColdStorageAfterDays": ***number***,
      "OptInToArchiveForSupportedResources": ***boolean***
   },
   "ParentRecoveryPointArn": "***string***",
   "RecoveryPointArn": "***string***",
   "ResourceArn": "***string***",
   "ResourceName": "***string***",
   "ResourceType": "***string***",
   "ScanResults": [
      {
         "Findings": [ "***string***" ],
         "LastScanTimestamp": ***number***,
         "MalwareScanner": "***string***",
         "ScanJobState": "***string***"
      }
   ],
   "SourceBackupVaultArn": "***string***",
   "Status": "***string***",
   "StatusMessage": "***string***",
   "StorageClass": "***string***",
   "VaultType": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[BackupSizeInBytes](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

The size, in bytes, of a backup.

Type: Long

**[BackupVaultArn](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

An ARN that uniquely identifies a backup vault; for example,
`arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.

Type: String

**[BackupVaultName](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

The name of a logical container where backups are stored. Backup vaults are identified
by names that are unique to the account used to create them and the Region where they are
created.

Type: String

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

**[CalculatedLifecycle](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

A `CalculatedLifecycle` object containing `DeleteAt` and
`MoveToColdStorageAt` timestamps.

Type: [CalculatedLifecycle](API_CalculatedLifecycle.md "API_CalculatedLifecycle.md") object

**[CompletionDate](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

The date and time that a job to create a recovery point is completed, in Unix format and
Coordinated Universal Time (UTC). The value of `CompletionDate` is accurate to
milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
12:11:30.087 AM.

Type: Timestamp

**[CompositeMemberIdentifier](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

The identifier of a resource within a composite group, such as
nested (child) recovery point belonging to a composite (parent) stack. The
ID is transferred from the [logical ID](../../../AWSCloudFormation/latest/UserGuide/resources-section-structure.md#resources-section-structure-syntax "../../../AWSCloudFormation/latest/UserGuide/resources-section-structure.md#resources-section-structure-syntax") within a stack.

Type: String

**[CreatedBy](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

Contains identifying information about the creation of a recovery point, including the
`BackupPlanArn`, `BackupPlanId`, `BackupPlanVersion`,
and `BackupRuleId` of the backup plan used to create it.

Type: [RecoveryPointCreator](API_RecoveryPointCreator.md "API_RecoveryPointCreator.md") object

**[CreationDate](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

The date and time that a recovery point is created, in Unix format and Coordinated
Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

**[EncryptionKeyArn](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

The server-side encryption key used to protect your backups; for example,
`arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`.

Type: String

**[EncryptionKeyType](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

The type of encryption key used for the recovery point. Valid values are CUSTOMER_MANAGED_KMS_KEY for customer-managed keys or AWS_OWNED_KMS_KEY for AWS-owned keys.

Type: String

Valid Values: `AWS_OWNED_KMS_KEY | CUSTOMER_MANAGED_KMS_KEY`

**[IamRoleArn](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

Specifies the IAM role ARN used to create the target recovery point; for example,
`arn:aws:iam::123456789012:role/S3Access`.

Type: String

**[IndexStatus](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

This is the current status for the backup index associated with the specified recovery
point.

Statuses are: `PENDING` | `ACTIVE` | `FAILED` |
`DELETING`

A recovery point with an index that has the status of `ACTIVE` can be
included in a search.

Type: String

Valid Values: `PENDING | ACTIVE | FAILED | DELETING`

**[IndexStatusMessage](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

A string in the form of a detailed message explaining the status of a backup index
associated with the recovery point.

Type: String

**[InitiationDate](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

The date and time when the backup job that created this recovery point was initiated, in
Unix format and Coordinated Universal Time (UTC).

Type: Timestamp

**[IsEncrypted](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

A Boolean value that is returned as `TRUE` if the specified recovery point is
encrypted, or `FALSE` if the recovery point is not encrypted.

Type: Boolean

**[IsParent](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

This returns the boolean value that a recovery point is a parent (composite) job.

Type: Boolean

**[LastRestoreTime](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

The date and time that a recovery point was last restored, in Unix format and
Coordinated Universal Time (UTC). The value of `LastRestoreTime` is accurate to
milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
12:11:30.087 AM.

Type: Timestamp

**[Lifecycle](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

The lifecycle defines when a protected resource is transitioned to cold storage and when
it expires. AWS Backup transitions and expires backups automatically according to
the lifecycle that you define.

Backups that are transitioned to cold storage must be stored in cold storage for a
minimum of 90 days. Therefore, the “retention” setting must be 90 days greater than the
“transition to cold after days” setting. The “transition to cold after days” setting cannot
be changed after a backup has been transitioned to cold.

Resource types that can transition to cold storage are listed in the [Feature
availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") table. AWS Backup ignores this expression for other resource types.

Type: [Lifecycle](API_Lifecycle.md "API_Lifecycle.md") object

**[ParentRecoveryPointArn](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

This is an ARN that uniquely identifies a parent (composite) recovery point; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.

Type: String

**[RecoveryPointArn](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

An ARN that uniquely identifies a recovery point; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.

Type: String

**[ResourceArn](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

An ARN that uniquely identifies a saved resource. The format of the ARN depends on the
resource type.

Type: String

**[ResourceName](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

The name of the resource that belongs to the specified backup.

Type: String

**[ResourceType](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

The type of AWS resource to save as a recovery point; for example, an
Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

Type: String

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

**[ScanResults](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

Contains the latest scanning results against the recovery point and currently include `MalwareScanner`, `ScanJobState`, `Findings`, and `LastScanTimestamp`

Type: Array of [ScanResult](API_ScanResult.md "API_ScanResult.md") objects

Array Members: Minimum number of 0 items. Maximum number of 5 items.

**[SourceBackupVaultArn](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies the source vault where the
resource was originally backed up in; for example,
`arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`. If the recovery is
restored to the same AWS account or Region, this value will be
`null`.

Type: String

**[Status](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

A status code specifying the state of the recovery point. For more information, see
[Recovery point status](applicationstackbackups.md#cfnrecoverypointstatus "applicationstackbackups.md#cfnrecoverypointstatus") in the _AWS Backup Developer
Guide_.

- `CREATING` status indicates that an AWS Backup job has been
  initiated for a resource. The backup process has started and is actively processing
  a backup job for the associated recovery point.
- `AVAILABLE` status indicates that the backup was successfully created
  for the recovery point. The backup process has completed without any issues, and the
  recovery point is now ready for use.
- `PARTIAL` status indicates a composite recovery point has one or more
  nested recovery points that were not in the backup.
- `EXPIRED` status indicates that the recovery point has exceeded its retention
  period, but AWS Backup lacks permission or is otherwise unable to delete it. To
  manually delete these recovery points, see [Step 3:
  Delete the recovery points](gs-cleanup-resources.md#cleanup-backups "gs-cleanup-resources.md#cleanup-backups") in the _Clean up resources_
  section of _Getting started_.
- `STOPPED` status occurs on a continuous backup where a user has taken some
  action that causes the continuous backup to be disabled. This can be caused by the removal
  of permissions, turning off versioning, turning off events being sent to EventBridge,
  or disabling the EventBridge rules that are put in place by AWS Backup. For
  recovery points of Amazon S3, Amazon RDS, and Amazon Aurora
  resources, this status occurs when the retention period of a continuous backup rule is
  changed.

To resolve `STOPPED` status, ensure that all requested permissions are in
place and that versioning is enabled on the S3 bucket. Once these conditions are met, the
next instance of a backup rule running will result in a new continuous recovery point being
created. The recovery points with STOPPED status do not need to be deleted.

For SAP HANA on Amazon EC2
`STOPPED` status occurs due to user action, application misconfiguration, or
backup failure. To ensure that future continuous backups succeed, refer to the recovery
point status and check SAP HANA for details.

Type: String

Valid Values: `COMPLETED | PARTIAL | DELETING | EXPIRED | AVAILABLE | STOPPED | CREATING`

**[StatusMessage](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

A status message explaining the status of the recovery point.

Type: String

**[StorageClass](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

Specifies the storage class of the recovery point. Valid values are `WARM` or
`COLD`.

Type: String

Valid Values: `WARM | COLD | DELETED`

**[VaultType](#API_DescribeRecoveryPoint_ResponseSyntax "#API_DescribeRecoveryPoint_ResponseSyntax")**

The type of vault in which the described recovery point is stored.

Type: String

Valid Values: `BACKUP_VAULT | LOGICALLY_AIR_GAPPED_BACKUP_VAULT | RESTORE_ACCESS_BACKUP_VAULT`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/DescribeRecoveryPoint.md "../../../goto/cli2/backup-2018-11-15/DescribeRecoveryPoint.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/DescribeRecoveryPoint.md "../../../goto/DotNetSDKV3/backup-2018-11-15/DescribeRecoveryPoint.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/DescribeRecoveryPoint.md "../../../goto/SdkForCpp/backup-2018-11-15/DescribeRecoveryPoint.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/DescribeRecoveryPoint.md "../../../goto/SdkForGoV2/backup-2018-11-15/DescribeRecoveryPoint.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/DescribeRecoveryPoint.md "../../../goto/SdkForJavaV2/backup-2018-11-15/DescribeRecoveryPoint.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeRecoveryPoint.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeRecoveryPoint.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/DescribeRecoveryPoint.md "../../../goto/SdkForKotlin/backup-2018-11-15/DescribeRecoveryPoint.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/DescribeRecoveryPoint.md "../../../goto/SdkForPHPV3/backup-2018-11-15/DescribeRecoveryPoint.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/DescribeRecoveryPoint.md "../../../goto/boto3/backup-2018-11-15/DescribeRecoveryPoint.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/DescribeRecoveryPoint.md "../../../goto/SdkForRubyV3/backup-2018-11-15/DescribeRecoveryPoint.md")
