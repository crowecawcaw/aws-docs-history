# Wait

Pauses the flow for a specified duration, or until a specified event happens,
whichever happens first.

## Parameter object

```
{
    "TimeoutSeconds": The amount of time to wait before the action finishes with the "WaitCompleted" result. This can be either statically defined, or a single valid JSONPath identifier. If defined statically, this must be a positive integer value no greater than 604800 (seven days),
    "Events": An optional list of all events that can trigger an interrupt. The supported events currently are "CustomerReturned" and "BotParticipantDisconnected". This must be defined statically.

}
```

## Execution results and conditions

If an event interrupts the wait, the run result is the event that interrupted. If
no event interrupts the Wait and the time elapses, the run result is WaitCompleted.
Conditions are supported, but only the "Equals" operator is supported.
"WaitCompleted" is always required operand, and every specified event is also
required to be present as a condition operand.

## Errors

- NoMatchingError - If no other Error matches.
- ParticipantNotFound - The supported event currently is
  "BotParticipantDisconnected".

## Restrictions

This is supported in every type of flow, but is supported only by the chat
channel.

## Corresponding block in the UI

[Wait](../adminguide/wait.md "../adminguide/wait.md")
