# Common structures in an AWS Lambda function for

Within the Lambda response, there are a number of structures that recur. Details about these common structures are provided in this section.

## Intent

```
"intent": {
    "confirmationState": "Confirmed | Denied | None",
    "name": `string`,
    "slots": {
        // see Slots for details about the structure
    },
    "state": "Failed | Fulfilled | FulfillmentInProgress | InProgress | ReadyForFulfillment | Waiting",
    "kendraResponse": {
        // Only present when intent is KendraSearchIntent. For details, see
// https://docs.aws.amazon.com/kendra/latest/dg/API_Query.html#API_Query_ResponseSyntax       }
}

```

The `intent` field is mapped to an object with the following fields:

Indicates whether the user has confirmed the slots for the intent and the intent is ready for fulfillment. The following values are possible:

`Confirmed` – The user confirms that the slot values are correct.

`Denied` – The user indicates that the slot values are incorrect.

`None` – The user has not reached the confirmation stage yet.

The name of the intent.

Information about the slots required to fulfill the intent. See [Slots](#lambda-slot "#lambda-slot") for details about the structure.

Indicates the fulfillment state for the intent. The following values are possible:

`Failed` – The bot failed to fulfill the intent.

`Fulfilled` – The bot has completed fulfillment of the intent.

`FulfillmentInProgress` – The bot is in the middle of fulfilling the intent.

`InProgress` – The bot is in the middle of eliciting the slot values that are necessary to fulfill the intent.

`ReadyForFulfillment` – The bot has elicited all the slot values for the intent and is ready to fulfill the intent.

`Waiting` – The bot is waiting for a response from the user (limited to streaming conversations).

Contains information about the results of the Kendra search query. This field only appears if the intent is a `KendraSearchIntent`. See [the response syntax in the Query API call for Kendra](../../../https:/docs.aws.amazon.com/kendra/latest/dg/API_Query.md#API_Query_ResponseSyntax "../../../https:/docs.aws.amazon.com/kendra/latest/dg/API_Query.md#API_Query_ResponseSyntax") for more information.

## Slots

The `slots` field exists within an `intent` structure and is mapped to a structure whose keys are the names of the slots for that intent. If the slot is not a multi-valued slot (see [Using multiple values in a
slot](multi-valued-slots.md "multi-valued-slots.md") for more details), it is mapped to a structure with the following format. Note that the `shape` is `Scalar`.

```
{
    `slot name`: {
        "shape": "Scalar",
        "value": {
            "originalValue": `string`,
            "interpretedValue": `string`,
            "resolvedValues": [
                `string`,
                ...
            ]
        }
    }
}
```

If the slot is a multi-valued slot, the object to which it is mapped contains another field called `values`, which is mapped to a list of structures, each containing information about a slot that makes up the multi-valued slot. The format of each object in the list matches that of the object to which a regular slot is mapped. Note that the `shape` is `List`, but the `shape` of the component slots under `values` is `Scalar`.

```
{
    `slot name`: {
    "shape": "List",
    "value": {
        "originalValue": `string`,
        "interpretedValue": `string`,
        "resolvedValues": [
            `string`,
            ...
        ]
    },
    "values": [
        {
            "shape": "Scalar",
            "value": {
                "originalValue": `string`,
                "interpretedValue": `string`,
                "resolvedValues": [
                    `string`,
                    ...
                ]
            }
        },
        {
            "shape": "Scalar",
            "value": {
                "originalValue": `string`,
                "interpretedValue": `string`,
                "resolvedValues": [
                    `string`,
                    ...
                ]
            }
        },
        ...
    ]
}
```

The fields in the slot object are described below:

The shape of the slot. This value is `List` if there are multiple values in the slot (see [Using multiple values in a
slot](multi-valued-slots.md "multi-valued-slots.md") for more details) and is `Scalar` otherwise.

An object containing information about the value that the user provided for a slot and 's interpretation, in the following format:

```
{
    "originalValue": `string`,
    "interpretedValue": `string`,
    "resolvedValues": [
        `string`,
        ...
    ]
}
```

The fields are described below:

- **originalValue** – The part of the user's response to the slot elicitation that determines is relevant to the slot value.
- **interpretedValue** – The value that determines for the slot, given the user input.
- **resolvedValues** – A list of values that determines are possible resolutions for the user input.
  A list of objects containing information about the slots that make up the multi-value slot. The format of each object matches that of a normal slot, with the `shape` and `value` fields described above. `values` only appears if the slot consists of multiple values (see [Using multiple values in a
  slot](multi-valued-slots.md "multi-valued-slots.md") for more details). The following JSON object shows two component slots:

```
"values": [
    {
        "shape": "Scalar",
        "value": {
            "originalValue": string,
            "interpretedValue": `string`,
            "resolvedValues": [
                `string`,
                ...
            ]
        }
    },
    {
        "shape": "Scalar",
        "value": {
            "originalValue": string,
            "interpretedValue": `string`,
            "resolvedValues": [
                `string`,
                ...
            ]
        }
    },
    ...
]
```

## Session state

The `sessionState` field is mapped to an object containing information about the state of the conversation with the user. The actual fields that appear in the object depend on the type of dialog action. See [Required fields in the response](lambda-response-format.md#lambda-response-required "lambda-response-format.md#lambda-response-required") for the required fields in a Lambda response. The format of the `sessionState` object is as follows:

```
"sessionState": {
    "activeContexts": [
        {
            "name": `string`,
            "contextAttributes": {
                `string`: `string`
            },
            "timeToLive": {
                "timeToLiveInSeconds": `number`,
                "turnsToLive": `number`
            }
        },
        ...
    ],
    "sessionAttributes": {
        `string`: `string`,
        ...
    },
    "runtimeHints": {
        "slotHints": {
            `intent name`: {
                `slot name`: {
                    "runtimeHintValues": [
                        {
                            "phrase": `string`
                        },
                        ...
                    ]
                },
                ...
            },
            ...
        }
    },
    "dialogAction": {
        "slotElicitationStyle": "Default | SpellByLetter | SpellByWord",
        "slotToElicit": `string`,
        "type": "Close | ConfirmIntent | Delegate | ElicitIntent | ElicitSlot"
    },
    "intent": {
        // see Intent for details about the structure
    },
    "originatingRequestId": `string`
}
```

The fields are described below:

A list of objects containing information about a context that a user is using in a session. Use contexts to facilitate and control intent recognition. For more information about contexts, see [Setting intent
context for your Lex V2 bot](context-mgmt-active-context.md "context-mgmt-active-context.md"). Each object is formatted as follows:

```
{
    "name": `string`,
    "contextAttributes": {
        `string`: `string`
    },
    "timeToLive": {
        "timeToLiveInSeconds": `number`,
        "turnsToLive": `number`
    }
}
```

The fields are described below:

- **name** – The name of the context.
- **contextAttributes** – An object containing the names of attributes for the context and the values that they are mapped to.
- **timeToLive** – An object that specifies how long the context remains active. This object can contain one or both of the following fields:

      + **timeToLiveInSeconds** – The number of seconds that the context remains active.
      + **turnsToLive** – The number of turns that the context remains active.

  A map of key/value pairs representing session-specific context information. For more information, see [Setting session
  attributes for your Lex V2 bot](context-mgmt-session-attribs.md "context-mgmt-session-attribs.md"). The object is formatted as follows:

```
{
    `string`: `string`,
    ...
}
```

Provides hints to the phrases that a customer is likely to use for a slot in order to improve audio recognition. The values that you provide in the hints boost audio recognition of those values over similar-sounding words. The format of the `runtimeHints` object is as follows:

```
{
    "slotHints": {
        `intent name`: {
            `slot name`: {
                "runtimeHintValues": [
                    {
                        "phrase": `string`
                    },
                    ...
                ]
            },
            ...
        },
        ...
    }
}
```

The `slotHints` field maps to an object whose fields are the names of the intents in the bot. Each intent name maps to an object whose fields are the names of the slots for that intent. Each slot name maps to a structure with a single field, `runtimeHintValues`, which is a list of objects. Each object contains a `phrase` field that maps to a hint.

Determines the next action for Amazon Lex V2 to take. The format of the object is as follows:

```
{
    "slotElicitationStyle": "Default | SpellByLetter | SpellByWord",
    "slotToElicit": `string`,
    "type": "Close | ConfirmIntent | Delegate | ElicitIntent | ElicitSlot"
}
```

The fields are described below:

- **slotElicitationStyle** – Determines how Amazon Lex V2 interprets audio input from the user if the `type` of `dialogAction` is `ElicitSlot`. For more information, see [Capturing slot values with spelling styles during the conversation](spelling-styles.md "spelling-styles.md"). The following values are possible:

`Default` – Amazon Lex V2 interprets the audio input in the default manner to fulfill a slot.

`SpellByLetter` – Amazon Lex V2 listens for the user's spelling of the slot value.

`SpellByWord` – Amazon Lex V2 listens for the user's spelling of the slot value using words associated with each letter (for example, "a as in apple").

- **slotToElicit**
  – Defines the slot to elicit from the user if the `type` of `dialogAction` is `ElicitSlot`.
- **type** – Defines the action that the bot should execute. The following values are possible:

`Delegate` – Lets Amazon Lex V2 determine the next step.

`ElicitIntent` – Prompts the customer to express an intent.

`ConfirmIntent` – Confirms the customer's slot values and whether the intent is ready for fulfillment.

`ElicitSlot` – Prompts the customer to provide a slot value for an intent.

`Close` – Ends the intent fulfillment process.
See [Intent](#lambda-intent "#lambda-intent") for the structure of the `intent` field.

A unique identifier for the request. This field is optional for the Lambda response.
