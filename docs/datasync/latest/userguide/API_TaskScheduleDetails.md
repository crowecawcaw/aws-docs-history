# TaskScheduleDetails

Provides information about your AWS DataSync
[task
schedule](task-scheduling.md "task-scheduling.md").

## Contents

**DisabledBy**

Indicates how your task schedule was disabled.

- `USER` - Your schedule was manually disabled by using the [UpdateTask](API_UpdateTask.md "API_UpdateTask.md") operation or DataSync console.
- `SERVICE` - Your schedule was automatically disabled by DataSync
  because the task failed repeatedly with the same error.

Type: String

Valid Values: `USER | SERVICE`

Required: No

**DisabledReason**

Provides a reason if the task schedule is disabled.

If your schedule is disabled by `USER`, you see a `Manually disabled by
 user.` message.

If your schedule is disabled by `SERVICE`, you see an error message to help you
understand why the task keeps failing. For information on resolving DataSync errors,
see [Troubleshooting issues with DataSync transfers](troubleshooting-datasync-locations-tasks.md "troubleshooting-datasync-locations-tasks.md").

Type: String

Length Constraints: Maximum length of 8192.

Pattern: `^[\w\s.,'?!:;\/=|<>()-]*$`

Required: No

**StatusUpdateTime**

Indicates the last time the status of your task schedule changed. For example, if DataSync automatically disables your schedule because of a repeated error, you can see
when the schedule was disabled.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/TaskScheduleDetails.md "../../../goto/SdkForCpp/datasync-2018-11-09/TaskScheduleDetails.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/TaskScheduleDetails.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/TaskScheduleDetails.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/TaskScheduleDetails.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/TaskScheduleDetails.md")
