# IndexedRecoveryPoint

This is a recovery point that has an associated backup index.

Only recovery points with a backup index can be
included in a search.

## Contents

**BackupCreationDate**

The date and time that a backup was created, in Unix format and Coordinated
Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

Required: No

**BackupVaultArn**

An ARN that uniquely identifies the backup vault where the recovery
point index is stored.

For example,
`arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.

Type: String

Required: No

**IamRoleArn**

This specifies the IAM role ARN used for this operation.

For example, arn:aws:iam::123456789012:role/S3Access

Type: String

Required: No

**IndexCreationDate**

The date and time that a backup index was created, in Unix format and Coordinated
Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

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

A string in the form of a detailed message explaining the status of a backup index associated
with the recovery point.

Type: String

Required: No

**RecoveryPointArn**

An ARN that uniquely identifies a recovery point; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`

Type: String

Required: No

**ResourceType**

The resource type of the indexed recovery point.

- `EBS` for Amazon Elastic Block Store
- `S3` for Amazon Simple Storage Service (Amazon S3)

Type: String

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

Required: No

**SourceResourceArn**

A string of the Amazon Resource Name (ARN) that uniquely identifies
the source resource.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/IndexedRecoveryPoint.md "../../../goto/SdkForCpp/backup-2018-11-15/IndexedRecoveryPoint.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/IndexedRecoveryPoint.md "../../../goto/SdkForJavaV2/backup-2018-11-15/IndexedRecoveryPoint.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/IndexedRecoveryPoint.md "../../../goto/SdkForRubyV3/backup-2018-11-15/IndexedRecoveryPoint.md")
