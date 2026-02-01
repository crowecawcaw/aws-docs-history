# DescribeStream

Returns the most current information about the specified stream. You must specify
either the `StreamName` or the `StreamARN`.

## Request Syntax

```
POST /describeStream HTTP/1.1
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

**[StreamARN](#API_DescribeStream_RequestSyntax "#API_DescribeStream_RequestSyntax")**

The Amazon Resource Name (ARN) of the stream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**[StreamName](#API_DescribeStream_RequestSyntax "#API_DescribeStream_RequestSyntax")**

The name of the stream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "StreamInfo": {
      "CreationTime": ***number***,
      "DataRetentionInHours": ***number***,
      "DeviceName": "***string***",
      "KmsKeyId": "***string***",
      "MediaType": "***string***",
      "Status": "***string***",
      "StreamARN": "***string***",
      "StreamName": "***string***",
      "Version": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[StreamInfo](#API_DescribeStream_ResponseSyntax "#API_DescribeStream_ResponseSyntax")**

An object that describes the stream.

Type: [StreamInfo](API_StreamInfo.md "API_StreamInfo.md") object

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

**ResourceNotFoundException**

Amazon Kinesis Video Streams can't find the stream that you specified.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/DescribeStream.md "../../../goto/cli2/kinesisvideo-2017-09-30/DescribeStream.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/DescribeStream.md "../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/DescribeStream.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/DescribeStream.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/DescribeStream.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/DescribeStream.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/DescribeStream.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/DescribeStream.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/DescribeStream.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/DescribeStream.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/DescribeStream.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/DescribeStream.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/DescribeStream.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/DescribeStream.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/DescribeStream.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/DescribeStream.md "../../../goto/boto3/kinesisvideo-2017-09-30/DescribeStream.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/DescribeStream.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/DescribeStream.md")
