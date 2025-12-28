# Unsubscribe from

participant resume capability change events in Amazon Connect Agent Workspace

Unsubscribes from participant capability change events.

**Signature**

```
offCanResumeParticipantChanged(
  handler: CanResumeParticipantChangedHandler,
  participantId?: string
): void
```

**Usage**

```
voiceClient.offCanResumeParticipantChanged(handleCanResumeChanged);
```

**Input**

| **Parameter**      | **Type**                           | **Description**                                                            |
| ------------------ | ---------------------------------- | -------------------------------------------------------------------------- |
| handler _Required_ | CanResumeParticipantChangedHandler | Event handler function to remove                                           |
| participantId      | string                             | Optional participant ID to unsubscribe from specific participant<br>events |
