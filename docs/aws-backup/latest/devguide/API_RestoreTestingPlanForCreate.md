# RestoreTestingPlanForCreate

This contains metadata about a restore testing plan.

## Contents

**RecoveryPointSelection**

`RecoveryPointSelection` has five parameters (three required and two
optional). The values you specify determine which recovery point is included in the restore
test. You must indicate with `Algorithm` if you want the latest recovery point
within your `SelectionWindowDays` or if you want a random recovery point, and
you must indicate through `IncludeVaults` from which vaults the recovery points
can be chosen.

`Algorithm` (_required_) Valid values:
"`LATEST_WITHIN_WINDOW`" or "`RANDOM_WITHIN_WINDOW`".

`Recovery point types` (_required_) Valid values:
"`SNAPSHOT`" and/or "`CONTINUOUS`". Include `SNAPSHOT`
to restore only snapshot recovery points; include `CONTINUOUS` to restore
continuous recovery points (point in time restore / PITR); use both to restore either a
snapshot or a continuous recovery point. The recovery point will be determined by the value
for `Algorithm`.

`IncludeVaults` (_required_). You must include one or more
backup vaults. Use the wildcard ["\*"] or specific ARNs.

`SelectionWindowDays` (_optional_) Value must be an
integer (in days) from 1 to 365. If not included, the value defaults to
`30`.

`ExcludeVaults` (_optional_). You can choose to input one
or more specific backup vault ARNs to exclude those vaults' contents from restore
eligibility. Or, you can include a list of selectors. If this parameter and its value are
not included, it defaults to empty list.

Type: [RestoreTestingRecoveryPointSelection](API_RestoreTestingRecoveryPointSelection.md "API_RestoreTestingRecoveryPointSelection.md") object

Required: Yes

**RestoreTestingPlanName**

The RestoreTestingPlanName is a unique string that is the name
of the restore testing plan. This cannot be changed after creation,
and it must consist of only alphanumeric characters and underscores.

Type: String

Required: Yes

**ScheduleExpression**

A CRON expression in specified timezone when a restore
testing plan is executed. When no CRON expression is provided, AWS Backup will use the default
expression `cron(0 5 ? * * *)`.

Type: String

Required: Yes

**ScheduleExpressionTimezone**

Optional. This is the timezone in which the schedule
expression is set. By default, ScheduleExpressions are in UTC.
You can modify this to a specified timezone.

Type: String

Required: No

**StartWindowHours**

Defaults to 24 hours.

A value in hours after a
restore test is scheduled before a job will be canceled if it
doesn't start successfully. This value is optional. If this value
is included, this parameter has a maximum value of 168 hours
(one week).

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/RestoreTestingPlanForCreate.md "../../../goto/SdkForCpp/backup-2018-11-15/RestoreTestingPlanForCreate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingPlanForCreate.md "../../../goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingPlanForCreate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingPlanForCreate.md "../../../goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingPlanForCreate.md")
