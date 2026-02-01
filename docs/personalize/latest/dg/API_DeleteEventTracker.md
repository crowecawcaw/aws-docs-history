# DeleteEventTracker

Deletes the event tracker. Does not delete the dataset from
the dataset group. For more
information on event trackers, see [CreateEventTracker](API_CreateEventTracker.md "API_CreateEventTracker.md").

## Request Syntax

```
{
   "eventTrackerArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[eventTrackerArn](#API_DeleteEventTracker_RequestSyntax "#API_DeleteEventTracker_RequestSyntax")**

The Amazon Resource Name (ARN) of the event tracker to delete.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DeleteEventTracker.md "../../../goto/cli2/personalize-2018-05-22/DeleteEventTracker.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/DeleteEventTracker.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/DeleteEventTracker.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DeleteEventTracker.md "../../../goto/SdkForCpp/personalize-2018-05-22/DeleteEventTracker.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DeleteEventTracker.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DeleteEventTracker.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DeleteEventTracker.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DeleteEventTracker.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DeleteEventTracker.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DeleteEventTracker.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DeleteEventTracker.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DeleteEventTracker.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DeleteEventTracker.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DeleteEventTracker.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DeleteEventTracker.md "../../../goto/boto3/personalize-2018-05-22/DeleteEventTracker.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DeleteEventTracker.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DeleteEventTracker.md")
