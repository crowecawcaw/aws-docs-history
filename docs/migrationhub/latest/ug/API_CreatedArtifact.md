AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# CreatedArtifact

An ARN of the AWS cloud resource target receiving the migration (e.g., AMI, EC2
instance, RDS instance, etc.).

## Contents

**Name**

An ARN that uniquely identifies the result of a migration task.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:[a-z-]+:[a-z0-9-]+:(?:[a-z0-9-]+|):(?:[0-9]{12}|):.*`

Required: Yes

**Description**

A description that can be free-form text to record additional detail about the artifact
for clarity or for later reference.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 500.

Pattern: `^.{0,500}$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/CreatedArtifact.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/CreatedArtifact.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/CreatedArtifact.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/CreatedArtifact.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/CreatedArtifact.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/CreatedArtifact.md")
