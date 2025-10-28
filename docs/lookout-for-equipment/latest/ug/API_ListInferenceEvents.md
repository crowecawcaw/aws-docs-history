On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# ListInferenceEvents

Lists all inference events that have been found for the specified inference scheduler.

## Request Syntax

```
{
   "InferenceSchedulerName": "`string`",
   "IntervalEndTime": `number`,
   "IntervalStartTime": `number`,
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[InferenceSchedulerName](#API_ListInferenceEvents_RequestSyntax "#API_ListInferenceEvents_RequestSyntax")**

The name of the inference scheduler for the inference events listed.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

**[IntervalEndTime](#API_ListInferenceEvents_RequestSyntax "#API_ListInferenceEvents_RequestSyntax")**

Returns all the inference events with an end start time equal to or greater than less
than the end time given.

Type: Timestamp

Required: Yes

**[IntervalStartTime](#API_ListInferenceEvents_RequestSyntax "#API_ListInferenceEvents_RequestSyntax")**

Lookout for Equipment will return all the inference events with an end time equal to or greater than
the start time given.

Type: Timestamp

Required: Yes

**[MaxResults](#API_ListInferenceEvents_RequestSyntax "#API_ListInferenceEvents_RequestSyntax")**

Specifies the maximum number of inference events to list.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 500.

Required: No

**[NextToken](#API_ListInferenceEvents_RequestSyntax "#API_ListInferenceEvents_RequestSyntax")**

An opaque pagination token indicating where to continue the listing of inference
events.

Type: String

Length Constraints: Maximum length of 8192.

Pattern: `\p{ASCII}{0,8192}`

Required: No

## Response Syntax

```
{
   "InferenceEventSummaries": [
      {
         "Diagnostics": "***string***",
         "EventDurationInSeconds": ***number***,
         "EventEndTime": ***number***,
         "EventStartTime": ***number***,
         "InferenceSchedulerArn": "***string***",
         "InferenceSchedulerName": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[InferenceEventSummaries](#API_ListInferenceEvents_ResponseSyntax "#API_ListInferenceEvents_ResponseSyntax")**

Provides an array of information about the individual inference events returned from the
`ListInferenceEvents` operation, including scheduler used, event start time,
event end time, diagnostics, and so on.

Type: Array of [InferenceEventSummary](API_InferenceEventSummary.md "API_InferenceEventSummary.md") objects

**[NextToken](#API_ListInferenceEvents_ResponseSyntax "#API_ListInferenceEvents_ResponseSyntax")**

An opaque pagination token indicating where to continue the listing of inference
executions.

Type: String

Length Constraints: Maximum length of 8192.

Pattern: `\p{ASCII}{0,8192}`

## Errors

**AccessDeniedException**

The request could not be completed because you do not have access to the resource.

HTTP Status Code: 400

**InternalServerException**

Processing of the request has failed because of an unknown error, exception or failure.

HTTP Status Code: 500

**ResourceNotFoundException**

The resource requested could not be found. Verify the resource ID and retry your
request.

HTTP Status Code: 400

**ThrottlingException**

The request was denied due to request throttling.

HTTP Status Code: 400

**ValidationException**

The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related AWS
service that's being utilized.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/ListInferenceEvents.md "../../../goto/cli2/lookoutequipment-2020-12-15/ListInferenceEvents.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/ListInferenceEvents.md "../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/ListInferenceEvents.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ListInferenceEvents.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ListInferenceEvents.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/ListInferenceEvents.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/ListInferenceEvents.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ListInferenceEvents.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ListInferenceEvents.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ListInferenceEvents.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ListInferenceEvents.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/ListInferenceEvents.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/ListInferenceEvents.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/ListInferenceEvents.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/ListInferenceEvents.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/ListInferenceEvents.md "../../../goto/boto3/lookoutequipment-2020-12-15/ListInferenceEvents.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ListInferenceEvents.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ListInferenceEvents.md")
