# PutActionInteractions

Records action interaction event data. An _action interaction_ event is an interaction between a user and an _action_.
For example, a user taking an action, such a enrolling in a membership program or downloading your app.

For more information about recording action interactions, see [Recording action interaction events](recording-action-interaction-events.md "recording-action-interaction-events.md").
For more information about actions in an Actions dataset, see [Actions dataset](actions-datasets.md "actions-datasets.md").

## Request Syntax

```
POST /action-interactions HTTP/1.1
Content-type: application/json

{
   "actionInteractions": [
      {
         "actionId": "`string`",
         "eventId": "`string`",
         "eventType": "`string`",
         "impression": [ "`string`" ],
         "properties": "`string`",
         "recommendationId": "`string`",
         "sessionId": "`string`",
         "timestamp": `number`,
         "userId": "`string`"
      }
   ],
   "trackingId": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[actionInteractions](#API_UBS_PutActionInteractions_RequestSyntax "#API_UBS_PutActionInteractions_RequestSyntax")**

A list of action interaction events from the session.

Type: Array of [ActionInteraction](API_UBS_ActionInteraction.md "API_UBS_ActionInteraction.md") objects

Array Members: Minimum number of 1 item. Maximum number of 10 items.

Required: Yes

**[trackingId](#API_UBS_PutActionInteractions_RequestSyntax "#API_UBS_PutActionInteractions_RequestSyntax")**

The ID of your action interaction event tracker. When you create an Action interactions dataset, Amazon Personalize creates an
action interaction event tracker for you. For more information, see [Action interaction event tracker ID](action-interaction-tracker-id.md "action-interaction-tracker-id.md").

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: Yes

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 409

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-events-2018-03-22/PutActionInteractions.md "../../../goto/cli2/personalize-events-2018-03-22/PutActionInteractions.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-events-2018-03-22/PutActionInteractions.md "../../../goto/DotNetSDKV4/personalize-events-2018-03-22/PutActionInteractions.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-events-2018-03-22/PutActionInteractions.md "../../../goto/SdkForCpp/personalize-events-2018-03-22/PutActionInteractions.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-events-2018-03-22/PutActionInteractions.md "../../../goto/SdkForGoV2/personalize-events-2018-03-22/PutActionInteractions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-events-2018-03-22/PutActionInteractions.md "../../../goto/SdkForJavaV2/personalize-events-2018-03-22/PutActionInteractions.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-events-2018-03-22/PutActionInteractions.md "../../../goto/SdkForJavaScriptV3/personalize-events-2018-03-22/PutActionInteractions.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-events-2018-03-22/PutActionInteractions.md "../../../goto/SdkForKotlin/personalize-events-2018-03-22/PutActionInteractions.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-events-2018-03-22/PutActionInteractions.md "../../../goto/SdkForPHPV3/personalize-events-2018-03-22/PutActionInteractions.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-events-2018-03-22/PutActionInteractions.md "../../../goto/boto3/personalize-events-2018-03-22/PutActionInteractions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-events-2018-03-22/PutActionInteractions.md "../../../goto/SdkForRubyV3/personalize-events-2018-03-22/PutActionInteractions.md")
