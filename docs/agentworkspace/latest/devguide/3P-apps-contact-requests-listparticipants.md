# List all participants for a

contact in Amazon Connect Agent Workspace

Retrieves all participants associated with a specific contact.

**Signature**

```

listParticipants(contactId: string): Promise<ParticipantData[]>

```

**Usage**

```

const participants = await contactClient.listParticipants("contact-123");
participants.forEach((p) => {
    console.log(`Participant ${p.participantId}: ${p.type.value}`);
    if (p.isSelf) {
        console.log("This is the current user");
    }
});

```

**Input**

| **Parameter**        | **Type** | **Description**                       |
| -------------------- | -------- | ------------------------------------- |
| contactId _Required_ | string   | The unique identifier for the contact |

**Output - ParticipantData[]**

The ParticipantData interface includes:

- `participantId`: string - Unique identifier for the participant
- `contactId`: string - Contact this participant belongs to
- `type`: ParticipantType - Type of participant (agent, outbound,
  inbound, monitoring, other)
- `isInitial`: boolean - Whether this is the initial participant
- `isSelf`: boolean - Whether this participant is associated with the
  current user

**Permissions required:**

```

*

```
