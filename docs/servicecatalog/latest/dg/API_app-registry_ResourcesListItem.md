# ResourcesListItem

The resource in a list of resources.

## Contents

**errorMessage**

The message returned if the call fails.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Required: No

**resourceArn**

The Amazon resource name (ARN) of the resource.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

Required: No

**resourceType**

Provides information about the AppRegistry resource type.

Type: String

Pattern: `AWS::[a-zA-Z0-9]+::\w+`

Required: No

**status**

The status of the list item.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ResourcesListItem.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ResourcesListItem.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ResourcesListItem.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ResourcesListItem.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ResourcesListItem.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ResourcesListItem.md")
