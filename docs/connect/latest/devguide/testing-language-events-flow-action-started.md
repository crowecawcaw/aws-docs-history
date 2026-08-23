# Flow action started

Observes when a specific flow action begins execution. This allows you to detect when particular flow actions are executed during the simulation.

## Invoke Lambda function

Observes when a Lambda function invocation action starts.

### Parameters

- Identifier - Unique identifier for the event (In preview, API need to specify this identifier in order for the UI to render properly)
- Type - Must always be `FlowActionStarted`.
- Actor - Must always be `System`. This indicates that the event
  originates from the testing system.
- Properties:

  - ActionType - Must always be
    `InvokeLambdaFunction`.
  - ActionParameters:

    - LambdaFunctionARN: The ARN of the Lambda function being invoked

```
{
    "Identifier": "unique identifier",
    "Type": "FlowActionStarted",
    "Actor": "System",
    "Properties": {
        "ActionType": "InvokeLambdaFunction", // V2 JSON action type.
        "ActionParameters": { // V2 JSON action parameters.
            "LambdaFunctionARN": "string"
        }
    }
}
```

## Check hours of operation

Observes when the flow checks hours of operation.

### Parameters

- Identifier - Unique identifier for the event (API need to specify this identifier in order for the UI to render properly)
- Type - Must always be `FlowActionStarted`.
- Actor - Must always be `System`. This indicates that the event
  originates from the testing system.
- Properties:

  - ActionType - Must always be
    `CheckHoursOfOperation`.
  - ActionParameters:

    - HoursOfOperationId: The ID or ARN of the hours of operation resource being checked

```
{
    "Identifier": "unique identifier",
    "Type": "FlowActionStarted",
    "Actor": "System",
    "Properties": {
        "ActionType": "CheckHoursOfOperation", // V2 JSON action type.
        "ActionParameters": { // V2 JSON action parameters.
            "HoursOfOperationId": "string"
        }
    }
}
```

## Transfer contact to queue

Observes when a contact is being transferred to a queue.

### Parameters

- Identifier - Unique identifier for the event (API need to specify this identifier in order for the UI to render properly)
- Type - Must always be `FlowActionStarted`.
- Actor - Must always be `System`. This indicates that the event
  originates from the testing system.
- Properties:

  - ActionType - Must always be
    `TransferContactToQueue`.
  - ActionParameters:

    - QueueId: The ID or ARN of the target queue
    - AgentId (Optional): Specific agent ID if transferring to a particular agent

```
{
    "Identifier": "unique identifier",
    "Type": "FlowActionStarted",
    "Actor": "System",
    "Properties": {
        "ActionType": "TransferContactToQueue", // V2 JSON action type.
        "ActionParameters": { // V2 JSON action parameters.
            "QueueId": "string",
            "AgentId": "string"
        }
    }
}
```

## Connect participant with Lex bot

Observes when a participant is being connected to a Lex bot.

### Parameters

- Identifier - Unique identifier for the event (API need to specify this identifier in order for the UI to render properly)
- Type - Must always be `FlowActionStarted`.
- Actor - Must always be `System`. This indicates that the event
  originates from the testing system.
- Properties:

  - ActionType - Must always be
    `ConnectParticipantWithLexBot`.
  - ActionParameters:

    - LexV2Bot: Object containing bot details

      - AliasArn: The ARN of the Lex V2 bot alias

```
{
    "Identifier": "unique identifier",
    "Type": "FlowActionStarted",
    "Actor": "System",
    "Properties": {
        "ActionType": "ConnectParticipantWithLexBot",
        "ActionParameters": {
            "LexV2Bot": {
                "AliasArn": "string"
            }
        }
    }
}
```
