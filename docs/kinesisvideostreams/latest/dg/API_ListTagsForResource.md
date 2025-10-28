# ListTagsForResource

Returns a list of tags associated with the specified signaling channel.

## Request Syntax

```
POST /ListTagsForResource HTTP/1.1
Content-type: application/json

{
   "NextToken": "`string`",
   "ResourceARN": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[NextToken](#API_ListTagsForResource_RequestSyntax "#API_ListTagsForResource_RequestSyntax")**

If you specify this parameter and the result of a `ListTagsForResource`
call is truncated, the response includes a token that you can use in the next request to
fetch the next batch of tags.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Pattern: `[a-zA-Z0-9+/=]*`

Required: No

**[ResourceARN](#API_ListTagsForResource_RequestSyntax "#API_ListTagsForResource_RequestSyntax")**

The Amazon Resource Name (ARN) of the signaling channel for which you want to list
tags.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "Tags": {
      "***string***" : "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListTagsForResource_ResponseSyntax "#API_ListTagsForResource_ResponseSyntax")**

If you specify this parameter and the result of a `ListTagsForResource`
call is truncated, the response includes a token that you can use in the next request to
fetch the next set of tags.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Pattern: `[a-zA-Z0-9+/=]*`

**[Tags](#API_ListTagsForResource_ResponseSyntax "#API_ListTagsForResource_ResponseSyntax")**

A map of tag keys and values associated with the specified signaling channel.

Type: String to string map

Map Entries: Maximum number of 50 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Value Length Constraints: Minimum length of 0. Maximum length of 256.

Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You do not have required permissions to perform this operation.

HTTP Status Code: 401

**ClientLimitExceededException**

Kinesis Video Streams has throttled the request because you have exceeded the limit of
allowed client calls. Try making the call later.

HTTP Status Code: 400

**InvalidArgumentException**

The value for this input parameter is invalid.

HTTP Status Code: 400

**ResourceNotFoundException**

Amazon Kinesis Video Streams can't find the stream that you specified.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/ListTagsForResource.md "../../../goto/cli2/kinesisvideo-2017-09-30/ListTagsForResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/kinesisvideo-2017-09-30/ListTagsForResource.md "../../../goto/DotNetSDKV3/kinesisvideo-2017-09-30/ListTagsForResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/ListTagsForResource.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/ListTagsForResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/ListTagsForResource.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/ListTagsForResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/ListTagsForResource.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/ListTagsForResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/ListTagsForResource.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/ListTagsForResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/ListTagsForResource.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/ListTagsForResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/ListTagsForResource.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/ListTagsForResource.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/ListTagsForResource.md "../../../goto/boto3/kinesisvideo-2017-09-30/ListTagsForResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/ListTagsForResource.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/ListTagsForResource.md")
