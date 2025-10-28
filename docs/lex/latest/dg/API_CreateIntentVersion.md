End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# CreateIntentVersion

Creates a new version of an intent based on the
`$LATEST` version of the intent. If the `$LATEST`
version of this intent hasn't changed since you last updated it, Amazon Lex
doesn't create a new version. It returns the last version you
created.

###### Note

You can update only the `$LATEST` version of the
intent. You can't update the numbered versions that you create with the
`CreateIntentVersion` operation.

When you create a version of an intent, Amazon Lex sets the version to

1.  Subsequent versions increment by 1. For more information, see [Versioning](versioning-aliases.md#versioning-intro "versioning-aliases.md#versioning-intro").

This operation requires permissions to perform the
`lex:CreateIntentVersion` action.

## Request Syntax

```
POST /intents/`name`/versions HTTP/1.1
Content-type: application/json

{
   "checksum": "`string`"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_CreateIntentVersion_RequestSyntax "#API_CreateIntentVersion_RequestSyntax")**

The name of the intent that you want to create a new version of.
The name is case sensitive.

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[checksum](#API_CreateIntentVersion_RequestSyntax "#API_CreateIntentVersion_RequestSyntax")**

Checksum of the `$LATEST` version of the intent that
should be used to create the new version. If you specify a checksum and
the `$LATEST` version of the intent has a different checksum,
Amazon Lex returns a `PreconditionFailedException` exception and
doesn't publish a new version. If you don't specify a checksum, Amazon Lex
publishes the `$LATEST` version.

Type: String

Required: No

## Response Syntax

```
HTTP/1.1 201
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

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

**[checksum](#API_CreateIntentVersion_ResponseSyntax "#API_CreateIntentVersion_ResponseSyntax")**

Checksum of the intent version created.

Type: String

**[conclusionStatement](#API_CreateIntentVersion_ResponseSyntax "#API_CreateIntentVersion_ResponseSyntax")**

After the Lambda function specified in the
`fulfillmentActivity` field fulfills the intent, Amazon Lex
conveys this statement to the user.

Type: [Statement](API_Statement.md "API_Statement.md") object

**[confirmationPrompt](#API_CreateIntentVersion_ResponseSyntax "#API_CreateIntentVersion_ResponseSyntax")**

If defined, the prompt that Amazon Lex uses to confirm the user's
intent before fulfilling it.

Type: [Prompt](API_Prompt.md "API_Prompt.md") object

**[createdDate](#API_CreateIntentVersion_ResponseSyntax "#API_CreateIntentVersion_ResponseSyntax")**

The date that the intent was created.

Type: Timestamp

**[description](#API_CreateIntentVersion_ResponseSyntax "#API_CreateIntentVersion_ResponseSyntax")**

A description of the intent.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 200.

**[dialogCodeHook](#API_CreateIntentVersion_ResponseSyntax "#API_CreateIntentVersion_ResponseSyntax")**

If defined, Amazon Lex invokes this Lambda function for each user
input.

Type: [CodeHook](API_CodeHook.md "API_CodeHook.md") object

**[followUpPrompt](#API_CreateIntentVersion_ResponseSyntax "#API_CreateIntentVersion_ResponseSyntax")**

If defined, Amazon Lex uses this prompt to solicit additional user
activity after the intent is fulfilled.

Type: [FollowUpPrompt](API_FollowUpPrompt.md "API_FollowUpPrompt.md") object

**[fulfillmentActivity](#API_CreateIntentVersion_ResponseSyntax "#API_CreateIntentVersion_ResponseSyntax")**

Describes how the intent is fulfilled.

Type: [FulfillmentActivity](API_FulfillmentActivity.md "API_FulfillmentActivity.md") object

**[inputContexts](#API_CreateIntentVersion_ResponseSyntax "#API_CreateIntentVersion_ResponseSyntax")**

An array of `InputContext` objects that lists the contexts
that must be active for Amazon Lex to choose the intent in a conversation with
the user.

Type: Array of [InputContext](API_InputContext.md "API_InputContext.md") objects

Array Members: Minimum number of 0 items. Maximum number of 5 items.

**[kendraConfiguration](#API_CreateIntentVersion_ResponseSyntax "#API_CreateIntentVersion_ResponseSyntax")**

Configuration information, if any, for connecting an Amazon Kendra
index with the `AMAZON.KendraSearchIntent` intent.

Type: [KendraConfiguration](API_KendraConfiguration.md "API_KendraConfiguration.md") object

**[lastUpdatedDate](#API_CreateIntentVersion_ResponseSyntax "#API_CreateIntentVersion_ResponseSyntax")**

The date that the intent was updated.

Type: Timestamp

**[name](#API_CreateIntentVersion_ResponseSyntax "#API_CreateIntentVersion_ResponseSyntax")**

The name of the intent.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

**[outputContexts](#API_CreateIntentVersion_ResponseSyntax "#API_CreateIntentVersion_ResponseSyntax")**

An array of `OutputContext` objects that lists the contexts
that the intent activates when the intent is fulfilled.

Type: Array of [OutputContext](API_OutputContext.md "API_OutputContext.md") objects

Array Members: Minimum number of 0 items. Maximum number of 10 items.

**[parentIntentSignature](#API_CreateIntentVersion_ResponseSyntax "#API_CreateIntentVersion_ResponseSyntax")**

A unique identifier for a built-in intent.

Type: String

**[rejectionStatement](#API_CreateIntentVersion_ResponseSyntax "#API_CreateIntentVersion_ResponseSyntax")**

If the user answers "no" to the question defined in
`confirmationPrompt`, Amazon Lex responds with this statement to
acknowledge that the intent was canceled.

Type: [Statement](API_Statement.md "API_Statement.md") object

**[sampleUtterances](#API_CreateIntentVersion_ResponseSyntax "#API_CreateIntentVersion_ResponseSyntax")**

An array of sample utterances configured for the intent.

Type: Array of strings

Array Members: Minimum number of 0 items. Maximum number of 1500 items.

Length Constraints: Minimum length of 1. Maximum length of 200.

**[slots](#API_CreateIntentVersion_ResponseSyntax "#API_CreateIntentVersion_ResponseSyntax")**

An array of slot types that defines the information required to
fulfill the intent.

Type: Array of [Slot](API_Slot.md "API_Slot.md") objects

Array Members: Minimum number of 0 items. Maximum number of 100 items.

**[version](#API_CreateIntentVersion_ResponseSyntax "#API_CreateIntentVersion_ResponseSyntax")**

The version number assigned to the new version of the
intent.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

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

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/CreateIntentVersion.md "../../../goto/cli2/lex-models-2017-04-19/CreateIntentVersion.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lex-models-2017-04-19/CreateIntentVersion.md "../../../goto/DotNetSDKV3/lex-models-2017-04-19/CreateIntentVersion.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/CreateIntentVersion.md "../../../goto/SdkForCpp/lex-models-2017-04-19/CreateIntentVersion.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/CreateIntentVersion.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/CreateIntentVersion.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/CreateIntentVersion.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/CreateIntentVersion.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/CreateIntentVersion.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/CreateIntentVersion.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/CreateIntentVersion.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/CreateIntentVersion.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/CreateIntentVersion.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/CreateIntentVersion.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/CreateIntentVersion.md "../../../goto/boto3/lex-models-2017-04-19/CreateIntentVersion.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/CreateIntentVersion.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/CreateIntentVersion.md")
