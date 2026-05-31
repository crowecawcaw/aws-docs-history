# CreateTask

Creates a new task to run an assigned flow.

## Parameter object

```
"Parameters":
{
        "ContactFlowId": A flow ID or flow ARN. *Must be fully static or a single valid JSONPath identifier*,
        "Attributes": [Optional] { an Object that holds the attributes to be set.
          "Key": "Value" Both the key and value may be defined statically or dynamically.
        },
        "Name": Name of the task that needs to be created. This is a string.,
        "Description": [Optional] Description of the task that needs to be created. This is a string.,
        "References": [Optional] { an Object that holds the references to be set.
          "Type": "Value" Both the key and value may be defined statically or dynamically.
        },
        "DelaySeconds": [Optional] Time in seconds after which the task should be created. This is used to schedule the task by the agent.
        The integer value between 1 and 518400 (6 days). If ScheduledTime is specified, this parameter may not be specified.
        "ScheduledTime": [Optional] The date and time at which the task should be created. If DelaySeconds is specified, this parameter may not be specified.
        "TaskTemplateId": [Optional] ID of the task template that will be used to create the task. This must be defined statically.
      }
}
```

## Results and conditions

None. No conditions are supported.

## Errors

NoMatchingError - if no other Error matches.

## Restrictions

This action is supported on all channels and in all contact flow types.

## Corresponding block in the UI

[Flow block: Create task](../adminguide/create-task-block.md "../adminguide/create-task-block.md")
