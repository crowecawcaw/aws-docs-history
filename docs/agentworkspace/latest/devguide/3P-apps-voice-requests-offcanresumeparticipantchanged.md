

# Unsubscribe from participant resume capability change events in Connect Customer agent workspace
<a name="3P-apps-voice-requests-offcanresumeparticipantchanged"></a>

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


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| handler Required | CanResumeParticipantChangedHandler | Event handler function to remove | 
| participantId | string | Optional participant ID to unsubscribe from specific participant events | 