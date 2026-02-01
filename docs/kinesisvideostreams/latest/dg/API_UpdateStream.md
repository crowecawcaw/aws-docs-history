# UpdateStream

Updates stream metadata, such as the device name and media type.

You must provide the stream name or the Amazon Resource Name (ARN) of the
stream.

To make sure that you have the latest version of the stream before updating it, you
can specify the stream version. Kinesis Video Streams assigns a version to each stream.
When you update a stream, Kinesis Video Streams assigns a new version number. To get the
latest stream version, use the `DescribeStream` API.

`UpdateStream` is an asynchronous operation, and takes time to
complete.

## Request Syntax

```
POST /updateStream HTTP/1.1
Content-type: application/json

{
   "CurrentVersion": "`string`",
   "DeviceName": "`string`",
   "MediaType": "`string`",
   "StreamARN": "`string`",
   "StreamName": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[CurrentVersion](#API_UpdateStream_RequestSyntax "#API_UpdateStream_RequestSyntax")**

The version of the stream whose metadata you want to update.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `[a-zA-Z0-9]+`

Required: Yes

**[DeviceName](#API_UpdateStream_RequestSyntax "#API_UpdateStream_RequestSyntax")**

The name of the device that is writing to the stream.

###### Note

In the current implementation, Kinesis Video Streams does not use this name.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

**[MediaType](#API_UpdateStream_RequestSyntax "#API_UpdateStream_RequestSyntax")**

The stream's media type. Use `MediaType` to specify the type of content
that the stream contains to the consumers of the stream. For more information about
media types, see [Media
Types](http://www.iana.org/assignments/media-types/media-types.xhtml "http://www.iana.org/assignments/media-types/media-types.xhtml"). If you choose to specify the `MediaType`, see [Naming
Requirements](https://tools.ietf.org/html/rfc6838#section-4.2 "https://tools.ietf.org/html/rfc6838#section-4.2").

To play video on the console, you must specify the correct video type. For example,
if the video in the stream is H.264, specify `video/h264` as the
`MediaType`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[\w\-\.\+]+/[\w\-\.\+]+(,[\w\-\.\+]+/[\w\-\.\+]+)*`

Required: No

**[StreamARN](#API_UpdateStream_RequestSyntax "#API_UpdateStream_RequestSyntax")**

The ARN of the stream whose metadata you want to update.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**[StreamName](#API_UpdateStream_RequestSyntax "#API_UpdateStream_RequestSyntax")**

The name of the stream whose metadata you want to update.

The stream name is an identifier for the stream, and must be unique for each
account and region.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

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

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/UpdateStream.md "../../../goto/cli2/kinesisvideo-2017-09-30/UpdateStream.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/UpdateStream.md "../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/UpdateStream.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/UpdateStream.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/UpdateStream.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/UpdateStream.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/UpdateStream.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/UpdateStream.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/UpdateStream.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/UpdateStream.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/UpdateStream.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/UpdateStream.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/UpdateStream.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/UpdateStream.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/UpdateStream.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/UpdateStream.md "../../../goto/boto3/kinesisvideo-2017-09-30/UpdateStream.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/UpdateStream.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/UpdateStream.md")
