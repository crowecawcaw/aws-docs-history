# ListEdgeAgentConfigurations

Returns an array of edge configurations associated with the specified Edge Agent.

In the request, you must specify the Edge Agent `HubDeviceArn`.

###### Note

This API isn't available in the AWS Africa (Cape Town) region, af-south-1.

## Request Syntax

```
POST /listEdgeAgentConfigurations HTTP/1.1
Content-type: application/json

{
   "HubDeviceArn": "`string`",
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[HubDeviceArn](#API_ListEdgeAgentConfigurations_RequestSyntax "#API_ListEdgeAgentConfigurations_RequestSyntax")**

The "Internet of Things (IoT) Thing" Arn of the edge agent.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:iot:[a-z0-9-]+:[0-9]+:thing/[a-zA-Z0-9_.-]+`

Required: Yes

**[MaxResults](#API_ListEdgeAgentConfigurations_RequestSyntax "#API_ListEdgeAgentConfigurations_RequestSyntax")**

The maximum number of edge configurations to return in the response. The default is 5.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 10.

Required: No

**[NextToken](#API_ListEdgeAgentConfigurations_RequestSyntax "#API_ListEdgeAgentConfigurations_RequestSyntax")**

If you specify this parameter, when the result of a `ListEdgeAgentConfigurations` operation is truncated, the call returns the `NextToken` in the response. To get another batch of edge configurations, provide this token in your next request.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Pattern: `[a-zA-Z0-9+/=]*`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "EdgeConfigs": [
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
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[EdgeConfigs](#API_ListEdgeAgentConfigurations_ResponseSyntax "#API_ListEdgeAgentConfigurations_ResponseSyntax")**

A description of a single stream's edge configuration.

Type: Array of [ListEdgeAgentConfigurationsEdgeConfig](API_ListEdgeAgentConfigurationsEdgeConfig.md "API_ListEdgeAgentConfigurationsEdgeConfig.md") objects

**[NextToken](#API_ListEdgeAgentConfigurations_ResponseSyntax "#API_ListEdgeAgentConfigurations_ResponseSyntax")**

If the response is truncated, the call returns this element with a given token. To get the next batch of edge configurations, use this token in your next request.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Pattern: `[a-zA-Z0-9+/=]*`

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

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md "../../../goto/cli2/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md "../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md "../../../goto/boto3/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations.md")
