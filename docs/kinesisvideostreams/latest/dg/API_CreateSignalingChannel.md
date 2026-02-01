# CreateSignalingChannel

Creates a signaling channel.

`CreateSignalingChannel` is an asynchronous operation.

## Request Syntax

```
POST /createSignalingChannel HTTP/1.1
Content-type: application/json

{
   "ChannelName": "`string`",
   "ChannelType": "`string`",
   "SingleMasterConfiguration": {
      "MessageTtlSeconds": `number`
   },
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[ChannelName](#API_CreateSignalingChannel_RequestSyntax "#API_CreateSignalingChannel_RequestSyntax")**

A name for the signaling channel that you are creating. It must be unique for each AWS account and AWS Region.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**[ChannelType](#API_CreateSignalingChannel_RequestSyntax "#API_CreateSignalingChannel_RequestSyntax")**

A type of the signaling channel that you are creating. Currently,
`SINGLE_MASTER` is the only supported channel type.

Type: String

Valid Values: `SINGLE_MASTER | FULL_MESH`

Required: No

**[SingleMasterConfiguration](#API_CreateSignalingChannel_RequestSyntax "#API_CreateSignalingChannel_RequestSyntax")**

A structure containing the configuration for the `SINGLE_MASTER` channel
type. The default configuration for the channel message's time to live is 60 seconds (1
minute).

Type: [SingleMasterConfiguration](API_SingleMasterConfiguration.md "API_SingleMasterConfiguration.md") object

Required: No

**[Tags](#API_CreateSignalingChannel_RequestSyntax "#API_CreateSignalingChannel_RequestSyntax")**

A set of tags (key-value pairs) that you want to associate with this channel.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 50 items.

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "ChannelARN": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ChannelARN](#API_CreateSignalingChannel_ResponseSyntax "#API_CreateSignalingChannel_ResponseSyntax")**

The Amazon Resource Name (ARN) of the created channel.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You do not have required permissions to perform this operation.

HTTP Status Code: 401

**AccountChannelLimitExceededException**

You have reached the maximum limit of active signaling channels for this AWS account
in this region.

HTTP Status Code: 400

**ClientLimitExceededException**

Kinesis Video Streams has throttled the request because you have exceeded the limit of
allowed client calls. Try making the call later.

HTTP Status Code: 400

**InvalidArgumentException**

The value for this input parameter is invalid.

HTTP Status Code: 400

**ResourceInUseException**

When the input `StreamARN` or `ChannelARN`
in `CLOUD_STORAGE_MODE` is already mapped to a different
Kinesis Video Stream resource, or if the provided input `StreamARN`
or `ChannelARN` is not in Active status, try one of the following :

1. The `DescribeMediaStorageConfiguration` API to determine what the stream given channel is mapped to.
2. The `DescribeMappedResourceConfiguration` API to determine the channel that the given stream is mapped to.
3. The `DescribeStream` or `DescribeSignalingChannel` API to determine the status of the resource.

HTTP Status Code: 400

**TagsPerResourceExceededLimitException**

You have exceeded the limit of tags that you can associate with the resource.
A Kinesis video stream can support up to 50 tags.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/CreateSignalingChannel.md "../../../goto/cli2/kinesisvideo-2017-09-30/CreateSignalingChannel.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/CreateSignalingChannel.md "../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/CreateSignalingChannel.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/CreateSignalingChannel.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/CreateSignalingChannel.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/CreateSignalingChannel.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/CreateSignalingChannel.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/CreateSignalingChannel.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/CreateSignalingChannel.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/CreateSignalingChannel.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/CreateSignalingChannel.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/CreateSignalingChannel.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/CreateSignalingChannel.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/CreateSignalingChannel.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/CreateSignalingChannel.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/CreateSignalingChannel.md "../../../goto/boto3/kinesisvideo-2017-09-30/CreateSignalingChannel.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/CreateSignalingChannel.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/CreateSignalingChannel.md")
