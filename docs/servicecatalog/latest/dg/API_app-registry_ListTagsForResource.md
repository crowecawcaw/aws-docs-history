# ListTagsForResource

Lists all of the tags on the resource.

## Request Syntax

```
GET /tags/`resourceArn` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[resourceArn](#API_app-registry_ListTagsForResource_RequestSyntax "#API_app-registry_ListTagsForResource_RequestSyntax")**

The Amazon resource name (ARN) that specifies the resource.

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "tags": {
      "***string***" : "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[tags](#API_app-registry_ListTagsForResource_ResponseSyntax "#API_app-registry_ListTagsForResource_ResponseSyntax")**

The tags on the resource.

Type: String to string map

Map Entries: Minimum number of 0 items. Maximum number of 50 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`

Value Length Constraints: Maximum length of 256.

Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`

## Errors

**InternalServerException**

The service is experiencing internal problems.

HTTP Status Code: 500

**ResourceNotFoundException**

The specified resource does not exist.

HTTP Status Code: 404

**ValidationException**

The request has invalid or missing parameters.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/ListTagsForResource.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/ListTagsForResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/ListTagsForResource.md "../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/ListTagsForResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ListTagsForResource.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ListTagsForResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/ListTagsForResource.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/ListTagsForResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ListTagsForResource.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ListTagsForResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/ListTagsForResource.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/ListTagsForResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/ListTagsForResource.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/ListTagsForResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/ListTagsForResource.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/ListTagsForResource.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/ListTagsForResource.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/ListTagsForResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ListTagsForResource.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ListTagsForResource.md")
