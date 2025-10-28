# BackupPlansListMember

Contains metadata about a backup plan.

## Contents

**AdvancedBackupSettings**

Contains a list of `BackupOptions` for a resource type.

Type: Array of [AdvancedBackupSetting](API_AdvancedBackupSetting.md "API_AdvancedBackupSetting.md") objects

Required: No

**BackupPlanArn**

An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
`arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`.

Type: String

Required: No

**BackupPlanId**

Uniquely identifies a backup plan.

Type: String

Required: No

**BackupPlanName**

The display name of a saved backup plan.

Type: String

Required: No

**CreationDate**

The date and time a resource backup plan is created, in Unix format and Coordinated
Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

Required: No

**CreatorRequestId**

A unique string that identifies the request and allows failed requests to be retried
without the risk of running the operation twice. This parameter is optional.

If used, this parameter must contain 1 to 50 alphanumeric or '-\_.' characters.

Type: String

Required: No

**DeletionDate**

The date and time a backup plan is deleted, in Unix format and Coordinated Universal
Time (UTC). The value of `DeletionDate` is accurate to milliseconds. For
example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

Required: No

**LastExecutionDate**

The last time this backup plan was run. A date and time, in
Unix format and Coordinated Universal Time (UTC). The value of
`LastExecutionDate` is accurate to milliseconds. For example, the value
1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

Type: Timestamp

Required: No

**VersionId**

Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes
long. Version IDs cannot be edited.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/BackupPlansListMember.md "../../../goto/SdkForCpp/backup-2018-11-15/BackupPlansListMember.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/BackupPlansListMember.md "../../../goto/SdkForJavaV2/backup-2018-11-15/BackupPlansListMember.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/BackupPlansListMember.md "../../../goto/SdkForRubyV3/backup-2018-11-15/BackupPlansListMember.md")
