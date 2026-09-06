

# Override system behavior
<a name="testing-language-actions-override-system-behavior"></a>

Modifies how specific flow actions behave during test execution. This allows you to mock external dependencies, substitute resources, or simulate specific scenarios without modifying the actual flow.

## InvokeLambdaFunction
<a name="testing-language-actions-override-lambda"></a>

Override Lambda function behavior by substituting with a different function or mocking the response.

### Substitute resource strategy
<a name="testing-language-actions-override-lambda-substitute"></a>

Redirects Lambda invocations to a different function ARN.

#### Parameters
<a name="testing-language-actions-override-lambda-substitute-parameters"></a>
+ Identifier: Unique identifier for the action
+ Type: Must be `OverrideSystemBehavior`
+ Parameters:
  + ActionType: Must be `OverrideSystemBehavior`
  + Behavior: Object defining the behavior to override
    + Type: Must be `FlowAction`
    + Properties:
      + ActionType: Must be `InvokeLambdaFunction`
      + ActionParameters:
        + LambdaFunctionARN: The ARN of the Lambda function to override
      + Strategy: Object defining the override strategy
        + Type: Must be `SubstituteResource`
        + SubstituteArn: ARN of the replacement Lambda function to use
+ Transitions:
  + NextAction: The unique identifier for the next action

```
{
    "Identifier": "ActionId",
    "Type": "OverrideSystemBehavior",
    "Parameters": {
        "ActionType": "OverrideSystemBehavior",
        "Behavior": {
            "Type": "FlowAction",
            "Properties": {
                "ActionType" : "InvokeLambdaFunction",
                "ActionParameters": { 
                    "LambdaFunctionARN" : "string"
                },
                "Strategy": { 
                    "Type": "SubstituteResource",
                    "SubstituteArn": "string"
                }
            }
        }
    },
    "Transitions": { "NextAction": "string" }
}
```

#### Mock response strategy - Success
<a name="testing-language-actions-override-lambda-mock-success"></a>

```
{
    "Identifier": "ActionId",
    "Type": "OverrideSystemBehavior",
    "Parameters": {
        "ActionType": "OverrideSystemBehavior",
        "Behavior": {
            "Type": "FlowAction",
            "Properties": {
                "ActionType" : "InvokeLambdaFunction",
                "ActionParameters": { 
                    "LambdaFunctionARN" : "string"
         
                },
                "Strategy": { 
                    "Type": "MockResponse",
                    "Response": {
                        "Type" : "ExecutionResult", 
                        "ExecutionResult" : {
                            "DelaySeconds" : Number,
                            "LoadedData" : "serialized JSON"
                        }
                    }
                }
            }
        }
    },
    "Transitions": { "NextAction": "string" }
}
```

#### Mock response strategy - Error
<a name="testing-language-actions-override-lambda-mock-error"></a>

Simulates a Lambda function error without actual invocation.

```
{
    "Identifier": "ActionId",
    "Type": "OverrideSystemBehavior",
    "Parameters": {
        "ActionType": "OverrideSystemBehavior",
        "Behavior": {
            "Type": "FlowAction",
            "Properties": {
                "ActionType" : "InvokeLambdaFunction",
                "ActionParameters": { 
                    "LambdaFunctionARN" : "lambda-arn-to-mock"
                },
                "Strategy": { 
                    "Type": "MockResponse",
                    "Response": {
                        "Type" : "Error", 
                        "Error" : {
                            "DelaySeconds" :  Number,
                            "Value" : "TimeLimitExceeded|NoMatchingError"
                        }
                    }
                }
            }
        }
    },
    "Transitions": { "NextAction": "string" }
}
```

## CheckHoursOfOperation
<a name="testing-language-actions-override-hours"></a>

Override hours of operation checks to test different time-based scenarios.

### Substitute resource strategy
<a name="testing-language-actions-override-hours-substitute"></a>

Redirects hours of operation checks to a different hours of operation configuration.

#### Parameters
<a name="testing-language-actions-override-hours-substitute-parameters"></a>
+ Identifier - Unique identifier for the action
+ Type - Must be `OverrideSystemBehavior`
+ Parameters:
  + ActionType: Must be `OverrideSystemBehavior`
  + Behavior: Object defining the behavior to override
    + Type: Must be `FlowAction`
    + Properties
      + ActionType: Must be `CheckHoursOfOperation`
      + ActionParameters:
        + HoursOfOperationId: The ID/ARN of the hours of operation to override
      + Strategy:
        + Type: Must be `SubstituteResource`
        + SubstituteArn: ARN of the replacement hours of operation resource
+ Transitions:
  + NextAction: The unique identifier for the next action

```
{
    "Identifier": "ActionId",
    "Type": "OverrideSystemBehavior",
    "Parameters": {
        "ActionType": "OverrideSystemBehavior",
        "Behavior": {
            "Type": "FlowAction",
            "Properties": {
                "ActionType" : "CheckHoursOfOperation",
                "ActionParameters": { 
                    "HoursOfOperationId" : "string"
                },
                "Strategy": { 
                    "Type": "SubstituteResource",
                    "SubstituteArn": "string"
                }
            }
        }
    },
    "Transitions": { "NextAction": "string" }
}
```

#### Mock response strategy - Success
<a name="testing-language-actions-override-hours-mock-success"></a>

Returns a predefined hours of operation check result.

```
{
    "Identifier": "ActionId",
    "Type": "OverrideSystemBehavior",
    "Parameters": {
        "ActionType": "OverrideSystemBehavior",
        "Behavior": {
            "Type": "FlowAction",
            "Properties": {
                "ActionType": "CheckHoursOfOperation",
                "ActionParameters": {
                    "HoursOfOperationId": "string"
                },
                "Strategy": {
                    "Type": "MockResponse",
                    "Response": {
                        "Type": "ExecutionResult",
                        "ExecutionResult": {
                            "Value": "InHours|OutOfHours"
                        }
                    }
                }
            }
        }
    },
    "Transitions": {
        "NextAction": "string"
    }
}
```

#### Mock response strategy - Error
<a name="testing-language-actions-override-hours-mock-error"></a>

Simulates an error during hours of operation check.

```
{
    "Identifier": "ActionId",
    "Type": "OverrideSystemBehavior",
    "Parameters": {
        "ActionType": "OverrideSystemBehavior",
        "Behavior": {
            "Type": "FlowAction",
            "Properties": {
                "ActionType": "CheckHoursOfOperation",
                "ActionParameters": {
                    "HoursOfOperationId": "arn:aws:connect:us-west-2:489887583805:instance/0b6b36d4-add8-4fc2-bb5b-72b8e4042838/operating-hours/90d61ae9-79b5-4940-91e5-3e38f8383958"
                },
                "Strategy": {
                    "Type": "MockResponse",
                    "Response": {
                        "Type": "Error",
                        "Error": {
                            "Value": "NoMatchingError"
                        }
                    }
                }
            }
        }
    },
    "Transitions": {
        "NextAction": "string"
    }
}
```

## ConnectParticipantWithLexBot
<a name="testing-language-actions-override-lex"></a>

Override Lex bot behaviors to use a different bot for testing or mock responses.

### Substitute resource strategy
<a name="testing-language-actions-override-lex-substitute"></a>

#### Parameters
<a name="testing-language-actions-override-lex-substitute-parameters"></a>
+ Identifier - Unique identifier for the action
+ Type - Must be `OverrideSystemBehavior`
+ Parameters
  + ActionType - Must be `OverrideSystemBehavior`
  + Behavior:
    + Type: Must be `FlowAction`
    + Properties:
      + ActionType - Must be `ConnectParticipantWithLexBot`
      + ActionParameters:
        + LexV2Bot: Object containing the bot to override
          + AliasArn: ARN of the Lex bot alias to override
      + Strategy:
        + Type: Must be `SubstituteResource`
        + SubstituteArn: ARN of the replacement Lex bot alias
+ Transitions:
  + NextAction: The unique identifier for the next action

```
{
    "Identifier": "ActionId",
    "Type": "OverrideSystemBehavior",
    "Parameters": {
        "ActionType": "OverrideSystemBehavior",
        "Behavior": {
            "Type": "FlowAction",
            "Properties": {
                "ActionType" : "ConnectParticipantWithLexBot",
                "ActionParameters" : {
                    "LexV2Bot": {
                       "AliasArn": "string"
                    }
                },
                "Strategy": {
                    "Type": "SubstituteResource",
                    "SubstituteArn": "string"
                }
             }
         }
    },
    "Transitions": { "NextAction": "string" }
}
```

#### Mock response strategy - Success
<a name="testing-language-actions-override-lex-mock-success"></a>

Returns a predefined successful response without invoking the actual Lex bot.

```
{
    "Identifier": "ActionId",
    "Type": "OverrideSystemBehavior",
    "Parameters": {
        "ActionType": "OverrideSystemBehavior",
        "Behavior": {
            "Type": "FlowAction",
            "Properties": {
                "ActionType": "ConnectParticipantWithLexBot",
                "ActionParameters": {
                    "LexV2Bot": {
                        "AliasArn": "string"
                    }
                },
                "Strategy": {
                    "Type": "MockResponse",
                    "Response": {
                        "Type": "ExecutionResult",
                        "ExecutionResult": {
                            "DelaySeconds": Number,
                            "LoadedData": "serialized JSON"
                        }
                    }
                }
            }
        }
    },
    "Transitions": { "NextAction": "string" }
}
```

#### Mock response strategy - Error
<a name="testing-language-actions-override-lex-mock-error"></a>

Simulates a Lex bot with error without actual invocation.

```
{
    "Identifier": "ActionId",
    "Type": "OverrideSystemBehavior",
    "Parameters": {
        "ActionType": "OverrideSystemBehavior",
        "Behavior": {
            "Type": "FlowAction",
            "Properties": {
                "ActionType": "ConnectParticipantWithLexBot",
                "ActionParameters": {
                    "LexV2Bot": {"AliasArn": "string"}
                },
                "Strategy": {
                    "Type": "MockResponse",
                    "Response": {
                        "Type": "Error",
                        "Error": {
                            "DelaySeconds": Number,
                            "Value": "TimeLimitExceeded|NoMatchingError"
                        }
                    }
                }
            }
        }
    },
    "Transitions": { "NextAction": "string" }
}
```

## TransferContactToQueue
<a name="testing-language-actions-override-transfer"></a>

Override queue transfer behavior to substitute queues or simulate transfer failures.

### Substitute resource strategy
<a name="testing-language-actions-override-transfer-substitute"></a>

Redirects queue transfers to a different queue.

#### Parameters
<a name="testing-language-actions-override-transfer-substitute-parameters"></a>
+ Identifier - Unique identifier for the action
+ Type - Must be `OverrideSystemBehavior`
+ Parameters
  + ActionType - Must be `OverrideSystemBehavior`
  + Behavior
    + Type: `FlowAction`
    + Properties
      + ActionType - Must be `TransferContactToQueue`
      + ActionParameters:
        + QueueId: ID/ARN of the queue to override
      + Strategy:
        + Type: Must be `SubstituteResource`
        + SubstituteArn: ARN of the replacement queue
+ Transitions:
  + NextAction: The unique identifier for the next action

```
{
    "Identifier": "ActionId",
    "Type": "OverrideSystemBehavior",
    "Parameters": {
        "ActionType": "OverrideSystemBehavior",
        "Behavior": {
            "Type": "FlowAction",
            "Properties": {
                "ActionType" : "TransferContactToQueue",
                "ActionParameters" : {
                    "QueueId": "string"
                },
                "Strategy": {
                    "Type": "SubstituteResource",
                    "SubstituteArn": "string"
                }
             }
         }
    },
    "Transitions": { "NextAction": "string" }
}
```

#### Mock response strategy - Error
<a name="testing-language-actions-override-transfer-mock-error"></a>

Simulates queue transfer failures for testing error paths.

```
{
    "Identifier": "ActionId",
    "Type": "OverrideSystemBehavior",
    "Parameters": {
        "ActionType": "OverrideSystemBehavior",
        "Behavior": {
            "Type": "FlowAction",
            "Properties": {
                "ActionType": "TransferContactToQueue",
                "ActionParameters": {
                    "QueueId": "string"
                },
                "Strategy": {
                    "Type": "MockResponse",
                    "Response": {
                        "Type": "Error",
                        "Error": {
                            "Value": "QueueAtCapacity|NoMatchingError"
                        }
                    }
                }
            }
        }
    },
    "Transitions": {
        "NextAction": "string"
    }
}
```

## DequeueAndTransferToQueue
<a name="testing-language-actions-override-dequeue"></a>

Override behavior when dequeuing a contact and transferring to another queue.

### Substitute resource strategy
<a name="testing-language-actions-override-dequeue-substitute"></a>

#### Parameters
<a name="testing-language-actions-override-dequeue-substitute-parameters"></a>
+ Identifier - Unique identifier for the action
+ Type - Must be `OverrideSystemBehavior`
+ Parameters
  + ActionType - Must be `OverrideSystemBehavior`
  + Behavior:
    + Type: `FlowAction`
    + Properties:
      + ActionType - Must be `DequeueAndTransferToQueue`
      + ActionParameters:
        + QueueId: ID/ARN of the queue to override
      + Strategy:
        + Type: Must be `SubstituteResource`
        + SubstituteArn: ARN of the replacement queue
+ Transitions
  + NextAction: The unique identifier for the next action

```
{
    "Identifier": "ActionId",
    "Type": "OverrideSystemBehavior",
    "Parameters": {
        "ActionType": "OverrideSystemBehavior",
        "Behavior": {
            "Type": "FlowAction",
            "Properties": {
                "ActionType" : "DequeueAndTransferToQueue",
                "ActionParameters" : {
                    "QueueId": "string"
                },
                "Strategy": {
                    "Type": "SubstituteResource",
                    "SubstituteArn": "string"
                }
             }
         }
    },
    "Transitions": { "NextAction": "string" }
}
```

#### Mock response strategy - Error
<a name="testing-language-actions-override-dequeue-mock-error"></a>

Simulates dequeue and transfer failures.

```
{
    "Identifier": "ActionId",
    "Type": "OverrideSystemBehavior",
    "Parameters": {
        "ActionType": "OverrideSystemBehavior",
        "Behavior": {
            "Type": "FlowAction",
            "Properties": {
                "ActionType": "DequeueAndTransferToQueue",
                "ActionParameters": {
                    "QueueId": "string"
                },
                "Strategy": {
                    "Type": "MockResponse",
                    "Response": {
                        "Type": "Error",
                        "Error": {
                            "Value": "QueueAtCapacity|NoMatchingError"
                        }
                    }
                }
            }
        }
    },
    "Transitions": {
        "NextAction": "string"
    }
}
```