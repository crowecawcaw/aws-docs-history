# RestoreTestingPlanForUpdate

This contains metadata about a restore testing plan.

## Contents

**RecoveryPointSelection**

Required: `Algorithm`; `RecoveryPointTypes`;
`IncludeVaults` (_one or more_).

Optional: _SelectionWindowDays_ (_'30' if
not specified_); `ExcludeVaults` (defaults to empty
list if not listed).

Type: [RestoreTestingRecoveryPointSelection](API_RestoreTestingRecoveryPointSelection.md "API_RestoreTestingRecoveryPointSelection.md") object

Required: No

**ScheduleExpression**

A CRON expression in specified timezone when a restore testing plan is executed. When no
CRON expression is provided, AWS Backup will use the default expression
`cron(0 5 ? * * *)`.

Type: String

Required: No

**ScheduleExpressionTimezone**

Optional. This is the timezone in which the schedule
expression is set. By default, ScheduleExpressions are in UTC.
You can modify this to a specified timezone.

Type: String

Required: No

**StartWindowHours**

Defaults to 24 hours.

A value in hours after a restore test is scheduled before a
job will be canceled if it doesn't start successfully. This value
is optional. If this value is included, this parameter has a
maximum value of 168 hours (one week).

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/RestoreTestingPlanForUpdate.md "../../../goto/SdkForCpp/backup-2018-11-15/RestoreTestingPlanForUpdate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingPlanForUpdate.md "../../../goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingPlanForUpdate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingPlanForUpdate.md "../../../goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingPlanForUpdate.md")
