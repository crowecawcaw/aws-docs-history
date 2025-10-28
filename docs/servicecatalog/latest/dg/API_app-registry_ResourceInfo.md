# ResourceInfo

The information about the resource.

## Contents

**arn**

The Amazon resource name (ARN) that specifies the resource across services.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

Required: No

**name**

The name of the resource.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `\S+`

Required: No

**options**

Determines whether an application tag is applied or skipped.

Type: Array of strings

Valid Values: `APPLY_APPLICATION_TAG | SKIP_APPLICATION_TAG`

Required: No

**resourceDetails**

The details related
to
the resource.

Type: [ResourceDetails](API_app-registry_ResourceDetails.md "API_app-registry_ResourceDetails.md") object

Required: No

**resourceType**

Provides information
about the AWS Service Catalog AppRegistry resource type.

Type: String

Valid Values: `CFN_STACK | RESOURCE_TAG_VALUE`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ResourceInfo.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ResourceInfo.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ResourceInfo.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ResourceInfo.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ResourceInfo.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ResourceInfo.md")
