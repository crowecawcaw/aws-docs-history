

# Event bus target: bus to bus
<a name="eb-custom-bus-target-bus"></a>

To forward events to another event bus, set `TargetArn` to that bus's ARN. The destination can be another Custom Event Bus or a Custom Event Bus - Classic, in your account or another account, in the same Region or a different one. No parameter block is needed. A Custom Event Bus - Classic rule can likewise name a Custom Event Bus as its target, so events can move in either direction during a migration.

## Parameters
<a name="eb-custom-bus-target-bus-parameters"></a>

This target has no parameters; the payload is the whole request.

## Delivery role
<a name="eb-custom-bus-target-bus-role"></a>

The role needs `events:PutEvents` on the destination bus for events that carry a `PutEvents` envelope, and `events:PutRawEvents` for events published with `PutRawEvents`. EventBridge chooses the action per event and you cannot override it, so grant both when the source bus carries both kinds. A destination bus in another account must also allow your role in its resource policy or through an AWS RAM share; see [Sharing a Custom Event Bus with other accounts](eb-custom-bus-sharing.md).

## Batching and payload
<a name="eb-custom-bus-target-bus-batching"></a>

Events arrive on the destination bus as new events: they get a new event identifier and ingestion time, and the destination bus's subscribers filter them as usual. Publishing to the destination counts against that bus's throughput quota.

## Loop detection
<a name="eb-custom-bus-target-bus-loops"></a>

A chain of buses, rules, subscribers, and functions can send an event back to a bus it already passed through, and multiply it on each pass. EventBridge detects such loops through a Custom Event Bus on a best-effort basis: if an event, or an event derived from it, already passed through the target Custom Event Bus, EventBridge does not deliver it again, and if the subscriber has a dead-letter queue, the record carries the error code `LOOP_DETECTED`. Do not design an application that depends on an event passing through the same bus more than once, and do not rely on EventBridge to stop a loop for you. Rules on a Custom Event Bus - Classic keep their existing behavior; see [Preventing infinite loops](eb-troubleshooting.md#eb-prevent-infinite-loops).