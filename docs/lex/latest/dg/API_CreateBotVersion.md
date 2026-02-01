End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# CreateBotVersion

Creates a new version of the bot based on the `$LATEST`
version. If the `$LATEST` version of this resource hasn't
changed since you created the last version, Amazon Lex doesn't create a new
version. It returns the last created version.

###### Note

You can update only the `$LATEST` version of the bot.
You can't update the numbered versions that you create with the
`CreateBotVersion` operation.

When you create the first version of a bot, Amazon Lex sets the version
to 1. Subsequent versions increment by 1. For more information, see [Versioning](versioning-aliases.md#versioning-intro "versioning-aliases.md#versioning-intro").

This operation requires permission for the
`lex:CreateBotVersion` action.

## Request Syntax

```
POST /bots/`name`/versions HTTP/1.1
Content-type: application/json

{
   "checksum": "`string`"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_CreateBotVersion_RequestSyntax "#API_CreateBotVersion_RequestSyntax")**

The name of the bot that you want to create a new version of. The
name is case sensitive.

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[checksum](#API_CreateBotVersion_RequestSyntax "#API_CreateBotVersion_RequestSyntax")**

Identifies a specific revision of the `$LATEST` version
of the bot. If you specify a checksum and the `$LATEST` version
of the bot has a different checksum, a
`PreconditionFailedException` exception is returned and Amazon Lex
doesn't publish a new version. If you don't specify a checksum, Amazon Lex
publishes the `$LATEST` version.

Type: String

Required: No

## Response Syntax

```
HTTP/1.1 201
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
   "status": "***string***",
   "version": "***string***",
   "voiceId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

**[abortStatement](#API_CreateBotVersion_ResponseSyntax "#API_CreateBotVersion_ResponseSyntax")**

The message that Amazon Lex uses to cancel a conversation. For more
information, see [PutBot](API_PutBot.md "API_PutBot.md").

Type: [Statement](API_Statement.md "API_Statement.md") object

**[checksum](#API_CreateBotVersion_ResponseSyntax "#API_CreateBotVersion_ResponseSyntax")**

Checksum identifying the version of the bot that was
created.

Type: String

**[childDirected](#API_CreateBotVersion_ResponseSyntax "#API_CreateBotVersion_ResponseSyntax")**

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

**[clarificationPrompt](#API_CreateBotVersion_ResponseSyntax "#API_CreateBotVersion_ResponseSyntax")**

The message that Amazon Lex uses when it doesn't understand the user's
request. For more information, see [PutBot](API_PutBot.md "API_PutBot.md").

Type: [Prompt](API_Prompt.md "API_Prompt.md") object

**[createdDate](#API_CreateBotVersion_ResponseSyntax "#API_CreateBotVersion_ResponseSyntax")**

The date when the bot version was created.

Type: Timestamp

**[description](#API_CreateBotVersion_ResponseSyntax "#API_CreateBotVersion_ResponseSyntax")**

A description of the bot.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 200.

**[detectSentiment](#API_CreateBotVersion_ResponseSyntax "#API_CreateBotVersion_ResponseSyntax")**

Indicates whether utterances entered by the user should be sent to
Amazon Comprehend for sentiment analysis.

Type: Boolean

**[enableModelImprovements](#API_CreateBotVersion_ResponseSyntax "#API_CreateBotVersion_ResponseSyntax")**

Indicates whether the bot uses accuracy improvements.
`true` indicates that the bot is using the improvements,
otherwise, `false`.

Type: Boolean

**[failureReason](#API_CreateBotVersion_ResponseSyntax "#API_CreateBotVersion_ResponseSyntax")**

If `status` is `FAILED`, Amazon Lex provides the
reason that it failed to build the bot.

Type: String

**[idleSessionTTLInSeconds](#API_CreateBotVersion_ResponseSyntax "#API_CreateBotVersion_ResponseSyntax")**

The maximum time in seconds that Amazon Lex retains the data gathered in
a conversation. For more information, see [PutBot](API_PutBot.md "API_PutBot.md").

Type: Integer

Valid Range: Minimum value of 60. Maximum value of 86400.

**[intents](#API_CreateBotVersion_ResponseSyntax "#API_CreateBotVersion_ResponseSyntax")**

An array of `Intent` objects. For more information, see
[PutBot](API_PutBot.md "API_PutBot.md").

Type: Array of [Intent](API_Intent.md "API_Intent.md") objects

**[lastUpdatedDate](#API_CreateBotVersion_ResponseSyntax "#API_CreateBotVersion_ResponseSyntax")**

The date when the `$LATEST` version of this bot was
updated.

Type: Timestamp

**[locale](#API_CreateBotVersion_ResponseSyntax "#API_CreateBotVersion_ResponseSyntax")**

Specifies the target locale for the bot.

Type: String

Valid Values: `de-DE | en-AU | en-GB | en-IN | en-US | es-419 | es-ES | es-US | fr-FR | fr-CA | it-IT | ja-JP | ko-KR`

**[name](#API_CreateBotVersion_ResponseSyntax "#API_CreateBotVersion_ResponseSyntax")**

The name of the bot.

Type: String

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

**[status](#API_CreateBotVersion_ResponseSyntax "#API_CreateBotVersion_ResponseSyntax")**

When you send a request to create or update a bot, Amazon Lex sets the
`status` response element to `BUILDING`. After
Amazon Lex builds the bot, it sets `status` to `READY`.
If Amazon Lex can't build the bot, it sets `status` to
`FAILED`. Amazon Lex returns the reason for the failure in the
`failureReason` response element.

Type: String

Valid Values: `BUILDING | READY | READY_BASIC_TESTING | FAILED | NOT_BUILT`

**[version](#API_CreateBotVersion_ResponseSyntax "#API_CreateBotVersion_ResponseSyntax")**

The version of the bot.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

**[voiceId](#API_CreateBotVersion_ResponseSyntax "#API_CreateBotVersion_ResponseSyntax")**

The Amazon Polly voice ID that Amazon Lex uses for voice interactions
with the user.

Type: String

## Errors

**BadRequestException**

The request is not well formed. For example, a value is invalid or
a required field is missing. Check the field values, and try
again.

HTTP Status Code: 400

**ConflictException**

There was a conflict processing the request. Try your request
again.

HTTP Status Code: 409

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

**PreconditionFailedException**

The checksum of the resource that you are trying to change does
not match the checksum in the request. Check the resource's checksum and
try again.

HTTP Status Code: 412

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/CreateBotVersion.md "../../../goto/cli2/lex-models-2017-04-19/CreateBotVersion.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lex-models-2017-04-19/CreateBotVersion.md "../../../goto/DotNetSDKV4/lex-models-2017-04-19/CreateBotVersion.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/CreateBotVersion.md "../../../goto/SdkForCpp/lex-models-2017-04-19/CreateBotVersion.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/CreateBotVersion.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/CreateBotVersion.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/CreateBotVersion.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/CreateBotVersion.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/CreateBotVersion.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/CreateBotVersion.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/CreateBotVersion.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/CreateBotVersion.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/CreateBotVersion.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/CreateBotVersion.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/CreateBotVersion.md "../../../goto/boto3/lex-models-2017-04-19/CreateBotVersion.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/CreateBotVersion.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/CreateBotVersion.md")
