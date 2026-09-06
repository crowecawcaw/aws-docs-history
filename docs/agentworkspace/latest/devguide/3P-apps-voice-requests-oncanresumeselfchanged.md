

# Subscribe to self resume capability change events in Connect Customer agent workspace
<a name="3P-apps-voice-requests-oncanresumeselfchanged"></a>

Subscribes to events when the current user's capability to be resumed from hold changes.

 **Signature** 

```
onCanResumeSelfChanged(
  handler: CanResumeParticipantChangedHandler,
  contactId?: string
): void
```

 **Usage** 

```
const handleCanResumeSelfChanged = (event) => {
  if (event.canResumeConnection) {
    console.log("You can now be resumed from hold");
    // Enable resume button in UI
  } else {
    console.log("You cannot be resumed at this time");
    // Disable resume button in UI
  }
};
voiceClient.onCanResumeSelfChanged(handleCanResumeSelfChanged, "contact-123");
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| handler Required | CanResumeParticipantChangedHandler | Event handler function to call when the capability changes | 
| contactId | string | Optional contact ID to filter events for a specific contact | 