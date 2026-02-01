# ListSpeechSynthesisTasks

Returns a list of SpeechSynthesisTask objects ordered by their
creation date. This operation can filter the tasks by their status, for
example, allowing users to list only tasks that are completed.

## Request Syntax

```
GET /v1/synthesisTasks?MaxResults=`MaxResults`&NextToken=`NextToken`&Status=`Status` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[MaxResults](#API_ListSpeechSynthesisTasks_RequestSyntax "#API_ListSpeechSynthesisTasks_RequestSyntax")**

Maximum number of speech synthesis tasks returned in a List
operation.

Valid Range: Minimum value of 1. Maximum value of 100.

**[NextToken](#API_ListSpeechSynthesisTasks_RequestSyntax "#API_ListSpeechSynthesisTasks_RequestSyntax")**

The pagination token to use in the next request to continue the
listing of speech synthesis tasks.

Length Constraints: Minimum length of 0. Maximum length of 4096.

**[Status](#API_ListSpeechSynthesisTasks_RequestSyntax "#API_ListSpeechSynthesisTasks_RequestSyntax")**

Status of the speech synthesis tasks returned in a List
operation

Valid Values: `scheduled | inProgress | completed | failed`

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "SynthesisTasks": [
      {
         "CreationTime": ***number***,
         "Engine": "***string***",
         "LanguageCode": "***string***",
         "LexiconNames": [ "***string***" ],
         "OutputFormat": "***string***",
         "OutputUri": "***string***",
         "RequestCharacters": ***number***,
         "SampleRate": "***string***",
         "SnsTopicArn": "***string***",
         "SpeechMarkTypes": [ "***string***" ],
         "TaskId": "***string***",
         "TaskStatus": "***string***",
         "TaskStatusReason": "***string***",
         "TextType": "***string***",
         "VoiceId": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListSpeechSynthesisTasks_ResponseSyntax "#API_ListSpeechSynthesisTasks_ResponseSyntax")**

An opaque pagination token returned from the previous List operation
in this request. If present, this indicates where to continue the
listing.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 4096.

**[SynthesisTasks](#API_ListSpeechSynthesisTasks_ResponseSyntax "#API_ListSpeechSynthesisTasks_ResponseSyntax")**

List of SynthesisTask objects that provides information from the
specified task in the list request, including output format, creation
time, task status, and so on.

Type: Array of [SynthesisTask](API_SynthesisTask.md "API_SynthesisTask.md") objects

## Errors

**InvalidNextTokenException**

The NextToken is invalid. Verify that it's spelled correctly, and
then try again.

HTTP Status Code: 400

**ServiceFailureException**

An unknown condition has caused a service failure.

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/polly-2016-06-10/ListSpeechSynthesisTasks.md "../../../goto/cli2/polly-2016-06-10/ListSpeechSynthesisTasks.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/polly-2016-06-10/ListSpeechSynthesisTasks.md "../../../goto/DotNetSDKV4/polly-2016-06-10/ListSpeechSynthesisTasks.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/polly-2016-06-10/ListSpeechSynthesisTasks.md "../../../goto/SdkForCpp/polly-2016-06-10/ListSpeechSynthesisTasks.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/polly-2016-06-10/ListSpeechSynthesisTasks.md "../../../goto/SdkForGoV2/polly-2016-06-10/ListSpeechSynthesisTasks.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/polly-2016-06-10/ListSpeechSynthesisTasks.md "../../../goto/SdkForJavaV2/polly-2016-06-10/ListSpeechSynthesisTasks.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/polly-2016-06-10/ListSpeechSynthesisTasks.md "../../../goto/SdkForJavaScriptV3/polly-2016-06-10/ListSpeechSynthesisTasks.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/polly-2016-06-10/ListSpeechSynthesisTasks.md "../../../goto/SdkForKotlin/polly-2016-06-10/ListSpeechSynthesisTasks.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/polly-2016-06-10/ListSpeechSynthesisTasks.md "../../../goto/SdkForPHPV3/polly-2016-06-10/ListSpeechSynthesisTasks.md")
- [AWS SDK for Python](../../../goto/boto3/polly-2016-06-10/ListSpeechSynthesisTasks.md "../../../goto/boto3/polly-2016-06-10/ListSpeechSynthesisTasks.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/polly-2016-06-10/ListSpeechSynthesisTasks.md "../../../goto/SdkForRubyV3/polly-2016-06-10/ListSpeechSynthesisTasks.md")
