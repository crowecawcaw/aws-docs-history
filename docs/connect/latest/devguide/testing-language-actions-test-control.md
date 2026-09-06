

# Test Control Actions
<a name="testing-language-actions-test-control"></a>

Special actions that control test execution flow and debugging.

## End Test
<a name="testing-language-actions-test-control-end"></a>

Explicitly terminates the test execution. Use this when you want to end the test at a specific point rather than waiting for natural completion.

### Parameters
<a name="testing-language-actions-test-control-end-parameters"></a>
+ Identifier - Unique identifier for the action
+ Type - Must be `TestControl`
+ Parameters:
  + Action Type: Must be `TestControl`
  + Command: Object defining the control command
    + Type: Must be `EndTest`
+ Transitions
  + NextAction: The unique identifier for the next action

```
{
    "Identifier": "ActionId",
    "Type": "TestControl",
    "Parameters": {
        "ActionType": "TestControl",
        "Command": {
           "Type": "EndTest"
        }
    },
    "Transitions": { "NextAction": "string" }
}
```

## Log Data
<a name="testing-language-actions-test-control-log"></a>

Captures and logs specific attribute values during test execution for debugging and validation purposes. The logged data appears in the test execution results.

### Parameters
<a name="testing-language-actions-test-control-log-parameters"></a>
+ Identifier - Unique identifier for the action
+ Type - Must be `TestControl`
+ Parameters:
  + Action Type: Must be `TestControl`
  + Command: Object defining the control command
    + Type: Must be `LogData`
    + Properties:
      + Expressions: Object containing key-value pairs where:
        + Key: A descriptive label for the logged value
        + Value: JSON path to extract the attributes (e.g., "$.Queue.Name")
+ Transitions
  + NextAction: The unique identifier for the next action

```
{
    "Identifier": "ActionId",
    "Type": "TestControl",
    "Parameters": {
        "ActionType": "TestControl",
        "Command": {
            "Type": "LogData",
            "Properties": {
                "Expressions": {
                    "string":"string", //"myContactId": "$.ContactId"
                ...
                }
            }
        }
    },
    "Transitions": { "NextAction": "string" }
}
```