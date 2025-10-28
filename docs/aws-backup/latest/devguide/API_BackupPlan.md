# BackupPlan

Contains an optional backup plan display name and an array of `BackupRule`
objects, each of which specifies a backup rule. Each rule in a backup plan is a separate
scheduled task and can back up a different selection of AWS
resources.

## Contents

**BackupPlanName**

The display name of a backup plan. Must contain only alphanumeric or '-\_.'
special characters.

If this is set in the console, it can contain 1 to 50 characters; if this
is set through CLI or API, it can contain 1 to 200 characters.

Type: String

Required: Yes

**Rules**

An array of `BackupRule` objects, each of which specifies a scheduled task
that is used to back up a selection of resources.

Type: Array of [BackupRule](API_BackupRule.md "API_BackupRule.md") objects

Required: Yes

**AdvancedBackupSettings**

Contains a list of `BackupOptions` for each resource type.

Type: Array of [AdvancedBackupSetting](API_AdvancedBackupSetting.md "API_AdvancedBackupSetting.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/BackupPlan.md "../../../goto/SdkForCpp/backup-2018-11-15/BackupPlan.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/BackupPlan.md "../../../goto/SdkForJavaV2/backup-2018-11-15/BackupPlan.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/BackupPlan.md "../../../goto/SdkForRubyV3/backup-2018-11-15/BackupPlan.md")
