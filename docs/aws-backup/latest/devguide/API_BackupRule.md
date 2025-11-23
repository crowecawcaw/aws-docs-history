# BackupRule

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

IndexActions is an array you use to specify how backup data should
be indexed.

eEach BackupRule can have 0 or 1 IndexAction, as each backup can have up
to one index associated with it.

Within the array is ResourceType. Only one will be accepted for each BackupRule.

Type: Array of [IndexAction](API_IndexAction.md "API_IndexAction.md") objects

Required: No

**Lifecycle**

The lifecycle defines when a protected resource is transitioned to cold storage and when
it expires. AWS Backup transitions and expires backups automatically according to
the lifecycle that you define.

Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
days. Therefore, the “retention” setting must be 90 days greater than the “transition to
cold after days” setting. The “transition to cold after days” setting cannot be changed
after a backup has been transitioned to cold.

Resource types that can transition to cold storage are listed in the [Feature availability
by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") table. AWS Backup ignores this expression for other resource types.

Type: [Lifecycle](API_Lifecycle.md "API_Lifecycle.md") object

Required: No

**RecoveryPointTags**

The tags that are assigned to resources that are associated
with this rule when restored from backup.

Type: String to string map

Required: No

**RuleId**

Uniquely identifies a rule that is used to schedule the backup of a selection of
resources.

Type: String

Required: No

**ScanActions**

Contains your scanning configuration for the backup rule and includes the malware scanner, and scan mode of either full or incremental.

Type: Array of [ScanAction](API_ScanAction.md "API_ScanAction.md") objects

Required: No

**ScheduleExpression**

A cron expression in UTC specifying when AWS Backup initiates a backup job.
When no CRON expression is provided, AWS Backup will use the default
expression `cron(0 5 ? * * *)`.

For more information about AWS cron expressions, see [Schedule Expressions for Rules](../../../AmazonCloudWatch/latest/events/ScheduledEvents.md "../../../AmazonCloudWatch/latest/events/ScheduledEvents.md") in the _Amazon CloudWatch Events User
Guide_.

Two examples of AWS cron expressions are `15 * ? * * *` (take
a backup every hour at 15 minutes past the hour) and `0 12 * * ? *` (take a
backup every day at 12 noon UTC).

For a table of examples, click the preceding link and scroll down the page.

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

During the start window, the backup job status remains in `CREATED` status until it
has successfully begun or until the start window time has run out. If within the start
window time AWS Backup receives an error that allows the job to be retried,
AWS Backup will automatically retry to begin the job at least every 10 minutes
until the backup
successfully begins (the job status changes to `RUNNING`) or until the job status
changes to `EXPIRED` (which is expected to occur when the start window time is over).

Type: Long

Required: No

**TargetLogicallyAirGappedBackupVaultArn**

The ARN of a logically air-gapped vault. ARN must be in the same account and Region.
If provided, supported fully managed resources back up directly to logically air-gapped vault,
while other supported resources create a temporary (billable) snapshot in backup vault,
then copy it to logically air-gapped vault. Unsupported resources only back up to the specified
backup vault.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/BackupRule.md "../../../goto/SdkForCpp/backup-2018-11-15/BackupRule.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/BackupRule.md "../../../goto/SdkForJavaV2/backup-2018-11-15/BackupRule.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/BackupRule.md "../../../goto/SdkForRubyV3/backup-2018-11-15/BackupRule.md")
