

# Subscribe to participant resume events in Connect Customer agent workspace
<a name="3P-apps-voice-requests-onparticipantresume"></a>

Subscribes to events when any participant is taken off hold.

 **Signature** 

```
onParticipantResume(
  handler: ParticipantResumeHandler,
  participantId?: string
): void
```

 **Usage** 

```
const handleParticipantResume = (event) => {
  console.log(`Participant ${event.participantId} has been resumed`);
};
voiceClient.onParticipantResume(handleParticipantResume, "participant-456");
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| handler Required | ParticipantResumeHandler | Event handler function to call when participants are taken off hold | 
| participantId | string | Optional participant ID to filter events for a specific participant | 