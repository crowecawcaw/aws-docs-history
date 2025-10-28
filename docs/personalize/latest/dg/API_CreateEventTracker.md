# CreateEventTracker

Creates an event tracker that you use when adding event data to a specified dataset
group using the
[PutEvents](API_UBS_PutEvents.md "API_UBS_PutEvents.md") API.

###### Note

Only one event tracker can be associated with a dataset group. You will get
an error if you call `CreateEventTracker` using the same dataset group as an
existing event tracker.

When you create an event tracker, the response includes a tracking ID, which you pass as a parameter when you use the
[PutEvents](API_UBS_PutEvents.md "API_UBS_PutEvents.md") operation.
Amazon Personalize then appends the event data to the Item interactions dataset of the dataset group you specify
in your event tracker.

The event tracker can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
- DELETE PENDING > DELETE IN_PROGRESS
  To get the status of the event tracker, call [DescribeEventTracker](API_DescribeEventTracker.md "API_DescribeEventTracker.md").

###### Note

The event tracker must be in the ACTIVE state before using the tracking ID.

###### Related APIs

- [ListEventTrackers](API_ListEventTrackers.md "API_ListEventTrackers.md")
- [DescribeEventTracker](API_DescribeEventTracker.md "API_DescribeEventTracker.md")
- [DeleteEventTracker](API_DeleteEventTracker.md "API_DeleteEventTracker.md")

## Request Syntax

```
{
   "datasetGroupArn": "`string`",
   "name": "`string`",
   "tags": [
      {
         "tagKey": "`string`",
         "tagValue": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[datasetGroupArn](#API_CreateEventTracker_RequestSyntax "#API_CreateEventTracker_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset group that receives the event data.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[name](#API_CreateEventTracker_RequestSyntax "#API_CreateEventTracker_RequestSyntax")**

The name for the event tracker.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: Yes

**[tags](#API_CreateEventTracker_RequestSyntax "#API_CreateEventTracker_RequestSyntax")**

A list of [tags](tagging-resources.md "tagging-resources.md") to apply to the event tracker.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "eventTrackerArn": "***string***",
   "trackingId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[eventTrackerArn](#API_CreateEventTracker_ResponseSyntax "#API_CreateEventTracker_ResponseSyntax")**

The ARN of the event tracker.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

**[trackingId](#API_CreateEventTracker_ResponseSyntax "#API_CreateEventTracker_ResponseSyntax")**

The ID of the event tracker. Include this ID in requests to the
[PutEvents](API_UBS_PutEvents.md "API_UBS_PutEvents.md") API.

Type: String

Length Constraints: Maximum length of 256.

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**LimitExceededException**

The limit on the number of requests per second has been exceeded.

HTTP Status Code: 400

**ResourceAlreadyExistsException**

The specified resource already exists.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

**TooManyTagsException**

You have exceeded the maximum number of tags you can apply to this resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/CreateEventTracker.md "../../../goto/cli2/personalize-2018-05-22/CreateEventTracker.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateEventTracker.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateEventTracker.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/CreateEventTracker.md "../../../goto/SdkForCpp/personalize-2018-05-22/CreateEventTracker.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/CreateEventTracker.md "../../../goto/SdkForGoV2/personalize-2018-05-22/CreateEventTracker.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateEventTracker.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateEventTracker.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateEventTracker.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateEventTracker.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/CreateEventTracker.md "../../../goto/SdkForKotlin/personalize-2018-05-22/CreateEventTracker.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateEventTracker.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateEventTracker.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/CreateEventTracker.md "../../../goto/boto3/personalize-2018-05-22/CreateEventTracker.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateEventTracker.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateEventTracker.md")
