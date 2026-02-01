# DeleteEdgeConfiguration

An asynchronous API that deletes a stream’s existing edge configuration, as well as the corresponding media from the Edge Agent.

When you invoke this API, the sync status is set to `DELETING`. A deletion process starts, in which active edge jobs are stopped and all media is deleted from the edge device. The time to delete varies, depending on the total amount of stored media. If the deletion process fails, the sync status changes to `DELETE_FAILED`. You will need to re-try the deletion.

When the deletion process has completed successfully, the edge configuration is no longer accessible.

###### Note

This API isn't available in the AWS Africa (Cape Town) region, af-south-1.

## Request Syntax

```
POST /deleteEdgeConfiguration HTTP/1.1
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

**[StreamARN](#API_DeleteEdgeConfiguration_RequestSyntax "#API_DeleteEdgeConfiguration_RequestSyntax")**

The Amazon Resource Name (ARN) of the stream. Specify either the `StreamName` or the `StreamARN`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**[StreamName](#API_DeleteEdgeConfiguration_RequestSyntax "#API_DeleteEdgeConfiguration_RequestSyntax")**

The name of the stream from which to delete the edge configuration. Specify either the `StreamName` or the `StreamARN`.

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

**StreamEdgeConfigurationNotFoundException**

The Exception rendered when the Amazon Kinesis Video Stream can't find a stream's edge configuration
that you specified.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md "../../../goto/cli2/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md "../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md "../../../goto/boto3/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/DeleteEdgeConfiguration.md")
