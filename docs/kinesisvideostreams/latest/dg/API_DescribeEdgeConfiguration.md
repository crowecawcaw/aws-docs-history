# DescribeEdgeConfiguration

Describes a stream’s edge configuration that was set using the
`StartEdgeConfigurationUpdate` API and the latest status of the edge
agent's recorder and uploader jobs. Use this API to get the status of the configuration
to determine if the configuration is in sync with the Edge Agent. Use this API to
evaluate the health of the Edge Agent.

###### Note

This API isn't available in the AWS Africa (Cape Town) region, af-south-1.

## Request Syntax

```
POST /describeEdgeConfiguration HTTP/1.1
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

**[StreamARN](#API_DescribeEdgeConfiguration_RequestSyntax "#API_DescribeEdgeConfiguration_RequestSyntax")**

The Amazon Resource Name (ARN) of the stream. Specify either the `StreamName`or the `StreamARN`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**[StreamName](#API_DescribeEdgeConfiguration_RequestSyntax "#API_DescribeEdgeConfiguration_RequestSyntax")**

The name of the stream whose edge configuration you want to update. Specify either the `StreamName` or
the `StreamARN`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationTime": ***number***,
   "EdgeAgentStatus": {
      "LastRecorderStatus": {
         "JobStatusDetails": "***string***",
         "LastCollectedTime": ***number***,
         "LastUpdatedTime": ***number***,
         "RecorderStatus": "***string***"
      },
      "LastUploaderStatus": {
         "JobStatusDetails": "***string***",
         "LastCollectedTime": ***number***,
         "LastUpdatedTime": ***number***,
         "UploaderStatus": "***string***"
      }
   },
   "EdgeConfig": {
      "DeletionConfig": {
         "DeleteAfterUpload": ***boolean***,
         "EdgeRetentionInHours": ***number***,
         "LocalSizeConfig": {
            "MaxLocalMediaSizeInMB": ***number***,
            "StrategyOnFullSize": "***string***"
         }
      },
      "HubDeviceArn": "***string***",
      "RecorderConfig": {
         "MediaSourceConfig": {
            "MediaUriSecretArn": "***string***",
            "MediaUriType": "***string***"
         },
         "ScheduleConfig": {
            "DurationInSeconds": ***number***,
            "ScheduleExpression": "***string***"
         }
      },
      "UploaderConfig": {
         "ScheduleConfig": {
            "DurationInSeconds": ***number***,
            "ScheduleExpression": "***string***"
         }
      }
   },
   "FailedStatusDetails": "***string***",
   "LastUpdatedTime": ***number***,
   "StreamARN": "***string***",
   "StreamName": "***string***",
   "SyncStatus": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_DescribeEdgeConfiguration_ResponseSyntax "#API_DescribeEdgeConfiguration_ResponseSyntax")**

The timestamp at which a stream’s edge configuration was first created.

Type: Timestamp

**[EdgeAgentStatus](#API_DescribeEdgeConfiguration_ResponseSyntax "#API_DescribeEdgeConfiguration_ResponseSyntax")**

An object that contains the latest status details for an edge agent's recorder and uploader jobs. Use this information to determine the current health of an edge agent.

Type: [EdgeAgentStatus](API_EdgeAgentStatus.md "API_EdgeAgentStatus.md") object

**[EdgeConfig](#API_DescribeEdgeConfiguration_ResponseSyntax "#API_DescribeEdgeConfiguration_ResponseSyntax")**

A description of the stream's edge configuration that will be used to sync
with the Edge Agent IoT Greengrass component. The Edge Agent component will run
on an IoT Hub Device setup at your premise.

Type: [EdgeConfig](API_EdgeConfig.md "API_EdgeConfig.md") object

**[FailedStatusDetails](#API_DescribeEdgeConfiguration_ResponseSyntax "#API_DescribeEdgeConfiguration_ResponseSyntax")**

A description of the generated failure status.

Type: String

**[LastUpdatedTime](#API_DescribeEdgeConfiguration_ResponseSyntax "#API_DescribeEdgeConfiguration_ResponseSyntax")**

The timestamp at which a stream’s edge configuration was last updated.

Type: Timestamp

**[StreamARN](#API_DescribeEdgeConfiguration_ResponseSyntax "#API_DescribeEdgeConfiguration_ResponseSyntax")**

The Amazon Resource Name (ARN) of the stream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

**[StreamName](#API_DescribeEdgeConfiguration_ResponseSyntax "#API_DescribeEdgeConfiguration_ResponseSyntax")**

The name of the stream from which the edge configuration was updated.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

**[SyncStatus](#API_DescribeEdgeConfiguration_ResponseSyntax "#API_DescribeEdgeConfiguration_ResponseSyntax")**

The latest status of the edge configuration update.

Type: String

Valid Values: `SYNCING | ACKNOWLEDGED | IN_SYNC | SYNC_FAILED | DELETING | DELETE_FAILED | DELETING_ACKNOWLEDGED`

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

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md "../../../goto/cli2/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md "../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md "../../../goto/boto3/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/DescribeEdgeConfiguration.md")
