# Unsubscribe from

participant
added events in Amazon Connect Agent Workspace

Unsubscribes from participant added events.

**Signature**

```

offParticipantAdded(handler: ParticipantAddedHandler, contactId?: string): void

```

**Usage**

```

contactClient.offParticipantAdded(handleParticipantAdded);

```

**Input**

| **Parameter**      | **Type**                | **Description**                                                 |
| ------------------ | ----------------------- | --------------------------------------------------------------- |
| handler _Required_ | ParticipantAddedHandler | Event handler function to remove                                |
| contactId          | string                  | Optional contact ID to unsubscribe from specific contact events |
