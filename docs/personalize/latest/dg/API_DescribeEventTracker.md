# DescribeEventTracker

Describes an event tracker. The response includes the `trackingId` and
`status` of the event tracker.
For more information on event trackers, see [CreateEventTracker](API_CreateEventTracker.md "API_CreateEventTracker.md").

## Request Syntax

```
{
   "eventTrackerArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[eventTrackerArn](#API_DescribeEventTracker_RequestSyntax "#API_DescribeEventTracker_RequestSyntax")**

The Amazon Resource Name (ARN) of the event tracker to describe.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "eventTracker": {
      "accountId": "***string***",
      "creationDateTime": ***number***,
      "datasetGroupArn": "***string***",
      "eventTrackerArn": "***string***",
      "lastUpdatedDateTime": ***number***,
      "name": "***string***",
      "status": "***string***",
      "trackingId": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[eventTracker](#API_DescribeEventTracker_ResponseSyntax "#API_DescribeEventTracker_ResponseSyntax")**

An object that describes the event tracker.

Type: [EventTracker](API_EventTracker.md "API_EventTracker.md") object

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DescribeEventTracker.md "../../../goto/cli2/personalize-2018-05-22/DescribeEventTracker.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeEventTracker.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeEventTracker.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DescribeEventTracker.md "../../../goto/SdkForCpp/personalize-2018-05-22/DescribeEventTracker.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeEventTracker.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeEventTracker.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeEventTracker.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeEventTracker.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeEventTracker.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeEventTracker.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeEventTracker.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeEventTracker.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeEventTracker.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeEventTracker.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DescribeEventTracker.md "../../../goto/boto3/personalize-2018-05-22/DescribeEventTracker.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeEventTracker.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeEventTracker.md")
