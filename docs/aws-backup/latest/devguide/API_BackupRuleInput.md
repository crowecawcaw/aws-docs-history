# BackupRuleInput

Specifies a scheduled task used to back up a selection of resources.

## Contents

**RuleName**

A display name for a backup rule. Must contain 1 to 50 alphanumeric or '-\_.'
characters.

Type: String

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

Required: Yes

**TargetBackupVaultName**

The name of a logical container where backups are stored. Backup vaults are identified
by names that are unique to the account used to create them and the AWS
Region where they are created.

Type: String

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: Yes

**CompletionWindowMinutes**

A value in minutes after a backup job is successfully started before it must be
completed or it will be canceled by AWS Backup. This value is optional.

Type: Long

Required: No

**CopyActions**

An array of `CopyAction` objects, which contains the details of the copy
operation.

Type: Array of [CopyAction](API_CopyAction.md "API_CopyAction.md") objects

Required: No

**EnableContinuousBackup**

Specifies whether AWS Backup creates continuous backups. True causes AWS Backup to create continuous backups capable of point-in-time restore (PITR). False
(or not specified) causes AWS Backup to create snapshot backups.

Type: Boolean

Required: No

**IndexActions**

There can up to one IndexAction in each BackupRule, as each backup
can have 0 or 1 backup index associated with it.

Within the array is ResourceTypes. Only 1 resource type will
be accepted for each BackupRule. Valid values:

- `EBS` for Amazon Elastic Block Store
- `S3` for Amazon Simple Storage Service (Amazon S3)

Type: Array of [IndexAction](API_IndexAction.md "API_IndexAction.md") objects

Required: No

**Lifecycle**

The lifecycle defines when a protected resource is transitioned to cold storage and when
it expires. AWS Backup will transition and expire backups automatically according
to the lifecycle that you define.

Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
days. Therefore, the “retention” setting must be 90 days greater than the “transition to
cold after days” setting. The “transition to cold after days” setting cannot be changed
after a backup has been transitioned to cold storage.

Resource types that can transition to cold storage are listed in the [Feature availability
by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") table. AWS Backup ignores this expression for other resource types.

This parameter has a maximum value of 100 years (36,500 days).

Type: [Lifecycle](API_Lifecycle.md "API_Lifecycle.md") object

Required: No

**RecoveryPointTags**

The tags to assign to the resources.

Type: String to string map

Required: No

**ScheduleExpression**

A CRON expression in UTC specifying when AWS Backup initiates a backup
job. When no CRON expression is provided, AWS Backup will use the default
expression `cron(0 5 ? * * *)`.

Type: String

Required: No

**ScheduleExpressionTimezone**

The timezone in which the schedule expression is set. By default,
ScheduleExpressions are in UTC. You can modify this to a specified timezone.

Type: String

Required: No

**StartWindowMinutes**

A value in minutes after a backup is scheduled before a job will be canceled if it
doesn't start successfully. This value is optional.
If this value is included, it must be at least 60 minutes to avoid errors.

This parameter has a maximum value of 100 years (52,560,000 minutes).

During the start window, the backup job status remains in `CREATED` status until it
has successfully begun or until the start window time has run out. If within the start
window time AWS Backup receives an error that allows the job to be retried,
AWS Backup will automatically retry to begin the job at least every 10 minutes
until the backup
successfully begins (the job status changes to `RUNNING`) or until the job status
changes to `EXPIRED` (which is expected to occur when the start window time is over).

Type: Long

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/BackupRuleInput.md "../../../goto/SdkForCpp/backup-2018-11-15/BackupRuleInput.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/BackupRuleInput.md "../../../goto/SdkForJavaV2/backup-2018-11-15/BackupRuleInput.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/BackupRuleInput.md "../../../goto/SdkForRubyV3/backup-2018-11-15/BackupRuleInput.md")
