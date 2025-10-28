# Resource

The information about the resource.

## Contents

**arn**

The Amazon resource name (ARN) of the resource.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

Required: No

**associationTime**

The time the resource was associated with the application.

Type: Timestamp

Required: No

**integrations**

The service integration information about the resource.

Type: [ResourceIntegrations](API_app-registry_ResourceIntegrations.md "API_app-registry_ResourceIntegrations.md") object

Required: No

**name**

The name of the resource.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `\S+`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/Resource.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/Resource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/Resource.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/Resource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/Resource.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/Resource.md")
