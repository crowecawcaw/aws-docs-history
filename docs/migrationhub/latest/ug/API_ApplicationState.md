AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# ApplicationState

The state of an application discovered through Migration Hub import, the AWS Agentless
Discovery Connector, or the AWS Application Discovery Agent.

## Contents

**ApplicationId**

The configurationId from the Application Discovery Service that uniquely identifies an
application.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `^.{1,1600}$`

Required: No

**ApplicationStatus**

The current status of an application.

Type: String

Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETED`

Required: No

**LastUpdatedTime**

The timestamp when the application status was last updated.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/ApplicationState.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/ApplicationState.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/ApplicationState.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/ApplicationState.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/ApplicationState.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/ApplicationState.md")
