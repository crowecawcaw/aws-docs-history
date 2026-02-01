# GetSpeechSynthesisTask

Retrieves a specific SpeechSynthesisTask object based on its TaskID.
This object contains information about the given speech synthesis task,
including the status of the task, and a link to the S3 bucket containing
the output of the task.

## Request Syntax

```
GET /v1/synthesisTasks/`TaskId` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[TaskId](#API_GetSpeechSynthesisTask_RequestSyntax "#API_GetSpeechSynthesisTask_RequestSyntax")**

The Amazon Polly generated identifier for a speech synthesis task.

Pattern: `^[a-zA-Z0-9_-]{1,100}$`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "SynthesisTask": {
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
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[SynthesisTask](#API_GetSpeechSynthesisTask_ResponseSyntax "#API_GetSpeechSynthesisTask_ResponseSyntax")**

SynthesisTask object that provides information from the requested
task, including output format, creation time, task status, and so
on.

Type: [SynthesisTask](API_SynthesisTask.md "API_SynthesisTask.md") object

## Errors

**InvalidTaskIdException**

The provided Task ID is not valid. Please provide a valid Task ID and
try again.

HTTP Status Code: 400

**ServiceFailureException**

An unknown condition has caused a service failure.

HTTP Status Code: 500

**SynthesisTaskNotFoundException**

The Speech Synthesis task with requested Task ID cannot be
found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/polly-2016-06-10/GetSpeechSynthesisTask.md "../../../goto/cli2/polly-2016-06-10/GetSpeechSynthesisTask.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/polly-2016-06-10/GetSpeechSynthesisTask.md "../../../goto/DotNetSDKV4/polly-2016-06-10/GetSpeechSynthesisTask.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/polly-2016-06-10/GetSpeechSynthesisTask.md "../../../goto/SdkForCpp/polly-2016-06-10/GetSpeechSynthesisTask.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/polly-2016-06-10/GetSpeechSynthesisTask.md "../../../goto/SdkForGoV2/polly-2016-06-10/GetSpeechSynthesisTask.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/polly-2016-06-10/GetSpeechSynthesisTask.md "../../../goto/SdkForJavaV2/polly-2016-06-10/GetSpeechSynthesisTask.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/polly-2016-06-10/GetSpeechSynthesisTask.md "../../../goto/SdkForJavaScriptV3/polly-2016-06-10/GetSpeechSynthesisTask.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/polly-2016-06-10/GetSpeechSynthesisTask.md "../../../goto/SdkForKotlin/polly-2016-06-10/GetSpeechSynthesisTask.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/polly-2016-06-10/GetSpeechSynthesisTask.md "../../../goto/SdkForPHPV3/polly-2016-06-10/GetSpeechSynthesisTask.md")
- [AWS SDK for Python](../../../goto/boto3/polly-2016-06-10/GetSpeechSynthesisTask.md "../../../goto/boto3/polly-2016-06-10/GetSpeechSynthesisTask.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/polly-2016-06-10/GetSpeechSynthesisTask.md "../../../goto/SdkForRubyV3/polly-2016-06-10/GetSpeechSynthesisTask.md")
