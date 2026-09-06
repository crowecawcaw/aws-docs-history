

# Unsubscribe from participant hold events in Connect Customer agent workspace
<a name="3P-apps-voice-requests-offparticipanthold"></a>

Unsubscribes from participant hold events.

 **Signature** 

```
offParticipantHold(
  handler: ParticipantHoldHandler,
  participantId?: string
): void
```

 **Usage** 

```
voiceClient.offParticipantHold(handleParticipantHold);
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| handler Required | ParticipantHoldHandler | Event handler function to remove | 
| participantId | string | Optional participant ID to unsubscribe from specific participant events | 