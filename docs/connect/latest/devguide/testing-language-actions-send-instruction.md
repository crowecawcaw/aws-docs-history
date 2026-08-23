# Send Instruction

Simulates customer input during the test execution. This action allows you to send DTMF tones or voice input as if a customer were interacting with the flow.

## DTMF input

Simulates a customer pressing keys on their phone keypad.

### Parameters

- Identifier: Unique identifier for the action
- Type: Must be `SendInstruction`
- Parameters:

  - ActionType: Must be `SendInstruction`
  - Actor: `Customer` indicates this simulates customer behavior
  - Instruction: Object defining the instruction type

    - Type: Must be `DtmfInput`
    - Properties:

      - Value: String or number representing the DTMF input (e.g., "1", "#", "\*")

- Transitions:

  - NextAction: The unique identifier for the next action

```
{
    "Identifier": "ActionId",
    "Type": "SendInstruction",
    "Parameters": {
        "ActionType": "SendInstruction",
        "Actor" : "Customer",
        "Instruction": {
            "Type": "DtmfInput",
            "Properties": {
                "Value": "string"
            }
        }
    },
    "Transitions": { "NextAction": "string" }
}
```

## Text and Utterance Input

Simulates customer voice or text input. This is used for Lex bot or AI agent interactions.

### Parameters

- Identifier: Unique identifier for the action
- Type: Must be `SendInstruction`
- Parameters:

  - ActionType: Must be `SendInstruction`
  - Actor: `Customer` indicates this simulates customer behavior
  - Instruction: Object defining the instruction

    - Type: Must be `Utterance`
    - Properties:

      - Text (Optional): Plain text input to send
      - SSML (Optional): SSML-formatted input to send
      - LanguageCode: Language code for the input (e.g., "en-US")

- Transitions:

  - NextAction: The unique identifier for the next action

```
{
    "Identifier": "ActionId",
    "Type": "SendInstruction",
    "Parameters": {
        "ActionType": "SendInstruction",
        "Actor" : "Customer",
        "Instruction": {
            "Type": "Utterance",
            "Properties": {
                "Text":  "string", // An optional string that defines text to send to the participant along with gathering input. May not be specified if PromptId or SSML is also specified. May be specified statically or dynamically.
                "SSML": "string", // An optional string that defines SSML to send to the participant along with gathering input. May not be specified if Text or PromptId is also specified May be specified statically or dynamically.,
                "LanguageCode": "en-US"
            }
        }
    },
    "Transitions": { "NextAction": "string" }
}
```

## Disconnect

Simulates customer ending the call.

### Parameters

- Identifier: Unique identifier for the action
- Type: Must be `SendInstruction`
- Parameters:

  - ActionType: Must be `SendInstruction`
  - Actor: `Customer` indicates this simulates customer behavior
  - Instruction: Object defining the instruction

    - ActionType: Must be `SendInstruction`
    - Type: Must be `Disconnect`

- Transitions:

  - NextAction: The unique identifier for the next action

```
{
    "Identifier": "ActionId",
    "Type": "SendInstruction",
    "Parameters": {
        "ActionType": "SendInstruction",
        "Actor" : "Customer",
        "Instruction": {
            "Type": "Disconnect"
        }
    },
    "Transitions": { "NextAction": "string" }
}
```
