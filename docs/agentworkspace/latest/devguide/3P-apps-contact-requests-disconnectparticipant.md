# Disconnect a participant from a contact in Amazon Connect Agent Workspace

Disconnects a specific participant from the contact.

**Signature**

```

disconnectParticipant(participantId: string): Promise<void>

```

**Usage**

```

await contactClient.disconnectParticipant("participant-456");
console.log("Participant disconnected");

```

**Input**

| **Parameter**            | **Type** | **Description**                                         |
| ------------------------ | -------- | ------------------------------------------------------- |
| participantId _Required_ | string   | The unique identifier for the participant to disconnect |

**Permissions required:**

```

*

```
