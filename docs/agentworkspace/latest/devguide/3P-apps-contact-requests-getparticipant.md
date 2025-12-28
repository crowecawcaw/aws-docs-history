# Get specific participant

information in Amazon Connect Agent Workspace

Retrieves information for a specific participant.

**Signature**

```

getParticipant(participantId: string): Promise<ParticipantData>

```

**Usage**

```

const participant = await contactClient.getParticipant("participant-456");
console.log(`Participant type: ${participant.type.value}`);
console.log(`Is initial: ${participant.isInitial}`);

```

**Input**

| **Parameter**            | **Type** | **Description**                           |
| ------------------------ | -------- | ----------------------------------------- |
| participantId _Required_ | string   | The unique identifier for the participant |

**Output - ParticipantData**

Returns a ParticipantData object with participant details.

**Permissions required:**

```

*

```
