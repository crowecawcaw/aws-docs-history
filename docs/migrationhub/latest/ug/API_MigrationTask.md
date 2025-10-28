AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# MigrationTask

Represents a migration task in a migration tool.

## Contents

**MigrationTaskName**

Unique identifier that references the migration task. _Do not store personal
data in this field._

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[^:|]+`

Required: No

**ProgressUpdateStream**

A name that identifies the vendor of the migration tool being used.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[^/:|\000-\037]+`

Required: No

**ResourceAttributeList**

Information about the resource that is being migrated. This data will be used to map the
task to a resource in the Application Discovery Service repository.

Type: Array of [ResourceAttribute](API_ResourceAttribute.md "API_ResourceAttribute.md") objects

Array Members: Minimum number of 0 items. Maximum number of 100 items.

Required: No

**Task**

Task object encapsulating task information.

Type: [Task](API_Task.md "API_Task.md") object

Required: No

**UpdateDateTime**

The timestamp when the task was gathered.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/MigrationTask.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/MigrationTask.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/MigrationTask.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/MigrationTask.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/MigrationTask.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/MigrationTask.md")
