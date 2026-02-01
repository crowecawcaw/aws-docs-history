# ListStreams

Returns an array of `StreamInfo` objects. Each object describes a
stream. To retrieve only streams that satisfy a specific condition, you can specify a
`StreamNameCondition`.

## Request Syntax

```
POST /listStreams HTTP/1.1
Content-type: application/json

{
   "MaxResults": `number`,
   "NextToken": "`string`",
   "StreamNameCondition": {
      "ComparisonOperator": "`string`",
      "ComparisonValue": "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[MaxResults](#API_ListStreams_RequestSyntax "#API_ListStreams_RequestSyntax")**

The maximum number of streams to return in the response. The default is
10,000.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 10000.

Required: No

**[NextToken](#API_ListStreams_RequestSyntax "#API_ListStreams_RequestSyntax")**

If you specify this parameter, when the result of a `ListStreams`
operation is truncated, the call returns the `NextToken` in the response. To
get another batch of streams, provide this token in your next request.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Pattern: `[a-zA-Z0-9+/=]*`

Required: No

**[StreamNameCondition](#API_ListStreams_RequestSyntax "#API_ListStreams_RequestSyntax")**

Optional: Returns only streams that satisfy a specific condition. Currently, you
can specify only the prefix of a stream name as a condition.

Type: [StreamNameCondition](API_StreamNameCondition.md "API_StreamNameCondition.md") object

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "StreamInfoList": [
      {
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
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListStreams_ResponseSyntax "#API_ListStreams_ResponseSyntax")**

If the response is truncated, the call returns this element with a token. To get
the next batch of streams, use this token in your next request.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Pattern: `[a-zA-Z0-9+/=]*`

**[StreamInfoList](#API_ListStreams_ResponseSyntax "#API_ListStreams_ResponseSyntax")**

An array of `StreamInfo` objects.

Type: Array of [StreamInfo](API_StreamInfo.md "API_StreamInfo.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientLimitExceededException**

Kinesis Video Streams has throttled the request because you have exceeded the limit of
allowed client calls. Try making the call later.

HTTP Status Code: 400

**InvalidArgumentException**

The value for this input parameter is invalid.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/ListStreams.md "../../../goto/cli2/kinesisvideo-2017-09-30/ListStreams.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/ListStreams.md "../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/ListStreams.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/ListStreams.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/ListStreams.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/ListStreams.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/ListStreams.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/ListStreams.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/ListStreams.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/ListStreams.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/ListStreams.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/ListStreams.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/ListStreams.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/ListStreams.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/ListStreams.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/ListStreams.md "../../../goto/boto3/kinesisvideo-2017-09-30/ListStreams.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/ListStreams.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/ListStreams.md")
