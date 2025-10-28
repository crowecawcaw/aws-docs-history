# UntagResource

Removes tags from a resource.

This operation returns an empty response if the call was successful.

## Request Syntax

```
DELETE /tags/`resourceArn`?tagKeys=`tagKeys` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[resourceArn](#API_app-registry_UntagResource_RequestSyntax "#API_app-registry_UntagResource_RequestSyntax")**

The Amazon resource name (ARN) that specifies the resource.

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

Required: Yes

**[tagKeys](#API_app-registry_UntagResource_RequestSyntax "#API_app-registry_UntagResource_RequestSyntax")**

A list of the tag keys to remove from the specified resource.

Array Members: Minimum number of 0 items. Maximum number of 50 items.

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`

Required: Yes

## Request Body

The request does not have a request body.

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

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/UntagResource.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/UntagResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/AWS242AppRegistry-2020-06-24/UntagResource.md "../../../goto/DotNetSDKV3/AWS242AppRegistry-2020-06-24/UntagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/UntagResource.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/UntagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/UntagResource.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/UntagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/UntagResource.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/UntagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/UntagResource.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/UntagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/UntagResource.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/UntagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/UntagResource.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/UntagResource.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/UntagResource.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/UntagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/UntagResource.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/UntagResource.md")
