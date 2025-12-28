# Subscribe to self resume events in

Amazon Connect Agent Workspace

Subscribes to events when the current user's participant is taken off hold.

**Signature**

```
onSelfResume(
  handler: ParticipantResumeHandler,
  contactId?: string
): void
```

**Usage**

```
const handleSelfResume = (event) => {
  console.log("You have been resumed from hold");
};
voiceClient.onSelfResume(handleSelfResume, "contact-123");
```

**Input**

| **Parameter**      | **Type**                 | **Description**                                                                         |
| ------------------ | ------------------------ | --------------------------------------------------------------------------------------- |
| handler _Required_ | ParticipantResumeHandler | Event handler function to call when the current user's participant is<br>taken off hold |
| contactId          | string                   | Optional contact ID to filter events for a specific contact                             |
