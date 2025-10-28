# TaskListEntry

Represents a single entry in a list of tasks. `TaskListEntry` returns an
array that contains a list of tasks when the [ListTasks](API_ListTasks.md "API_ListTasks.md") operation is called. A
task includes the source and destination file systems to sync and the options to use for the
tasks.

## Contents

**Name**

The name of the task.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 256.

Pattern: `^[a-zA-Z0-9\s+=._:@/-]+$`

Required: No

**Status**

The status of the task.

Type: String

Valid Values: `AVAILABLE | CREATING | QUEUED | RUNNING | UNAVAILABLE`

Required: No

**TaskArn**

The Amazon Resource Name (ARN) of the task.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]*:[0-9]{12}:task/task-[0-9a-f]{17}$`

Required: No

**TaskMode**

The task mode that you're using. For more information, see [Choosing a task mode for your data
transfer](choosing-task-mode.md "choosing-task-mode.md").

Type: String

Valid Values: `BASIC | ENHANCED`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/TaskListEntry.md "../../../goto/SdkForCpp/datasync-2018-11-09/TaskListEntry.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/TaskListEntry.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/TaskListEntry.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/TaskListEntry.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/TaskListEntry.md")
