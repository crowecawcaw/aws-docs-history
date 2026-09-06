

# Unsubscribe from self resume capability change events in Connect Customer agent workspace
<a name="3P-apps-voice-requests-offcanresumeselfchanged"></a>

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


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| handler Required | CanResumeParticipantChangedHandler | Event handler function to remove | 
| contactId | string | Optional contact ID to unsubscribe from specific contact events | 