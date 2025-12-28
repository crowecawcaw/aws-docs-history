# Resume a participant from

hold in Amazon Connect Agent Workspace

Resumes a specific participant from hold.

**Signature**

```
resumeParticipant(participantId: string): Promise<void>
```

**Usage**

```
await voiceClient.resumeParticipant("participant-456");
console.log("Participant has been resumed");
```

**Input**

| **Parameter**            | **Type** | **Description**                                     |
| ------------------------ | -------- | --------------------------------------------------- |
| participantId _Required_ | string   | The unique identifier for the participant to resume |
