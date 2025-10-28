# ApplicationSummary

Summary of a AWS Service Catalog AppRegistry application.

## Contents

**arn**

The Amazon resource name (ARN) that specifies the application across services.

Type: String

Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`

Required: No

**creationTime**

The ISO-8601 formatted timestamp of the moment when the application was created.

Type: Timestamp

Required: No

**description**

The description of the application.

Type: String

Length Constraints: Maximum length of 1024.

Required: No

**id**

The identifier of the application.

Type: String

Length Constraints: Fixed length of 26.

Pattern: `[a-z0-9]+`

Required: No

**lastUpdateTime**

The ISO-8601 formatted timestamp of the moment when the application was last updated.

Type: Timestamp

Required: No

**name**

The name of the application. The name must be unique in the region in which you are creating the application.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[-.\w]+`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ApplicationSummary.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ApplicationSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ApplicationSummary.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ApplicationSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ApplicationSummary.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ApplicationSummary.md")
