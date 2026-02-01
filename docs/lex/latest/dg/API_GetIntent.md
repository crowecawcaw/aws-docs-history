End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# GetIntent

Returns information about an intent. In addition to the intent
name, you must specify the intent version.

This operation requires permissions to perform the
`lex:GetIntent` action.

## Request Syntax

```
GET /intents/`name`/versions/`version` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_GetIntent_RequestSyntax "#API_GetIntent_RequestSyntax")**

The name of the intent. The name is case sensitive.

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

**[version](#API_GetIntent_RequestSyntax "#API_GetIntent_RequestSyntax")**

The version of the intent.

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "checksum": "***string***",
   "conclusionStatement": {
      "messages": [
         {
            "content": "***string***",
            "contentType": "***string***",
            "groupNumber": ***number***
         }
      ],
      "responseCard": "***string***"
   },
   "confirmationPrompt": {
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
   "dialogCodeHook": {
      "messageVersion": "***string***",
      "uri": "***string***"
   },
   "followUpPrompt": {
      "prompt": {
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
      "rejectionStatement": {
         "messages": [
            {
               "content": "***string***",
               "contentType": "***string***",
               "groupNumber": ***number***
            }
         ],
         "responseCard": "***string***"
      }
   },
   "fulfillmentActivity": {
      "codeHook": {
         "messageVersion": "***string***",
         "uri": "***string***"
      },
      "type": "***string***"
   },
   "inputContexts": [
      {
         "name": "***string***"
      }
   ],
   "kendraConfiguration": {
      "kendraIndex": "***string***",
      "queryFilterString": "***string***",
      "role": "***string***"
   },
   "lastUpdatedDate": ***number***,
   "name": "***string***",
   "outputContexts": [
      {
         "name": "***string***",
         "timeToLiveInSeconds": ***number***,
         "turnsToLive": ***number***
      }
   ],
   "parentIntentSignature": "***string***",
   "rejectionStatement": {
      "messages": [
         {
            "content": "***string***",
            "contentType": "***string***",
            "groupNumber": ***number***
         }
      ],
      "responseCard": "***string***"
   },
   "sampleUtterances": [ "***string***" ],
   "slots": [
      {
         "defaultValueSpec": {
            "defaultValueList": [
               {
                  "defaultValue": "***string***"
               }
            ]
         },
         "description": "***string***",
         "name": "***string***",
         "obfuscationSetting": "***string***",
         "priority": ***number***,
         "responseCard": "***string***",
         "sampleUtterances": [ "***string***" ],
         "slotConstraint": "***string***",
         "slotType": "***string***",
         "slotTypeVersion": "***string***",
         "valueElicitationPrompt": {
            "maxAttempts": ***number***,
            "messages": [
               {
                  "content": "***string***",
                  "contentType": "***string***",
                  "groupNumber": ***number***
               }
            ],
            "responseCard": "***string***"
         }
      }
   ],
   "version": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[checksum](#API_GetIntent_ResponseSyntax "#API_GetIntent_ResponseSyntax")**

Checksum of the intent.

Type: String

**[conclusionStatement](#API_GetIntent_ResponseSyntax "#API_GetIntent_ResponseSyntax")**

After the Lambda function specified in the
`fulfillmentActivity` element fulfills the intent, Amazon Lex
conveys this statement to the user.

Type: [Statement](API_Statement.md "API_Statement.md") object

**[confirmationPrompt](#API_GetIntent_ResponseSyntax "#API_GetIntent_ResponseSyntax")**

If defined in the bot, Amazon Lex uses prompt to confirm the intent
before fulfilling the user's request. For more information, see [PutIntent](API_PutIntent.md "API_PutIntent.md").

Type: [Prompt](API_Prompt.md "API_Prompt.md") object

**[createdDate](#API_GetIntent_ResponseSyntax "#API_GetIntent_ResponseSyntax")**

The date that the intent was created.

Type: Timestamp

**[description](#API_GetIntent_ResponseSyntax "#API_GetIntent_ResponseSyntax")**

A description of the intent.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 200.

**[dialogCodeHook](#API_GetIntent_ResponseSyntax "#API_GetIntent_ResponseSyntax")**

If defined in the bot, Amazon Amazon Lex invokes this Lambda function
for each user input. For more information, see [PutIntent](API_PutIntent.md "API_PutIntent.md").

Type: [CodeHook](API_CodeHook.md "API_CodeHook.md") object

**[followUpPrompt](#API_GetIntent_ResponseSyntax "#API_GetIntent_ResponseSyntax")**

If defined in the bot, Amazon Lex uses this prompt to solicit additional
user activity after the intent is fulfilled. For more information, see
[PutIntent](API_PutIntent.md "API_PutIntent.md").

Type: [FollowUpPrompt](API_FollowUpPrompt.md "API_FollowUpPrompt.md") object

**[fulfillmentActivity](#API_GetIntent_ResponseSyntax "#API_GetIntent_ResponseSyntax")**

Describes how the intent is fulfilled. For more information, see
[PutIntent](API_PutIntent.md "API_PutIntent.md").

Type: [FulfillmentActivity](API_FulfillmentActivity.md "API_FulfillmentActivity.md") object

**[inputContexts](#API_GetIntent_ResponseSyntax "#API_GetIntent_ResponseSyntax")**

An array of `InputContext` objects that lists the contexts
that must be active for Amazon Lex to choose the intent in a conversation with
the user.

Type: Array of [InputContext](API_InputContext.md "API_InputContext.md") objects

Array Members: Minimum number of 0 items. Maximum number of 5 items.

**[kendraConfiguration](#API_GetIntent_ResponseSyntax "#API_GetIntent_ResponseSyntax")**

Configuration information, if any, to connect to an Amazon Kendra
index with the `AMAZON.KendraSearchIntent` intent.

Type: [KendraConfiguration](API_KendraConfiguration.md "API_KendraConfiguration.md") object

**[lastUpdatedDate](#API_GetIntent_ResponseSyntax "#API_GetIntent_ResponseSyntax")**

The date that the intent was updated. When you create a resource,
the creation date and the last updated date are the same.

Type: Timestamp

**[name](#API_GetIntent_ResponseSyntax "#API_GetIntent_ResponseSyntax")**

The name of the intent.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

**[outputContexts](#API_GetIntent_ResponseSyntax "#API_GetIntent_ResponseSyntax")**

An array of `OutputContext` objects that lists the contexts
that the intent activates when the intent is fulfilled.

Type: Array of [OutputContext](API_OutputContext.md "API_OutputContext.md") objects

Array Members: Minimum number of 0 items. Maximum number of 10 items.

**[parentIntentSignature](#API_GetIntent_ResponseSyntax "#API_GetIntent_ResponseSyntax")**

A unique identifier for a built-in intent.

Type: String

**[rejectionStatement](#API_GetIntent_ResponseSyntax "#API_GetIntent_ResponseSyntax")**

If the user answers "no" to the question defined in
`confirmationPrompt`, Amazon Lex responds with this statement to
acknowledge that the intent was canceled.

Type: [Statement](API_Statement.md "API_Statement.md") object

**[sampleUtterances](#API_GetIntent_ResponseSyntax "#API_GetIntent_ResponseSyntax")**

An array of sample utterances configured for the intent.

Type: Array of strings

Array Members: Minimum number of 0 items. Maximum number of 1500 items.

Length Constraints: Minimum length of 1. Maximum length of 200.

**[slots](#API_GetIntent_ResponseSyntax "#API_GetIntent_ResponseSyntax")**

An array of intent slots configured for the intent.

Type: Array of [Slot](API_Slot.md "API_Slot.md") objects

Array Members: Minimum number of 0 items. Maximum number of 100 items.

**[version](#API_GetIntent_ResponseSyntax "#API_GetIntent_ResponseSyntax")**

The version of the intent.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

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

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/GetIntent.md "../../../goto/cli2/lex-models-2017-04-19/GetIntent.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lex-models-2017-04-19/GetIntent.md "../../../goto/DotNetSDKV4/lex-models-2017-04-19/GetIntent.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/GetIntent.md "../../../goto/SdkForCpp/lex-models-2017-04-19/GetIntent.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/GetIntent.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/GetIntent.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetIntent.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetIntent.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetIntent.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetIntent.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/GetIntent.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/GetIntent.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetIntent.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetIntent.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/GetIntent.md "../../../goto/boto3/lex-models-2017-04-19/GetIntent.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetIntent.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetIntent.md")
