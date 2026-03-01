# Check if a participant can be resumed from hold in Amazon Connect Agent Workspace

Checks whether a specific participant can be resumed from hold.

**Signature**

```
canResumeParticipant(participantId: string): Promise<boolean>
```

**Usage**

```
const canResume = await voiceClient.canResumeParticipant("participant-456");
if (canResume) {
  await voiceClient.resumeParticipant("participant-456");
}
```

**Input**

| **Parameter**            | **Type** | **Description**                           |
| ------------------------ | -------- | ----------------------------------------- |
| participantId _Required_ | string   | The unique identifier for the participant |

**Output**

Returns a Promise that resolves to a boolean: true if the participant can be resumed,
false otherwise
