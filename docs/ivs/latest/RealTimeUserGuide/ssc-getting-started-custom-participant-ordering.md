# Custom Participant Ordering

Custom participant ordering allows you to control the positioning of participants in both grid and PiP layouts based on
custom attribute values in participant tokens, including the positioning of the featured participants and selection of participants
the PiP window. This provides deterministic participant positioning and enables role-based layouts.

## How Custom Ordering Works

When `participantOrderAttribute` is specified in your layout configuration, participants are ordered according to the
following rules:

- Participants with the specified ordering attribute in their tokens are positioned first, sorted numerically by their attribute values.
- Participants without the ordering attribute fall back to arrival-time ordering and are positioned after the ordered participants.
- When multiple participants have identical ordering values, they are sub-sorted by their arrival time into the stage.
- The ordering uses numeric sorting (not lexicographic), so "10" comes after "9" (not after "1").
- Negative values are supported. They are positioned before positive values.
- Non-numeric values (e.g., "abc", "1.5") are treated as invalid, and those participants fall back to arrival-time ordering.

**Important:** Participant ordering (whether based on the arrival time or custom) takes effect after
the composition has started. The correct ordering of participants is not guaranteed for participants who join the stage before the
composition begins.

## Creating Tokens with Ordering Attributes

To use custom participant ordering, include the ordering attribute in your participant tokens when creating them:

```
aws ivs-realtime create-participant-token --stage-arn "arn:aws:ivs:us-east-1:123456789012:stage/u9OiE29bT7Xp" --attributes order=1

aws ivs-realtime create-participant-token --stage-arn "arn:aws:ivs:us-east-1:123456789012:stage/u9OiE29bT7Xp" --attributes order=2

aws ivs-realtime create-participant-token --stage-arn "arn:aws:ivs:us-east-1:123456789012:stage/u9OiE29bT7Xp" --attributes order=3
```

You can combine the custom-participant-order attribute with the attributes for selecting participants for the featured slot and the
PiP window:

```
aws ivs-realtime create-participant-token --stage-arn "arn:aws:ivs:us-east-1:123456789012:stage/u9OiE29bT7Xp" --attributes order=2,isFeatured=true

aws ivs-realtime create-participant-token --stage-arn "arn:aws:ivs:us-east-1:123456789012:stage/u9OiE29bT7Xp" --attributes order=3,isFeatured=true

aws ivs-realtime create-participant-token --stage-arn "arn:aws:ivs:us-east-1:123456789012:stage/u9OiE29bT7Xp" --attributes order=4,isPip=true
```

## Example Use Cases

Example use cases include:

- Consistent positioning – Participants maintain their positions when reconnecting with the same token.
- Role-based positioning – For instance, you could specify teachers with order=1 and students with order=2.
- Priority-based layouts – VIP participants with lower order values would appear first.
- Dynamic layouts – You can combine custom ordering with `featuredParticipantAttribute`
  and `pipParticipantAttribute` for complex scenarios.
- Cross-stage interactions – When using participant replication for scenarios like VS Mode competitions where streamers from
  different stages interact, you can override ordering attributes to control positioning in the destination stage composition.

**Note:** For participant-replication use cases, you can override participant attributes (including the order
attribute) as needed when starting a replication to achieve the desired layout in the destination stage.

## Backward Compatibility

Custom participant ordering is an optional feature and is fully backward compatible. Existing compositions
without `participantOrderAttribute` continue to work unchanged, using arrival-time ordering.
When `participantOrderAttribute` is set to an empty string, the system ignores custom ordering entirely and falls back to
default behavior.
