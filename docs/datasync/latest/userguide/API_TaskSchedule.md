# TaskSchedule

Configures your AWS DataSync task to run on a [schedule](task-scheduling.md "task-scheduling.md")
(at a minimum interval of 1 hour).

## Contents

**ScheduleExpression**

Specifies your task schedule by using a cron or rate expression.

Use cron expressions for task schedules that run on a specific time and day. For example,
the following cron expression creates a task schedule that runs at 8 AM on the first Wednesday
of every month:

`cron(0 8 * * 3#1)`

Use rate expressions for task schedules that run on a regular interval. For example, the
following rate expression creates a task schedule that runs every 12 hours:

`rate(12 hours)`

For information about cron and rate expression syntax, see the [_Amazon EventBridge User Guide_](../../../eventbridge/latest/userguide/eb-scheduled-rule-pattern.md "../../../eventbridge/latest/userguide/eb-scheduled-rule-pattern.md").

Type: String

Length Constraints: Maximum length of 256.

Pattern: `^[a-zA-Z0-9\ \_\*\?\,\|\^\-\/\#\s\(\)\+]*$`

Required: Yes

**Status**

Specifies whether to enable or disable your task schedule. Your schedule is enabled by
default, but there can be situations where you need to disable it. For example, you might need
to pause a recurring transfer to fix an issue with your task or perform maintenance on your
storage system.

DataSync might disable your schedule automatically if your task fails repeatedly
with the same error. For more information, see [TaskScheduleDetails](API_TaskScheduleDetails.md "API_TaskScheduleDetails.md").

Type: String

Valid Values: `ENABLED | DISABLED`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/TaskSchedule.md "../../../goto/SdkForCpp/datasync-2018-11-09/TaskSchedule.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/TaskSchedule.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/TaskSchedule.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/TaskSchedule.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/TaskSchedule.md")
