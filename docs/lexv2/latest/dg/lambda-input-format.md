# AWS Lambda input event format for Lex V2

The first step in integrating a Lambda function into your Amazon Lex V2 bot is to understand the fields in the Amazon Lex V2 event and to determine the information from these fields that you want to use when writing your script. The following JSON object shows the general format of an Amazon Lex V2 event passed to a Lambda function:

###### Note

The input format may change without a corresponding change to the `messageVersion`. Your code shouldn't throw an error if new fields are present.

```
{
    "messageVersion": "1.0",
    "invocationSource": "DialogCodeHook | FulfillmentCodeHook",
    "inputMode": "DTMF | Speech | Text",
    "responseContentType": "audio/mpeg | audio/ogg | audio/pcm | text/plain; charset=utf-8",
    "sessionId": `string`,
    "inputTranscript": `string`,
    "invocationLabel": `string`,
    "bot": {
        "id": `string`,
        "name": `string`,
        "localeId": `string`,
        "version": `string`,
        "aliasId": `string`,
        "aliasName": `string`
    },
    "interpretations": [
        {
            "interpretationSource": "Bedrock | Lex",
            "intent": {
                // see Intent for details about the structure
            },
            "nluConfidence": `number`,
            "sentimentResponse": {
                "sentiment": "MIXED | NEGATIVE | NEUTRAL | POSITIVE",
                "sentimentScore": {
                    "mixed": `number`,
                    "negative": `number`,
                    "neutral": `number`,
                    "positive": `number`
                }
            }
        },
        ...
    ],
    "proposedNextState": {
        "dialogAction": {
            "slotToElicit": `string`,
            "type": "Close | ConfirmIntent | Delegate | ElicitIntent | ElicitSlot"
        },
        "intent": {
            // see Intent for details about the structure
        },
        "prompt": {
            "attempt": `string`
        }
    },
    "requestAttributes": {
        `string`: `string`,
        ...
    },
    "sessionState": {
        // see Session state for details about the structure
    },
    "transcriptions": [
        {
            "transcription": `string`,
            "transcriptionConfidence": `number`,
            "resolvedContext": {
                "intent": `string`
            },
            "resolvedSlots": {
                `slot name`: {
                    // see Slots for details about the structure
                },
                ...
            }
        },
        ...
    ]
}
```

Each field in the input event is described below:

The version of the message that identifies the format of the event data going into the Lambda function and the expected format of the response from a Lambda function.

###### Note

You configure this value when you define an intent. In the current implementation, Amazon Lex V2 only supports message version 1.0. Therefore, the console assumes the default value of 1.0 and doesn't show the message version.

The code hook that called the Lambda function. The following values are possible:

`DialogCodeHook` – Amazon Lex V2 called the Lambda function after input from the user.

`FulfillmentCodeHook` – Amazon Lex V2 called the Lambda function after filling all the required slots and the intent is ready for fulfillment.

The mode of the user utterance. The possible values are as follows:

`DTMF` – The user input the utterance using a touch-tone keypad (Dual Tone Multi-Frequency).

`Speech` – The user spoke the utterance.

`Text` – The user typed the utterance.

The mode of the bot's response to the user. `text/plain; charset=utf-8` indicates that the last utterance was written, while a value beginning with `audio` indicates that the last utterance was spoken.

The alphanumeric session identifier used for the conversation.

A transcription of the input from the user.

- For text input, this is the text that the user typed. For DTMF input, this is the key that the user input.
- For speech input, this is the text to which Amazon Lex V2 converts the user utterance in order to invoke an intent or fill a slot.
  A value that indicates the response that invoked the Lambda function. You can set invocation labels for the initial response, slots, and confirmation response.

Information about the bot that processed the request, consisting of the following fields:

- **id** – The identifier assigned to the bot when you created it. You can see the bot ID in the Amazon Lex V2 console on the bot **Settings** page.
- **name** – The name that you gave the bot when you created it.
- **localeId** – The identifier of the locale that you used for your bot. For a list of locales, see [Languages and locales supported by
  Amazon Lex V2](how-languages.md "how-languages.md").
- **version** – The version of the bot that processed the request.
- **aliasId** – The identifier assigned to the bot alias when you created it. You can see the bot alias ID in the Amazon Lex V2 console on the **Aliases** page. If you can't see the alias ID in the list, choose the gear icon on the upper right and turn on **Alias ID**.
- **aliasName** – The name that you gave the bot alias.
  A list of information about intents that Amazon Lex V2 considers possible matches to the user's utterance. Each item is a structure that provides information about the utterance's match to an intent, with the following format:

```
{
    "intent": {
        // see Intent for details about the structure
    },
    "interpretationSource": "Bedrock | Lex",
    "nluConfidence": `number`,
    "sentimentResponse": {
        "sentiment": "MIXED | NEGATIVE | NEUTRAL | POSITIVE",
        "sentimentScore": {
            "mixed": `number`,
            "negative": `number`,
            "neutral": `number`,
            "positive": `number`
        }
    }
}
```

The fields within the structure are as follows:

- **intent** – A structure containing information about the intent. See [Intent](lambda-common-structures.md#lambda-intent "lambda-common-structures.md#lambda-intent") for details about the structure.
- **nluConfidence** – A score that indicates how confident Amazon Lex V2 is that the intent matches the user's intent.
- **sentimentResponse** – An analysis of the sentiment of the response, containing the following fields:
  - **sentiment** – Indicates whether the sentiment of the utterance is `POSITIVE`, `NEGATIVE`, `NEUTRAL`, or `MIXED`.
  - **sentimentScore** – A structure mapping each sentiment to a number indicating how confident Amazon Lex V2 is that the utterance conveys that sentiment.

- **interpretationSource** – Indicates whether a slot is resolved by Amazon Lex V2 or Amazon Bedrock.
  If the Lambda function sets the `dialogAction` of the `sessionState` to `Delegate`, this field appears and shows Amazon Lex V2's proposal for the next step in the conversation. Otherwise, the next state depends on the settings that you return in the response from your Lambda function. This structure is only present if both of the following statements are true:

1. The `invocationSource` value is `DialogCodeHook`
2. The predicted `type` of `dialogAction` is `ElicitSlot`.
   You can use this information to add `runtimeHints` at the right point in the conversation. See [Improving recognition of slot values with runtime hints in the conversation](using-hints.md "using-hints.md") for more information. `proposedNextState` is a structure containing the following fields:

The structure of `proposedNextState` is as follows:

```
"proposedNextState": {
    "dialogAction": {
        "slotToElicit": `string`,
        "type": "Close | ConfirmIntent | Delegate | ElicitIntent | ElicitSlot"
    },
    "intent": {
        // see Intent for details about the structure
    },
    "prompt": {
        "attempt": `string`
    }
}
```

- **dialogAction** – Contains information about the next step that Amazon Lex V2 proposes. The fields in the structure are as follows:
  - **slotToElicit** – The slot to elicit next as proposed by Amazon Lex V2. This field only appears if the `type` is `ElicitSlot`.
  - **type** – The next step in the conversation as proposed by Amazon Lex V2. The following values are possible:

  `Delegate` – Amazon Lex V2 determines the next action.

  `ElicitIntent` – The next action is to elicit an intent from the user.

  `ElicitSlot` – The next action is to elicit a slot value from the user.

  `Close` – Ends the intent fulfillment process and indicates that there will not be a response from the user.

  `ConfirmIntent` – The next action is to ask the user if the slots are correct and the intent is ready for fulfillment.

- **intent** – The intent that the bot has determined that the user is trying to fulfill. See [Intent](lambda-common-structures.md#lambda-intent "lambda-common-structures.md#lambda-intent") for details about the structure.
- **prompt**
  – A structure containing the field `attempt`, which maps to a value that specifies how many times Amazon Lex V2 has prompted the user for the next slot. The possible values are `Initial` for the first attempt and `Retry1`, `Retry2`, `Retry3`, `Retry4`, and `Retry5` for subsequent attempts.
  A structure containing request-specific attributes that the client sends in the request. Use request attributes to pass information that doesn't need to persist for the entire session. If there are no request attributes, the value will be null. For more information, see [Setting request
  attributes for your Lex V2 bot](context-mgmt-request-attribs.md "context-mgmt-request-attribs.md").

The current state of the conversation between the user and your Amazon Lex V2 bot. See [Session state](lambda-common-structures.md#lambda-session-state "lambda-common-structures.md#lambda-session-state") for details about the structure.

A list of transcriptions that Amazon Lex V2 considers possible matches to the user's utterance. For more information, see [Using voice transcription confidence scores to improve conversations with your Lex V2 bot](using-transcript-confidence-scores.md "using-transcript-confidence-scores.md"). Each item is an object with the following format, containing information about one possible transcription:

```
{
    "transcription": `string`,
    "transcriptionConfidence": `number`,
    "resolvedContext": {
        "intent": `string`
    },
    "resolvedSlots": {
        `slot name`: {
            // see Slots for details about the structure
        },
        ...
    }
}
```

The fields are described below:

- **transcription** – A transcription that Amazon Lex V2 considers a possible match to the user's audio utterance.
- **transcriptionConfidence** – A score that indicates how confident Amazon Lex V2 is that the intent matches the user's intent.
- **resolvedContext** – A structure containing the field `intent`, which maps to the intent to which the utterance pertains.
- **resolvedSlots** – A structure whose keys are the names of each slot that is resolved by the utterance. Each slot name maps to a structure containing information about that slot. See [Slots](lambda-common-structures.md#lambda-slot "lambda-common-structures.md#lambda-slot") for details about the structure.
