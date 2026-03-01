# Subscribe to participant added events in Amazon Connect Agent Workspace

Subscribes to participant added events. This event fires when a new participant joins
a
contact.

**Signature**

```

onParticipantAdded(handler: ParticipantAddedHandler, contactId?: string): void

```

**Usage**

```

const handleParticipantAdded = (event) => {
    console.log(`New participant added: ${event.participant.participantId}`);
    console.log(`Type: ${event.participant.type.value}`);
};

// Subscribe to all contacts
contactClient.onParticipantAdded(handleParticipantAdded);

// Or subscribe to a specific contact
contactClient.onParticipantAdded(handleParticipantAdded, "contact-123");

```

**Input**

| **Parameter**      | **Type**                | **Description**                                             |
| ------------------ | ----------------------- | ----------------------------------------------------------- |
| handler _Required_ | ParticipantAddedHandler | Event handler function to call when participants are added  |
| contactId          | string                  | Optional contact ID to filter events for a specific contact |

**Event Structure - ParticipantAdded**

The handler receives a ParticipantAdded event with:

- `participant`: ParticipantData - The participant that was added

**Permissions required:**

```

*

```
