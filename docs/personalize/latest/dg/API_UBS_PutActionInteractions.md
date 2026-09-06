

# PutActionInteractions
<a name="API_UBS_PutActionInteractions"></a>

Records action interaction event data. An *action interaction* event is an interaction between a user and an *action*. For example, a user taking an action, such a enrolling in a membership program or downloading your app.

 For more information about recording action interactions, see [Recording action interaction events](https://docs.aws.amazon.com/personalize/latest/dg/recording-action-interaction-events.html). For more information about actions in an Actions dataset, see [Actions dataset](https://docs.aws.amazon.com/personalize/latest/dg/actions-datasets.html).

## Request Syntax
<a name="API_UBS_PutActionInteractions_RequestSyntax"></a>

```
POST /action-interactions HTTP/1.1
Content-type: application/json

{
   "actionInteractions": [ 
      { 
         "actionId": "{{string}}",
         "eventId": "{{string}}",
         "eventType": "{{string}}",
         "impression": [ "{{string}}" ],
         "properties": "{{string}}",
         "recommendationId": "{{string}}",
         "sessionId": "{{string}}",
         "timestamp": {{number}},
         "userId": "{{string}}"
      }
   ],
   "trackingId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UBS_PutActionInteractions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UBS_PutActionInteractions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actionInteractions](#API_UBS_PutActionInteractions_RequestSyntax) **   <a name="personalize-UBS_PutActionInteractions-request-actionInteractions"></a>
A list of action interaction events from the session.  
Type: Array of [ActionInteraction](API_UBS_ActionInteraction.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: Yes

 ** [trackingId](#API_UBS_PutActionInteractions_RequestSyntax) **   <a name="personalize-UBS_PutActionInteractions-request-trackingId"></a>
The ID of your action interaction event tracker. When you create an Action interactions dataset, Amazon Personalize creates an action interaction event tracker for you. For more information, see [Action interaction event tracker ID](https://docs.aws.amazon.com/personalize/latest/dg/action-interaction-tracker-id.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

## Response Syntax
<a name="API_UBS_PutActionInteractions_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UBS_PutActionInteractions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UBS_PutActionInteractions_Errors"></a>

 ** InvalidInputException **   
Provide a valid value for the field or parameter.  
HTTP Status Code: 400

 ** ResourceInUseException **   
The specified resource is in use.  
HTTP Status Code: 409

 ** ResourceNotFoundException **   
Could not find the specified resource.  
HTTP Status Code: 404

## See Also
<a name="API_UBS_PutActionInteractions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/personalize-events-2018-03-22/PutActionInteractions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/personalize-events-2018-03-22/PutActionInteractions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-events-2018-03-22/PutActionInteractions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/personalize-events-2018-03-22/PutActionInteractions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-events-2018-03-22/PutActionInteractions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/personalize-events-2018-03-22/PutActionInteractions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/personalize-events-2018-03-22/PutActionInteractions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/personalize-events-2018-03-22/PutActionInteractions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/personalize-events-2018-03-22/PutActionInteractions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-events-2018-03-22/PutActionInteractions) 