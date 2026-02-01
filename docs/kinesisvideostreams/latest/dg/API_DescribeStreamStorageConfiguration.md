# DescribeStreamStorageConfiguration

Retrieves the current storage configuration for the specified Kinesis video stream.

In the request, you must specify either the `StreamName` or the `StreamARN`.

You must have permissions for the `KinesisVideo:DescribeStreamStorageConfiguration` action.

## Request Syntax

```
POST /describeStreamStorageConfiguration HTTP/1.1
Content-type: application/json

{
   "StreamARN": "`string`",
   "StreamName": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[StreamARN](#API_DescribeStreamStorageConfiguration_RequestSyntax "#API_DescribeStreamStorageConfiguration_RequestSyntax")**

The Amazon Resource Name (ARN) of the stream for which you want to retrieve the storage configuration.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**[StreamName](#API_DescribeStreamStorageConfiguration_RequestSyntax "#API_DescribeStreamStorageConfiguration_RequestSyntax")**

The name of the stream for which you want to retrieve the storage configuration.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "StreamARN": "***string***",
   "StreamName": "***string***",
   "StreamStorageConfiguration": {
      "DefaultStorageTier": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[StreamARN](#API_DescribeStreamStorageConfiguration_ResponseSyntax "#API_DescribeStreamStorageConfiguration_ResponseSyntax")**

The Amazon Resource Name (ARN) of the stream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

**[StreamName](#API_DescribeStreamStorageConfiguration_ResponseSyntax "#API_DescribeStreamStorageConfiguration_ResponseSyntax")**

The name of the stream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

**[StreamStorageConfiguration](#API_DescribeStreamStorageConfiguration_ResponseSyntax "#API_DescribeStreamStorageConfiguration_ResponseSyntax")**

The current storage configuration for the stream, including the default storage tier and other storage-related settings.

Type: [StreamStorageConfiguration](API_StreamStorageConfiguration.md "API_StreamStorageConfiguration.md") object

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

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md "../../../goto/cli2/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md "../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md "../../../goto/boto3/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/DescribeStreamStorageConfiguration.md")
