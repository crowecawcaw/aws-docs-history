

# Unsubscribe from self resume events in Connect Customer agent workspace
<a name="3P-apps-voice-requests-offselfresume"></a>

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


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| handler Required | ParticipantResumeHandler | Event handler function to remove | 
| contactId | string | Optional contact ID to unsubscribe from specific contact events | 