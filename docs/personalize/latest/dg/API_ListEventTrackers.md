# ListEventTrackers

Returns the list of event trackers associated with the account.
The response provides the properties for each event tracker, including the Amazon Resource
Name (ARN) and tracking ID. For more
information on event trackers, see [CreateEventTracker](API_CreateEventTracker.md "API_CreateEventTracker.md").

## Request Syntax

```
{
   "datasetGroupArn": "`string`",
   "maxResults": `number`,
   "nextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[datasetGroupArn](#API_ListEventTrackers_RequestSyntax "#API_ListEventTrackers_RequestSyntax")**

The ARN of a dataset group used to filter the response.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**[maxResults](#API_ListEventTrackers_RequestSyntax "#API_ListEventTrackers_RequestSyntax")**

The maximum number of event trackers to return.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[nextToken](#API_ListEventTrackers_RequestSyntax "#API_ListEventTrackers_RequestSyntax")**

A token returned from the previous call to `ListEventTrackers` for getting
the next set of event trackers (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

Required: No

## Response Syntax

```
{
   "eventTrackers": [
      {
         "creationDateTime": ***number***,
         "eventTrackerArn": "***string***",
         "lastUpdatedDateTime": ***number***,
         "name": "***string***",
         "status": "***string***"
      }
   ],
   "nextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[eventTrackers](#API_ListEventTrackers_ResponseSyntax "#API_ListEventTrackers_ResponseSyntax")**

A list of event trackers.

Type: Array of [EventTrackerSummary](API_EventTrackerSummary.md "API_EventTrackerSummary.md") objects

Array Members: Maximum number of 100 items.

**[nextToken](#API_ListEventTrackers_ResponseSyntax "#API_ListEventTrackers_ResponseSyntax")**

A token for getting the next set of event trackers (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**InvalidNextTokenException**

The token is not valid.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/ListEventTrackers.md "../../../goto/cli2/personalize-2018-05-22/ListEventTrackers.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/ListEventTrackers.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/ListEventTrackers.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/ListEventTrackers.md "../../../goto/SdkForCpp/personalize-2018-05-22/ListEventTrackers.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/ListEventTrackers.md "../../../goto/SdkForGoV2/personalize-2018-05-22/ListEventTrackers.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/ListEventTrackers.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/ListEventTrackers.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListEventTrackers.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListEventTrackers.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/ListEventTrackers.md "../../../goto/SdkForKotlin/personalize-2018-05-22/ListEventTrackers.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/ListEventTrackers.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/ListEventTrackers.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/ListEventTrackers.md "../../../goto/boto3/personalize-2018-05-22/ListEventTrackers.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/ListEventTrackers.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/ListEventTrackers.md")
