# ShowView

Initiates a UI-based workflow that can be surfaced to users of front end applications.
This action can be used to create [step-by-step
guides](../adminguide/step-by-step-guided-experiences.md "../adminguide/step-by-step-guided-experiences.md") for agents who are using the Connect Customer agent
workspace.

## Parameter object

```

{
    "ViewResource": {
        "Id": "`Id of the View Resource that will be shown in the UI.`",
        "Version": "`Version of the View Resource that will be shown in the UI.`"
    },
    "InvocationTimeLimitSeconds": 400,
    "ViewData": {
        "Description": "`An optional map of data that will be passed to the View Resource. Keys and values may be set statically or dynamically.`"
    },
    "SensitiveDataConfiguration": {
        "HideResponseOn": ["`TRANSCRIPT`"]
    }
}

```

## Results and conditions

The result that the user selects when interacting with the View. The available
conditions will be dependent on the View resource specified in action
parameters.

## Errors

- NoMatchingError - if no other Error matches.
- NoMatchingCondition - if no other Condition matches.
- TimeLimitExceeded - if there is no response before the configured
  `InvocationTimeLimitSeconds`.

## Restrictions

This action is only supported on the chat channel.

This action can be used in inbound flows and customer queue flows.

To ensure reliable show view rendering, limit combined inputs and contact
attributes to 16KB or less.

## Corresponding block in the UI

[Show View](../adminguide/show-view-block.md "../adminguide/show-view-block.md")

This action routes step-by-step guides that are to be displayed to agents in the
agent workspace. It routes the guides as chat contacts. This type of chat contact is
different from the customer-based contact that the agent is handling.

This action can only be used in inbound contact flows.
