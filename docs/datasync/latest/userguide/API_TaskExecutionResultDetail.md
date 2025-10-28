# TaskExecutionResultDetail

Provides detailed information about the result of your AWS DataSync task
execution.

## Contents

**ErrorCode**

An error that DataSync encountered during your task execution. You can use
this information to help [troubleshoot
issues](troubleshooting-datasync-locations-tasks.md "troubleshooting-datasync-locations-tasks.md").

Type: String

Required: No

**ErrorDetail**

The detailed description of an error that DataSync encountered during your
task execution. You can use this information to help [troubleshoot
issues](troubleshooting-datasync-locations-tasks.md "troubleshooting-datasync-locations-tasks.md").

Type: String

Required: No

**PrepareDuration**

The time in milliseconds that your task execution was in the `PREPARING`
step. For more information, see [Task
execution statuses](run-task.md#understand-task-execution-statuses "run-task.md#understand-task-execution-statuses").

For Enhanced mode tasks, the value is always `0`. For more information, see
[How DataSync prepares your data transfer](how-datasync-transfer-works.md#how-datasync-prepares "how-datasync-transfer-works.md#how-datasync-prepares").

Type: Long

Valid Range: Minimum value of 0.

Required: No

**PrepareStatus**

The status of the `PREPARING` step for your task execution. For more
information, see [Task
execution statuses](run-task.md#understand-task-execution-statuses "run-task.md#understand-task-execution-statuses").

Type: String

Valid Values: `PENDING | SUCCESS | ERROR`

Required: No

**TotalDuration**

The time in milliseconds that your task execution ran.

Type: Long

Valid Range: Minimum value of 0.

Required: No

**TransferDuration**

The time in milliseconds that your task execution was in the `TRANSFERRING`
step. For more information, see [Task
execution statuses](run-task.md#understand-task-execution-statuses "run-task.md#understand-task-execution-statuses").

For Enhanced mode tasks, the value is always `0`. For more information, see
[How DataSync transfers your data](how-datasync-transfer-works.md#how-datasync-transfers "how-datasync-transfer-works.md#how-datasync-transfers").

Type: Long

Valid Range: Minimum value of 0.

Required: No

**TransferStatus**

The status of the `TRANSFERRING` step for your task execution. For more
information, see [Task
execution statuses](run-task.md#understand-task-execution-statuses "run-task.md#understand-task-execution-statuses").

Type: String

Valid Values: `PENDING | SUCCESS | ERROR`

Required: No

**VerifyDuration**

The time in milliseconds that your task execution was in the `VERIFYING`
step. For more information, see [Task
execution statuses](run-task.md#understand-task-execution-statuses "run-task.md#understand-task-execution-statuses").

For Enhanced mode tasks, the value is always `0`. For more information, see
[How DataSync verifies your data's
integrity](how-datasync-transfer-works.md#how-verifying-works "how-datasync-transfer-works.md#how-verifying-works").

Type: Long

Valid Range: Minimum value of 0.

Required: No

**VerifyStatus**

The status of the `VERIFYING` step for your task execution. For more
information, see [Task
execution statuses](run-task.md#understand-task-execution-statuses "run-task.md#understand-task-execution-statuses").

Type: String

Valid Values: `PENDING | SUCCESS | ERROR`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/TaskExecutionResultDetail.md "../../../goto/SdkForCpp/datasync-2018-11-09/TaskExecutionResultDetail.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/TaskExecutionResultDetail.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/TaskExecutionResultDetail.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/TaskExecutionResultDetail.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/TaskExecutionResultDetail.md")
