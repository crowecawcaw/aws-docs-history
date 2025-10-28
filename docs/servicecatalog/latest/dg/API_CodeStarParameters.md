# CodeStarParameters

The subtype containing details about the Codestar connection `Type`.

## Contents

**ArtifactPath**

The absolute path wehre the artifact resides within the repo and branch, formatted as
"folder/file.json."

Type: String

Length Constraints: Minimum length of 1. Maximum length of 4096.

Required: Yes

**Branch**

The specific branch where the artifact resides.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 250.

Required: Yes

**ConnectionArn**

The CodeStar ARN, which is the connection between AWS Service Catalog and the external repository.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1224.

Pattern: `arn:[a-z0-9][-.a-z0-9]{0,62}:(codestar-connections|codeconnections):([a-z0-9][-.a-z0-9]{0,62})?:([a-z0-9][-.a-z0-9]{0,62})?:[^/].{0,1023}$`

Required: Yes

**Repository**

The specific repository where the product’s artifact-to-be-synced resides, formatted as
"Account/Repo."

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/CodeStarParameters.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/CodeStarParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/CodeStarParameters.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/CodeStarParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/CodeStarParameters.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/CodeStarParameters.md")
