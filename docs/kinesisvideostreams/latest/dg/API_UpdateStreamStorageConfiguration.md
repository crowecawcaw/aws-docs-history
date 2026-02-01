# UpdateStreamStorageConfiguration

Updates the storage configuration for an existing Kinesis video stream.

This operation allows you to modify the storage tier settings for a stream, enabling you to optimize storage costs and performance based on your access patterns.

`UpdateStreamStorageConfiguration` is an asynchronous operation.

You must have permissions for the `KinesisVideo:UpdateStreamStorageConfiguration` action.

## Request Syntax

```
POST /updateStreamStorageConfiguration HTTP/1.1
Content-type: application/json

{
   "CurrentVersion": "`string`",
   "StreamARN": "`string`",
   "StreamName": "`string`",
   "StreamStorageConfiguration": {
      "DefaultStorageTier": "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[CurrentVersion](#API_UpdateStreamStorageConfiguration_RequestSyntax "#API_UpdateStreamStorageConfiguration_RequestSyntax")**

The version of the stream whose storage configuration you want to change. To get the
version, call either the `DescribeStream` or the `ListStreams`
API.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `[a-zA-Z0-9]+`

Required: Yes

**[StreamARN](#API_UpdateStreamStorageConfiguration_RequestSyntax "#API_UpdateStreamStorageConfiguration_RequestSyntax")**

The Amazon Resource Name (ARN) of the stream for which you want to update the storage configuration.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**[StreamName](#API_UpdateStreamStorageConfiguration_RequestSyntax "#API_UpdateStreamStorageConfiguration_RequestSyntax")**

The name of the stream for which you want to update the storage configuration.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

**[StreamStorageConfiguration](#API_UpdateStreamStorageConfiguration_RequestSyntax "#API_UpdateStreamStorageConfiguration_RequestSyntax")**

The new storage configuration for the stream. This includes the default storage tier that determines how stream data is stored and accessed.

Different storage tiers offer varying levels of performance and cost optimization to match your specific use case requirements.

Type: [StreamStorageConfiguration](API_StreamStorageConfiguration.md "API_StreamStorageConfiguration.md") object

Required: Yes

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

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

**ResourceInUseException**

When the input `StreamARN` or `ChannelARN`
in `CLOUD_STORAGE_MODE` is already mapped to a different
Kinesis Video Stream resource, or if the provided input `StreamARN`
or `ChannelARN` is not in Active status, try one of the following :

1. The `DescribeMediaStorageConfiguration` API to determine what the stream given channel is mapped to.
2. The `DescribeMappedResourceConfiguration` API to determine the channel that the given stream is mapped to.
3. The `DescribeStream` or `DescribeSignalingChannel` API to determine the status of the resource.

HTTP Status Code: 400

**ResourceNotFoundException**

Amazon Kinesis Video Streams can't find the stream that you specified.

HTTP Status Code: 404

**VersionMismatchException**

The stream version that you specified is not the latest version. To get the latest
version, use the [DescribeStream](API_DescribeStream.md "API_DescribeStream.md")
API.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md "../../../goto/cli2/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md "../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md "../../../goto/boto3/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/UpdateStreamStorageConfiguration.md")
