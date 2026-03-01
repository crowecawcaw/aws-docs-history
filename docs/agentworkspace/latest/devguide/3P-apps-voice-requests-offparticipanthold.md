# Unsubscribe from participant hold events in Amazon Connect Agent Workspace

Unsubscribes from participant hold events.

**Signature**

```
offParticipantHold(
  handler: ParticipantHoldHandler,
  participantId?: string
): void
```

**Usage**

```
voiceClient.offParticipantHold(handleParticipantHold);
```

**Input**

| **Parameter**      | **Type**               | **Description**                                                            |
| ------------------ | ---------------------- | -------------------------------------------------------------------------- |
| handler _Required_ | ParticipantHoldHandler | Event handler function to remove                                           |
| participantId      | string                 | Optional participant ID to unsubscribe from specific participant<br>events |
