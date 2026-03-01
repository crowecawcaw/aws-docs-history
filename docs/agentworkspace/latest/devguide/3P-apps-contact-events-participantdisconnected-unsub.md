# Unsubscribe from participant disconnected events in Amazon Connect Agent Workspace

Unsubscribes from participant disconnected events.

**Signature**

```

offParticipantDisconnected(handler: ParticipantDisconnectedHandler, contactId?: string): void

```

**Usage**

```

contactClient.offParticipantDisconnected(handleParticipantDisconnected);

```

**Input**

| **Parameter**      | **Type**                       | **Description**                                                 |
| ------------------ | ------------------------------ | --------------------------------------------------------------- |
| handler _Required_ | ParticipantDisconnectedHandler | Event handler function to remove                                |
| contactId          | string                         | Optional contact ID to unsubscribe from specific contact events |
