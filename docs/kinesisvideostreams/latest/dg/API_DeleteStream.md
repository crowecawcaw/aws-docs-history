# DeleteStream

Deletes a Kinesis video stream and the data contained in the stream.

This method marks the stream for deletion, and makes the data in the stream
inaccessible immediately.

To ensure that you have the latest version of the stream before deleting it, you
can specify the stream version. Kinesis Video Streams assigns a version to each stream.
When you update a stream, Kinesis Video Streams assigns a new version number. To get the
latest stream version, use the `DescribeStream` API.

This operation requires permission for the `KinesisVideo:DeleteStream`
action.

## Request Syntax

```
POST /deleteStream HTTP/1.1
Content-type: application/json

{
   "CurrentVersion": "`string`",
   "StreamARN": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[CurrentVersion](#API_DeleteStream_RequestSyntax "#API_DeleteStream_RequestSyntax")**

Optional: The version of the stream that you want to delete.

Specify the version as a safeguard to ensure that your are deleting the correct
stream. To get the stream version, use the `DescribeStream` API.

If not specified, only the `CreationTime` is checked before deleting the
stream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `[a-zA-Z0-9]+`

Required: No

**[StreamARN](#API_DeleteStream_RequestSyntax "#API_DeleteStream_RequestSyntax")**

The Amazon Resource Name (ARN) of the stream that you want to delete.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

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

**NotAuthorizedException**

The caller is not authorized to perform this operation.

HTTP Status Code: 401

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

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/DeleteStream.md "../../../goto/cli2/kinesisvideo-2017-09-30/DeleteStream.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/kinesisvideo-2017-09-30/DeleteStream.md "../../../goto/DotNetSDKV3/kinesisvideo-2017-09-30/DeleteStream.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/DeleteStream.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/DeleteStream.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/DeleteStream.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/DeleteStream.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/DeleteStream.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/DeleteStream.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/DeleteStream.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/DeleteStream.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/DeleteStream.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/DeleteStream.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/DeleteStream.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/DeleteStream.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/DeleteStream.md "../../../goto/boto3/kinesisvideo-2017-09-30/DeleteStream.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/DeleteStream.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/DeleteStream.md")
