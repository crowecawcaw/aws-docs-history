# RestoreTestingPlanForList

This contains metadata about a restore testing plan.

## Contents

**CreationTime**

The date and time that a restore testing plan was created,
in Unix format and Coordinated Universal Time (UTC). The value
of `CreationTime` is accurate to milliseconds. For
example, the value 1516925490.087 represents Friday, January 26,
2018 12:11:30.087 AM.

Type: Timestamp

Required: Yes

**RestoreTestingPlanArn**

An Amazon Resource Name (ARN) that uniquely identifiesa
restore testing plan.

Type: String

Required: Yes

**RestoreTestingPlanName**

The restore testing plan name.

Type: String

Required: Yes

**ScheduleExpression**

A CRON expression in specified timezone when a restore testing plan is executed. When no
CRON expression is provided, AWS Backup will use the default expression
`cron(0 5 ? * * *)`.

Type: String

Required: Yes

**LastExecutionTime**

The last time a restore test was run with the specified
restore testing plan. A date and time, in Unix format and
Coordinated Universal Time (UTC). The value of
`LastExecutionDate` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday,
January 26, 2018 12:11:30.087 AM.

Type: Timestamp

Required: No

**LastUpdateTime**

The date and time that the restore testing plan was updated.
This update is in Unix format and Coordinated Universal Time (UTC).
The value of `LastUpdateTime` is accurate to
milliseconds. For example, the value 1516925490.087 represents
Friday, January 26, 2018 12:11:30.087 AM.

Type: Timestamp

Required: No

**ScheduleExpressionTimezone**

Optional. This is the timezone in which the schedule
expression is set. By default, ScheduleExpressions are in UTC.
You can modify this to a specified timezone.

Type: String

Required: No

**StartWindowHours**

Defaults to 24 hours.

A value in hours after a restore test is scheduled before
a job will be canceled if it doesn't start successfully. This
value is optional. If this value is included, this parameter
has a maximum value of 168 hours (one week).

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/RestoreTestingPlanForList.md "../../../goto/SdkForCpp/backup-2018-11-15/RestoreTestingPlanForList.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingPlanForList.md "../../../goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingPlanForList.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingPlanForList.md "../../../goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingPlanForList.md")
