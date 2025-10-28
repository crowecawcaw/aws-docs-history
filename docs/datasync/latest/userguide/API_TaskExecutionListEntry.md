# TaskExecutionListEntry

Represents a single entry in a list of AWS DataSync task executions that's
returned with the [ListTaskExecutions](API_ListTaskExecutions.md "API_ListTaskExecutions.md")
operation.

## Contents

**Status**

The status of a task execution. For more information, see [Task execution statuses](run-task.md#understand-task-execution-statuses "run-task.md#understand-task-execution-statuses").

Type: String

Valid Values: `QUEUED | CANCELLING | LAUNCHING | PREPARING | TRANSFERRING | VERIFYING | SUCCESS | ERROR`

Required: No

**TaskExecutionArn**

The Amazon Resource Name (ARN) of a task execution.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]*:[0-9]{12}:task/task-[0-9a-f]{17}/execution/exec-[0-9a-f]{17}$`

Required: No

**TaskMode**

The task mode that you're using. For more information, see [Choosing a task mode for your data
transfer](choosing-task-mode.md "choosing-task-mode.md").

Type: String

Valid Values: `BASIC | ENHANCED`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/TaskExecutionListEntry.md "../../../goto/SdkForCpp/datasync-2018-11-09/TaskExecutionListEntry.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/TaskExecutionListEntry.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/TaskExecutionListEntry.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/TaskExecutionListEntry.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/TaskExecutionListEntry.md")
