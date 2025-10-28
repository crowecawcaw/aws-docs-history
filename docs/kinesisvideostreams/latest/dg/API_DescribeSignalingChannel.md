# DescribeSignalingChannel

Returns the most current information about the signaling channel. You must specify
either the name or the Amazon Resource Name (ARN) of the channel that you want to
describe.

## Request Syntax

```
POST /describeSignalingChannel HTTP/1.1
Content-type: application/json

{
   "ChannelARN": "`string`",
   "ChannelName": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[ChannelARN](#API_DescribeSignalingChannel_RequestSyntax "#API_DescribeSignalingChannel_RequestSyntax")**

The ARN of the signaling channel that you want to describe.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**[ChannelName](#API_DescribeSignalingChannel_RequestSyntax "#API_DescribeSignalingChannel_RequestSyntax")**

The name of the signaling channel that you want to describe.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "ChannelInfo": {
      "ChannelARN": "***string***",
      "ChannelName": "***string***",
      "ChannelStatus": "***string***",
      "ChannelType": "***string***",
      "CreationTime": ***number***,
      "SingleMasterConfiguration": {
         "MessageTtlSeconds": ***number***
      },
      "Version": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ChannelInfo](#API_DescribeSignalingChannel_ResponseSyntax "#API_DescribeSignalingChannel_ResponseSyntax")**

A structure that encapsulates the specified signaling channel's metadata and
properties.

Type: [ChannelInfo](API_ChannelInfo.md "API_ChannelInfo.md") object

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

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/DescribeSignalingChannel.md "../../../goto/cli2/kinesisvideo-2017-09-30/DescribeSignalingChannel.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/kinesisvideo-2017-09-30/DescribeSignalingChannel.md "../../../goto/DotNetSDKV3/kinesisvideo-2017-09-30/DescribeSignalingChannel.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/DescribeSignalingChannel.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/DescribeSignalingChannel.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/DescribeSignalingChannel.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/DescribeSignalingChannel.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/DescribeSignalingChannel.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/DescribeSignalingChannel.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/DescribeSignalingChannel.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/DescribeSignalingChannel.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/DescribeSignalingChannel.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/DescribeSignalingChannel.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/DescribeSignalingChannel.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/DescribeSignalingChannel.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/DescribeSignalingChannel.md "../../../goto/boto3/kinesisvideo-2017-09-30/DescribeSignalingChannel.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/DescribeSignalingChannel.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/DescribeSignalingChannel.md")
