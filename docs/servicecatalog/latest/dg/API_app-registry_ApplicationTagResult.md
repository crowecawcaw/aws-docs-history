# ApplicationTagResult

The result of the application tag that's applied to a resource.

## Contents

**applicationTagStatus**

The application tag is in the process of being applied to a resource, was successfully applied to a resource, or failed to apply to a resource.

Type: String

Valid Values: `IN_PROGRESS | SUCCESS | FAILURE`

Required: No

**errorMessage**

The message returned if the call fails.

Type: String

Required: No

**nextToken**

A unique pagination token for each page of results. Make the call again with the returned token to retrieve the next page of results.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2024.

Pattern: `[A-Za-z0-9+/=]+`

Required: No

**resources**

The resources associated with an application

Type: Array of [ResourcesListItem](API_app-registry_ResourcesListItem.md "API_app-registry_ResourcesListItem.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ApplicationTagResult.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ApplicationTagResult.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ApplicationTagResult.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ApplicationTagResult.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ApplicationTagResult.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ApplicationTagResult.md")
