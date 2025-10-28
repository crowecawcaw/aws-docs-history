# AWS Lambda response format for Lex V2

The second step in integrating a Lambda function into your Amazon Lex V2 bot is to understand the fields in the Lambda function response and to determine which parameters you want to manipulate. The following JSON object shows the general format of an Lambda response that is returned to Amazon Lex V2:

```
{
    "sessionState": {
        // see Session state for details about the structure
    },
    "messages": [
        {
            "contentType": "CustomPayload | ImageResponseCard | PlainText | SSML",
            "content": `string`,
            "imageResponseCard": {
                "title": `string`,
                "subtitle": `string`,
                "imageUrl": `string`,
                "buttons": [
                    {
                        "text": `string`,
                        "value": `string`
                    },
                    ...
                ]
            }
        },
        ...
    ],
    "requestAttributes": {
        `string`: `string`,
        ...
    }
}
```

Each field in the response is described below:

The state of the conversation between the user and your Amazon Lex V2 bot that you want to return. See [Session state](lambda-common-structures.md#lambda-session-state "lambda-common-structures.md#lambda-session-state") for details about the structure. This field is always required.

A list of messages that Amazon Lex V2 returns to the customer for the next turn of
the conversation. If the `contentType` you provide is
`PlainText`, `CustomPayload`, or `SSML`,
write the message you want to return to the customer in the `content`
field. If the `contentType` you provide is
`ImageResponseCard`, give the details of the card in the
`imageResponseCard` field. If you don't supply messages, Amazon Lex V2
uses the appropriate message defined when the bot was created.

The `messages` field is required if the `dialogAction.type` is `ElicitIntent` or `ConfirmIntent`.

Each item in the list is a structure in the following format, containing
information about a message to return to the user. Here is an example:

```
{
    "contentType": "CustomPayload | ImageResponseCard | PlainText | SSML",
    "content": `string`,
    "imageResponseCard": {
        "title": `string`,
        "subtitle": `string`,
        "imageUrl": `string`,
        "buttons": [
            {
                "text": `string`,
                "value": `string`
            },
            ...
        ]
    }
}
```

A description for each field is provided below:

- **contentType**
  – The type of message to use.

`CustomPayload` – A response string that you can customize to include data or metadata for your application.

`ImageResponseCard` – An image with buttons that the customer can select. See [ImageResponseCard](../APIReference/API_runtime_ImageResponseCard.md "../APIReference/API_runtime_ImageResponseCard.md") for more information.

`PlainText` – A plain text string.

`SSML` – A string that includes Speech Synthesis Markup Language to customize the audio response.

- **content** – The message to send to the user. Use this field if the message type is `PlainText`, `CustomPayload`, or `SSML`.
- **imageResponseCard** – Contains the definition of the response card to show to the user. Use this field if the message type is `ImageResponseCard`. Maps to a structure containing the following fields:

      + **title** – The title of the response card.
      + **subtitle** – The prompt for the user to choose a button.
      + **imageUrl** – A link to an image for the card.
      + **buttons** – A list of structures containing information about a button. Each structure contains a `text` field with the text to display and a `value` field with the value to send to Amazon Lex V2 if the customer selects that button. You can include up to three buttons.

  A structure containing request-specific attributes for the response to the customer. See [Setting request
  attributes for your Lex V2 bot](context-mgmt-request-attribs.md "context-mgmt-request-attribs.md") for more information. This field is optional.

## Required fields in the response

Minimally, the Lambda response must include a `sessionState` object. Within that, provide a `dialogAction` object
and specify the `type` field. Depending on the `type` of `dialogAction` that you provide, there may
be other required fields for the Lambda response. These requirements are described as follows, alongside minimal working examples:

**Delegate** lets Amazon Lex V2 determine the next step. No other fields are required.

```
{
    "sessionState": {
        "dialogAction": {
            "type": "Delegate"
    }
}
```

**ElicitIntent** prompts the customer to express an intent. You must include at least one message in the `messages` field to prompt elicitation of an intent.

```
{
    "sessionState": {
        "dialogAction": {
            "type": "ElicitIntent"
    },
    "messages": [
        {
            "contentType": PlainText,
            "content": "How can I help you?"
        }
    ]
}
```

**ElicitSlot** prompts the customer to provide a slot value. You must include the name of the slot in the `slotToElicit` field in the `dialogAction` object. You must also include the `name` of the `intent` in the `sessionState` object.

```
{`
    "sessionState": {
        "dialogAction": {
            "slotToElicit": `"OriginCity"`,
            "type": "ElicitSlot"
        },
        "intent": {
            "name": `"BookFlight"`
        }
    }
}
```

**ConfirmIntent** confirms the customer's slot values and whether the intent is ready to be fulfilled. You must include the `name` of the `intent` in the `sessionState` object and the `slots` to be confirmed. You must also include at least one message in the `messages` field to ask the user for confirmation of the slot values. Your message should prompt a "yes" or "no" response. If the user responds "yes", Amazon Lex V2 sets the `confirmationState` of the intent to `Confirmed`. If the user responds "no", Amazon Lex V2 sets the `confirmationState` of the intent to `Denied`.

```
{
    "sessionState": {
        "dialogAction": {
            "type": "ConfirmIntent"
        },
        "intent": {
            "name": `"BookFlight"`,
            "slots": {
                `"DepartureDate"`: {
                    "value": {
                        "originalValue": "tomorrow",
                        "interpretedValue": "2023-05-09",
                        "resolvedValues": [
                            "2023-05-09"
                    ]
                 }
                },
                `"DestinationCity"`: {
                    "value": {
                        "originalValue": "sf",
                        "interpretedValue": "sf",
                        "resolvedValues": [
                            "sf"
                        ]
                    }
                },
                `"OriginCity"`: {
                    "value": {
                        "originalValue": "nyc",
                        "interpretedValue": "nyc",
                        "resolvedValues": [
                            "nyc"
                        ]
                    }
                }
            }
        }
    },
    "messages": [
        {
            "contentType": PlainText,
            "content": "Okay, you want to fly from {OriginCity} to \
            {DestinationCity} on {DepartureDate}. Is that correct?"
        }
    ]
}
```

**Close** ends the fulfillment process of the intent and indicates that no further responses are expected from the user. You must include the `name` and `state` of the `intent` in the `sessionState` object. The compatible intent states are `Failed`, `Fulfilled`, and `InProgress`.

```
"sessionState": {
    "dialogAction": {
        "type": "Close"
    },
    "intent": {
        "name": `"BookFlight"`,
        "state": "Failed | Fulfilled | InProgress"
    }
}
```
