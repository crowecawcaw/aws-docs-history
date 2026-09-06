

# ConnectParticipantWithLexBot
<a name="participant-actions-connectparticipantwithlexbot"></a>

Connects the participant with the specified Amazon Lex bot. When the interaction is over, the Intent and Slots of the bot are available to the flow during its run. 

## Action syntax
<a name="connectparticipantwithlexbot-action-syntax"></a>

```
{
      "Parameters": {
        "PromptId": "string",
        "Text": "string",
        "SSML": "string",
        "Media": {
            "Uri": "string",
            "SourceType": "string",
            "MediaType": "string"
        },
        "LexV2Bot": {
          "AliasArn": "string"
        },
        "LexBot": {
            "Name": "string",
            "Region": "string",
            "Alias": "string"
        },
        "LexSessionAttributes": {
          "string": "string"
        },
        "LexInitializationData": {
          "InitialMessage": "string"
        },
        "LexTimeoutSeconds": {
          "Text": "number"
        }
      },
      "Identifier": "string",
      "Type": "ConnectParticipantWithLexBot",
      "Transitions": {
        "NextAction": "string",
        "Errors": [
          {
            "NextAction": "string",
            "ErrorType": "InputTimeLimitExceeded"
          },
          {
            "NextAction": "string",
            "ErrorType": "NoMatchingError"
          },
          {
            "NextAction": "string",
            "ErrorType": "NoMatchingCondition"
          }
        ]
      }
    }
```

## Parameter object
<a name="connectparticipantwithlexbot-parameter"></a>

Provide either LexBot or LexV2Bot object depending on the Amazon Lex version in the following format.

 **PromptId** 

 A prompt ID or prompt ARN to play to the participant along with gathering input. This is an optional property and is not required if Text or SSML is specified. This must be either statically defined or a single valid JSONPath identifier. 

 Type: String 

 Required: No 

 **Text** 

 An optional string that defines text to send to the participant along with gathering input. May not be specified if PromptId or SSML is also specified. May be defined statically or dynamically. 

 Type: String 

 Required: No 

 **SSML** 

 An optional string that defines SSML to send to the participant along with gathering input. May not be specified if Text or PromptId is also specified. May be defined statically or dynamically. 

 Type: String 

 Required: No 

 **Media** 

 An optional object that defines an external media source.
+ **Uri**: Location of the message.
+ **SourceType**: The source from which the message will be fetched. The only supported type is S3.
+ **MediaType**: The type of the message to be played. The only supported type is Audio.

 **LexV2Bot** 

 The details of the LexV2 bot to invoke.
+ **AliasArn**: The alias ARN of the LexV2 bot to invoke. May be specified statically or dynamically.

 Required: Yes 

 **LexSessionAttributes** 

 A map of session attributes to pass to the Amazon LexV2 bot when it is invoked. The keys and values may be static or dynamic. 

 Required: No 

 **LexInitializationData** 

 A mapping that defines the initialization data which will be passed to Lex to prime the bot to improve end-customer experience. Lex initialization experience is only supported for Chat channel today. The Voice channel is not supported.
+ **InitialMessage**: An optional string that defines the initial message parsed to Lex to prime the bot. The value for InitialMessage parameter is always serialized to$.Media.InitialMessage which resolves to the customer's initial chat message.

 Required: No 

**Note**  
 If the initial message attribute is not included as part of the contact, it will result in the Get customer input block taking the error branch in the flow. To have separate flow configurations for different messaging types, such as web chat, SMS, or Apple Messages for Business, you can use the Check contact attributes block prior to using the Get customer input block to verify the initial message is available. 

 **LexTimeoutSeconds** 

 A mapping that defines the length of Lex timer in second, which will timeout inactive customers in a Lex interaction.
+ **Text**: An optional string that defines the Lex timer length for chat.

 Required: No 

## Transitions
<a name="connectparticipantwithlexbot-results"></a>

If the Amazon Lex interaction succeeds, the result is the Intent of the bot. Conditions are supported, but only the Equals operator is supported within these conditions.

## Errors
<a name="connectparticipantwithlexbot-errors"></a>
+ **NoMatchingCondition**: If no specified condition evaluated to True.
+ **NoMatchingError**: If an error occurred and no other error matched.
+ **InputTimeLimitExceeded**: if there is no response before the configured LexTimeoutSeconds.

## Conditions
<a name="connectparticipantwithlexbot-conditions"></a>
+ **NextAction**: A string that contains the Identifier of the Action that should be run after this Action, if no error or condition is preferentially chosen.
+ **Supported Conditions**: Conditions are supported but only the EQUALS operator may be used on conditions. 

## Restrictions
<a name="connectparticipantwithlexbot-restrictions"></a>

This action is supported by all channels.

This action is available only in contact flows, transfer flows, and customer queue flows. It is not available in whisper flows or hold flows.

## Corresponding block in the UI
<a name="connectparticipantwithlexbot-ui"></a>

[Get customer input](https://docs.aws.amazon.com/connect/latest/adminguide/get-customer-input.html) 