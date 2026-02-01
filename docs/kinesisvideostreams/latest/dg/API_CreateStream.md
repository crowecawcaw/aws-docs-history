# CreateStream

Creates a new Kinesis video stream.

When you create a new stream, Kinesis Video Streams assigns it a version number.
When you change the stream's metadata, Kinesis Video Streams updates the version.

`CreateStream` is an asynchronous operation.

For information about how the service works, see [How it Works](how-it-works.md "how-it-works.md").

You must have permissions for the `KinesisVideo:CreateStream`
action.

## Request Syntax

```
POST /createStream HTTP/1.1
Content-type: application/json

{
   "DataRetentionInHours": `number`,
   "DeviceName": "`string`",
   "KmsKeyId": "`string`",
   "MediaType": "`string`",
   "StreamName": "`string`",
   "StreamStorageConfiguration": {
      "DefaultStorageTier": "`string`"
   },
   "Tags": {
      "`string`" : "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[DataRetentionInHours](#API_CreateStream_RequestSyntax "#API_CreateStream_RequestSyntax")**

The number of hours that you want to retain the data in the stream. Kinesis Video Streams retains the data in a data store that is associated with the stream.

The default value is 0, indicating that the stream does not persist data. The minimum
is 1 hour.

When the `DataRetentionInHours` value is 0, consumers can still consume
the fragments that remain in the service host buffer, which has a retention time limit
of 5 minutes and a retention memory limit of 200 MB. Fragments are removed from the
buffer when either limit is reached.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**[DeviceName](#API_CreateStream_RequestSyntax "#API_CreateStream_RequestSyntax")**

The name of the device that is writing to the stream.

###### Note

In the current implementation, Kinesis Video Streams doesn't use this name.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

**[KmsKeyId](#API_CreateStream_RequestSyntax "#API_CreateStream_RequestSyntax")**

The ID of the AWS Key Management Service (AWS KMS) key that you want Kinesis Video
Streams to use to encrypt stream data.

If no key ID is specified, the default, Kinesis Video-managed key
(`aws/kinesisvideo`) is used.

For more information, see [DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md#API_DescribeKey_RequestParameters "../../../kms/latest/APIReference/API_DescribeKey.md#API_DescribeKey_RequestParameters").

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `.+`

Required: No

**[MediaType](#API_CreateStream_RequestSyntax "#API_CreateStream_RequestSyntax")**

The media type of the stream. Consumers of the stream can use this information when
processing the stream. For more information about media types, see [Media
Types](http://www.iana.org/assignments/media-types/media-types.xhtml "http://www.iana.org/assignments/media-types/media-types.xhtml"). If you choose to specify the `MediaType`, see [Naming Requirements](https://tools.ietf.org/html/rfc6838#section-4.2 "https://tools.ietf.org/html/rfc6838#section-4.2")
for guidelines.

Example valid values include "video/h264" and "video/h264,audio/aac".

This parameter is optional; the default value is `null` (or empty in
JSON).

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[\w\-\.\+]+/[\w\-\.\+]+(,[\w\-\.\+]+/[\w\-\.\+]+)*`

Required: No

**[StreamName](#API_CreateStream_RequestSyntax "#API_CreateStream_RequestSyntax")**

A name for the stream that you are creating.

The stream name is an identifier for the stream, and must be unique for each
account and region.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**[StreamStorageConfiguration](#API_CreateStream_RequestSyntax "#API_CreateStream_RequestSyntax")**

The configuration for the stream's storage, including the default storage tier for stream data. This configuration determines how stream data is stored and accessed, with different tiers offering varying levels of performance and cost optimization.

If not specified, the stream will use the default storage configuration with HOT tier for optimal performance.

Type: [StreamStorageConfiguration](API_StreamStorageConfiguration.md "API_StreamStorageConfiguration.md") object

Required: No

**[Tags](#API_CreateStream_RequestSyntax "#API_CreateStream_RequestSyntax")**

A list of tags to associate with the specified stream. Each tag is a key-value pair
(the value is optional).

Type: String to string map

Map Entries: Maximum number of 50 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Value Length Constraints: Minimum length of 0. Maximum length of 256.

Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "StreamARN": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[StreamARN](#API_CreateStream_ResponseSyntax "#API_CreateStream_ResponseSyntax")**

The Amazon Resource Name (ARN) of the stream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccountStreamLimitExceededException**

The number of streams created for the account is too high.

HTTP Status Code: 400

**ClientLimitExceededException**

Kinesis Video Streams has throttled the request because you have exceeded the limit of
allowed client calls. Try making the call later.

HTTP Status Code: 400

**DeviceStreamLimitExceededException**

Not implemented.

HTTP Status Code: 400

**InvalidArgumentException**

The value for this input parameter is invalid.

HTTP Status Code: 400

**InvalidDeviceException**

Not implemented.

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

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/CreateStream.md "../../../goto/cli2/kinesisvideo-2017-09-30/CreateStream.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/CreateStream.md "../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/CreateStream.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/CreateStream.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/CreateStream.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/CreateStream.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/CreateStream.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/CreateStream.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/CreateStream.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/CreateStream.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/CreateStream.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/CreateStream.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/CreateStream.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/CreateStream.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/CreateStream.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/CreateStream.md "../../../goto/boto3/kinesisvideo-2017-09-30/CreateStream.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/CreateStream.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/CreateStream.md")
