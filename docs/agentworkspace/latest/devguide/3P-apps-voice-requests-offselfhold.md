# Unsubscribe from self hold events

in Amazon Connect Agent Workspace

Unsubscribes from self hold events.

**Signature**

```
offSelfHold(
  handler: ParticipantHoldHandler,
  contactId?: string
): void
```

**Usage**

```
voiceClient.offSelfHold(handleSelfHold);
```

**Input**

| **Parameter**      | **Type**               | **Description**                                                 |
| ------------------ | ---------------------- | --------------------------------------------------------------- |
| handler _Required_ | ParticipantHoldHandler | Event handler function to remove                                |
| contactId          | string                 | Optional contact ID to unsubscribe from specific contact events |
