# ListSignalingChannels

Returns an array of `ChannelInfo` objects. Each object describes a
signaling channel. To retrieve only those channels that satisfy a specific condition,
you can specify a `ChannelNameCondition`.

## Request Syntax

```
POST /listSignalingChannels HTTP/1.1
Content-type: application/json

{
   "ChannelNameCondition": {
      "ComparisonOperator": "`string`",
      "ComparisonValue": "`string`"
   },
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[ChannelNameCondition](#API_ListSignalingChannels_RequestSyntax "#API_ListSignalingChannels_RequestSyntax")**

Optional: Returns only the channels that satisfy a specific condition.

Type: [ChannelNameCondition](API_ChannelNameCondition.md "API_ChannelNameCondition.md") object

Required: No

**[MaxResults](#API_ListSignalingChannels_RequestSyntax "#API_ListSignalingChannels_RequestSyntax")**

The maximum number of channels to return in the response. The default is 500.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 10000.

Required: No

**[NextToken](#API_ListSignalingChannels_RequestSyntax "#API_ListSignalingChannels_RequestSyntax")**

If you specify this parameter, when the result of a `ListSignalingChannels`
operation is truncated, the call returns the `NextToken` in the response. To
get another batch of channels, provide this token in your next request.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Pattern: `[a-zA-Z0-9+/=]*`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "ChannelInfoList": [
      {
         "ChannelARN": "***string***",
         "ChannelName": "***string***",
         "ChannelStatus": "***string***",
         "ChannelType": "***string***",
         "CreationTime": ***number***,
         "SingleMasterConfiguration": {
            "MessageTtlSeconds": ***number***
         },
         "Version": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ChannelInfoList](#API_ListSignalingChannels_ResponseSyntax "#API_ListSignalingChannels_ResponseSyntax")**

An array of `ChannelInfo` objects.

Type: Array of [ChannelInfo](API_ChannelInfo.md "API_ChannelInfo.md") objects

**[NextToken](#API_ListSignalingChannels_ResponseSyntax "#API_ListSignalingChannels_ResponseSyntax")**

If the response is truncated, the call returns this element with a token. To get the
next batch of streams, use this token in your next request.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Pattern: `[a-zA-Z0-9+/=]*`

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

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/ListSignalingChannels.md "../../../goto/cli2/kinesisvideo-2017-09-30/ListSignalingChannels.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/ListSignalingChannels.md "../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/ListSignalingChannels.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/ListSignalingChannels.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/ListSignalingChannels.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/ListSignalingChannels.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/ListSignalingChannels.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/ListSignalingChannels.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/ListSignalingChannels.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/ListSignalingChannels.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/ListSignalingChannels.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/ListSignalingChannels.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/ListSignalingChannels.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/ListSignalingChannels.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/ListSignalingChannels.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/ListSignalingChannels.md "../../../goto/boto3/kinesisvideo-2017-09-30/ListSignalingChannels.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/ListSignalingChannels.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/ListSignalingChannels.md")
