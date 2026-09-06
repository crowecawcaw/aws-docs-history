

# Send Instruction
<a name="testing-language-actions-send-instruction"></a>

Simulates customer input during the test execution. This action allows you to send DTMF tones or voice input as if a customer were interacting with the flow.

## DTMF input
<a name="testing-language-actions-send-instruction-dtmf"></a>

Simulates a customer pressing keys on their phone keypad.

### Parameters
<a name="testing-language-actions-send-instruction-dtmf-parameters"></a>
+ Identifier: Unique identifier for the action
+ Type: Must be `SendInstruction`
+ Parameters:
  + ActionType: Must be `SendInstruction`
  + Actor: `Customer` indicates this simulates customer behavior
  + Instruction: Object defining the instruction type
    + Type: Must be `DtmfInput`
    + Properties:
      + Value: String or number representing the DTMF input (e.g., "1", "\#", "\*")
+ Transitions:
  + NextAction: The unique identifier for the next action

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
<a name="testing-language-actions-send-instruction-text-utterance"></a>

Simulates customer voice or text input. This is used for Lex bot or AI agent interactions.

### Parameters
<a name="testing-language-actions-send-instruction-text-utterance-parameters"></a>
+ Identifier: Unique identifier for the action
+ Type: Must be `SendInstruction`
+ Parameters:
  + ActionType: Must be `SendInstruction`
  + Actor: `Customer` indicates this simulates customer behavior
  + Instruction: Object defining the instruction
    + Type: Must be `Utterance`
    + Properties:
      + Text (Optional): Plain text input to send
      + SSML (Optional): SSML-formatted input to send
      + LanguageCode: Language code for the input (e.g., "en-US")
+ Transitions:
  + NextAction: The unique identifier for the next action

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
<a name="testing-language-actions-send-instruction-disconnect"></a>

Simulates customer ending the call.

### Parameters
<a name="testing-language-actions-send-instruction-disconnect-parameters"></a>
+ Identifier: Unique identifier for the action
+ Type: Must be `SendInstruction`
+ Parameters:
  + ActionType: Must be `SendInstruction`
  + Actor: `Customer` indicates this simulates customer behavior
  + Instruction: Object defining the instruction
    + ActionType: Must be `SendInstruction`
    + Type: Must be `Disconnect`
+ Transitions:
  + NextAction: The unique identifier for the next action

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