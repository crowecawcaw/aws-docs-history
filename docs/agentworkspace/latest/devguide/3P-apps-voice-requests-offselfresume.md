# Unsubscribe from self resume events in Amazon Connect Customer agent workspace

Unsubscribes from self resume events.

**Signature**

```
offSelfResume(
  handler: ParticipantResumeHandler,
  contactId?: string
): void
```

**Usage**

```
voiceClient.offSelfResume(handleSelfResume);
```

**Input**

| **Parameter**      | **Type**                 | **Description**                                                 |
| ------------------ | ------------------------ | --------------------------------------------------------------- |
| handler _Required_ | ParticipantResumeHandler | Event handler function to remove                                |
| contactId          | string                   | Optional contact ID to unsubscribe from specific contact events |
