# TagStream

Adds one or more tags to a stream. A _tag_ is a key-value pair
(the value is optional) that you can define and assign to AWS resources. If you specify
a tag that already exists, the tag value is replaced with the value that you specify in
the request. For more information, see [Using Cost Allocation
Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing and Cost Management and Cost Management User Guide_.

You must provide either the `StreamName` or the
`StreamARN`.

This operation requires permission for the `KinesisVideo:TagStream`
action.

A Kinesis video stream can support up to 50 tags.

## Request Syntax

```
POST /tagStream HTTP/1.1
Content-type: application/json

{
   "StreamARN": "`string`",
   "StreamName": "`string`",
   "Tags": {
      "`string`" : "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[StreamARN](#API_TagStream_RequestSyntax "#API_TagStream_RequestSyntax")**

The Amazon Resource Name (ARN) of the resource that you want to add the tag or tags
to.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**[StreamName](#API_TagStream_RequestSyntax "#API_TagStream_RequestSyntax")**

The name of the stream that you want to add the tag or tags to.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

**[Tags](#API_TagStream_RequestSyntax "#API_TagStream_RequestSyntax")**

A list of tags to associate with the specified stream. Each tag is a key-value pair
(the value is optional).

Type: String to string map

Map Entries: Maximum number of 50 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Value Length Constraints: Minimum length of 0. Maximum length of 256.

Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`

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

**TagsPerResourceExceededLimitException**

You have exceeded the limit of tags that you can associate with the resource.
A Kinesis video stream can support up to 50 tags.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/TagStream.md "../../../goto/cli2/kinesisvideo-2017-09-30/TagStream.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/kinesisvideo-2017-09-30/TagStream.md "../../../goto/DotNetSDKV3/kinesisvideo-2017-09-30/TagStream.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/TagStream.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/TagStream.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/TagStream.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/TagStream.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/TagStream.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/TagStream.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/TagStream.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/TagStream.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/TagStream.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/TagStream.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/TagStream.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/TagStream.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/TagStream.md "../../../goto/boto3/kinesisvideo-2017-09-30/TagStream.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/TagStream.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/TagStream.md")
