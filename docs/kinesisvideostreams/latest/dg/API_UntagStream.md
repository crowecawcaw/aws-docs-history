# UntagStream

Removes one or more tags from a stream. In the request, specify only a tag key or
keys; don't specify the value. If you specify a tag key that does not exist, it's
ignored.

In the request, you must provide the `StreamName` or
`StreamARN`.

## Request Syntax

```
POST /untagStream HTTP/1.1
Content-type: application/json

{
   "StreamARN": "`string`",
   "StreamName": "`string`",
   "TagKeyList": [ "`string`" ]
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[StreamARN](#API_UntagStream_RequestSyntax "#API_UntagStream_RequestSyntax")**

The Amazon Resource Name (ARN) of the stream that you want to remove tags
from.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**[StreamName](#API_UntagStream_RequestSyntax "#API_UntagStream_RequestSyntax")**

The name of the stream that you want to remove tags from.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

**[TagKeyList](#API_UntagStream_RequestSyntax "#API_UntagStream_RequestSyntax")**

A list of the keys of the tags that you want to remove.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 50 items.

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Required: Yes

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientLimitExceededException**

Kinesis Video Streams has throttled the request because you have exceeded the limit of
allowed client calls. Try making the call later.

HTTP Status Code: 400

**InvalidArgumentException**

The value for this input parameter is invalid.

HTTP Status Code: 400

**InvalidResourceFormatException**

The format of the `StreamARN` is invalid.

HTTP Status Code: 400

**NotAuthorizedException**

The caller is not authorized to perform this operation.

HTTP Status Code: 401

**ResourceNotFoundException**

Amazon Kinesis Video Streams can't find the stream that you specified.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/UntagStream.md "../../../goto/cli2/kinesisvideo-2017-09-30/UntagStream.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/UntagStream.md "../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/UntagStream.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/UntagStream.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/UntagStream.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/UntagStream.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/UntagStream.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/UntagStream.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/UntagStream.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/UntagStream.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/UntagStream.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/UntagStream.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/UntagStream.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/UntagStream.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/UntagStream.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/UntagStream.md "../../../goto/boto3/kinesisvideo-2017-09-30/UntagStream.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/UntagStream.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/UntagStream.md")
