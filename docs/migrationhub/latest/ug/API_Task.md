AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Task

Task object encapsulating task information.

## Contents

**Status**

Status of the task - Not Started, In-Progress, Complete.

Type: String

Valid Values: `NOT_STARTED | IN_PROGRESS | FAILED | COMPLETED`

Required: Yes

**ProgressPercent**

Indication of the percentage completion of the task.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 100.

Required: No

**StatusDetail**

Details of task status as notified by a migration tool. A tool might use this field to
provide clarifying information about the status that is unique to that tool or that
explains an error state.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 2500.

Pattern: `^.{0,2500}$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/Task.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/Task.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/Task.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/Task.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/Task.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/Task.md")
