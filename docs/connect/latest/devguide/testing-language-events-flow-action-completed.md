

# Flow action completed
<a name="testing-language-events-flow-action-completed"></a>

Observes when a specific flow action completes successfully. This allows you to detect when particular flow actions successfully complete during the simulation, and to assert against and reference the attributes those actions produced.

## Invoke Lambda function
<a name="testing-language-events-flow-action-completed-invoke-lambda"></a>

Observes when a Lambda function invocation action completes successfully.

### Parameters
<a name="testing-language-events-flow-action-completed-invoke-lambda-parameters"></a>
+ Identifier - Unique identifier for the event. The API must specify this identifier for the UI to render it properly.
+ Type - Must always be `FlowActionCompleted`.
+ Actor - Must always be `System`. This indicates that the event originates from the testing system.
+ Properties:
  + ActionType - Must always be `InvokeLambdaFunction`.
  + ActionParameters:
    + LambdaFunctionARN: The ARN of the Lambda function being invoked.

```
{
    "Identifier": "unique identifier",
    "Type": "FlowActionCompleted",
    "Actor": "System",
    "Properties": {
        "ActionType": "InvokeLambdaFunction",
        "ActionParameters": {
            "LambdaFunctionARN": "string"
        }
    }
}
```

After the observation matches, reference the Lambda function's results under the `External` namespace, for example `$.External.orderStatus`. The flow-language alias `$.LambdaInvocation.ResultData.orderStatus` resolves to the same value.

## Connect participant with Lex bot
<a name="testing-language-events-flow-action-completed-connect-participant-with-lex-bot"></a>

Observes when a Lex bot interaction completes successfully.

### Parameters
<a name="testing-language-events-flow-action-completed-connect-participant-with-lex-bot-parameters"></a>
+ Identifier - Unique identifier for the event. The API must specify this identifier for the UI to render it properly.
+ Type - Must always be `FlowActionCompleted`.
+ Actor - Must always be `System`. This indicates that the event originates from the testing system.
+ Properties:
  + ActionType - Must always be `ConnectParticipantWithLexBot`.
  + ActionParameters:
    + LexV2Bot: Object containing bot details.
      + AliasArn: The ARN of the Lex V2 bot alias.

```
{
    "Identifier": "unique identifier",
    "Type": "FlowActionCompleted",
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

After the observation matches, reference the Lex results under the `Lex` namespace, for example `$.Lex.IntentName`, `$.Lex.Slots.OrderNumber`, or `$.Lex.IntentConfidence.Score`.

## Connect participant with Agentic CX
<a name="testing-language-events-flow-action-completed-connect-participant-with-agentic-cx"></a>

Observes when an Agentic CX interaction completes successfully.

### Parameters
<a name="testing-language-events-flow-action-completed-connect-participant-with-agentic-cx-parameters"></a>
+ Identifier - Unique identifier for the event. The API must specify this identifier for the UI to render it properly.
+ Type - Must always be `FlowActionCompleted`.
+ Actor - Must always be `System`. This indicates that the event originates from the testing system.
+ Properties:
  + ActionType - Must always be `ConnectParticipantWithAgenticCX`.
  + ActionParameters:
    + AgentConfiguration: Object identifying the Agentic CX resource.
      + WorkspaceId: The ID of the Agentic CX workspace.
      + ApplicationId: The ID of the Agentic CX application.
      + Alias: The alias of the Agentic CX application.

```
{
    "Identifier": "unique identifier",
    "Type": "FlowActionCompleted",
    "Actor": "System",
    "Properties": {
        "ActionType": "ConnectParticipantWithAgenticCX",
        "ActionParameters": {
            "AgentConfiguration": {
                "WorkspaceId": "string",
                "ApplicationId": "string",
                "Alias": "string"
            }
        }
    }
}
```

After the observation matches, reference the context variables the interaction produced under `$.AgenticCX.ContextVariables.<key>`, and reference interaction metadata under `$.AgenticCX.metadata.<key>`.