# Unsubscribe from participant resume events in Amazon Connect Agent Workspace

Unsubscribes from participant resume events.

**Signature**

```
offParticipantResume(
  handler: ParticipantResumeHandler,
  participantId?: string
): void
```

**Usage**

```
voiceClient.offParticipantResume(handleParticipantResume);
```

**Input**

| **Parameter**      | **Type**                 | **Description**                                                            |
| ------------------ | ------------------------ | -------------------------------------------------------------------------- |
| handler _Required_ | ParticipantResumeHandler | Event handler function to remove                                           |
| participantId      | string                   | Optional participant ID to unsubscribe from specific participant<br>events |
