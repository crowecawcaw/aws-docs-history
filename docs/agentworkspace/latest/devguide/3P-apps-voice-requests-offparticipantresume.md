

# Unsubscribe from participant resume events in Connect Customer agent workspace
<a name="3P-apps-voice-requests-offparticipantresume"></a>

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


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| handler Required | ParticipantResumeHandler | Event handler function to remove | 
| participantId | string | Optional participant ID to unsubscribe from specific participant events | 