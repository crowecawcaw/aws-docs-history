End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# GetSession

Returns session information for a specified bot, alias, and user
ID.

## Request Syntax

```
GET /bot/`botName`/alias/`botAlias`/user/`userId`/session/?checkpointLabelFilter=`checkpointLabelFilter` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[botAlias](#API_runtime_GetSession_RequestSyntax "#API_runtime_GetSession_RequestSyntax")**

The alias in use for the bot that contains the session data.

Required: Yes

**[botName](#API_runtime_GetSession_RequestSyntax "#API_runtime_GetSession_RequestSyntax")**

The name of the bot that contains the session data.

Required: Yes

**[checkpointLabelFilter](#API_runtime_GetSession_RequestSyntax "#API_runtime_GetSession_RequestSyntax")**

A string used to filter the intents returned in the
`recentIntentSummaryView` structure.

When you specify a filter, only intents with their
`checkpointLabel` field set to that string are
returned.

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[a-zA-Z0-9-]+`

**[userId](#API_runtime_GetSession_RequestSyntax "#API_runtime_GetSession_RequestSyntax")**

The ID of the client application user. Amazon Lex uses this to identify a
user's conversation with your bot.

Length Constraints: Minimum length of 2. Maximum length of 100.

Pattern: `[0-9a-zA-Z._:-]+`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "activeContexts": [
      {
         "name": "***string***",
         "parameters": {
            "***string***" : "***string***"
         },
         "timeToLive": {
            "timeToLiveInSeconds": ***number***,
            "turnsToLive": ***number***
         }
      }
   ],
   "dialogAction": {
      "fulfillmentState": "***string***",
      "intentName": "***string***",
      "message": "***string***",
      "messageFormat": "***string***",
      "slots": {
         "***string***" : "***string***"
      },
      "slotToElicit": "***string***",
      "type": "***string***"
   },
   "recentIntentSummaryView": [
      {
         "checkpointLabel": "***string***",
         "confirmationStatus": "***string***",
         "dialogActionType": "***string***",
         "fulfillmentState": "***string***",
         "intentName": "***string***",
         "slots": {
            "***string***" : "***string***"
         },
         "slotToElicit": "***string***"
      }
   ],
   "sessionAttributes": {
      "***string***" : "***string***"
   },
   "sessionId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[activeContexts](#API_runtime_GetSession_ResponseSyntax "#API_runtime_GetSession_ResponseSyntax")**

A list of active contexts for the session. A context can be set when
an intent is fulfilled or by calling the `PostContent`,
`PostText`, or `PutSession` operation.

You can use a context to control the intents that can follow up an
intent, or to modify the operation of your application.

Type: Array of [ActiveContext](API_runtime_ActiveContext.md "API_runtime_ActiveContext.md") objects

Array Members: Minimum number of 0 items. Maximum number of 20 items.

**[dialogAction](#API_runtime_GetSession_ResponseSyntax "#API_runtime_GetSession_ResponseSyntax")**

Describes the current state of the bot.

Type: [DialogAction](API_runtime_DialogAction.md "API_runtime_DialogAction.md") object

**[recentIntentSummaryView](#API_runtime_GetSession_ResponseSyntax "#API_runtime_GetSession_ResponseSyntax")**

An array of information about the intents used in the session. The
array can contain a maximum of three summaries. If more than three intents
are used in the session, the `recentIntentSummaryView`
operation contains information about the last three intents used.

If you set the `checkpointLabelFilter` parameter in the
request, the array contains only the intents with the specified
label.

Type: Array of [IntentSummary](API_runtime_IntentSummary.md "API_runtime_IntentSummary.md") objects

Array Members: Minimum number of 0 items. Maximum number of 3 items.

**[sessionAttributes](#API_runtime_GetSession_ResponseSyntax "#API_runtime_GetSession_ResponseSyntax")**

Map of key/value pairs representing the session-specific context
information. It contains application information passed between Amazon Lex and
a client application.

Type: String to string map

**[sessionId](#API_runtime_GetSession_ResponseSyntax "#API_runtime_GetSession_ResponseSyntax")**

A unique identifier for the session.

Type: String

## Errors

**BadRequestException**

Request validation failed, there is no usable message in the context,
or the bot build failed, is still in progress, or contains unbuilt
changes.

HTTP Status Code: 400

**InternalFailureException**

Internal service error. Retry the call.

HTTP Status Code: 500

**LimitExceededException**

Exceeded a limit.

HTTP Status Code: 429

**NotFoundException**

The resource (such as the Amazon Lex bot or an alias) that is referred
to is not found.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/runtime.lex-2016-11-28/GetSession.md "../../../goto/cli2/runtime.lex-2016-11-28/GetSession.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/runtime.lex-2016-11-28/GetSession.md "../../../goto/DotNetSDKV4/runtime.lex-2016-11-28/GetSession.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/runtime.lex-2016-11-28/GetSession.md "../../../goto/SdkForCpp/runtime.lex-2016-11-28/GetSession.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/runtime.lex-2016-11-28/GetSession.md "../../../goto/SdkForGoV2/runtime.lex-2016-11-28/GetSession.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/runtime.lex-2016-11-28/GetSession.md "../../../goto/SdkForJavaV2/runtime.lex-2016-11-28/GetSession.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/runtime.lex-2016-11-28/GetSession.md "../../../goto/SdkForJavaScriptV3/runtime.lex-2016-11-28/GetSession.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/runtime.lex-2016-11-28/GetSession.md "../../../goto/SdkForKotlin/runtime.lex-2016-11-28/GetSession.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/runtime.lex-2016-11-28/GetSession.md "../../../goto/SdkForPHPV3/runtime.lex-2016-11-28/GetSession.md")
- [AWS SDK for Python](../../../goto/boto3/runtime.lex-2016-11-28/GetSession.md "../../../goto/boto3/runtime.lex-2016-11-28/GetSession.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/runtime.lex-2016-11-28/GetSession.md "../../../goto/SdkForRubyV3/runtime.lex-2016-11-28/GetSession.md")
