# BackupPlanInput

Contains an optional backup plan display name and an array of `BackupRule`
objects, each of which specifies a backup rule. Each rule in a backup plan is a separate
scheduled task.

## Contents

**BackupPlanName**

The display name of a backup plan. Must contain 1 to 50 alphanumeric or '-\_.'
characters.

Type: String

Required: Yes

**Rules**

An array of `BackupRule` objects, each of which specifies a scheduled task
that is used to back up a selection of resources.

Type: Array of [BackupRuleInput](API_BackupRuleInput.md "API_BackupRuleInput.md") objects

Required: Yes

**AdvancedBackupSettings**

Specifies a list of `BackupOptions` for each resource type. These settings
are only available for Windows Volume Shadow Copy Service (VSS) backup jobs.

Type: Array of [AdvancedBackupSetting](API_AdvancedBackupSetting.md "API_AdvancedBackupSetting.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/BackupPlanInput.md "../../../goto/SdkForCpp/backup-2018-11-15/BackupPlanInput.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/BackupPlanInput.md "../../../goto/SdkForJavaV2/backup-2018-11-15/BackupPlanInput.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/BackupPlanInput.md "../../../goto/SdkForRubyV3/backup-2018-11-15/BackupPlanInput.md")
