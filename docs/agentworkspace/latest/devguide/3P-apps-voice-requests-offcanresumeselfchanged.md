# Unsubscribe from self resume capability change events in Amazon Connect Agent Workspace

Unsubscribes from capability change events for the current user.

**Signature**

```
offCanResumeSelfChanged(
  handler: CanResumeParticipantChangedHandler,
  contactId?: string
): void
```

**Usage**

```
voiceClient.offCanResumeSelfChanged(handleCanResumeSelfChanged);
```

**Input**

| **Parameter**      | **Type**                           | **Description**                                                 |
| ------------------ | ---------------------------------- | --------------------------------------------------------------- |
| handler _Required_ | CanResumeParticipantChangedHandler | Event handler function to remove                                |
| contactId          | string                             | Optional contact ID to unsubscribe from specific contact events |
