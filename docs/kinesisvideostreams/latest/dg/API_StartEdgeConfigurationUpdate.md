# StartEdgeConfigurationUpdate

An asynchronous API that updates a stream’s existing edge configuration.
The Kinesis Video Stream will sync the stream’s edge configuration with the Edge Agent IoT Greengrass
component that runs on an IoT Hub Device, setup at your premise. The time to sync can vary
and depends on the connectivity of the Hub Device.
The `SyncStatus` will be updated as the edge configuration is acknowledged,
and synced with the Edge Agent.

If this API is invoked for the first time, a new edge configuration will be created for the stream,
and the sync status will be set to `SYNCING`. You will have to wait for the sync status
to reach a terminal state such as: `IN_SYNC`, or `SYNC_FAILED`, before using this API again.
If you invoke this API during the syncing process, a `ResourceInUseException` will be thrown.
The connectivity of the stream’s edge configuration and the Edge Agent will be retried for 15 minutes. After 15 minutes,
the status will transition into the `SYNC_FAILED` state.

To move an edge configuration from one device to another, use [DeleteEdgeConfiguration](API_DeleteEdgeConfiguration.md "API_DeleteEdgeConfiguration.md") to delete
the current edge configuration. You can then invoke StartEdgeConfigurationUpdate with an updated Hub Device ARN.

###### Note

This API isn't available in the AWS Africa (Cape Town) region, af-south-1.

## Request Syntax

```
POST /startEdgeConfigurationUpdate HTTP/1.1
Content-type: application/json

{
   "EdgeConfig": {
      "DeletionConfig": {
         "DeleteAfterUpload": `boolean`,
         "EdgeRetentionInHours": `number`,
         "LocalSizeConfig": {
            "MaxLocalMediaSizeInMB": `number`,
            "StrategyOnFullSize": "`string`"
         }
      },
      "HubDeviceArn": "`string`",
      "RecorderConfig": {
         "MediaSourceConfig": {
            "MediaUriSecretArn": "`string`",
            "MediaUriType": "`string`"
         },
         "ScheduleConfig": {
            "DurationInSeconds": `number`,
            "ScheduleExpression": "`string`"
         }
      },
      "UploaderConfig": {
         "ScheduleConfig": {
            "DurationInSeconds": `number`,
            "ScheduleExpression": "`string`"
         }
      }
   },
   "StreamARN": "`string`",
   "StreamName": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[EdgeConfig](#API_StartEdgeConfigurationUpdate_RequestSyntax "#API_StartEdgeConfigurationUpdate_RequestSyntax")**

The edge configuration details required to invoke the update process.

Type: [EdgeConfig](API_EdgeConfig.md "API_EdgeConfig.md") object

Required: Yes

**[StreamARN](#API_StartEdgeConfigurationUpdate_RequestSyntax "#API_StartEdgeConfigurationUpdate_RequestSyntax")**

The Amazon Resource Name (ARN) of the stream. Specify either the
`StreamName` or the `StreamARN`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**[StreamName](#API_StartEdgeConfigurationUpdate_RequestSyntax "#API_StartEdgeConfigurationUpdate_RequestSyntax")**

The name of the stream whose edge configuration you want to update. Specify either the `StreamName`
or the `StreamARN`.

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

**[CreationTime](#API_StartEdgeConfigurationUpdate_ResponseSyntax "#API_StartEdgeConfigurationUpdate_ResponseSyntax")**

The timestamp at which a stream’s edge configuration was first created.

Type: Timestamp

**[EdgeConfig](#API_StartEdgeConfigurationUpdate_ResponseSyntax "#API_StartEdgeConfigurationUpdate_ResponseSyntax")**

A description of the stream's edge configuration that will be used to sync
with the Edge Agent IoT Greengrass component. The Edge Agent component will run
on an IoT Hub Device setup at your premise.

Type: [EdgeConfig](API_EdgeConfig.md "API_EdgeConfig.md") object

**[FailedStatusDetails](#API_StartEdgeConfigurationUpdate_ResponseSyntax "#API_StartEdgeConfigurationUpdate_ResponseSyntax")**

A description of the generated failure status.

Type: String

**[LastUpdatedTime](#API_StartEdgeConfigurationUpdate_ResponseSyntax "#API_StartEdgeConfigurationUpdate_ResponseSyntax")**

The timestamp at which a stream’s edge configuration was last updated.

Type: Timestamp

**[StreamARN](#API_StartEdgeConfigurationUpdate_ResponseSyntax "#API_StartEdgeConfigurationUpdate_ResponseSyntax")**

The Amazon Resource Name (ARN) of the stream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

**[StreamName](#API_StartEdgeConfigurationUpdate_ResponseSyntax "#API_StartEdgeConfigurationUpdate_ResponseSyntax")**

The name of the stream from which the edge configuration was updated.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

**[SyncStatus](#API_StartEdgeConfigurationUpdate_ResponseSyntax "#API_StartEdgeConfigurationUpdate_ResponseSyntax")**

The current sync status of the stream's edge configuration. When you invoke this API, the sync
status will be set to the `SYNCING` state. Use the `DescribeEdgeConfiguration` API
to get the latest status of the edge configuration.

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

**NoDataRetentionException**

The Stream data retention in hours is equal to zero.

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

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md "../../../goto/cli2/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md "../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md "../../../goto/boto3/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/StartEdgeConfigurationUpdate.md")
