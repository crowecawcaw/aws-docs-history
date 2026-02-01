End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# GetBot

Returns metadata information for a specific bot. You must provide
the bot name and the bot version or alias.

This operation requires permissions for the
`lex:GetBot` action.

## Request Syntax

```
GET /bots/`name`/versions/`versionoralias` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_GetBot_RequestSyntax "#API_GetBot_RequestSyntax")**

The name of the bot. The name is case sensitive.

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

**[versionoralias](#API_GetBot_RequestSyntax "#API_GetBot_RequestSyntax")**

The version or alias of the bot.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "abortStatement": {
      "messages": [
         {
            "content": "***string***",
            "contentType": "***string***",
            "groupNumber": ***number***
         }
      ],
      "responseCard": "***string***"
   },
   "checksum": "***string***",
   "childDirected": ***boolean***,
   "clarificationPrompt": {
      "maxAttempts": ***number***,
      "messages": [
         {
            "content": "***string***",
            "contentType": "***string***",
            "groupNumber": ***number***
         }
      ],
      "responseCard": "***string***"
   },
   "createdDate": ***number***,
   "description": "***string***",
   "detectSentiment": ***boolean***,
   "enableModelImprovements": ***boolean***,
   "failureReason": "***string***",
   "idleSessionTTLInSeconds": ***number***,
   "intents": [
      {
         "intentName": "***string***",
         "intentVersion": "***string***"
      }
   ],
   "lastUpdatedDate": ***number***,
   "locale": "***string***",
   "name": "***string***",
   "nluIntentConfidenceThreshold": ***number***,
   "status": "***string***",
   "version": "***string***",
   "voiceId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[abortStatement](#API_GetBot_ResponseSyntax "#API_GetBot_ResponseSyntax")**

The message that Amazon Lex returns when the user elects to end the
conversation without completing it. For more information, see [PutBot](API_PutBot.md "API_PutBot.md").

Type: [Statement](API_Statement.md "API_Statement.md") object

**[checksum](#API_GetBot_ResponseSyntax "#API_GetBot_ResponseSyntax")**

Checksum of the bot used to identify a specific revision of the
bot's `$LATEST` version.

Type: String

**[childDirected](#API_GetBot_ResponseSyntax "#API_GetBot_ResponseSyntax")**

For each Amazon Lex bot created with the Amazon Lex Model Building Service,
you must specify whether your use of Amazon Lex is related to a website,
program, or other application that is directed or targeted, in whole or in
part, to children under age 13 and subject to the Children's Online
Privacy Protection Act (COPPA) by specifying `true` or
`false` in the `childDirected` field. By
specifying `true` in the `childDirected` field, you
confirm that your use of Amazon Lex **is** related
to a website, program, or other application that is directed or targeted,
in whole or in part, to children under age 13 and subject to COPPA. By
specifying `false` in the `childDirected` field, you
confirm that your use of Amazon Lex **is not**
related to a website, program, or other application that is directed or
targeted, in whole or in part, to children under age 13 and subject to
COPPA. You may not specify a default value for the
`childDirected` field that does not accurately reflect
whether your use of Amazon Lex is related to a website, program, or other
application that is directed or targeted, in whole or in part, to children
under age 13 and subject to COPPA.

If your use of Amazon Lex relates to a website, program, or other
application that is directed in whole or in part, to children under age
13, you must obtain any required verifiable parental consent under COPPA.
For information regarding the use of Amazon Lex in connection with websites,
programs, or other applications that are directed or targeted, in whole or
in part, to children under age 13, see the [Amazon Lex FAQ.](https://aws.amazon.com/lex/faqs#data-security "https://aws.amazon.com/lex/faqs#data-security")

Type: Boolean

**[clarificationPrompt](#API_GetBot_ResponseSyntax "#API_GetBot_ResponseSyntax")**

The message Amazon Lex uses when it doesn't understand the user's
request. For more information, see [PutBot](API_PutBot.md "API_PutBot.md").

Type: [Prompt](API_Prompt.md "API_Prompt.md") object

**[createdDate](#API_GetBot_ResponseSyntax "#API_GetBot_ResponseSyntax")**

The date that the bot was created.

Type: Timestamp

**[description](#API_GetBot_ResponseSyntax "#API_GetBot_ResponseSyntax")**

A description of the bot.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 200.

**[detectSentiment](#API_GetBot_ResponseSyntax "#API_GetBot_ResponseSyntax")**

Indicates whether user utterances should be sent to Amazon Comprehend
for sentiment analysis.

Type: Boolean

**[enableModelImprovements](#API_GetBot_ResponseSyntax "#API_GetBot_ResponseSyntax")**

Indicates whether the bot uses accuracy improvements.
`true` indicates that the bot is using the improvements,
otherwise, `false`.

Type: Boolean

**[failureReason](#API_GetBot_ResponseSyntax "#API_GetBot_ResponseSyntax")**

If `status` is `FAILED`, Amazon Lex explains why
it failed to build the bot.

Type: String

**[idleSessionTTLInSeconds](#API_GetBot_ResponseSyntax "#API_GetBot_ResponseSyntax")**

The maximum time in seconds that Amazon Lex retains the data gathered in
a conversation. For more information, see [PutBot](API_PutBot.md "API_PutBot.md").

Type: Integer

Valid Range: Minimum value of 60. Maximum value of 86400.

**[intents](#API_GetBot_ResponseSyntax "#API_GetBot_ResponseSyntax")**

An array of `intent` objects. For more information, see
[PutBot](API_PutBot.md "API_PutBot.md").

Type: Array of [Intent](API_Intent.md "API_Intent.md") objects

**[lastUpdatedDate](#API_GetBot_ResponseSyntax "#API_GetBot_ResponseSyntax")**

The date that the bot was updated. When you create a resource, the
creation date and last updated date are the same.

Type: Timestamp

**[locale](#API_GetBot_ResponseSyntax "#API_GetBot_ResponseSyntax")**

The target locale for the bot.

Type: String

Valid Values: `de-DE | en-AU | en-GB | en-IN | en-US | es-419 | es-ES | es-US | fr-FR | fr-CA | it-IT | ja-JP | ko-KR`

**[name](#API_GetBot_ResponseSyntax "#API_GetBot_ResponseSyntax")**

The name of the bot.

Type: String

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

**[nluIntentConfidenceThreshold](#API_GetBot_ResponseSyntax "#API_GetBot_ResponseSyntax")**

The score that determines where Amazon Lex inserts the
`AMAZON.FallbackIntent`,
`AMAZON.KendraSearchIntent`, or both when returning
alternative intents in a [PostContent](API_runtime_PostContent.md "API_runtime_PostContent.md") or
[PostText](API_runtime_PostText.md "API_runtime_PostText.md") response.
`AMAZON.FallbackIntent` is inserted if the confidence score
for all intents is below this value.
`AMAZON.KendraSearchIntent` is only inserted if it is
configured for the bot.

Type: Double

Valid Range: Minimum value of 0. Maximum value of 1.

**[status](#API_GetBot_ResponseSyntax "#API_GetBot_ResponseSyntax")**

The status of the bot.

When the status is `BUILDING` Amazon Lex is building the bot
for testing and use.

If the status of the bot is `READY_BASIC_TESTING`, you
can test the bot using the exact utterances specified in the bot's
intents. When the bot is ready for full testing or to run, the status is
`READY`.

If there was a problem with building the bot, the status is
`FAILED` and the `failureReason` field explains
why the bot did not build.

If the bot was saved but not built, the status is
`NOT_BUILT`.

Type: String

Valid Values: `BUILDING | READY | READY_BASIC_TESTING | FAILED | NOT_BUILT`

**[version](#API_GetBot_ResponseSyntax "#API_GetBot_ResponseSyntax")**

The version of the bot. For a new bot, the version is always
`$LATEST`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

**[voiceId](#API_GetBot_ResponseSyntax "#API_GetBot_ResponseSyntax")**

The Amazon Polly voice ID that Amazon Lex uses for voice interaction
with the user. For more information, see [PutBot](API_PutBot.md "API_PutBot.md").

Type: String

## Errors

**BadRequestException**

The request is not well formed. For example, a value is invalid or
a required field is missing. Check the field values, and try
again.

HTTP Status Code: 400

**InternalFailureException**

An internal Amazon Lex error occurred. Try your request again.

HTTP Status Code: 500

**LimitExceededException**

The request exceeded a limit. Try your request again.

HTTP Status Code: 429

**NotFoundException**

The resource specified in the request was not found. Check the
resource and try again.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/GetBot.md "../../../goto/cli2/lex-models-2017-04-19/GetBot.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lex-models-2017-04-19/GetBot.md "../../../goto/DotNetSDKV4/lex-models-2017-04-19/GetBot.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/GetBot.md "../../../goto/SdkForCpp/lex-models-2017-04-19/GetBot.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/GetBot.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/GetBot.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetBot.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetBot.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetBot.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetBot.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/GetBot.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/GetBot.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetBot.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetBot.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/GetBot.md "../../../goto/boto3/lex-models-2017-04-19/GetBot.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetBot.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetBot.md")
