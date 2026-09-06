

# CreateTask
<a name="createtask"></a>

Creates a new task to run an assigned flow.

## Parameter object
<a name="createtask-parameter"></a>

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
<a name="createtask-results"></a>

None. No conditions are supported.

## Errors
<a name="createtask-errors"></a>

NoMatchingError - if no other Error matches.

## Restrictions
<a name="createtask-restrictions"></a>

This action is supported on all channels and in all contact flow types.

## Corresponding block in the UI
<a name="createtask-ui"></a>

[Flow block: Create task](https://docs.aws.amazon.com/connect/latest/adminguide/create-task-block.html)