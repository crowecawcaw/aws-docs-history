# TagResource

Assigns one or more tags (key-value pairs) to the specified resource.

Each tag consists of a key and an optional value. If a tag with the same key is already associated with the resource, this action updates its value.

This operation returns an empty response if the call was successful.

## Request Syntax

```
POST /tags/`resourceArn` HTTP/1.1
Content-type: application/json

{
   "tags": {
      "`string`" : "`string`"
   }
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[resourceArn](#API_app-registry_TagResource_RequestSyntax "#API_app-registry_TagResource_RequestSyntax")**

The Amazon resource name (ARN) that specifies the resource.

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[tags](#API_app-registry_TagResource_RequestSyntax "#API_app-registry_TagResource_RequestSyntax")**

The new or modified tags for the resource.

Type: String to string map

Map Entries: Minimum number of 0 items. Maximum number of 50 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`

Value Length Constraints: Maximum length of 256.

Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`

Required: Yes

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

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

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/TagResource.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/TagResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/AWS242AppRegistry-2020-06-24/TagResource.md "../../../goto/DotNetSDKV3/AWS242AppRegistry-2020-06-24/TagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/TagResource.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/TagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/TagResource.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/TagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/TagResource.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/TagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/TagResource.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/TagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/TagResource.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/TagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/TagResource.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/TagResource.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/TagResource.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/TagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/TagResource.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/TagResource.md")
