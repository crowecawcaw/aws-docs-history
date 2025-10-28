End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# PutBot

Creates an Amazon Lex conversational bot or replaces an existing bot.
When you create or update a bot you are only required to specify a name, a
locale, and whether the bot is directed toward children under age 13. You
can use this to add intents later, or to remove intents from an existing
bot. When you create a bot with the minimum information, the bot is
created or updated but Amazon Lex returns the response
`FAILED`. You can build the bot after you add one or more
intents. For more information about Amazon Lex bots, see [Amazon Lex: How It Works](how-it-works.md "how-it-works.md").

If you specify the name of an existing bot, the fields in the
request replace the existing values in the `$LATEST` version of
the bot. Amazon Lex removes any fields that you don't provide values for in the
request, except for the `idleTTLInSeconds` and
`privacySettings` fields, which are set to their default
values. If you don't specify values for required fields, Amazon Lex throws an
exception.

This operation requires permissions for the `lex:PutBot`
action. For more information, see [Identity and Access Management for Amazon Lex](security-iam.md "security-iam.md").

## Request Syntax

```
PUT /bots/`name`/versions/$LATEST HTTP/1.1
Content-type: application/json

{
   "abortStatement": {
      "messages": [
         {
            "content": "`string`",
            "contentType": "`string`",
            "groupNumber": `number`
         }
      ],
      "responseCard": "`string`"
   },
   "checksum": "`string`",
   "childDirected": `boolean`,
   "clarificationPrompt": {
      "maxAttempts": `number`,
      "messages": [
         {
            "content": "`string`",
            "contentType": "`string`",
            "groupNumber": `number`
         }
      ],
      "responseCard": "`string`"
   },
   "createVersion": `boolean`,
   "description": "`string`",
   "detectSentiment": `boolean`,
   "enableModelImprovements": `boolean`,
   "idleSessionTTLInSeconds": `number`,
   "intents": [
      {
         "intentName": "`string`",
         "intentVersion": "`string`"
      }
   ],
   "locale": "`string`",
   "nluIntentConfidenceThreshold": `number`,
   "processBehavior": "`string`",
   "tags": [
      {
         "key": "`string`",
         "value": "`string`"
      }
   ],
   "voiceId": "`string`"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_PutBot_RequestSyntax "#API_PutBot_RequestSyntax")**

The name of the bot. The name is _not_ case
sensitive.

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[abortStatement](#API_PutBot_RequestSyntax "#API_PutBot_RequestSyntax")**

When Amazon Lex can't understand the user's input in context, it tries
to elicit the information a few times. After that, Amazon Lex sends the message
defined in `abortStatement` to the user, and then cancels the
conversation. To set the number of retries, use the
`valueElicitationPrompt` field for the slot type.

For example, in a pizza ordering bot, Amazon Lex might ask a user "What
type of crust would you like?" If the user's response is not one of the
expected responses (for example, "thin crust, "deep dish," etc.), Amazon Lex
tries to elicit a correct response a few more times.

For example, in a pizza ordering application,
`OrderPizza` might be one of the intents. This intent might
require the `CrustType` slot. You specify the
`valueElicitationPrompt` field when you create the
`CrustType` slot.

If you have defined a fallback intent the cancel statement will not be
sent to the user, the fallback intent is used instead. For more
information, see [AMAZON.FallbackIntent](built-in-intent-fallback.md "built-in-intent-fallback.md").

Type: [Statement](API_Statement.md "API_Statement.md") object

Required: No

**[checksum](#API_PutBot_RequestSyntax "#API_PutBot_RequestSyntax")**

Identifies a specific revision of the `$LATEST`
version.

When you create a new bot, leave the `checksum` field
blank. If you specify a checksum you get a
`BadRequestException` exception.

When you want to update a bot, set the `checksum` field
to the checksum of the most recent revision of the `$LATEST`
version. If you don't specify the `checksum` field, or if the
checksum does not match the `$LATEST` version, you get a
`PreconditionFailedException` exception.

Type: String

Required: No

**[childDirected](#API_PutBot_RequestSyntax "#API_PutBot_RequestSyntax")**

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

Required: Yes

**[clarificationPrompt](#API_PutBot_RequestSyntax "#API_PutBot_RequestSyntax")**

When Amazon Lex doesn't understand the user's intent, it uses this
message to get clarification. To specify how many times Amazon Lex should
repeat the clarification prompt, use the `maxAttempts` field.
If Amazon Lex still doesn't understand, it sends the message in the
`abortStatement` field.

When you create a clarification prompt, make sure that it suggests
the correct response from the user. for example, for a bot that orders
pizza and drinks, you might create this clarification prompt: "What would
you like to do? You can say 'Order a pizza' or 'Order a drink.'"

If you have defined a fallback intent, it will be invoked if the
clarification prompt is repeated the number of times defined in the
`maxAttempts` field. For more information, see [AMAZON.FallbackIntent](built-in-intent-fallback.md "built-in-intent-fallback.md").

If you don't define a clarification prompt, at runtime Amazon Lex will
return a 400 Bad Request exception in three cases:

- Follow-up prompt - When the user responds to a follow-up prompt
  but does not provide an intent. For example, in response to a
  follow-up prompt that says "Would you like anything else today?" the
  user says "Yes." Amazon Lex will return a 400 Bad Request exception because
  it does not have a clarification prompt to send to the user to get an
  intent.
- Lambda function - When using a Lambda function, you return an
  `ElicitIntent` dialog type. Since Amazon Lex does not have a
  clarification prompt to get an intent from the user, it returns a 400
  Bad Request exception.
- PutSession operation - When using the `PutSession`
  operation, you send an `ElicitIntent` dialog type. Since
  Amazon Lex does not have a clarification prompt to get an intent from the
  user, it returns a 400 Bad Request exception.

Type: [Prompt](API_Prompt.md "API_Prompt.md") object

Required: No

**[createVersion](#API_PutBot_RequestSyntax "#API_PutBot_RequestSyntax")**

When set to `true` a new numbered version of the bot is
created. This is the same as calling the `CreateBotVersion`
operation. If you don't specify `createVersion`, the default is
`false`.

Type: Boolean

Required: No

**[description](#API_PutBot_RequestSyntax "#API_PutBot_RequestSyntax")**

A description of the bot.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 200.

Required: No

**[detectSentiment](#API_PutBot_RequestSyntax "#API_PutBot_RequestSyntax")**

When set to `true` user utterances are sent to Amazon
Comprehend for sentiment analysis. If you don't specify
`detectSentiment`, the default is `false`.

Type: Boolean

Required: No

**[enableModelImprovements](#API_PutBot_RequestSyntax "#API_PutBot_RequestSyntax")**

Set to `true` to enable access to natural language
understanding improvements.

When you set the `enableModelImprovements` parameter to
`true` you can use the
`nluIntentConfidenceThreshold` parameter to configure
confidence scores. For more information, see [Confidence Scores](confidence-scores.md "confidence-scores.md").

You can only set the `enableModelImprovements` parameter in
certain Regions. If you set the parameter to `true`, your bot
has access to accuracy improvements.

The Regions where you can set the `enableModelImprovements`
parameter to `false` for the en-US locale are:

- US East (N. Virginia) (us-east-1)
- US West (Oregon) (us-west-2)
- Asia Pacific (Sydney) (ap-southeast-2)
- EU (Ireland) (eu-west-1)

In other Regions and locales, the `enableModelImprovements`
parameter is set to `true` by default. In these Regions and
locales setting the parameter to `false` throws a
`ValidationException` exception.

Type: Boolean

Required: No

**[idleSessionTTLInSeconds](#API_PutBot_RequestSyntax "#API_PutBot_RequestSyntax")**

The maximum time in seconds that Amazon Lex retains the data gathered in
a conversation.

A user interaction session remains active for the amount of time
specified. If no conversation occurs during this time, the session expires
and Amazon Lex deletes any data provided before the timeout.

For example, suppose that a user chooses the OrderPizza intent, but
gets sidetracked halfway through placing an order. If the user doesn't
complete the order within the specified time, Amazon Lex discards the slot
information that it gathered, and the user must start over.

If you don't include the `idleSessionTTLInSeconds`
element in a `PutBot` operation request, Amazon Lex uses the default
value. This is also true if the request replaces an existing
bot.

The default is 300 seconds (5 minutes).

Type: Integer

Valid Range: Minimum value of 60. Maximum value of 86400.

Required: No

**[intents](#API_PutBot_RequestSyntax "#API_PutBot_RequestSyntax")**

An array of `Intent` objects. Each intent represents a
command that a user can express. For example, a pizza ordering bot might
support an OrderPizza intent. For more information, see [Amazon Lex: How It Works](how-it-works.md "how-it-works.md").

Type: Array of [Intent](API_Intent.md "API_Intent.md") objects

Required: No

**[locale](#API_PutBot_RequestSyntax "#API_PutBot_RequestSyntax")**

Specifies the target locale for the bot. Any intent used in the
bot must be compatible with the locale of the bot.

The default is `en-US`.

Type: String

Valid Values: `de-DE | en-AU | en-GB | en-IN | en-US | es-419 | es-ES | es-US | fr-FR | fr-CA | it-IT | ja-JP | ko-KR`

Required: Yes

**[nluIntentConfidenceThreshold](#API_PutBot_RequestSyntax "#API_PutBot_RequestSyntax")**

Determines the threshold where Amazon Lex will insert the
`AMAZON.FallbackIntent`,
`AMAZON.KendraSearchIntent`, or both when returning
alternative intents in a [PostContent](API_runtime_PostContent.md "API_runtime_PostContent.md") or
[PostText](API_runtime_PostText.md "API_runtime_PostText.md") response.
`AMAZON.FallbackIntent` and
`AMAZON.KendraSearchIntent` are only inserted if they are
configured for the bot.

You must set the `enableModelImprovements` parameter to
`true` to use confidence scores in the following
regions.

- US East (N. Virginia) (us-east-1)
- US West (Oregon) (us-west-2)
- Asia Pacific (Sydney) (ap-southeast-2)
- EU (Ireland) (eu-west-1)

In other Regions, the `enableModelImprovements` parameter
is set to `true` by default.

For example, suppose a bot is configured with the confidence threshold
of 0.80 and the `AMAZON.FallbackIntent`. Amazon Lex returns three
alternative intents with the following confidence scores: IntentA (0.70),
IntentB (0.60), IntentC (0.50). The response from the
`PostText` operation would be:

- AMAZON.FallbackIntent
- IntentA
- IntentB
- IntentC

Type: Double

Valid Range: Minimum value of 0. Maximum value of 1.

Required: No

**[processBehavior](#API_PutBot_RequestSyntax "#API_PutBot_RequestSyntax")**

If you set the `processBehavior` element to
`BUILD`, Amazon Lex builds the bot so that it can be run. If you
set the element to `SAVE` Amazon Lex saves the bot, but doesn't
build it.

If you don't specify this value, the default value is
`BUILD`.

Type: String

Valid Values: `SAVE | BUILD`

Required: No

**[tags](#API_PutBot_RequestSyntax "#API_PutBot_RequestSyntax")**

A list of tags to add to the bot. You can only add tags when you
create a bot, you can't use the `PutBot` operation to update
the tags on a bot. To update tags, use the `TagResource`
operation.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

**[voiceId](#API_PutBot_RequestSyntax "#API_PutBot_RequestSyntax")**

The Amazon Polly voice ID that you want Amazon Lex to use for voice
interactions with the user. The locale configured for the voice must match
the locale of the bot. For more information, see [Voices
in Amazon Polly](../../../polly/latest/dg/voicelist.md "../../../polly/latest/dg/voicelist.md") in the _Amazon Polly Developer
Guide_.

Type: String

Required: No

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
   "createVersion": ***boolean***,
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
   "tags": [
      {
         "key": "***string***",
         "value": "***string***"
      }
   ],
   "version": "***string***",
   "voiceId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[abortStatement](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

The message that Amazon Lex uses to cancel a conversation. For more
information, see [PutBot](API_PutBot.md "API_PutBot.md").

Type: [Statement](API_Statement.md "API_Statement.md") object

**[checksum](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

Checksum of the bot that you created.

Type: String

**[childDirected](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

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

**[clarificationPrompt](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

The prompts that Amazon Lex uses when it doesn't understand the user's
intent. For more information, see [PutBot](API_PutBot.md "API_PutBot.md").

Type: [Prompt](API_Prompt.md "API_Prompt.md") object

**[createdDate](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

The date that the bot was created.

Type: Timestamp

**[createVersion](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

`True` if a new version of the bot was created. If the
`createVersion` field was not specified in the request, the
`createVersion` field is set to false in the
response.

Type: Boolean

**[description](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

A description of the bot.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 200.

**[detectSentiment](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

`true` if the bot is configured to send user utterances to
Amazon Comprehend for sentiment analysis. If the
`detectSentiment` field was not specified in the request, the
`detectSentiment` field is `false` in the
response.

Type: Boolean

**[enableModelImprovements](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

Indicates whether the bot uses accuracy improvements.
`true` indicates that the bot is using the improvements,
otherwise, `false`.

Type: Boolean

**[failureReason](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

If `status` is `FAILED`, Amazon Lex provides the
reason that it failed to build the bot.

Type: String

**[idleSessionTTLInSeconds](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

The maximum length of time that Amazon Lex retains the data gathered in
a conversation. For more information, see [PutBot](API_PutBot.md "API_PutBot.md").

Type: Integer

Valid Range: Minimum value of 60. Maximum value of 86400.

**[intents](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

An array of `Intent` objects. For more information, see
[PutBot](API_PutBot.md "API_PutBot.md").

Type: Array of [Intent](API_Intent.md "API_Intent.md") objects

**[lastUpdatedDate](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

The date that the bot was updated. When you create a resource, the
creation date and last updated date are the same.

Type: Timestamp

**[locale](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

The target locale for the bot.

Type: String

Valid Values: `de-DE | en-AU | en-GB | en-IN | en-US | es-419 | es-ES | es-US | fr-FR | fr-CA | it-IT | ja-JP | ko-KR`

**[name](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

The name of the bot.

Type: String

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

**[nluIntentConfidenceThreshold](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

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

**[status](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

When you send a request to create a bot with
`processBehavior` set to `BUILD`, Amazon Lex sets the
`status` response element to `BUILDING`.

In the `READY_BASIC_TESTING` state you can test the bot
with user inputs that exactly match the utterances configured for the
bot's intents and values in the slot types.

If Amazon Lex can't build the bot, Amazon Lex sets `status` to
`FAILED`. Amazon Lex returns the reason for the failure in the
`failureReason` response element.

When you set `processBehavior` to `SAVE`,
Amazon Lex sets the status code to `NOT BUILT`.

When the bot is in the `READY` state you can test and
publish the bot.

Type: String

Valid Values: `BUILDING | READY | READY_BASIC_TESTING | FAILED | NOT_BUILT`

**[tags](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

A list of tags associated with the bot.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

**[version](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

The version of the bot. For a new bot, the version is always
`$LATEST`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

**[voiceId](#API_PutBot_ResponseSyntax "#API_PutBot_ResponseSyntax")**

The Amazon Polly voice ID that Amazon Lex uses for voice interaction
with the user. For more information, see [PutBot](API_PutBot.md "API_PutBot.md").

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

**PreconditionFailedException**

The checksum of the resource that you are trying to change does
not match the checksum in the request. Check the resource's checksum and
try again.

HTTP Status Code: 412

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/PutBot.md "../../../goto/cli2/lex-models-2017-04-19/PutBot.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lex-models-2017-04-19/PutBot.md "../../../goto/DotNetSDKV3/lex-models-2017-04-19/PutBot.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/PutBot.md "../../../goto/SdkForCpp/lex-models-2017-04-19/PutBot.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/PutBot.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/PutBot.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/PutBot.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/PutBot.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/PutBot.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/PutBot.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/PutBot.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/PutBot.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/PutBot.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/PutBot.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/PutBot.md "../../../goto/boto3/lex-models-2017-04-19/PutBot.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/PutBot.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/PutBot.md")
