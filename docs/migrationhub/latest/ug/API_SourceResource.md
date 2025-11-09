AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# SourceResource

A source resource can be a source server, a migration wave, an application, or any other
resource that you track.

## Contents

**Name**

This is the name that you want to use to identify the resource. If the resource is an
AWS resource, we recommend that you set this parameter to the ARN of the resource.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Required: Yes

**Description**

A description that can be free-form text to record additional detail about the resource
for clarity or later reference.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 500.

Pattern: `^.{0,500}$`

Required: No

**StatusDetail**

A free-form description of the status of the resource.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 2500.

Pattern: `^.{0,2500}$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/SourceResource.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/SourceResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/SourceResource.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/SourceResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/SourceResource.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/SourceResource.md")
