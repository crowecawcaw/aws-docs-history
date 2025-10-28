AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# MigrationTaskSummary

MigrationTaskSummary includes `MigrationTaskName`,
`ProgressPercent`, `ProgressUpdateStream`, `Status`,
and `UpdateDateTime` for each task.

## Contents

**MigrationTaskName**

Unique identifier that references the migration task. _Do not store personal
data in this field._

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[^:|]+`

Required: No

**ProgressPercent**

Indication of the percentage completion of the task.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 100.

Required: No

**ProgressUpdateStream**

An AWS resource used for access control. It should uniquely identify the migration tool
as it is used for all updates made by the tool.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[^/:|\000-\037]+`

Required: No

**Status**

Status of the task.

Type: String

Valid Values: `NOT_STARTED | IN_PROGRESS | FAILED | COMPLETED`

Required: No

**StatusDetail**

Detail information of what is being done within the overall status state.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 2500.

Pattern: `^.{0,2500}$`

Required: No

**UpdateDateTime**

The timestamp when the task was gathered.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/MigrationTaskSummary.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/MigrationTaskSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/MigrationTaskSummary.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/MigrationTaskSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/MigrationTaskSummary.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/MigrationTaskSummary.md")
