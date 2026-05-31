# UpdateContactEventHooks

Sets one or more contact event hooks, which are flows associated with contact events,
such as customer whisper or agent hold. For more information, see [Contact
records data model](../adminguide/ctr-data-model.md "../adminguide/ctr-data-model.md"). The following event hooks are valid:

- AgentHold
- AgentWhisper
- CustomerHold
- CustomerQueue
- CustomerRemaining
- CustomerWhisper
- DefaultAgentUI
- DisconnectAgentUI
- PauseContact
- ResumeContact

## Parameter object

```
{
    "EventHooks": { an Object that holds the event hooks to be set. Only one entry may be present in this map.
        "Key": "Value" - the event hook to be set where the key is the event type and the value is the flow ID or ARN to run when that event occurs. Keys must be defined statically.
    }
}
```

## Results and conditions

None.

## Errors

- NoMatchingError - if no other Error matches.

## Restrictions

This is supported in all types of flows.

## Corresponding blocks in the UI

- [Set
  customer queue flow](../adminguide/set-customer-queue-flow.md "../adminguide/set-customer-queue-flow.md")
- [Set event
  flow](../adminguide/set-event-flow.md "../adminguide/set-event-flow.md")
- [Set hold flow](../adminguide/set-hold-flow.md "../adminguide/set-hold-flow.md")
- [Set whisper
  flow](../adminguide/set-whisper-flow.md "../adminguide/set-whisper-flow.md")
