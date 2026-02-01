# UpdateDataRetention

Increases or decreases the stream's data retention period by the value that you
specify. To indicate whether you want to increase or decrease the data retention period,
specify the `Operation` parameter in the request body. In the request, you
must specify either the `StreamName` or the `StreamARN`.

This operation requires permission for the
`KinesisVideo:UpdateDataRetention` action.

Changing the data retention period affects the data in the stream as
follows:

- If the data retention period is increased, existing data is retained for
  the new retention period. For example, if the data retention period is increased
  from one hour to seven hours, all existing data is retained for seven
  hours.
- If the data retention period is decreased, existing data is retained for
  the new retention period. For example, if the data retention period is decreased
  from seven hours to one hour, all existing data is retained for one hour, and
  any data older than one hour is deleted immediately.

## Request Syntax

```
POST /updateDataRetention HTTP/1.1
Content-type: application/json

{
   "CurrentVersion": "`string`",
   "DataRetentionChangeInHours": `number`,
   "Operation": "`string`",
   "StreamARN": "`string`",
   "StreamName": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[CurrentVersion](#API_UpdateDataRetention_RequestSyntax "#API_UpdateDataRetention_RequestSyntax")**

The version of the stream whose retention period you want to change. To get the
version, call either the `DescribeStream` or the `ListStreams`
API.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `[a-zA-Z0-9]+`

Required: Yes

**[DataRetentionChangeInHours](#API_UpdateDataRetention_RequestSyntax "#API_UpdateDataRetention_RequestSyntax")**

The number of hours to adjust the current retention by. The value you specify is added to or subtracted from the current value, depending on the `operation`.

The minimum value for data retention is 0 and the maximum value is 87600 (ten years).

Type: Integer

Valid Range: Minimum value of 1.

Required: Yes

**[Operation](#API_UpdateDataRetention_RequestSyntax "#API_UpdateDataRetention_RequestSyntax")**

Indicates whether you want to increase or decrease the retention period.

Type: String

Valid Values: `INCREASE_DATA_RETENTION | DECREASE_DATA_RETENTION`

Required: Yes

**[StreamARN](#API_UpdateDataRetention_RequestSyntax "#API_UpdateDataRetention_RequestSyntax")**

The Amazon Resource Name (ARN) of the stream whose retention period you want to
change.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**[StreamName](#API_UpdateDataRetention_RequestSyntax "#API_UpdateDataRetention_RequestSyntax")**

The name of the stream whose retention period you want to change.

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

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/UpdateDataRetention.md "../../../goto/cli2/kinesisvideo-2017-09-30/UpdateDataRetention.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/UpdateDataRetention.md "../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/UpdateDataRetention.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/UpdateDataRetention.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/UpdateDataRetention.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/UpdateDataRetention.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/UpdateDataRetention.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/UpdateDataRetention.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/UpdateDataRetention.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/UpdateDataRetention.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/UpdateDataRetention.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/UpdateDataRetention.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/UpdateDataRetention.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/UpdateDataRetention.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/UpdateDataRetention.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/UpdateDataRetention.md "../../../goto/boto3/kinesisvideo-2017-09-30/UpdateDataRetention.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/UpdateDataRetention.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/UpdateDataRetention.md")
