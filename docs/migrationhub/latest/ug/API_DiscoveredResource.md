AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# DiscoveredResource

Object representing the on-premises resource being migrated.

## Contents

**ConfigurationId**

The configurationId in Application Discovery Service that uniquely identifies the
on-premise resource.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `^.{1,1600}$`

Required: Yes

**Description**

A description that can be free-form text to record additional detail about the
discovered resource for clarity or later reference.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 500.

Pattern: `^.{0,500}$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/DiscoveredResource.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/DiscoveredResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/DiscoveredResource.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/DiscoveredResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/DiscoveredResource.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/DiscoveredResource.md")
